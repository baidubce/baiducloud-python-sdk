"""
Request entity for HotGroupModifyNameRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HotGroupModifyNameRequest(AbstractModel):
    """
    Request entity for HotGroupModifyNameRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, group_name):
        """
        Initialize HotGroupModifyNameRequest request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param group_name: 新的名称。规则：支持大小写字母、数字以及-_.等特殊字符，长度6~32
        :type group_name: str (required)
        """
        super().__init__()
        self.group_id = group_id
        self.group_name = group_name

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
        if self.group_name is not None:
            result['groupName'] = self.group_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HotGroupModifyNameRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        return self
