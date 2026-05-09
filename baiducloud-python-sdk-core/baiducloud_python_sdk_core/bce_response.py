# Copyright 2014 Baidu, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the
# License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

"""
This module provides a general response class for BCE services.
"""
from future.utils import iteritems
from builtins import str
from builtins import bytes
from baiducloud_python_sdk_core import utils
from baiducloud_python_sdk_core import compat
from baiducloud_python_sdk_core.http import http_headers
import json


class BceResponse(object):
    """

    """
    def __init__(self):
        self.metadata = {}
        self._map = None

    def set_metadata_from_headers(self, headers):
        """

        :param headers: Response headers dict with original header names
        :return:
        """
        self.metadata = dict(headers) if headers else {}

    def to_dict(self):
        return self._map

    def from_dict(self, map=None):
        pass

    def to_json_string(self, *args, **kwargs):
        if "ensure_ascii" not in kwargs:
            kwargs["ensure_ascii"] = False
        return json.dumps(self.to_dict(), *args, **kwargs)

    def __getattr__(self, item):
        if item.startswith('__'):
            raise AttributeError
        return None


class BceStreamResponse(BceResponse):
    """
    Response class for BCE responses that contain a file stream.
    The caller is responsible for closing the stream after use.
    """
    def __init__(self):
        super(BceStreamResponse, self).__init__()
        self._stream = None
        self._content_type = None
        self._content_length = -1
        self._http_response = None

    @property
    def stream(self):
        """
        Get the raw content stream from the HTTP response.
        The caller is responsible for reading and closing this stream.
        """
        return self._stream

    @stream.setter
    def stream(self, value):
        self._stream = value

    @property
    def content_type(self):
        """Get the content type of the response."""
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value

    @property
    def content_length(self):
        """Get the content length of the response, or -1 if unknown."""
        return self._content_length

    @content_length.setter
    def content_length(self, value):
        self._content_length = value

    def read(self, size=None):
        """
        Read content from the stream.
        :param size: Number of bytes to read, or None to read all.
        :return: The content bytes.
        """
        if self._stream is None:
            return b''
        if size is None:
            return self._stream.read()
        return self._stream.read(size)

    def close(self):
        """
        Close the underlying stream and HTTP response.
        Must be called after the stream has been fully consumed.
        """
        if self._http_response is not None:
            self._http_response.close()
            self._http_response = None
        self._stream = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False
