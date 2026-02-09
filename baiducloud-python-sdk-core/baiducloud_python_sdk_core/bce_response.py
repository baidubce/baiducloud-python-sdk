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

        :param headers:
        :return:
        """
        for k, v in iteritems(headers):
            if k.startswith(compat.convert_to_string(http_headers.BCE_PREFIX)):
                k = 'bce_' + k[len(compat.convert_to_string(http_headers.BCE_PREFIX)):]
            k = utils.pythonize_name(k.replace('-', '_'))
            if k.lower() == compat.convert_to_string(http_headers.ETAG.lower()):
                v = v.strip('"')
            self.metadata[k] = v

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
