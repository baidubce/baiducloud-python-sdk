"""
AssociateBlbModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AssociateBlbModel(AbstractModel):
    """
    AssociateBlbModel
    """

    def __init__(
        self,
        blb_id=None,
        name=None,
        status=None,
        blb_type=None,
        public_ip=None,
        eip_route_type=None,
        bandwidth=None,
        address=None,
        ipv6=None,
        vpc_id=None,
        subnet_id=None,
    ):
        """
        Initialize AssociateBlbModel instance.

        :param blb_id: 负载均衡id
        :type blb_id: str (optional)

        :param name: blb名称
        :type name: str (optional)

        :param status: blb状态
        :type status: str (optional)

        :param blb_type: blb类型
        :type blb_type: str (optional)

        :param public_ip: 公网ip
        :type public_ip: str (optional)

        :param eip_route_type: eip线路类型
        :type eip_route_type: str (optional)

        :param bandwidth: 带宽
        :type bandwidth: int (optional)

        :param address: 内网ip地址
        :type address: str (optional)

        :param ipv6: ipv6地址
        :type ipv6: str (optional)

        :param vpc_id: vpcId
        :type vpc_id: str (optional)

        :param subnet_id: 子网id
        :type subnet_id: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.name = name
        self.status = status
        self.blb_type = blb_type
        self.public_ip = public_ip
        self.eip_route_type = eip_route_type
        self.bandwidth = bandwidth
        self.address = address
        self.ipv6 = ipv6
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id

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
        if self.blb_id is not None:
            result['blbId'] = self.blb_id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.blb_type is not None:
            result['blbType'] = self.blb_type
        if self.public_ip is not None:
            result['publicIp'] = self.public_ip
        if self.eip_route_type is not None:
            result['eipRouteType'] = self.eip_route_type
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.address is not None:
            result['address'] = self.address
        if self.ipv6 is not None:
            result['ipv6'] = self.ipv6
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AssociateBlbModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('blbType') is not None:
            self.blb_type = m.get('blbType')
        if m.get('publicIp') is not None:
            self.public_ip = m.get('publicIp')
        if m.get('eipRouteType') is not None:
            self.eip_route_type = m.get('eipRouteType')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('ipv6') is not None:
            self.ipv6 = m.get('ipv6')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        return self
