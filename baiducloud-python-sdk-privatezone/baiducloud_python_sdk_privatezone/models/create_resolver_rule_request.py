"""
Request entity for CreateResolverRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_privatezone.models.dns_server_config import DnsServerConfig


class CreateResolverRuleRequest(AbstractModel):
    """
    Request entity for CreateResolverRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, zone, resolver_id, dns_server_configs, client_token=None, description=None):
        """
        Initialize CreateResolverRuleRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 转发规则名称，大小写字母、数字、中文以及 `-_/ .` 特殊字符，必须以字母或者中文开头，长度1-65
        :type name: str (required)

        :param description: 转发规则描述，最长不超过200个字符
        :type description: str (optional)

        :param zone: 转发的私有域
        :type zone: str (required)

        :param resolver_id: 必须为出站解析器，使用该出站终端节点将DNS查询流量转发到目标IP地址列表中指定的IP地址
        :type resolver_id: str (required)

        :param dns_server_configs: 外部DNS系统的IP地址和端口列表
        :type dns_server_configs: List[DnsServerConfig] (required)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.description = description
        self.zone = zone
        self.resolver_id = resolver_id
        self.dns_server_configs = dns_server_configs

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
        if self.zone is not None:
            result['zone'] = self.zone
        if self.resolver_id is not None:
            result['resolverId'] = self.resolver_id
        if self.dns_server_configs is not None:
            result['dnsServerConfigs'] = [i.to_dict() for i in self.dns_server_configs]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateResolverRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('resolverId') is not None:
            self.resolver_id = m.get('resolverId')
        if m.get('dnsServerConfigs') is not None:
            self.dns_server_configs = [DnsServerConfig().from_dict(i) for i in m.get('dnsServerConfigs')]
        return self
