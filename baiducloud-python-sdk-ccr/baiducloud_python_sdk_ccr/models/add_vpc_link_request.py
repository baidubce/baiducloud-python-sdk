"""
Request entity for AddVpcLinkRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AddVpcLinkRequest(AbstractModel):
    """
    Request entity for AddVpcLinkRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, vpc_id, subnet_id, ip_type, auto_dns_resolve, ip_address=None):
        """
        Initialize AddVpcLinkRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param vpc_id: 私有网络ID
        :type vpc_id: str (required)

        :param subnet_id: 私有网络子网ID
        :type subnet_id: str (required)

        :param ip_type: IP分配方式，取值范围：auto、manual，分别表示自动分配、手动指定
        :type ip_type: str (required)

        :param ip_address: 当ipType为manual为必填，子网内可用的IP
        :type ip_address: str (optional)

        :param auto_dns_resolve: 自动DNS解析，取值范围：true、false
        :type auto_dns_resolve: bool (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.ip_type = ip_type
        self.ip_address = ip_address
        self.auto_dns_resolve = auto_dns_resolve

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
        if self.vpc_id is not None:
            result['vpcID'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetID'] = self.subnet_id
        if self.ip_type is not None:
            result['ipType'] = self.ip_type
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.auto_dns_resolve is not None:
            result['autoDnsResolve'] = self.auto_dns_resolve
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddVpcLinkRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('vpcID') is not None:
            self.vpc_id = m.get('vpcID')
        if m.get('subnetID') is not None:
            self.subnet_id = m.get('subnetID')
        if m.get('ipType') is not None:
            self.ip_type = m.get('ipType')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('autoDnsResolve') is not None:
            self.auto_dns_resolve = m.get('autoDnsResolve')
        return self
