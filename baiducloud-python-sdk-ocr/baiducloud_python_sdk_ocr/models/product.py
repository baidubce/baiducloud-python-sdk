"""
Product information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.shopping_receipt_location import ShoppingReceiptLocation

from baiducloud_python_sdk_ocr.models.shopping_receipt_probability import ShoppingReceiptProbability


class Product(AbstractModel):
    """
    Product
    """

    def __init__(self, word=None, location=None, probability=None):
        """
        Initialize Product instance.

        :param word: 内容
        :type word: str (optional)

        :param location: location attribute
        :type location: ShoppingReceiptLocation (optional)

        :param probability: probability attribute
        :type probability: ShoppingReceiptProbability (optional)
        """
        super().__init__()
        self.word = word
        self.location = location
        self.probability = probability

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
        if self.word is not None:
            result['word'] = self.word
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.probability is not None:
            result['probability'] = self.probability.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Product

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('location') is not None:
            self.location = ShoppingReceiptLocation().from_dict(m.get('location'))
        if m.get('probability') is not None:
            self.probability = ShoppingReceiptProbability().from_dict(m.get('probability'))
        return self
