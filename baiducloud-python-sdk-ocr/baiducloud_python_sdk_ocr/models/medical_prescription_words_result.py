"""
MedicalPrescriptionWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.medical_prescription_common_data_item import MedicalPrescriptionCommonDataItem


class MedicalPrescriptionWordsResult(AbstractModel):
    """
    MedicalPrescriptionWordsResult
    """

    def __init__(self, common_data=None, cost_detail=None):
        """
        Initialize MedicalPrescriptionWordsResult instance.

        :param common_data: 患者个人信息
        :type common_data: List[MedicalPrescriptionCommonDataItem] (optional)

        :param cost_detail: 具体项目
        :type cost_detail: List[List[MedicalPrescriptionCostDetailItem]] (optional)
        """
        super().__init__()
        self.common_data = common_data
        self.cost_detail = cost_detail

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
        if self.cost_detail is not None:
            result['CostDetail'] = self.cost_detail
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalPrescriptionWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('CommonData') is not None:
            self.common_data = [MedicalPrescriptionCommonDataItem().from_dict(i) for i in m.get('CommonData')]
        if m.get('CostDetail') is not None:
            self.cost_detail = m.get('CostDetail')
        return self
