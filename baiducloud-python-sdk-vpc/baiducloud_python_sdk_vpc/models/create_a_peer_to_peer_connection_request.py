"""
Request entity for CreateAPeerToPeerConnectionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.billing import Billing
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class CreateAPeerToPeerConnectionRequest(AbstractModel):
    """
    Request entity for CreateAPeerToPeerConnectionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        bandwidth_in_mbps,
        local_vpc_id,
        peer_vpc_id,
        peer_region,
        billing,
        client_token=None,
        description=None,
        local_if_name=None,
        peer_account_id=None,
        peer_if_name=None,
        tags=None,
        resource_group_id=None,
        delete_protect=None,
    ):
        """
        Initialize CreateAPeerToPeerConnectionRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param bandwidth_in_mbps: 对等连接的带宽
        :type bandwidth_in_mbps: int (required)

        :param description: 对等连接的备注
        :type description: str (optional)

        :param local_if_name: 本端接口名称
        :type local_if_name: str (optional)

        :param local_vpc_id: 本端VPC的ID
        :type local_vpc_id: str (required)

        :param peer_account_id: 对端账户ID，只有在建立跨账号的对等连接时需要该字段
        :type peer_account_id: str (optional)

        :param peer_vpc_id: 对等连接对端VPC的ID
        :type peer_vpc_id: str (required)

        :param peer_region: 对等连接的对端区域
        :type peer_region: str (required)

        :param peer_if_name: 对等连接对端接口名称，只有本账号的对等连接才允许设置该字段
        :type peer_if_name: str (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param tags: 待创建的标签键值对列表
        :type tags: List[TagModel] (optional)

        :param resource_group_id: 资源组ID
        :type resource_group_id: str (optional)

        :param delete_protect: 是否开启释放保护。缺省值为false，代表允许删除
        :type delete_protect: bool (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.description = description
        self.local_if_name = local_if_name
        self.local_vpc_id = local_vpc_id
        self.peer_account_id = peer_account_id
        self.peer_vpc_id = peer_vpc_id
        self.peer_region = peer_region
        self.peer_if_name = peer_if_name
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
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.description is not None:
            result['description'] = self.description
        if self.local_if_name is not None:
            result['localIfName'] = self.local_if_name
        if self.local_vpc_id is not None:
            result['localVpcId'] = self.local_vpc_id
        if self.peer_account_id is not None:
            result['peerAccountId'] = self.peer_account_id
        if self.peer_vpc_id is not None:
            result['peerVpcId'] = self.peer_vpc_id
        if self.peer_region is not None:
            result['peerRegion'] = self.peer_region
        if self.peer_if_name is not None:
            result['peerIfName'] = self.peer_if_name
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
        :rtype: CreateAPeerToPeerConnectionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('localIfName') is not None:
            self.local_if_name = m.get('localIfName')
        if m.get('localVpcId') is not None:
            self.local_vpc_id = m.get('localVpcId')
        if m.get('peerAccountId') is not None:
            self.peer_account_id = m.get('peerAccountId')
        if m.get('peerVpcId') is not None:
            self.peer_vpc_id = m.get('peerVpcId')
        if m.get('peerRegion') is not None:
            self.peer_region = m.get('peerRegion')
        if m.get('peerIfName') is not None:
            self.peer_if_name = m.get('peerIfName')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self
