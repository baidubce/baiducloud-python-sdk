"""
Request entity for UserCopyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UserCopyRequest(AbstractModel):
    """
    Request entity for UserCopyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_id, src_group_id, dst_group_id):
        """
        Initialize UserCopyRequest request entity.

        :param user_id: 用户ID，长度限制48B
        :type user_id: str (required)

        :param src_group_id: 从指定组里复制信息
        :type src_group_id: str (required)

        :param dst_group_id: 需要添加用户的组id
        :type dst_group_id: str (required)
        """
        super().__init__()
        self.user_id = user_id
        self.src_group_id = src_group_id
        self.dst_group_id = dst_group_id

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
        if self.src_group_id is not None:
            result['src_group_id'] = self.src_group_id
        if self.dst_group_id is not None:
            result['dst_group_id'] = self.dst_group_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UserCopyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('src_group_id') is not None:
            self.src_group_id = m.get('src_group_id')
        if m.get('dst_group_id') is not None:
            self.dst_group_id = m.get('dst_group_id')
        return self
