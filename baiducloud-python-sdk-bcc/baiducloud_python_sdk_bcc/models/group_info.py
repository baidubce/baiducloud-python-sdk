"""
GroupInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GroupInfo(AbstractModel):
    """
    GroupInfo
    """

    def __init__(self, group_id=None, group_name=None):
        """
        Initialize GroupInfo instance.

        :param group_id: 资源组id
        :type group_id: str (optional)

        :param group_name: 资源组名称
        :type group_name: str (optional)
        """
        super().__init__()
        self.group_id = group_id
        self.group_name = group_name

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
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GroupInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        return self
