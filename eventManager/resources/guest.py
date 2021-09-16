from flask import request
from flask_jwt_extended import jwt_required, current_user
from flask_restful import Resource
from marshmallow import ValidationError

from model import db, Guest, Event
from schema.guest import GuestSchema


class GuestList(Resource):
    def get(self, event_pk):
        result = Event.query.filter(Event.id == event_pk).first().guests
        return GuestSchema(many=True).dump(result)

    @jwt_required()
    def post(self, event_pk):
        event = Event.query.get(event_pk)
        if event.owner_id == current_user.id:
            try:
                result = GuestSchema().load(request.form)
            except ValidationError as err:
                return err.messages
            db.session.add(result)
            event.guests.append(result)
            db.session.commit()
            return GuestSchema().dump(result)
        else:
            return "You don`t have permissions."


class GuestDetail(Resource):
    def get(self, event_pk, guest_pk):
        guest = Guest.query.filter((Guest.id == guest_pk) & (Event.id == event_pk)).first()
        return GuestSchema().dump(guest)

    @jwt_required()
    def delete(self, event_pk, guest_pk):
        event = Event.query.get(event_pk)
        if event.owner_id == current_user.id:
            guest = Guest.query.get(guest_pk)
            event.guests.remove(guest)
            db.session.commit()
            return GuestSchema().dump(guest)
        else:
            return "You don`t have permissions."
