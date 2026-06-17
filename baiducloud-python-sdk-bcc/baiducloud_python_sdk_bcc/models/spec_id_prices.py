"""
SpecIdPrices information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.spec_prices import SpecPrices


class SpecIdPrices(AbstractModel):
    """
    SpecIdPrices
    """

    def __init__(self, spec_id=None, spec_prices=None):
        """
        Initialize SpecIdPrices instance.

        :param spec_id: 规格族ID（查询实例套餐价格接口返回）
        :type spec_id: str (optional)

        :param spec_prices: 规格价格列表（查询实例套餐价格接口返回）
        :type spec_prices: List[SpecPrices] (optional)
        """
        super().__init__()
        self.spec_id = spec_id
        self.spec_prices = spec_prices

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
        if self.spec_id is not None:
            result['specId'] = self.spec_id
        if self.spec_prices is not None:
            result['specPrices'] = [i.to_dict() for i in self.spec_prices]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SpecIdPrices

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('specId') is not None:
            self.spec_id = m.get('specId')
        if m.get('specPrices') is not None:
            self.spec_prices = [SpecPrices().from_dict(i) for i in m.get('specPrices')]
        return self
