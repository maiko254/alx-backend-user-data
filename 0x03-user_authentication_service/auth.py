#!/usr/bin/env python3
"""Module to authenticate user"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the given email and password """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pw = _hash_password(password)
            return self._db.add_user(email, hashed_pw)

    def valid_login(self, email: str, password: str) -> bool:
        """Check if the given email and password are valid """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode("utf-8"),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for the given email """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None


def _hash_password(password: str) -> str:
    """Hash the given password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def _generate_uuid() -> str:
    """Generate a UUID
    """
    return str(uuid.uuid4())
