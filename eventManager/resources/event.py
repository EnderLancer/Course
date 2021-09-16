from flask import request
from flask_jwt_extended import jwt_required, current_user
from flask_restful import Resource
from marshmallow import ValidationError

from model import Event, db, EventStatusType
from schema.event import EventListSchema, EventDetailSchema


class EventList(Resource):
    def get(self):
        result = Event.query.all()
        return EventListSchema(many=True).dump(result)

    @jwt_required()
    def post(self):
        try:
            result = EventDetailSchema().load(request.form)
        except ValidationError as err:
            return err.messages
        result.owner_id = current_user.id
        db.session.add(result)
        db.session.commit()
        return EventDetailSchema().dump(result)


class EventDetail(Resource):
    def get(self, pk):
        result = Event.query.get(pk)
        return EventDetailSchema().dump(result)

    @jwt_required()
    def put(self, pk):
        event = Event.query.get(pk)
        if event.owner_id == current_user.id:
            try:
                result = EventDetailSchema().load(request.form,
                                                  instance=Event().query.get(pk),
                                                  partial=True)
            except ValidationError as err:
                return err.messages
            db.session.commit()
            return EventDetailSchema().dump(result)
        else:
            return {"message": "You don`t have permissions."}

    @jwt_required()
    def delete(self, pk):
        event = Event.query.get(pk)
        if event.owner_id == current_user.id:
            if event.status != EventStatusType.FINISHED:
                event.status = EventStatusType.CANCELED
            db.session.commit()
            return EventDetailSchema().dump(event)
        else:
            return {"message": "You don`t have permissions."}
