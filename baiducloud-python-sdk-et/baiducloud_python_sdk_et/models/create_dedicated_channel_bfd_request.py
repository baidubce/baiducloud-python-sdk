"""
Request entity for CreateDedicatedChannelBfdRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateDedicatedChannelBfdRequest(AbstractModel):
    """
    Request entity for CreateDedicatedChannelBfdRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, et_id, et_channel_id, send_interval, receiv_interval, detect_multiplier, client_token=None):
        """
        Initialize CreateDedicatedChannelBfdRequest request entity.

        :param et_id: et_id parameter
        :type et_id: str (required)

        :param et_channel_id: et_channel_id parameter
        :type et_channel_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param send_interval: 报文发送间隔, 200-1000间的整数，单位为ms,推荐值为300
        :type send_interval: int (required)

        :param receiv_interval: 报文接收间隔, 200-1000间的整数，单位为ms,推荐值为300
        :type receiv_interval: int (required)

        :param detect_multiplier: 检测时间倍数, 3-10间的整数，推荐值为4
        :type detect_multiplier: int (required)
        """
        super().__init__()
        self.et_id = et_id
        self.et_channel_id = et_channel_id
        self.client_token = client_token
        self.send_interval = send_interval
        self.receiv_interval = receiv_interval
        self.detect_multiplier = detect_multiplier

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
        if self.send_interval is not None:
            result['sendInterval'] = self.send_interval
        if self.receiv_interval is not None:
            result['receivInterval'] = self.receiv_interval
        if self.detect_multiplier is not None:
            result['detectMultiplier'] = self.detect_multiplier
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDedicatedChannelBfdRequest

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
        if m.get('sendInterval') is not None:
            self.send_interval = m.get('sendInterval')
        if m.get('receivInterval') is not None:
            self.receiv_interval = m.get('receivInterval')
        if m.get('detectMultiplier') is not None:
            self.detect_multiplier = m.get('detectMultiplier')
        return self
