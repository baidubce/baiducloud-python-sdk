"""
Request entity for GetDnsResolverRuleDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_privatezone.models.dns_server_config import DnsServerConfig


class GetDnsResolverRuleDetailResponse(BceResponse):
    """
    GetDnsResolverRuleDetailResponse
    """

    def __init__(
        self,
        id=None,
        name=None,
        status=None,
        description=None,
        zone=None,
        resolver_id=None,
        resolver_region=None,
        dns_server_configs=None,
        create_time=None,
        update_time=None,
    ):
        """
        Initialize GetDnsResolverRuleDetailResponse response.

        :param id: 解析器ID
        :type id: str (optional)

        :param name: 解析器名称
        :type name: str (optional)

        :param status: status field
        :type status: str (optional)

        :param description: 解析器描述
        :type description: str (optional)

        :param zone: 转发私有域
        :type zone: str (optional)

        :param resolver_id: 出站解析器的ID
        :type resolver_id: str (optional)

        :param resolver_region: 出站解析器的地区
        :type resolver_region: str (optional)

        :param dns_server_configs: 外部DNS系统的IP地址和端口
        :type dns_server_configs: List[DnsServerConfig] (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.zone = zone
        self.resolver_id = resolver_id
        self.resolver_region = resolver_region
        self.dns_server_configs = dns_server_configs
        self.create_time = create_time
        self.update_time = update_time

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.description is not None:
            result['description'] = self.description
        if self.zone is not None:
            result['zone'] = self.zone
        if self.resolver_id is not None:
            result['resolverId'] = self.resolver_id
        if self.resolver_region is not None:
            result['resolverRegion'] = self.resolver_region
        if self.dns_server_configs is not None:
            result['dnsServerConfigs'] = [i.to_dict() for i in self.dns_server_configs]
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetDnsResolverRuleDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('resolverId') is not None:
            self.resolver_id = m.get('resolverId')
        if m.get('resolverRegion') is not None:
            self.resolver_region = m.get('resolverRegion')
        if m.get('dnsServerConfigs') is not None:
            self.dns_server_configs = [DnsServerConfig().from_dict(i) for i in m.get('dnsServerConfigs')]
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
