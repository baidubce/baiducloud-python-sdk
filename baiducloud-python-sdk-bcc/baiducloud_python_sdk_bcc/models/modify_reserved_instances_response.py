"""
Request entity for ModifyReservedInstancesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.modify_reserved_instance_order import ModifyReservedInstanceOrder


class ModifyReservedInstancesResponse(BceResponse):
    """
    ModifyReservedInstancesResponse
    """

    def __init__(self, modify_reserved_instance_orders=None):
        """
        Initialize ModifyReservedInstancesResponse response.

        :param modify_reserved_instance_orders: 调整预留实例券的返回集合
        :type modify_reserved_instance_orders: List[ModifyReservedInstanceOrder] (optional)
        """
        super().__init__()
        self.modify_reserved_instance_orders = modify_reserved_instance_orders

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
        if self.modify_reserved_instance_orders is not None:
            result['modifyReservedInstanceOrders'] = [i.to_dict() for i in self.modify_reserved_instance_orders]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyReservedInstancesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('modifyReservedInstanceOrders') is not None:
            self.modify_reserved_instance_orders = [
                ModifyReservedInstanceOrder().from_dict(i) for i in m.get('modifyReservedInstanceOrders')
            ]
        return self
