"""
APIKey information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class APIKey(AbstractModel):
    """
    APIKey
    """

    def __init__(self, id=None, token_id=None, name=None, user_id=None, create_time=None):
        """
        Initialize APIKey instance.

        :param id: API Key在的标识
        :type id: str (optional)

        :param token_id: API Key本身
        :type token_id: str (optional)

        :param name: API Key名称
        :type name: str (optional)

        :param user_id:
        :type user_id: str (optional)

        :param create_time:
        :type create_time: str (optional)
        """
        super().__init__()
        self.id = id
        self.token_id = token_id
        self.name = name
        self.user_id = user_id
        self.create_time = create_time

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: APIKey

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self
