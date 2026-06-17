"""
Request entity for AutoRenewReservedInstanceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class AutoRenewReservedInstanceResponse(BceResponse):
    """
    AutoRenewReservedInstanceResponse
    """

    def __init__(self, reserved_instance_ids=None):
        """
        Initialize AutoRenewReservedInstanceResponse response.

        :param reserved_instance_ids: 预留实例券的id集合
        :type reserved_instance_ids: List[str] (optional)
        """
        super().__init__()
        self.reserved_instance_ids = reserved_instance_ids

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
        if self.reserved_instance_ids is not None:
            result['reservedInstanceIds'] = self.reserved_instance_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AutoRenewReservedInstanceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstanceIds') is not None:
            self.reserved_instance_ids = m.get('reservedInstanceIds')
        return self
