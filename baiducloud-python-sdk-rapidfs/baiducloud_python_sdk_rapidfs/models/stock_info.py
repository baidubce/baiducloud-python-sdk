"""
StockInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class StockInfo(AbstractModel):
    """
    StockInfo
    """

    def __init__(self, zone=None, stock_capacity_ti_b=None, stock_quantity=None):
        """
        Initialize StockInfo instance.

        :param zone: 用户可购买的可用区，例如 zoneA
        :type zone: str (optional)

        :param stock_capacity_ti_b: FullyManaged 部署模式下，可购买的缓存容量，0 表示售罄，单位 TiB
        :type stock_capacity_ti_b: int (optional)

        :param stock_quantity: MasterManaged 部署模式下，可购买的 Master 托管实例数量，0 表示售罄
        :type stock_quantity: int (optional)
        """
        super().__init__()
        self.zone = zone
        self.stock_capacity_ti_b = stock_capacity_ti_b
        self.stock_quantity = stock_quantity

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
        if self.zone is not None:
            result['zone'] = self.zone
        if self.stock_capacity_ti_b is not None:
            result['stockCapacityTiB'] = self.stock_capacity_ti_b
        if self.stock_quantity is not None:
            result['stockQuantity'] = self.stock_quantity
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: StockInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('stockCapacityTiB') is not None:
            self.stock_capacity_ti_b = m.get('stockCapacityTiB')
        if m.get('stockQuantity') is not None:
            self.stock_quantity = m.get('stockQuantity')
        return self
