"""
Request entity for DeleteApikeyPermanentlyValidRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteApikeyPermanentlyValidRequest(AbstractModel):
    """
    Request entity for DeleteApikeyPermanentlyValidRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, user_id=None):
        """
        Initialize DeleteApikeyPermanentlyValidRequest request entity.

        :param user_id: 子用户Id；如果apikey归属其他子用户则必填
        :type user_id: str (optional)

        :param id: APIKey ID
        :type id: str (required)
        """
        super().__init__()
        self.user_id = user_id
        self.id = id

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
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteApikeyPermanentlyValidRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self
