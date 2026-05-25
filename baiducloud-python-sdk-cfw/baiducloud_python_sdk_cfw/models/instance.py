"""
Instance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Instance(AbstractModel):
    """
    Instance
    """

    def __init__(
        self,
        instance_id=None,
        instance_name=None,
        status=None,
        region=None,
        cfw_id=None,
        cfw_name=None,
        vpc_id=None,
        vpc_name=None,
        public_ip=None,
        role=None,
        local_if_id=None,
        local_if_name=None,
        peer_region=None,
        peer_vpc_id=None,
        peer_vpc_name=None,
        member_id=None,
        member_name=None,
        member_account_id=None,
    ):
        """
        Initialize Instance instance.

        :param instance_id: 防火墙边界实例的id
        :type instance_id: str (optional)

        :param instance_name: 防火墙边界实例的name
        :type instance_name: str (optional)

        :param status: 防护状态，取值 \\[ unbound \\| protected \\| unprotected \\]
        :type status: str (optional)

        :param region: region attribute
        :type region: str (optional)

        :param cfw_id: 关联的CFW的id
        :type cfw_id: str (optional)

        :param cfw_name: 关联的CFW的name
        :type cfw_name: str (optional)

        :param vpc_id: VPC边界实例特有属性，所属VPC的id
        :type vpc_id: str (optional)

        :param vpc_name: VPC边界实例特有属性，所属VPC的name
        :type vpc_name: str (optional)

        :param public_ip: EIP实例特有属性
        :type public_ip: str (optional)

        :param role: PEERCONN特有属性，本端角色，取值\\[ acceptor \\| initiator ]
        :type role: str (optional)

        :param local_if_id: PEERCONN实例特有属性，本端端口的id
        :type local_if_id: str (optional)

        :param local_if_name: PEERCONN实例特有属性，本端端口的name
        :type local_if_name: str (optional)

        :param peer_region: PEERCONN实例特有属性，对端地域
        :type peer_region: str (optional)

        :param peer_vpc_id: PEERCONN实例特有属性，对端VPC的id
        :type peer_vpc_id: str (optional)

        :param peer_vpc_name: PEERCONN实例特有属性，对端VPC的name
        :type peer_vpc_name: str (optional)

        :param member_id: CSN实例特有属性，CSN中网络实例的id
        :type member_id: str (optional)

        :param member_name: CSN实例特有属性，CSN中网络实例的name
        :type member_name: str (optional)

        :param member_account_id: CSN实例特有属性，CSN中网络实例的所属用户
        :type member_account_id: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.status = status
        self.region = region
        self.cfw_id = cfw_id
        self.cfw_name = cfw_name
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.public_ip = public_ip
        self.role = role
        self.local_if_id = local_if_id
        self.local_if_name = local_if_name
        self.peer_region = peer_region
        self.peer_vpc_id = peer_vpc_id
        self.peer_vpc_name = peer_vpc_name
        self.member_id = member_id
        self.member_name = member_name
        self.member_account_id = member_account_id

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.status is not None:
            result['status'] = self.status
        if self.region is not None:
            result['region'] = self.region
        if self.cfw_id is not None:
            result['cfwId'] = self.cfw_id
        if self.cfw_name is not None:
            result['cfwName'] = self.cfw_name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['vpcName'] = self.vpc_name
        if self.public_ip is not None:
            result['publicIp'] = self.public_ip
        if self.role is not None:
            result['role'] = self.role
        if self.local_if_id is not None:
            result['localIfId'] = self.local_if_id
        if self.local_if_name is not None:
            result['localIfName'] = self.local_if_name
        if self.peer_region is not None:
            result['peerRegion'] = self.peer_region
        if self.peer_vpc_id is not None:
            result['peerVpcId'] = self.peer_vpc_id
        if self.peer_vpc_name is not None:
            result['peerVpcName'] = self.peer_vpc_name
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.member_name is not None:
            result['memberName'] = self.member_name
        if self.member_account_id is not None:
            result['memberAccountId'] = self.member_account_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Instance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        if m.get('cfwName') is not None:
            self.cfw_name = m.get('cfwName')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcName') is not None:
            self.vpc_name = m.get('vpcName')
        if m.get('publicIp') is not None:
            self.public_ip = m.get('publicIp')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('localIfId') is not None:
            self.local_if_id = m.get('localIfId')
        if m.get('localIfName') is not None:
            self.local_if_name = m.get('localIfName')
        if m.get('peerRegion') is not None:
            self.peer_region = m.get('peerRegion')
        if m.get('peerVpcId') is not None:
            self.peer_vpc_id = m.get('peerVpcId')
        if m.get('peerVpcName') is not None:
            self.peer_vpc_name = m.get('peerVpcName')
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('memberName') is not None:
            self.member_name = m.get('memberName')
        if m.get('memberAccountId') is not None:
            self.member_account_id = m.get('memberAccountId')
        return self
