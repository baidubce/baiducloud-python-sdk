"""
MedicalReportDetectionWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.medical_report_detection_common_data_item import (
    MedicalReportDetectionCommonDataItem,
)


class MedicalReportDetectionWordsResult(AbstractModel):
    """
    MedicalReportDetectionWordsResult
    """

    def __init__(self, common_data=None, item=None):
        """
        Initialize MedicalReportDetectionWordsResult instance.

        :param common_data: 患者具体信息
        :type common_data: List[MedicalReportDetectionCommonDataItem] (optional)

        :param item: 检查项目
        :type item: List[List[MedicalReportDetectionItemField]] (optional)
        """
        super().__init__()
        self.common_data = common_data
        self.item = item

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
        if self.common_data is not None:
            result['CommonData'] = [i.to_dict() for i in self.common_data]
        if self.item is not None:
            result['Item'] = self.item
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalReportDetectionWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('CommonData') is not None:
            self.common_data = [MedicalReportDetectionCommonDataItem().from_dict(i) for i in m.get('CommonData')]
        if m.get('Item') is not None:
            self.item = m.get('Item')
        return self
