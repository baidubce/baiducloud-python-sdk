"""
Request entity for GroupAddRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GroupAddRequest(AbstractModel):
    """
    Request entity for GroupAddRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id):
        """
        Initialize GroupAddRequest request entity.

        :param group_id: 用户组id，标识一组用户（由数字、字母、下划线组成），长度限制48B。
        :type group_id: str (required)
        """
        super().__init__()
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
        :rtype: GroupAddRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self
