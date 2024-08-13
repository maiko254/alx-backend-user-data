#!/usr/bin/env python3
"""Module to authenticate user"""
import bcrypt


def _hash_password(password: str) -> str:
    """Hash the given password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)
