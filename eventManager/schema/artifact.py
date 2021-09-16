import requests
from marshmallow import fields, post_load

from model import Artifact, EndpointUrl, db
from schema import ma


class ArtifactSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Artifact
        load_instance = True
        include_relationships = True

    id = ma.auto_field()
    name = ma.auto_field()
    occupation_id = ma.auto_field()
    link = fields.Str(default="")

    @post_load
    def set_artifact(self, in_artifact, **kwargs):
        artifact_endpoint_list = EndpointUrl.query.filter(
            EndpointUrl.occupation_id == in_artifact.occupation_id
        )
        print(in_artifact.name)
        for artifact_endpoint in artifact_endpoint_list:
            search_by_guest = f"?name={in_artifact.name}"
            artifacts = requests.get(artifact_endpoint.url + search_by_guest).json()
            if artifacts:
                artifact_url = artifacts[0]["url"]
                artifact_with_link = Artifact.query.filter(Artifact.link == artifact_url).first()
                if artifact_with_link:
                    return artifact_with_link
                in_artifact.link = artifact_url
                db.session.commit()
            break
        return in_artifact
