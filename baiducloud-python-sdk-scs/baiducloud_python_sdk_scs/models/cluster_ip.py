"""
ClusterIP information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ClusterIP(AbstractModel):
    """
    ClusterIP
    """

    def __init__(self, group_name=None, ip_list=None):
        """
        Initialize ClusterIP instance.

        :param group_name: 白名单分组名称
        :type group_name: str (optional)

        :param ip_list: 白名单IP列表
        :type ip_list: List[str] (optional)
        """
        super().__init__()
        self.group_name = group_name
        self.ip_list = ip_list

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
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClusterIP

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        return self
