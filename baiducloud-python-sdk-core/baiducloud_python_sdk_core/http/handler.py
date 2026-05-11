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
This module provides general http handler functions for processing http responses from BCE services.
"""

import http.client
from builtins import str
from builtins import bytes
import json
from baiducloud_python_sdk_core import utils
from baiducloud_python_sdk_core import compat
from baiducloud_python_sdk_core.exception import BceClientError
from baiducloud_python_sdk_core.exception import BceServerError
from baiducloud_python_sdk_core.bce_response import BceStreamResponse


def parse_stream(http_response, response):
    """
    Handle stream responses for both BceStreamResponse and Response models with stream fields.

    For BceStreamResponse: sets _stream and _http_response
    For Response models: finds the stream field (marked with x-bce-stream:download) and assigns http_response to it

    :param http_response: the http_response object returned by HTTPConnection.getresponse()
    :param response: response object (BceStreamResponse or Response model with stream field)
    :return: True if handled as stream, False to continue handler chain
    """
    if isinstance(response, BceStreamResponse):
        # Legacy BceStreamResponse handling
        response._stream = http_response
        response._http_response = http_response

        # Get content type
        content_type = None
        for k, v in response.metadata.items():
            if k.lower() == 'content-type':
                content_type = v
                break
        response.content_type = content_type

        # Get content length
        content_length = -1
        for k, v in response.metadata.items():
            if k.lower() == 'content-length':
                try:
                    content_length = int(v)
                except (ValueError, TypeError):
                    pass
                break
        response.content_length = content_length

        # Return True to stop the handler chain
        return True

    # Check if response model has a stream field (e.g., GetObjectResponse.object_content)
    # Look for fields that should contain the stream (typically named like object_content, body, etc.)
    stream_field_candidates = ['object_content', 'body', 'content', 'data']

    for field_name in stream_field_candidates:
        if hasattr(response, field_name):
            # Set the http_response as the stream field value
            setattr(response, field_name, http_response)
            # Return True to indicate we handled the stream and stop further processing
            return True
    # Not a stream response, continue to next handler
    return False


def parse_json(http_response, response):
    """If the body is not empty, convert it to a python object and set as the value of
    response.body. http_response is always closed if no error occurs.

    :param http_response: the http_response object returned by HTTPConnection.getresponse()
    :type http_response: httplib.HTTPResponse

    :param response: general response object which will be returned to the caller
    :type response: baiducloud_python_sdk_core.BceResponse

    :return: always true
    :rtype bool
    """
    body = http_response.read()
    if body:
        body = compat.convert_to_string(body)
        obj = json.loads(body)
        if isinstance(obj, dict):
            response.from_dict(obj)
    http_response.close()
    return True


def parse_error(http_response, response):
    """If the body is not empty, convert it to a python object and set as the value of
    response.body. http_response is always closed if no error occurs.

    :param http_response: the http_response object returned by HTTPConnection.getresponse()
    :type http_response: httplib.HTTPResponse

    :param response: general response object which will be returned to the caller
    :type response: baiducloud_python_sdk_core.BceResponse

    :return: false if http status code is 2xx, raise an error otherwise
    :rtype bool

    :raise baiducloud_python_sdk_core.exception.BceClientError: if http status code is NOT 2xx
    """
    if http_response.status // 100 == http.client.OK // 100:
        return False
    if http_response.status // 100 == http.client.CONTINUE // 100:
        raise BceClientError(b'Can not handle 1xx http status code')
    bse = None
    body = http_response.read()
    if body:
        d = json.loads(compat.convert_to_string(body))
        bse = BceServerError(d['message'], code=d['code'], request_id=d['requestId'])
    if bse is None:
        request_id = response.metadata.get('x-bce-request-id')
        bse = BceServerError(http_response.reason, request_id=request_id)
    bse.status_code = http_response.status
    raise bse
