"""
Request entity for CreateDedicatedChannelRouteRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateDedicatedChannelRouteRulesRequest(AbstractModel):
    """
    Request entity for CreateDedicatedChannelRouteRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        et_id,
        et_channel_id,
        dest_address,
        nexthop_type,
        nexthop_id,
        client_token=None,
        ip_version=None,
        description=None,
    ):
        """
        Initialize CreateDedicatedChannelRouteRulesRequest request entity.

        :param et_id: et_id parameter
        :type et_id: str (required)

        :param et_channel_id: et_channel_id parameter
        :type et_channel_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_version: IP协议类型，取值[4 \\| 6]，默认为4
        :type ip_version: int (optional)

        :param dest_address: 目标网段
        :type dest_address: str (required)

        :param nexthop_type: 下一跳类型，取值[\"etGateway\" \\| \"etChannel\"]，分别表示专线网关、专线通道
        :type nexthop_type: str (required)

        :param nexthop_id: 下一跳实例ID
        :type nexthop_id: str (required)

        :param description: 描述
        :type description: str (optional)
        """
        super().__init__()
        self.et_id = et_id
        self.et_channel_id = et_channel_id
        self.client_token = client_token
        self.ip_version = ip_version
        self.dest_address = dest_address
        self.nexthop_type = nexthop_type
        self.nexthop_id = nexthop_id
        self.description = description

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
        if self.dest_address is not None:
            result['destAddress'] = self.dest_address
        if self.nexthop_type is not None:
            result['nexthopType'] = self.nexthop_type
        if self.nexthop_id is not None:
            result['nexthopId'] = self.nexthop_id
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDedicatedChannelRouteRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etId') is not None:
            self.et_id = m.get('etId')
        if m.get('etChannelId') is not None:
            self.et_channel_id = m.get('etChannelId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('destAddress') is not None:
            self.dest_address = m.get('destAddress')
        if m.get('nexthopType') is not None:
            self.nexthop_type = m.get('nexthopType')
        if m.get('nexthopId') is not None:
            self.nexthop_id = m.get('nexthopId')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
