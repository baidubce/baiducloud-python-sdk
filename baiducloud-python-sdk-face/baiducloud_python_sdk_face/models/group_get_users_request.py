"""
Request entity for GroupGetUsersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GroupGetUsersRequest(AbstractModel):
    """
    Request entity for GroupGetUsersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, start=None, length=None):
        """
        Initialize GroupGetUsersRequest request entity.

        :param group_id: 用户组ID，长度限制48B
        :type group_id: str (required)

        :param start: 起始序号，默认为0
        :type start: int (optional)

        :param length: 返回数量，默认100，最大1000
        :type length: int (optional)
        """
        super().__init__()
        self.group_id = group_id
        self.start = start
        self.length = length

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
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.start is not None:
            result['start'] = self.start
        if self.length is not None:
            result['length'] = self.length
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GroupGetUsersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('length') is not None:
            self.length = m.get('length')
        return self
