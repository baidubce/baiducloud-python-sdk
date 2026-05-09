# Copyright 2024 Baidu, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from enum import Enum


class BodyType(Enum):

    JSON = "application/json; charset=utf-8"

    FORM = "application/x-www-form-urlencoded; charset=utf-8"

    BINARY = "application/octet-stream"

    XML = "application/xml; charset=utf-8"

    NONE = None
    
    def get_content_type(self):
        return self.value
    
    def has_content_type(self):
        return self.value is not None
    
    def __str__(self):
        """String representation of the body type."""
        return self.name if self.value is None else f"{self.name}({self.value})"
    
    def __repr__(self):
        """Detailed string representation."""
        return f"<BodyType.{self.name}: {self.value!r}>"
