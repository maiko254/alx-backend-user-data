#!/usr/bin/env python3
"""Module obsfucating select fields in log messages"""
import re
import logging
import os
import mysql.connector
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function obsfucating select fields in log messages with `redaction` arg
    """
    for i in fields:
        pattern = re.compile(f'{i}=.*?{separator}')
        message = re.sub(pattern, f'{i}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """Function returning a logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Function returning a connector to a MySQL database
    """
    return mysql.connector.connect(
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME', ''),
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''))


def main() -> None:
    """Main function
    """
    db = get_db()
    cursor = db.cursor()
    fields = "name, email, phone, ssn, password, ip, last_login, user_agent"
    columns = fields.split(", ")
    query = f"SELECT {fields} FROM users"
    cursor.execute("SELECT * FROM users")
    logger = get_logger()
    rows = cursor.fetchall()
    for row in rows:
        record = map(
                lambda m: '{}={}'.format(m[0], m[1]),
                zip(columns, row),
            )
        message = '{};'.format('; '.join(list(record)))
        log_args = ("user_data,", logging.INFO,
                    None, None, message, None, None)
        log_record = logging.LogRecord(*log_args)
        logger.handle(log_record)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """Initialize class with log formatter and string fields"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats and filters log records to hide PII fields"""
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


if __name__ == '__main__':
    main()
