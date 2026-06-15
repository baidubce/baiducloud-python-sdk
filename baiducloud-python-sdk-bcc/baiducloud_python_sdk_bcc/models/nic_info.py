"""
NicInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.eri_info import EriInfo

from baiducloud_python_sdk_bcc.models.eni_info import EniInfo

from baiducloud_python_sdk_bcc.models.ip_info import IpInfo

from baiducloud_python_sdk_bcc.models.ip_info import IpInfo


class NicInfo(AbstractModel):
    """
    NicInfo
    """

    def __init__(
        self,
        eni_id=None,
        eni_uuid=None,
        name=None,
        type=None,
        subnet_id=None,
        subnet_type=None,
        az=None,
        description=None,
        device_id=None,
        status=None,
        mac_address=None,
        vpc_id=None,
        created_time=None,
        eni_num=None,
        eri_num=None,
        eri_infos=None,
        eni_infos=None,
        ips=None,
        ipv6s=None,
        security_groups=None,
        enterprise_security_groups=None,
    ):
        """
        Initialize NicInfo instance.

        :param eni_id: 网卡ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type eni_id: str (optional)

        :param eni_uuid: 网卡长ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type eni_uuid: str (optional)

        :param name: 网卡名称（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type name: str (optional)

        :param type: 网卡类型，primary为主网卡（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type type: str (optional)

        :param subnet_id: 子网ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type subnet_id: str (optional)

        :param subnet_type: 子网类型（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type subnet_type: str (optional)

        :param az: 可用区信息（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type az: str (optional)

        :param description: 描述（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type description: str (optional)

        :param device_id: 虚机长ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type device_id: str (optional)

        :param status: 网卡状态（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type status: str (optional)

        :param mac_address: 物理地址（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type mac_address: str (optional)

        :param vpc_id: VPC ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type vpc_id: str (optional)

        :param created_time: 创建时间（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type created_time: str (optional)

        :param eni_num: 网卡数量（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type eni_num: int (optional)

        :param eri_num: rdma套餐的eri网卡数量（查询实例列表、查询指定实例详情）
        :type eri_num: int (optional)

        :param eri_infos: eri网卡信息（查询实例列表、查询指定实例详情）
        :type eri_infos: List[EriInfo] (optional)

        :param eni_infos: eni网卡信息（查询实例列表、查询指定实例详情）
        :type eni_infos: List[EniInfo] (optional)

        :param ips: 辅助IP和主IP信息（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type ips: List[IpInfo] (optional)

        :param ipv6s: ipv6信息（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type ipv6s: List[IpInfo] (optional)

        :param security_groups: security_groups attribute
        :type security_groups: List[str] (optional)

        :param enterprise_security_groups: 企业安全组短ID列表（主网卡+弹性网卡的企业安全组）（查询实例列表、查询指定实例详情）
        :type enterprise_security_groups: List[str] (optional)
        """
        super().__init__()
        self.eni_id = eni_id
        self.eni_uuid = eni_uuid
        self.name = name
        self.type = type
        self.subnet_id = subnet_id
        self.subnet_type = subnet_type
        self.az = az
        self.description = description
        self.device_id = device_id
        self.status = status
        self.mac_address = mac_address
        self.vpc_id = vpc_id
        self.created_time = created_time
        self.eni_num = eni_num
        self.eri_num = eri_num
        self.eri_infos = eri_infos
        self.eni_infos = eni_infos
        self.ips = ips
        self.ipv6s = ipv6s
        self.security_groups = security_groups
        self.enterprise_security_groups = enterprise_security_groups

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
        if self.eni_uuid is not None:
            result['eniUuid'] = self.eni_uuid
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.subnet_type is not None:
            result['subnetType'] = self.subnet_type
        if self.az is not None:
            result['az'] = self.az
        if self.description is not None:
            result['description'] = self.description
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.status is not None:
            result['status'] = self.status
        if self.mac_address is not None:
            result['macAddress'] = self.mac_address
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.eni_num is not None:
            result['eniNum'] = self.eni_num
        if self.eri_num is not None:
            result['eriNum'] = self.eri_num
        if self.eri_infos is not None:
            result['eriInfos'] = [i.to_dict() for i in self.eri_infos]
        if self.eni_infos is not None:
            result['eniInfos'] = [i.to_dict() for i in self.eni_infos]
        if self.ips is not None:
            result['ips'] = [i.to_dict() for i in self.ips]
        if self.ipv6s is not None:
            result['ipv6s'] = [i.to_dict() for i in self.ipv6s]
        if self.security_groups is not None:
            result['securityGroups'] = self.security_groups
        if self.enterprise_security_groups is not None:
            result['enterpriseSecurityGroups'] = self.enterprise_security_groups
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NicInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')
        if m.get('eniUuid') is not None:
            self.eni_uuid = m.get('eniUuid')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('az') is not None:
            self.az = m.get('az')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('macAddress') is not None:
            self.mac_address = m.get('macAddress')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('eniNum') is not None:
            self.eni_num = m.get('eniNum')
        if m.get('eriNum') is not None:
            self.eri_num = m.get('eriNum')
        if m.get('eriInfos') is not None:
            self.eri_infos = [EriInfo().from_dict(i) for i in m.get('eriInfos')]
        if m.get('eniInfos') is not None:
            self.eni_infos = [EniInfo().from_dict(i) for i in m.get('eniInfos')]
        if m.get('ips') is not None:
            self.ips = [IpInfo().from_dict(i) for i in m.get('ips')]
        if m.get('ipv6s') is not None:
            self.ipv6s = [IpInfo().from_dict(i) for i in m.get('ipv6s')]
        if m.get('securityGroups') is not None:
            self.security_groups = m.get('securityGroups')
        if m.get('enterpriseSecurityGroups') is not None:
            self.enterprise_security_groups = m.get('enterpriseSecurityGroups')
        return self
