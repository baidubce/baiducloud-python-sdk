# Copyright 2024 Baidu, Inc.
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
Host annotation utilities for marking and checking host fields.
"""

# Host 装饰器标记
HOST_ANNOTATION = '__bce_host__'


def host(func_or_attr):
    """
    Decorator to mark a function or attribute as a host field.

    :param func_or_attr: Function or attribute to mark
    :return: The decorated function or attribute
    """
    setattr(func_or_attr, HOST_ANNOTATION, True)
    return func_or_attr


def is_host_field(obj):
    """
    Check if an object is marked as a host field.

    :param obj: Object to check
    :return: True if the object is marked as a host field
    """
    return hasattr(obj, HOST_ANNOTATION) and getattr(obj, HOST_ANNOTATION) is True
