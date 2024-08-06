#!/usr/bin/env python3
"""Auth class for Basic authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Base class for Basic Authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """doc doc doc """
        return False

    def authorization_header(self, request=None) -> str:
        """doc doc doc"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """doc doc doc"""
        return request
