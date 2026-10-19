"""
Request entity for GetNewPurchasePriceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.instance import Instance


class GetNewPurchasePriceRequest(AbstractModel):
    """
    Request entity for GetNewPurchasePriceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance, product_type, duration=None, number=None):
        """
        Initialize GetNewPurchasePriceRequest request entity.

        :param instance: instance parameter
        :type instance: Instance (required)

        :param duration: 时长。支付方式为后支付时不需要设置，预支付时必须设置。时间单位默认为month。
        :type duration: int (optional)

        :param number: 购买数量，默认值为1。
        :type number: int (optional)

        :param product_type: 付费方式。 预付费：prepay，后付费：postpay。
        :type product_type: str (required)
        """
        super().__init__()
        self.instance = instance
        self.duration = duration
        self.number = number
        self.product_type = product_type

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
        if self.instance is not None:
            result['instance'] = self.instance.to_dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.number is not None:
            result['number'] = self.number
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetNewPurchasePriceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instance') is not None:
            self.instance = Instance().from_dict(m.get('instance'))
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self
