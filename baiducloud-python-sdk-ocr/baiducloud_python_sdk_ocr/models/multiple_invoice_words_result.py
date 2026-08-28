"""
MultipleInvoiceWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.multiple_invoice_result import MultipleInvoiceResult


class MultipleInvoiceWordsResult(AbstractModel):
    """
    MultipleInvoiceWordsResult
    """

    def __init__(self, type=None, top=None, left=None, width=None, height=None, probability=None, result=None):
        """
        Initialize MultipleInvoiceWordsResult instance.

        :param type: 票据类型，如 air_ticket、vat_invoice 等
        :type type: str (optional)

        :param top: 票据位置上边距
        :type top: int (optional)

        :param left: 票据位置左边距
        :type left: int (optional)

        :param width: 票据宽度
        :type width: int (optional)

        :param height: 票据高度
        :type height: int (optional)

        :param probability: 票据检测置信度
        :type probability: float (optional)

        :param result: result attribute
        :type result: MultipleInvoiceResult (optional)
        """
        super().__init__()
        self.type = type
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.probability = probability
        self.result = result

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
        if self.type is not None:
            result['type'] = self.type
        if self.top is not None:
            result['top'] = self.top
        if self.left is not None:
            result['left'] = self.left
        if self.width is not None:
            result['width'] = self.width
        if self.height is not None:
            result['height'] = self.height
        if self.probability is not None:
            result['probability'] = self.probability
        if self.result is not None:
            result['result'] = self.result.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MultipleInvoiceWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('left') is not None:
            self.left = m.get('left')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('result') is not None:
            self.result = MultipleInvoiceResult().from_dict(m.get('result'))
        return self
