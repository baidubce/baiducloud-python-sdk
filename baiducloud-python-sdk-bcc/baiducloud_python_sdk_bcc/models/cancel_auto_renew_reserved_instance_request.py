"""
Request entity for CancelAutoRenewReservedInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CancelAutoRenewReservedInstanceRequest(AbstractModel):
    """
    Request entity for CancelAutoRenewReservedInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, reserved_instance_ids):
        """
        Initialize CancelAutoRenewReservedInstanceRequest request entity.

        :param reserved_instance_ids: 实例券id集合
        :type reserved_instance_ids: List[str] (required)
        """
        super().__init__()
        self.reserved_instance_ids = reserved_instance_ids

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
        if self.reserved_instance_ids is not None:
            result['reservedInstanceIds'] = self.reserved_instance_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CancelAutoRenewReservedInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstanceIds') is not None:
            self.reserved_instance_ids = m.get('reservedInstanceIds')
        return self
