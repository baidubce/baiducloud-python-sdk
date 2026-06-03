"""
Request entity for DescribePriceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribePriceRequest(AbstractModel):
    """
    Request entity for DescribePriceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, currency=None, managed_mode=None, meta_spec=None, data_spec=None, capacity_ti_b=None):
        """
        Initialize DescribePriceRequest request entity.

        :param currency: 货币单位，枚举值：<br> • CNY：人民币，默认；<br> • USD：美元。
        :type currency: str (optional)

        :param managed_mode: managed_mode parameter
        :type managed_mode: str (optional)

        :param meta_spec: meta_spec parameter
        :type meta_spec: str (optional)

        :param data_spec: data_spec parameter
        :type data_spec: str (optional)

        :param capacity_ti_b: capacity_ti_b parameter
        :type capacity_ti_b: int (optional)
        """
        super().__init__()
        self.currency = currency
        self.managed_mode = managed_mode
        self.meta_spec = meta_spec
        self.data_spec = data_spec
        self.capacity_ti_b = capacity_ti_b

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
        if self.currency is not None:
            result['currency'] = self.currency
        if self.managed_mode is not None:
            result['managedMode'] = self.managed_mode
        if self.meta_spec is not None:
            result['metaSpec'] = self.meta_spec
        if self.data_spec is not None:
            result['dataSpec'] = self.data_spec
        if self.capacity_ti_b is not None:
            result['capacityTiB'] = self.capacity_ti_b
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribePriceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('currency') is not None:
            self.currency = m.get('currency')
        if m.get('managedMode') is not None:
            self.managed_mode = m.get('managedMode')
        if m.get('metaSpec') is not None:
            self.meta_spec = m.get('metaSpec')
        if m.get('dataSpec') is not None:
            self.data_spec = m.get('dataSpec')
        if m.get('capacityTiB') is not None:
            self.capacity_ti_b = m.get('capacityTiB')
        return self
