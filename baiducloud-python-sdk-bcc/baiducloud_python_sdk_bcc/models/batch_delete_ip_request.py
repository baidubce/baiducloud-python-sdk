"""
Request entity for BatchDeleteIpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchDeleteIpRequest(AbstractModel):
    """
    Request entity for BatchDeleteIpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, private_ips):
        """
        Initialize BatchDeleteIpRequest request entity.

        :param instance_id: 虚机ID
        :type instance_id: str (required)

        :param private_ips: 需要删除的IPV6/IPV4地址
        :type private_ips: List[str] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.private_ips = private_ips

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.private_ips is not None:
            result['privateIps'] = self.private_ips
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchDeleteIpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('privateIps') is not None:
            self.private_ips = m.get('privateIps')
        return self
