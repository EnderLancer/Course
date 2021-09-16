from enum import Enum
from hashlib import md5

from flask_sqlalchemy import SQLAlchemy

from resources import jwt

db = SQLAlchemy()

JWT_SECRET_KEY = 'SECRET_KEY'  # TODO refactor this ugly solution


class ListedEnum(Enum):
    @classmethod
    def to_list(cls):
        return list(map(lambda c: c.name, cls))


class RoleType(ListedEnum):
    USER = "user"
    STAFF = "staff"
    ADMIN = "admin"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.Enum(RoleType), default=RoleType.USER.name)

    @staticmethod
    def hash_password(password):
        return md5(password.encode()).hexdigest()

    @staticmethod
    def login(username, password):
        return User.query.filter((User.username == username) & (User.password == User.hash_password(password))).first()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


class Occupation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)


class EndpointUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(120), nullable=False)
    occupation_id = db.Column(db.Integer, db.ForeignKey('occupation.id'), nullable=False)


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(1023))
    occupation_id = db.Column(db.Integer, db.ForeignKey('occupation.id'), nullable=False)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Artifact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    occupation_id = db.Column(db.Integer, db.ForeignKey('occupation.id'), nullable=False)
    link = db.Column(db.String(255), unique=True)


event_member = db.Table(
    "members",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True)
)

event_guest = db.Table(
    "guests",
    db.Column("guest_id", db.Integer, db.ForeignKey("guest.id"), primary_key=True),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True)
)

event_artifact = db.Table(
    "artifacts",
    db.Column("artifact_id", db.Integer, db.ForeignKey("artifact.id"), primary_key=True),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True)
)


class EventStatusType(ListedEnum):
    NEW = "new"
    FINISHED = "finished"
    CANCELED = "canceled"


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = db.relationship('User')
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(1023), nullable=False)
    start_datetime = db.Column(db.DateTime)
    status = db.Column(db.Enum(EventStatusType), default=EventStatusType.NEW.name, nullable=False)
    guests = db.relationship('Guest', secondary=event_guest, lazy='subquery',
                             backref=db.backref('events', lazy=True))
    members = db.relationship('User', secondary=event_member, lazy='subquery',
                              backref=db.backref('events', lazy="dynamic"))
    artifacts = db.relationship('Artifact', secondary=event_artifact, lazy='subquery',
                                backref=db.backref('events', lazy="dynamic"))
