#!/usr/bin/env python3
"""Module obsfucating select fields in log messages"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 seperator: str) -> str:
    """Function obsfucating select fields in log messages with `redaction` arg
    """
    for i in fields:
        pattern = re.compile(f'{i}=.*?{seperator}')
        message = re.sub(pattern, f'{i}={redaction}{seperator}', message)
    return message
