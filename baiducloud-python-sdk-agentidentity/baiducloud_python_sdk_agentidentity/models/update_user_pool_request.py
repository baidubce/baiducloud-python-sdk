"""
Request entity for UpdateUserPoolRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateUserPoolRequest(AbstractModel):
    """
    Request entity for UpdateUserPoolRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, name=None, description=None):
        """
        Initialize UpdateUserPoolRequest request entity.

        :param id: 用户池 ID
        :type id: str (required)

        :param name: 新的用户池名称
        :type name: str (optional)

        :param description: 新的用户池描述；不传保持不变，传空字符串表示清空
        :type description: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.description = description

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateUserPoolRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
