from flask import request
from flask_restful import Resource

from model import Event, db, Artifact
from schema.artifact import ArtifactSchema


class ArtifactList(Resource):
    def get(self, event_pk):
        result = Event.query.filter(Event.id == event_pk).first().artifacts
        return ArtifactSchema(many=True).dump(result)

    def post(self, event_pk):
        result = ArtifactSchema().load(request.form)
        db.session.add(result)
        event = Event.query.get(event_pk)
        if result not in event.artifacts:
            event.artifacts.append(result)
            db.session.commit()
        return ArtifactSchema().dump(result)


class ArtifactDetail(Resource):
    def get(self, event_pk, artifact_pk):
        member = Artifact.query.filter((Artifact.id == artifact_pk) & (Event.id == event_pk)).first()
        return ArtifactSchema().dump(member)

    def delete(self, event_pk, artifact_pk):
        artifact = Artifact.query.get(artifact_pk)
        event_queue = Event.query.filter(Event.id == event_pk).first()
        event_queue.artifacts.remove(artifact)
        db.session.commit()
        return ArtifactSchema().dump(artifact)
