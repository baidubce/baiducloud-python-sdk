"""
Request entity for ModifySyncGroupNameRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifySyncGroupNameRequest(AbstractModel):
    """
    Request entity for ModifySyncGroupNameRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, sync_group_show_id, group_name):
        """
        Initialize ModifySyncGroupNameRequest request entity.

        :param sync_group_show_id: sync_group_show_id parameter
        :type sync_group_show_id: str (required)

        :param group_name: 修改后的实例组名称。
        :type group_name: str (required)
        """
        super().__init__()
        self.sync_group_show_id = sync_group_show_id
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
        :rtype: ModifySyncGroupNameRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('syncGroupShowId') is not None:
            self.sync_group_show_id = m.get('syncGroupShowId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        return self
