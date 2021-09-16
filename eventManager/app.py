import os

from flask import Flask, Blueprint
from flask_restful import Api

from model import db
from resources import jwt
from resources.artifact import ArtifactList, ArtifactDetail
from resources.event import EventList, EventDetail
from resources.guest import GuestList, GuestDetail
from resources.login import Login
from resources.member import MemberList, MemberDetail
from resources.registration import Registration
from schema.event import ma

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:post123@localhost/event_service"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # TODO for testing
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY', 'my_precious')
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
api.add_resource(EventList, '/events')
api.add_resource(EventDetail, '/events/<int:pk>')
api.add_resource(MemberList, '/events/<int:event_pk>/members')
api.add_resource(MemberDetail, '/events/<int:event_pk>/members/<int:member_pk>')
api.add_resource(GuestList, '/events/<int:event_pk>/guests')
api.add_resource(GuestDetail, '/events/<int:event_pk>/guests/<int:guest_pk>')
api.add_resource(ArtifactList, '/events/<int:event_pk>/artifacts')
api.add_resource(ArtifactDetail, '/events/<int:event_pk>/artifacts/<int:artifact_pk>')
api.add_resource(Registration, '/registration')
api.add_resource(Login, '/profile', '/login')

app.register_blueprint(api_bp, url_prefix='/api')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=5000)
