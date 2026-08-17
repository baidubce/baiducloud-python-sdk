"""
MedicalInvoiceCostCategoryItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.medi_info import MediInfo


class MedicalInvoiceCostCategoryItem(AbstractModel):
    """
    MedicalInvoiceCostCategoryItem
    """

    def __init__(self, name=None, word=None, medi_info=None):
        """
        Initialize MedicalInvoiceCostCategoryItem instance.

        :param name: 字段名，包括：收费项目、金额
        :type name: str (optional)

        :param word: name字段对应的识别结果
        :type word: str (optional)

        :param medi_info: medi_info attribute
        :type medi_info: MediInfo (optional)
        """
        super().__init__()
        self.name = name
        self.word = word
        self.medi_info = medi_info

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
        if self.medi_info is not None:
            result['medi_info'] = self.medi_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalInvoiceCostCategoryItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('medi_info') is not None:
            self.medi_info = MediInfo().from_dict(m.get('medi_info'))
        return self
