"""
GroupGetListResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GroupGetListResult(AbstractModel):
    """
    GroupGetListResult
    """

    def __init__(self, group_id_list=None):
        """
        Initialize GroupGetListResult instance.

        :param group_id_list: 用户组ID列表
        :type group_id_list: List[str] (optional)
        """
        super().__init__()
        self.group_id_list = group_id_list

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
        if self.group_id_list is not None:
            result['group_id_list'] = self.group_id_list
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GroupGetListResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('group_id_list') is not None:
            self.group_id_list = m.get('group_id_list')
        return self
