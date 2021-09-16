from flask import request
from flask_jwt_extended import jwt_required, current_user
from flask_restful import Resource

from model import db, Member, Event
from schema.member import MemberSchema


class MemberList(Resource):
    def get(self, event_pk):
        result = Event.query.filter(Event.id == event_pk).first().members
        return MemberSchema(many=True).dump(result)

    @jwt_required()
    def post(self, event_pk):
        event = Event.query.get(event_pk)
        if current_user not in event.members:
            event.members.append(current_user)
            db.session.commit()
        return MemberSchema().dump(current_user)


class MemberDetail(Resource):
    def get(self, event_pk, member_pk):
        member = Member.query.filter((Member.id == member_pk) & (Event.id == event_pk)).first()
        return MemberSchema().dump(member)

    @jwt_required()
    def delete(self, event_pk, member_pk):
        event = Event.query.get(event_pk)
        if (event.owner_id == current_user.id
                or member_pk == current_user.id):
            member = Member.query.get(member_pk)
            event.members.remove(member)
            db.session.commit()
            return MemberSchema().dump(member)
        else:
            return {"message": "You don`t have permissions."}
