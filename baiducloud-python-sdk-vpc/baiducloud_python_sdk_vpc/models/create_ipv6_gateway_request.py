"""
Request entity for CreateIpv6GatewayRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.billing import Billing
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class CreateIpv6GatewayRequest(AbstractModel):
    """
    Request entity for CreateIpv6GatewayRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        vpc_id,
        name,
        bandwidth_in_mbps,
        billing,
        client_token=None,
        tags=None,
        resource_group_id=None,
        delete_protect=None,
    ):
        """
        Initialize CreateIpv6GatewayRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param vpc_id: vpc的ID
        :type vpc_id: str (required)

        :param name: IPv6网关的名称
        :type name: str (required)

        :param bandwidth_in_mbps: IPv6网关的带宽上限
        :type bandwidth_in_mbps: int (required)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param tags: 待创建的标签键值对列表。
        :type tags: List[TagModel] (optional)

        :param resource_group_id: 资源组
        :type resource_group_id: str (optional)

        :param delete_protect: 是否开启释放保护。缺省值为false，代表允许删除
        :type delete_protect: bool (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.vpc_id = vpc_id
        self.name = name
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.billing = billing
        self.tags = tags
        self.resource_group_id = resource_group_id
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
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
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
        :rtype: CreateIpv6GatewayRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self
