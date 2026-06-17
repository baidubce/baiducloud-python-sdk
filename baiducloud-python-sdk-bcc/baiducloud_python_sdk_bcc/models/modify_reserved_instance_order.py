"""
ModifyReservedInstanceOrder information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyReservedInstanceOrder(AbstractModel):
    """
    ModifyReservedInstanceOrder
    """

    def __init__(self, reserved_instance_id=None, order_id=None):
        """
        Initialize ModifyReservedInstanceOrder instance.

        :param reserved_instance_id: 预留实例券的id
        :type reserved_instance_id: str (optional)

        :param order_id: 预留实例券变更的订单号
        :type order_id: str (optional)
        """
        super().__init__()
        self.reserved_instance_id = reserved_instance_id
        self.order_id = order_id

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.reserved_instance_id is not None:
            result['reservedInstanceId'] = self.reserved_instance_id
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyReservedInstanceOrder

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstanceId') is not None:
            self.reserved_instance_id = m.get('reservedInstanceId')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self
