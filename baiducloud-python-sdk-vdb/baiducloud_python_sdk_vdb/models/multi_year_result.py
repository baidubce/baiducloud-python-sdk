"""
MultiYearResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MultiYearResult(AbstractModel):
    """
    MultiYearResult
    """

    def __init__(self, multi_discount=None, multi_year=None):
        """
        Initialize MultiYearResult instance.

        :param multi_discount:
        :type multi_discount: float (optional)

        :param multi_year:
        :type multi_year: float (optional)
        """
        super().__init__()
        self.multi_discount = multi_discount
        self.multi_year = multi_year

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
        if self.multi_discount is not None:
            result['multiDiscount'] = self.multi_discount
        if self.multi_year is not None:
            result['multiYear'] = self.multi_year
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MultiYearResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('multiDiscount') is not None:
            self.multi_discount = m.get('multiDiscount')
        if m.get('multiYear') is not None:
            self.multi_year = m.get('multiYear')
        return self
