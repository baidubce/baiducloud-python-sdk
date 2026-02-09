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
import json

"""
This module provides a general model class for baiducloud services.
"""
class AbstractModel(object):
    """

    """
    def __init__(self):
        self._map = None

    def to_dict(self):
        return self._map

    def from_dict(self, map=None):
        pass

    def to_json_string(self, *args, **kwargs):
        if "ensure_ascii" not in kwargs:
            kwargs["ensure_ascii"] = False
        return json.dumps(self.to_dict(), *args, **kwargs)
