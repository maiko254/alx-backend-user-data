#!/usr/bin/env python3
"""Hashing string password using bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt package"""
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate the password against the hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
