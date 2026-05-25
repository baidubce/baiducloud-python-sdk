"""
Request entity for BindPhysicalDedicatedLineRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BindPhysicalDedicatedLineRequest(AbstractModel):
    """
    Request entity for BindPhysicalDedicatedLineRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, et_gateway_id, et_id, channel_id, client_token=None, local_cidrs=None):
        """
        Initialize BindPhysicalDedicatedLineRequest request entity.

        :param et_gateway_id: et_gateway_id parameter
        :type et_gateway_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param et_id: 绑定的物理专线的ID，etid和channelId必须同时存在
        :type et_id: str (required)

        :param channel_id: 绑定的专线通道的ID，etid和channelId必须同时存在
        :type channel_id: str (required)

        :param local_cidrs: 专线网关的云端网络，用户可以选本VPC网段或自定义一个或多个网段
        :type local_cidrs: List[str] (optional)
        """
        super().__init__()
        self.et_gateway_id = et_gateway_id
        self.client_token = client_token
        self.et_id = et_id
        self.channel_id = channel_id
        self.local_cidrs = local_cidrs

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
        if self.et_id is not None:
            result['etId'] = self.et_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.local_cidrs is not None:
            result['localCidrs'] = self.local_cidrs
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindPhysicalDedicatedLineRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etGatewayId') is not None:
            self.et_gateway_id = m.get('etGatewayId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('etId') is not None:
            self.et_id = m.get('etId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('localCidrs') is not None:
            self.local_cidrs = m.get('localCidrs')
        return self
