"""
Request entity for GetReservedInstancePriceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetReservedInstancePriceRequest(AbstractModel):
    """
    Request entity for GetReservedInstancePriceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        spec_id,
        spec,
        offering_type,
        zone_name,
        scope=None,
        reserved_instance_count=None,
        price_time_unit=None,
        reserved_instance_time=None,
        purchase_num=None,
    ):
        """
        Initialize GetReservedInstancePriceRequest request entity.

        :param spec_id: 实例规格族
        :type spec_id: str (required)

        :param spec: 实例套餐规格
        :type spec: str (required)

        :param offering_type: 付费方式，可选值：FullyPrepay：全预付；半预付：PartPrepay；0预付：NoPrepay。
        :type offering_type: str (required)

        :param scope: 实例券的可用范围；默认：AZ可用区级券：AZ地域级券：Region
        :type scope: str (optional)

        :param zone_name: 可用区名称
        :type zone_name: str (required)

        :param reserved_instance_count: 查询在指定实例套餐规格下，任意数量实例的总价格，必须为大于0的整数，可选参数，缺省为1
        :type reserved_instance_count: int (optional)

        :param price_time_unit: 后付费计价时间单位，可选值： month：按月计费； hour：按小时计费，缺省值。
        :type price_time_unit: str (optional)

        :param reserved_instance_time: 实例券购买时长，[1,2,3,4,5,6,7,8,9,12,24,36]，单位：月。
        :type reserved_instance_time: int (optional)

        :param purchase_num: 预留实例券购买数量
        :type purchase_num: int (optional)
        """
        super().__init__()
        self.spec_id = spec_id
        self.spec = spec
        self.offering_type = offering_type
        self.scope = scope
        self.zone_name = zone_name
        self.reserved_instance_count = reserved_instance_count
        self.price_time_unit = price_time_unit
        self.reserved_instance_time = reserved_instance_time
        self.purchase_num = purchase_num

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
        if self.offering_type is not None:
            result['offeringType'] = self.offering_type
        if self.scope is not None:
            result['scope'] = self.scope
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.reserved_instance_count is not None:
            result['reservedInstanceCount'] = self.reserved_instance_count
        if self.price_time_unit is not None:
            result['priceTimeUnit'] = self.price_time_unit
        if self.reserved_instance_time is not None:
            result['reservedInstanceTime'] = self.reserved_instance_time
        if self.purchase_num is not None:
            result['purchaseNum'] = self.purchase_num
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetReservedInstancePriceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('specId') is not None:
            self.spec_id = m.get('specId')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('offeringType') is not None:
            self.offering_type = m.get('offeringType')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('reservedInstanceCount') is not None:
            self.reserved_instance_count = m.get('reservedInstanceCount')
        if m.get('priceTimeUnit') is not None:
            self.price_time_unit = m.get('priceTimeUnit')
        if m.get('reservedInstanceTime') is not None:
            self.reserved_instance_time = m.get('reservedInstanceTime')
        if m.get('purchaseNum') is not None:
            self.purchase_num = m.get('purchaseNum')
        return self
