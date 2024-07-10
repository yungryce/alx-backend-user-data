#!/usr/bin/env python3
"""
Module for authentication
"""


import os
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """_summary_
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
                path (str): _description_
                excluded_paths (List[str]): _description_

        Returns:
                bool: _description_
        """
        # if path is not None and excluded_paths is not None:
        #     for exclusion_path in map(lambda x: x.strip(), excluded_paths):
        #         pattern = ''
        #         if exclusion_path[-1] == '*':
        #             pattern = '{}.*'.format(exclusion_path[0:-1])
        #         elif exclusion_path[-1] == '/':
        #             pattern = '{}/*'.format(exclusion_path[0:-1])
        #         else:
        #             pattern = '{}/*'.format(exclusion_path)
        #         if re.match(pattern, path):
        #             return False
        # return True
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
                request (_type_, optional): _description_. Defaults to None.

        Returns:
                str: _description_
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request.
        """

        return None

    def session_cookie(self, request=None) -> str:
        """Gets the value of the cookie named SESSION_NAME.
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
