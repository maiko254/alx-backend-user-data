#!/usr/bin/env python3
"""class BasicAuth """
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class for Basic Authentication
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts base64 part from authorization header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[len('Basic '):]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Decodes a base64 string to UTF-8
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None
