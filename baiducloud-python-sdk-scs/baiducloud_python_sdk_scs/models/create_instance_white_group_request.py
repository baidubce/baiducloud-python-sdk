"""
Request entity for CreateInstanceWhiteGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateInstanceWhiteGroupRequest(AbstractModel):
    """
    Request entity for CreateInstanceWhiteGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, group_name, cluster_ip_list):
        """
        Initialize CreateInstanceWhiteGroupRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param group_name: 白名单分组名称
        :type group_name: str (required)

        :param cluster_ip_list: 白名单分组名称
        :type cluster_ip_list: List[str] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.group_name = group_name
        self.cluster_ip_list = cluster_ip_list

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
        if self.cluster_ip_list is not None:
            result['clusterIpList'] = self.cluster_ip_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateInstanceWhiteGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('clusterIpList') is not None:
            self.cluster_ip_list = m.get('clusterIpList')
        return self
