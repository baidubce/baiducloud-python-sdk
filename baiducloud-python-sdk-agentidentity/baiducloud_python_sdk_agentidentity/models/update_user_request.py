"""
Request entity for UpdateUserRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateUserRequest(AbstractModel):
    """
    Request entity for UpdateUserRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_pool_id, id, display_name=None, description=None):
        """
        Initialize UpdateUserRequest request entity.

        :param user_pool_id: 用户池 ID
        :type user_pool_id: str (required)

        :param id: 用户 ID
        :type id: str (required)

        :param display_name: 新的显示名称
        :type display_name: str (optional)

        :param description: 新的描述
        :type description: str (optional)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
        self.id = id
        self.display_name = display_name
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
        if self.user_pool_id is not None:
            result['userPoolId'] = self.user_pool_id
        if self.id is not None:
            result['id'] = self.id
        if self.display_name is not None:
            result['displayName'] = self.display_name
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
        :rtype: UpdateUserRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
