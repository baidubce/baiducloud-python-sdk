"""
Request entity for CreateSubnetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class CreateSubnetRequest(AbstractModel):
    """
    Request entity for CreateSubnetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        zone_name,
        cidr,
        vpc_id,
        client_token=None,
        enable_ipv6=None,
        vpc_secondary_cidr=None,
        subnet_type=None,
        description=None,
        tags=None,
    ):
        """
        Initialize CreateSubnetRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 子网名称，不能取值\"default\"，长度不超过65个字符，可由数字、字符、下划线组成
        :type name: str (required)

        :param enable_ipv6: 是否开启IPv6网段，true表示开启，默认false不开启
        :type enable_ipv6: bool (optional)

        :param zone_name: 可用区名称，其查询方式参考[查询可用区列表](BCC/API参考/地域及可用区相关接口/查询可用区列表.md)
        :type zone_name: str (required)

        :param cidr: 子网cidr，需在所属VPC网段范围内
        :type cidr: str (required)

        :param vpc_id: 子网所属VPC的ID
        :type vpc_id: str (required)

        :param vpc_secondary_cidr: 子网所属VPC的辅助网段的cidr
        :type vpc_secondary_cidr: str (optional)

        :param subnet_type: 子网类型，BCC、BBC
        :type subnet_type: str (optional)

        :param description: 描述，不超过200字符
        :type description: str (optional)

        :param tags: 待创建的标签键值对列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.enable_ipv6 = enable_ipv6
        self.zone_name = zone_name
        self.cidr = cidr
        self.vpc_id = vpc_id
        self.vpc_secondary_cidr = vpc_secondary_cidr
        self.subnet_type = subnet_type
        self.description = description
        self.tags = tags

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
        if self.name is not None:
            result['name'] = self.name
        if self.enable_ipv6 is not None:
            result['enableIpv6'] = self.enable_ipv6
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_secondary_cidr is not None:
            result['vpcSecondaryCidr'] = self.vpc_secondary_cidr
        if self.subnet_type is not None:
            result['subnetType'] = self.subnet_type
        if self.description is not None:
            result['description'] = self.description
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSubnetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcSecondaryCidr') is not None:
            self.vpc_secondary_cidr = m.get('vpcSecondaryCidr')
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
