"""
Request entity for UpdateVpcRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateVpcRequest(AbstractModel):
    """
    Request entity for UpdateVpcRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpc_id, name, client_token=None, description=None, enable_ipv6=None, secondary_cidr=None):
        """
        Initialize UpdateVpcRequest request entity.

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: VPC名称，不能取值\"default\"，长度不超过65个字符，可由数字，字符，下划线组成
        :type name: str (required)

        :param description: VPC描述，不超过200字符
        :type description: str (optional)

        :param enable_ipv6: 是否开启Ipv6网段，true开启，false关闭；不传表示不做更改
        :type enable_ipv6: bool (optional)

        :param secondary_cidr: vpc的辅助网段cidr列表，**替换式更新**
        :type secondary_cidr: List[str] (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.enable_ipv6 = enable_ipv6
        self.secondary_cidr = secondary_cidr

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
        if self.description is not None:
            result['description'] = self.description
        if self.enable_ipv6 is not None:
            result['enableIpv6'] = self.enable_ipv6
        if self.secondary_cidr is not None:
            result['secondaryCidr'] = self.secondary_cidr
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateVpcRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enableIpv6') is not None:
            self.enable_ipv6 = m.get('enableIpv6')
        if m.get('secondaryCidr') is not None:
            self.secondary_cidr = m.get('secondaryCidr')
        return self
