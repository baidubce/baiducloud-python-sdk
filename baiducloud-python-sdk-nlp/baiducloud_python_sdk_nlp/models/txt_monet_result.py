"""
TxtMonetResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.txt_monet_item import TxtMonetItem


class TxtMonetResult(AbstractModel):
    """
    TxtMonetResult
    """

    def __init__(self, items=None):
        """
        Initialize TxtMonetResult instance.

        :param items: 每个query的返回结果集合
        :type items: List[TxtMonetItem] (optional)
        """
        super().__init__()
        self.items = items

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
        if self.items is not None:
            result['items'] = [i.to_dict() for i in self.items]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TxtMonetResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('items') is not None:
            self.items = [TxtMonetItem().from_dict(i) for i in m.get('items')]
        return self
