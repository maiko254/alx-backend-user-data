#!/usr/bin/env python3
"""Hashing string password using bcrypt"""
import bcrypt


def hash_password(password):
    """Hashes a password using bcrypt package"""
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
