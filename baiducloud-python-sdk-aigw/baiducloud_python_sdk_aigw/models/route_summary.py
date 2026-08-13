"""
RouteSummary information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aigw.models.route_match_path import RouteMatchPath

from baiducloud_python_sdk_aigw.models.target_service import TargetService


class RouteSummary(AbstractModel):
    """
    RouteSummary
    """

    def __init__(
        self,
        route_name=None,
        route_status=None,
        domains=None,
        associated_domain_count=None,
        match_path=None,
        target_service=None,
        create_time=None,
        src_product=None,
    ):
        """
        Initialize RouteSummary instance.

        :param route_name: 路由名称
        :type route_name: str (optional)

        :param route_status: 路由状态，当前为 PUBLISHED
        :type route_status: str (optional)

        :param domains: 绑定的自定义域名
        :type domains: List[str] (optional)

        :param associated_domain_count: 关联域名数量
        :type associated_domain_count: int (optional)

        :param match_path: match_path attribute
        :type match_path: RouteMatchPath (optional)

        :param target_service: 目标服务摘要列表
        :type target_service: List[TargetService] (optional)

        :param create_time: 创建时间，格式为 `YYYY-MM-DD HH:mm:ss`
        :type create_time: str (optional)

        :param src_product: 来源产品标识
        :type src_product: str (optional)
        """
        super().__init__()
        self.route_name = route_name
        self.route_status = route_status
        self.domains = domains
        self.associated_domain_count = associated_domain_count
        self.match_path = match_path
        self.target_service = target_service
        self.create_time = create_time
        self.src_product = src_product

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
        if self.route_name is not None:
            result['routeName'] = self.route_name
        if self.route_status is not None:
            result['routeStatus'] = self.route_status
        if self.domains is not None:
            result['domains'] = self.domains
        if self.associated_domain_count is not None:
            result['associatedDomainCount'] = self.associated_domain_count
        if self.match_path is not None:
            result['matchPath'] = self.match_path.to_dict()
        if self.target_service is not None:
            result['targetService'] = [i.to_dict() for i in self.target_service]
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.src_product is not None:
            result['srcProduct'] = self.src_product
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RouteSummary

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('routeName') is not None:
            self.route_name = m.get('routeName')
        if m.get('routeStatus') is not None:
            self.route_status = m.get('routeStatus')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('associatedDomainCount') is not None:
            self.associated_domain_count = m.get('associatedDomainCount')
        if m.get('matchPath') is not None:
            self.match_path = RouteMatchPath().from_dict(m.get('matchPath'))
        if m.get('targetService') is not None:
            self.target_service = [TargetService().from_dict(i) for i in m.get('targetService')]
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('srcProduct') is not None:
            self.src_product = m.get('srcProduct')
        return self
