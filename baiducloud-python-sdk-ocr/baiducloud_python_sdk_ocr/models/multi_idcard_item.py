"""
MultiIdcardItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.multi_idcard_card_info import MultiIdcardCardInfo


class MultiIdcardItem(AbstractModel):
    """
    MultiIdcardItem
    """

    def __init__(self, card_info=None, card_result=None):
        """
        Initialize MultiIdcardItem instance.

        :param card_info: card_info attribute
        :type card_info: MultiIdcardCardInfo (optional)

        :param card_result: 识别结果
        :type card_result: object (optional)
        """
        super().__init__()
        self.card_info = card_info
        self.card_result = card_result

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
        if self.card_info is not None:
            result['card_info'] = self.card_info.to_dict()
        if self.card_result is not None:
            result['card_result'] = self.card_result
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MultiIdcardItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('card_info') is not None:
            self.card_info = MultiIdcardCardInfo().from_dict(m.get('card_info'))
        if m.get('card_result') is not None:
            self.card_result = m.get('card_result')
        return self
