"""
EniInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.ip_address import IpAddress


class EniInfo(AbstractModel):
    """
    EniInfo
    """

    def __init__(
        self,
        eni_id=None,
        name=None,
        vpc_id=None,
        subnet_id=None,
        zone_name=None,
        description=None,
        created_time=None,
        instance_id=None,
        mac_address=None,
        status=None,
        security_group_ids=None,
        private_ip_set=None,
    ):
        """
        Initialize EniInfo instance.

        :param eni_id: 网卡ID
        :type eni_id: str (optional)

        :param name: 网卡名称
        :type name: str (optional)

        :param vpc_id: VPC ID
        :type vpc_id: str (optional)

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)

        :param zone_name: 区域
        :type zone_name: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param created_time: 创建时间
        :type created_time: str (optional)

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param mac_address: 物理地址
        :type mac_address: str (optional)

        :param status: 状态
        :type status: str (optional)

        :param security_group_ids: 绑定的安全组列表
        :type security_group_ids: List[str] (optional)

        :param private_ip_set: IP地址信息
        :type private_ip_set: List[IpAddress] (optional)
        """
        super().__init__()
        self.eni_id = eni_id
        self.name = name
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.zone_name = zone_name
        self.description = description
        self.created_time = created_time
        self.instance_id = instance_id
        self.mac_address = mac_address
        self.status = status
        self.security_group_ids = security_group_ids
        self.private_ip_set = private_ip_set

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
        if self.eni_id is not None:
            result['eniId'] = self.eni_id
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.description is not None:
            result['description'] = self.description
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.mac_address is not None:
            result['macAddress'] = self.mac_address
        if self.status is not None:
            result['status'] = self.status
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.private_ip_set is not None:
            result['privateIpSet'] = [i.to_dict() for i in self.private_ip_set]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EniInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('macAddress') is not None:
            self.mac_address = m.get('macAddress')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('privateIpSet') is not None:
            self.private_ip_set = [IpAddress().from_dict(i) for i in m.get('privateIpSet')]
        return self
