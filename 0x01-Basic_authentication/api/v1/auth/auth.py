#!/usr/bin/env python3
"""Auth class for Basic authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Base class for Basic Authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if route requires authentication"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """doc doc doc"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """doc doc doc"""
        return request
