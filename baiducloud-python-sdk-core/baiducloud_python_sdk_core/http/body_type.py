# Copyright 2024 Baidu, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.
"""
HTTP body type enum for specifying request/response content encoding formats.
"""

from enum import Enum


class BodyType(Enum):
    """
    Enumeration of supported HTTP body content types.
    """

    JSON = "application/json; charset=utf-8"

    FORM = "application/x-www-form-urlencoded; charset=utf-8"

    BINARY = "application/octet-stream"

    XML = "application/xml; charset=utf-8"

    NONE = None
    
    def get_content_type(self):
        """
        Get the content type string value.

        :return: The content type string or None
        """
        return self.value

    def has_content_type(self):
        """
        Check if this body type has a content type value.

        :return: True if content type is not None
        """
        return self.value is not None
    
    def __str__(self):
        """String representation of the body type."""
        if self.value is None:
            return self.name
        return f"{self.name}({self.value})"
    
    def __repr__(self):
        """Detailed string representation."""
        return f"<BodyType.{self.name}: {self.value!r}>"
