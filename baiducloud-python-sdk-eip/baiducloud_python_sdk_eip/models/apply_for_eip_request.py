"""
Request entity for ApplyForEipRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_eip.models.billing import Billing
from baiducloud_python_sdk_eip.models.tag_model import TagModel


class ApplyForEipRequest(AbstractModel):
    """
    Request entity for ApplyForEipRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        bandwidth_in_mbps,
        billing,
        client_token=None,
        ip_version=None,
        route_type=None,
        name=None,
        tags=None,
        resource_group_id=None,
        auto_renew_time_unit=None,
        auto_renew_time=None,
        delete_protect=None,
    ):
        """
        Initialize ApplyForEipRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_version: EIP IP类型，包含ipv4和ipv6，默认ipv4。
        :type ip_version: str (optional)

        :param route_type: EIP线路类型，包含标准BGP（BGP）和增强BGP（BGP_S），默认标准BGP。
        :type route_type: str (optional)

        :param bandwidth_in_mbps:
            公网带宽，单位为Mbps。对于预付费以及按使用带宽计费的后付费EIP，标准型BGP限制为1~500之间的整数，增强型BGP限制为100~5000之间的整数（代表带宽上限）；对于按使用流量计费的后付费EIP，
            标准型BGP限制为1~200之间的整数（代表允许的带宽流量峰值）
        :type bandwidth_in_mbps: int (required)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param name: 长度1~65个字节，字母开头，可包含字母数字-\\_/.字符。若不传该参数，服务会自动生成name。
        :type name: str (optional)

        :param tags: 待创建的标签键值对列表。
        :type tags: List[TagModel] (optional)

        :param resource_group_id: 创建EIP的同时绑定的资源分组的ID
        :type resource_group_id: str (optional)

        :param auto_renew_time_unit: 支持创建 EIP同时开通自动续费，取值为 month 获 year （默认 month）。
        :type auto_renew_time_unit: str (optional)

        :param auto_renew_time: 支持创建 EIP同时开通自动续费，根据autoRenewTimeUnit的取值有不同的范围，month 为1到9，year 为1到3。
        :type auto_renew_time: int (optional)

        :param delete_protect: 是否开启释放保护。缺省值为false，代表允许删除
        :type delete_protect: bool (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.ip_version = ip_version
        self.route_type = route_type
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.billing = billing
        self.name = name
        self.tags = tags
        self.resource_group_id = resource_group_id
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time
        self.delete_protect = delete_protect

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
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.name is not None:
            result['name'] = self.name
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ApplyForEipRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self
