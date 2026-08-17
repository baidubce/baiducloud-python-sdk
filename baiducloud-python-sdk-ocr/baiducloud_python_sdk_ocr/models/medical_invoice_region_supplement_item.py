"""
MedicalInvoiceRegionSupplementItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.medical_invoice_probability import MedicalInvoiceProbability

from baiducloud_python_sdk_ocr.models.medical_invoice_position import MedicalInvoicePosition


class MedicalInvoiceRegionSupplementItem(AbstractModel):
    """
    MedicalInvoiceRegionSupplementItem
    """

    def __init__(self, name=None, word=None, probability=None, position=None):
        """
        Initialize MedicalInvoiceRegionSupplementItem instance.

        :param name: 字段名，不同省市返回字段不同
        :type name: str (optional)

        :param word: name字段对应的识别结果
        :type word: str (optional)

        :param probability: probability attribute
        :type probability: MedicalInvoiceProbability (optional)

        :param position: position attribute
        :type position: MedicalInvoicePosition (optional)
        """
        super().__init__()
        self.name = name
        self.word = word
        self.probability = probability
        self.position = position

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
        if self.name is not None:
            result['name'] = self.name
        if self.word is not None:
            result['word'] = self.word
        if self.probability is not None:
            result['probability'] = self.probability.to_dict()
        if self.position is not None:
            result['position'] = self.position.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalInvoiceRegionSupplementItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('probability') is not None:
            self.probability = MedicalInvoiceProbability().from_dict(m.get('probability'))
        if m.get('position') is not None:
            self.position = MedicalInvoicePosition().from_dict(m.get('position'))
        return self
