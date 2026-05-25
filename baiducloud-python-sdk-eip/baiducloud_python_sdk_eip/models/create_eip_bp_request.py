"""
Request entity for CreateEipBpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_eip.models.tag_model import TagModel


class CreateEipBpRequest(AbstractModel):
    """
    Request entity for CreateEipBpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        eip,
        eip_group_id,
        bandwidth_in_mbps,
        client_token=None,
        name=None,
        type=None,
        auto_release_time=None,
        tags=None,
        resource_group_id=None,
    ):
        """
        Initialize CreateEipBpRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 带宽包名称，不填将自动生成
        :type name: str (optional)

        :param eip: 带宽包绑定的弹性公网EIP的Ip地址
        :type eip: str (required)

        :param eip_group_id: 带宽包绑定的共享带宽id
        :type eip_group_id: str (required)

        :param bandwidth_in_mbps: 带宽包的公网带宽
        :type bandwidth_in_mbps: int (required)

        :param type: type parameter
        :type type: str (optional)

        :param auto_release_time: 带宽包自动释放时间，时间格式要求符合UTC格式（格式形如：”2019-08-03T20:38:43Z”）
        :type auto_release_time: str (optional)

        :param tags: 待创建的标签键值对列表。
        :type tags: List[TagModel] (optional)

        :param resource_group_id: 创建带宽包的同时绑定的资源分组的ID
        :type resource_group_id: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.eip = eip
        self.eip_group_id = eip_group_id
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.type = type
        self.auto_release_time = auto_release_time
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
        if self.name is not None:
            result['name'] = self.name
        if self.eip is not None:
            result['eip'] = self.eip
        if self.eip_group_id is not None:
            result['eipGroupId'] = self.eip_group_id
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.type is not None:
            result['type'] = self.type
        if self.auto_release_time is not None:
            result['autoReleaseTime'] = self.auto_release_time
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
        :rtype: CreateEipBpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('eipGroupId') is not None:
            self.eip_group_id = m.get('eipGroupId')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('autoReleaseTime') is not None:
            self.auto_release_time = m.get('autoReleaseTime')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self
