"""
Request entity for GetPriceBySpecRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetPriceBySpecRequest(AbstractModel):
    """
    Request entity for GetPriceBySpecRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, payment_timing, zone_name, purchase_length, spec_id=None, spec=None, purchase_count=None):
        """
        Initialize GetPriceBySpecRequest request entity.

        :param spec_id: 实例规格族
        :type spec_id: str (optional)

        :param spec: 实例套餐规格
        :type spec: str (optional)

        :param payment_timing: 付费方式，包括Postpaid(后付费)、Prepaid(预付费)
        :type payment_timing: str (required)

        :param zone_name: 可用区名称
        :type zone_name: str (required)

        :param purchase_count: 查询数量，必须为大于0的整数，缺省为1
        :type purchase_count: int (optional)

        :param purchase_length: 时长，[1,2,3,4,5,6,7,8,9,12,24,36]，单位：月
        :type purchase_length: int (required)
        """
        super().__init__()
        self.spec_id = spec_id
        self.spec = spec
        self.payment_timing = payment_timing
        self.zone_name = zone_name
        self.purchase_count = purchase_count
        self.purchase_length = purchase_length

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
        if self.spec_id is not None:
            result['specId'] = self.spec_id
        if self.spec is not None:
            result['spec'] = self.spec
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        if self.purchase_length is not None:
            result['purchaseLength'] = self.purchase_length
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPriceBySpecRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('specId') is not None:
            self.spec_id = m.get('specId')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        if m.get('purchaseLength') is not None:
            self.purchase_length = m.get('purchaseLength')
        return self
