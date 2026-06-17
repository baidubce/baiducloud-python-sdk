"""
Request entity for BatchAddIpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchAddIpRequest(AbstractModel):
    """
    Request entity for BatchAddIpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, instance_id, allocate_multi_ipv6_addr, secondary_private_ip_address_count=None, private_ips=None
    ):
        """
        Initialize BatchAddIpRequest request entity.

        :param instance_id: 虚机ID
        :type instance_id: str (required)

        :param secondary_private_ip_address_count: 需要增加IPV6/IPV4的数量，与privateIps必须存在一个
        :type secondary_private_ip_address_count: int (optional)

        :param private_ips: 需要增加的IPV6/IPV4地址，与secondaryPrivateIpAddressCount必须存在一个
        :type private_ips: List[str] (optional)

        :param allocate_multi_ipv6_addr: 是否分配IPV6，创建IPV6必须是true
        :type allocate_multi_ipv6_addr: bool (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        self.private_ips = private_ips
        self.allocate_multi_ipv6_addr = allocate_multi_ipv6_addr

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
        if self.secondary_private_ip_address_count is not None:
            result['secondaryPrivateIpAddressCount'] = self.secondary_private_ip_address_count
        if self.private_ips is not None:
            result['privateIps'] = self.private_ips
        if self.allocate_multi_ipv6_addr is not None:
            result['allocateMultiIpv6Addr'] = self.allocate_multi_ipv6_addr
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchAddIpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('secondaryPrivateIpAddressCount') is not None:
            self.secondary_private_ip_address_count = m.get('secondaryPrivateIpAddressCount')
        if m.get('privateIps') is not None:
            self.private_ips = m.get('privateIps')
        if m.get('allocateMultiIpv6Addr') is not None:
            self.allocate_multi_ipv6_addr = m.get('allocateMultiIpv6Addr')
        return self
