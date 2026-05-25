"""
Request entity for HighAvailabilityVirtualIpUnbindingInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HighAvailabilityVirtualIpUnbindingInstanceRequest(AbstractModel):
    """
    Request entity for HighAvailabilityVirtualIpUnbindingInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ha_vip_id, instance_ids, instance_type, client_token=None):
        """
        Initialize HighAvailabilityVirtualIpUnbindingInstanceRequest request entity.

        :param ha_vip_id: ha_vip_id parameter
        :type ha_vip_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_ids: 解绑的实例ID列表，列表长度不大于5
        :type instance_ids: List[str] (required)

        :param instance_type: 解绑的实例类型，\"SERVER\"表示云服务器（BCC/BBC/DCC），\"ENI\"表示弹性网卡
        :type instance_type: str (required)
        """
        super().__init__()
        self.ha_vip_id = ha_vip_id
        self.client_token = client_token
        self.instance_ids = instance_ids
        self.instance_type = instance_type

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
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HighAvailabilityVirtualIpUnbindingInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('haVipId') is not None:
            self.ha_vip_id = m.get('haVipId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        return self
