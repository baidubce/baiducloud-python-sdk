"""
Request entity for EnableAccessKeyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EnableAccessKeyRequest(AbstractModel):
    """
    Request entity for EnableAccessKeyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_name, access_key_id):
        """
        Initialize EnableAccessKeyRequest request entity.

        :param user_name: user_name parameter
        :type user_name: str (required)

        :param access_key_id: access_key_id parameter
        :type access_key_id: str (required)
        """
        super().__init__()
        self.user_name = user_name
        self.access_key_id = access_key_id

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EnableAccessKeyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        return self
