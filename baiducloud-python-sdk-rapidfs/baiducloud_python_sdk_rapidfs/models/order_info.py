"""
OrderInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OrderInfo(AbstractModel):
    """
    OrderInfo
    """

    def __init__(self, order_id=None, instance_id=None, order_status=None):
        """
        Initialize OrderInfo instance.

        :param order_id: 订单ID
        :type order_id: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (optional)

        :param order_status: 订单状态，见 OrderStatus
        :type order_status: str (optional)
        """
        super().__init__()
        self.order_id = order_id
        self.instance_id = instance_id
        self.order_status = order_status

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
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.order_status is not None:
            result['orderStatus'] = self.order_status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OrderInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')
        return self
