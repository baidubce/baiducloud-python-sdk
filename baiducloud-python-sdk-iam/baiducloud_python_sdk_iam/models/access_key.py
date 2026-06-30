"""
AccessKey information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AccessKey(AbstractModel):
    """
    AccessKey
    """

    def __init__(self, id=None, secret=None, create_time=None, description=None):
        """
        Initialize AccessKey instance.

        :param id: AccessKey的公开Id，即AK
        :type id: str (optional)

        :param secret: AccessKey的密钥，即SK
        :type secret: str (optional)

        :param create_time: AccessKey的创建时间
        :type create_time: datetime (optional)

        :param description: AccessKey的描述
        :type description: str (optional)
        """
        super().__init__()
        self.id = id
        self.secret = secret
        self.create_time = create_time
        self.description = description

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
        if self.secret is not None:
            result['secret'] = self.secret
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccessKey

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
