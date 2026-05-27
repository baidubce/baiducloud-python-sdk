"""
Request entity for CreateHaVipResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateHaVipResponse(BceResponse):
    """
    CreateHaVipResponse
    """

    def __init__(self, ha_vip_id=None):
        """
        Initialize CreateHaVipResponse response.

        :param ha_vip_id: 高可用虚拟IP的ID
        :type ha_vip_id: str (optional)
        """
        super().__init__()
        self.ha_vip_id = ha_vip_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.ha_vip_id is not None:
            result['haVipId'] = self.ha_vip_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateHaVipResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('haVipId') is not None:
            self.ha_vip_id = m.get('haVipId')
        return self
