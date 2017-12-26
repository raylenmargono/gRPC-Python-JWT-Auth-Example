import binascii
import datetime
import hashlib
import uuid

import jwt

from sqlalchemy import Column, String, Boolean
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy.orm.exc import NoResultFound
from settings import settings, db_session

Base = declarative_base()

_TOKEN_EXPIRATION = 24 * 30


def make_password(raw_password, iterations=100000, hash_name='sha256'):
    '''
        Secure password hashing using the PBKDF2 algorithm (recommended)
        Configured to use PBKDF2 + HMAC + SHA256.
        The result is a 64 byte binary string.  Iterations may be changed
        safely but you must rename the algorithm if you change SHA256.
    '''
    salt = settings.CRYPT_SALT
    dk = hashlib.pbkdf2_hmac(password=raw_password.encode('utf-8'),
                             salt=salt.encode('utf-8'),
                             iterations=iterations,
                             hash_name=hash_name)
    return binascii.hexlify(dk).decode('ascii')


def generate_token(user):
    user_info = {
        'username': user.username,
        'email': user.email,
        'is_admin': user.is_admin,
        'user_id': user.id
    }
    return jwt.encode({
        'user_info': user_info,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=_TOKEN_EXPIRATION)
    }, settings.JWT_SECRET, algorithm='HS256')


class User(Base):
    __tablename__ = 'User'
    _id = Column('id', String, primary_key=True, default=str(uuid.uuid4()), unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)
    is_admin = Column(Boolean, default=False)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address

    @hybrid_property
    def id(self):
        return self._id

    @staticmethod
    def login(username, password):
        hashed_password = make_password(password)
        try:
            user = db_session.session.query(User).filter_by(username=username, password=hashed_password).one()
            token = generate_token(user)
            return token
        except NoResultFound:
            return None

    @staticmethod
    def create(username, password, email, is_admin=False):
        hashed_password = make_password(password)
        try:
            new_user = User(username=username, password=hashed_password, email=email, is_admin=is_admin)
            db_session.session.add(new_user)
            db_session.session.commit()
            token = generate_token(new_user)
            return token, True
        except SQLAlchemyError as e:
            db_session.session.rollback()
            return str(e), False
