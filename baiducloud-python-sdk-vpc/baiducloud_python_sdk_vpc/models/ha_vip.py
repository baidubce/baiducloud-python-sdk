"""
HaVip information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HaVip(AbstractModel):
    """
    HaVip
    """

    def __init__(
        self,
        ha_vip_id=None,
        name=None,
        description=None,
        vpc_id=None,
        subnet_id=None,
        status=None,
        private_ip_address=None,
        public_ip_address=None,
        created_time=None,
    ):
        """
        Initialize HaVip instance.

        :param ha_vip_id: 高可用虚拟IP的ID
        :type ha_vip_id: str (optional)

        :param name: 高可用虚拟IP的名称
        :type name: str (optional)

        :param description: 高可用虚拟IP的描述
        :type description: str (optional)

        :param vpc_id: 高可用虚拟IP所在VPC的ID
        :type vpc_id: str (optional)

        :param subnet_id: 高可用虚拟IP所在子网的ID
        :type subnet_id: str (optional)

        :param status: 高可用虚拟IP的状态，\"available\"表示可用，\"binded\"表示已绑定实例
        :type status: str (optional)

        :param private_ip_address: 高可用虚拟IP内网地址
        :type private_ip_address: str (optional)

        :param public_ip_address: 高可用虚拟IP公网地址
        :type public_ip_address: str (optional)

        :param created_time: 高可用虚拟IP实例创建时间
        :type created_time: str (optional)
        """
        super().__init__()
        self.ha_vip_id = ha_vip_id
        self.name = name
        self.description = description
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.status = status
        self.private_ip_address = private_ip_address
        self.public_ip_address = public_ip_address
        self.created_time = created_time

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
        if self.ha_vip_id is not None:
            result['haVipId'] = self.ha_vip_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.status is not None:
            result['status'] = self.status
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
        if self.public_ip_address is not None:
            result['publicIpAddress'] = self.public_ip_address
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HaVip

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('haVipId') is not None:
            self.ha_vip_id = m.get('haVipId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        if m.get('publicIpAddress') is not None:
            self.public_ip_address = m.get('publicIpAddress')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        return self
