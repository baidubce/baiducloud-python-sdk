"""
CdsPrices information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CdsPrices(AbstractModel):
    """
    CdsPrices
    """

    def __init__(self, storage_type=None, cds_size_in_gb=None, price=None, spec_price=None, unit=None):
        """
        Initialize CdsPrices instance.

        :param storage_type: 磁盘存储类型（查询CDS价格返回）
        :type storage_type: str (optional)

        :param cds_size_in_gb: 磁盘容量（查询CDS价格返回）
        :type cds_size_in_gb: int (optional)

        :param price: 价格（查询CDS价格返回）
        :type price: float (optional)

        :param spec_price: 实例规格的原始标价（查询CDS价格返回）
        :type spec_price: float (optional)

        :param unit: 计费单位（查询CDS价格返回）
        :type unit: str (optional)
        """
        super().__init__()
        self.storage_type = storage_type
        self.cds_size_in_gb = cds_size_in_gb
        self.price = price
        self.spec_price = spec_price
        self.unit = unit

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
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.cds_size_in_gb is not None:
            result['cdsSizeInGB'] = self.cds_size_in_gb
        if self.price is not None:
            result['price'] = self.price
        if self.spec_price is not None:
            result['specPrice'] = self.spec_price
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CdsPrices

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('cdsSizeInGB') is not None:
            self.cds_size_in_gb = m.get('cdsSizeInGB')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('specPrice') is not None:
            self.spec_price = m.get('specPrice')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self
