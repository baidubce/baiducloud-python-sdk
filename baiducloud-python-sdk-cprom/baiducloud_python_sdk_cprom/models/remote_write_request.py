"""
Request entity for RemoteWriteRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoteWriteRequest(AbstractModel):
    """
    Request entity for RemoteWriteRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, remote_write_url, body, content_type, content_encoding, instance_id, authorization):
        """
        Initialize RemoteWriteRequest request entity.

        :param remote_write_url: remote_write_url parameter
        :type remote_write_url: str (required)

        :param body: body parameter
        :type body: bytearray (required)

        :param content_type: content_type parameter
        :type content_type: str (required)

        :param content_encoding: content_encoding parameter
        :type content_encoding: str (required)

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param authorization: authorization parameter
        :type authorization: str (required)
        """
        super().__init__()
        self.remote_write_url = remote_write_url
        self.body = body
        self.content_type = content_type
        self.content_encoding = content_encoding
        self.instance_id = instance_id
        self.authorization = authorization

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoteWriteRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('remoteWriteUrl') is not None:
            self.remote_write_url = m.get('remoteWriteUrl')
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('Content-Type') is not None:
            self.content_type = m.get('Content-Type')
        if m.get('Content-Encoding') is not None:
            self.content_encoding = m.get('Content-Encoding')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self
