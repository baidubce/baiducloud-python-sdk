"""
Request entity for FaceGetListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceGetListRequest(AbstractModel):
    """
    Request entity for FaceGetListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_id, group_id):
        """
        Initialize FaceGetListRequest request entity.

        :param user_id: 用户ID（由数字、字母、下划线组成），长度限制48B
        :type user_id: str (required)

        :param group_id: 用户组ID (由数字、字母、下划线组成），长度限制48B
        :type group_id: str (required)
        """
        super().__init__()
        self.user_id = user_id
        self.group_id = group_id

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
            result['user_id'] = self.user_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceGetListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self
