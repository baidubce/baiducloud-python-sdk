"""
Request entity for CreateEipGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_eip.models.billing import Billing
from baiducloud_python_sdk_eip.models.tag_model import TagModel


class CreateEipGroupRequest(AbstractModel):
    """
    Request entity for CreateEipGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        bandwidth_in_mbps,
        billing,
        client_token=None,
        route_type=None,
        eip_count=None,
        eipv6_count=None,
        name=None,
        tags=None,
        resource_group_id=None,
    ):
        """
        Initialize CreateEipGroupRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param route_type: 线路类型，包含标准BGP（BGP）和增强BGP（BGP_S），默认标准BGP。
        :type route_type: str (optional)

        :param eip_count: eip_count parameter
        :type eip_count: int (optional)

        :param eipv6_count: 共享带宽中IPv6 EIP的个数。公网IPv6数量最少为0个，最多受配额控制，默认是256个。
        :type eipv6_count: int (optional)

        :param bandwidth_in_mbps: bandwidth_in_mbps parameter
        :type bandwidth_in_mbps: int (required)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param name: 长度1~65个字节，字母开头，可包含字母数字-\\_/.字符。若不传该参数，服务会自动生成name
        :type name: str (optional)

        :param tags: 待创建的标签键值对列表。
        :type tags: List[TagModel] (optional)

        :param resource_group_id: 创建共享带宽的同时绑定的资源分组的ID
        :type resource_group_id: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.route_type = route_type
        self.eip_count = eip_count
        self.eipv6_count = eipv6_count
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.billing = billing
        self.name = name
        self.tags = tags
        self.resource_group_id = resource_group_id

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
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.eip_count is not None:
            result['eipCount'] = self.eip_count
        if self.eipv6_count is not None:
            result['eipv6Count'] = self.eipv6_count
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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateEipGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('eipCount') is not None:
            self.eip_count = m.get('eipCount')
        if m.get('eipv6Count') is not None:
            self.eipv6_count = m.get('eipv6Count')
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
        return self
