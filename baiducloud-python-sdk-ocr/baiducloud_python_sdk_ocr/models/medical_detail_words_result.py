"""
MedicalDetailWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.field_value import FieldValue

from baiducloud_python_sdk_ocr.models.field_value import FieldValue

from baiducloud_python_sdk_ocr.models.field_value import FieldValue

from baiducloud_python_sdk_ocr.models.field_value import FieldValue


class MedicalDetailWordsResult(AbstractModel):
    """
    MedicalDetailWordsResult
    """

    def __init__(self, name=None, ocr_date=None, patient_id=None, total_amount=None, cost_detail=None):
        """
        Initialize MedicalDetailWordsResult instance.

        :param name: name attribute
        :type name: FieldValue (optional)

        :param ocr_date: ocr_date attribute
        :type ocr_date: FieldValue (optional)

        :param patient_id: patient_id attribute
        :type patient_id: FieldValue (optional)

        :param total_amount: total_amount attribute
        :type total_amount: FieldValue (optional)

        :param cost_detail: 项目明细
        :type cost_detail: List[List[CostDetailItem]] (optional)
        """
        super().__init__()
        self.name = name
        self.ocr_date = ocr_date
        self.patient_id = patient_id
        self.total_amount = total_amount
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
        if self.name is not None:
            result['Name'] = self.name.to_dict()
        if self.ocr_date is not None:
            result['Date'] = self.ocr_date.to_dict()
        if self.patient_id is not None:
            result['PatientID'] = self.patient_id.to_dict()
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount.to_dict()
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
        :rtype: MedicalDetailWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('Name') is not None:
            self.name = FieldValue().from_dict(m.get('Name'))
        if m.get('Date') is not None:
            self.ocr_date = FieldValue().from_dict(m.get('Date'))
        if m.get('PatientID') is not None:
            self.patient_id = FieldValue().from_dict(m.get('PatientID'))
        if m.get('TotalAmount') is not None:
            self.total_amount = FieldValue().from_dict(m.get('TotalAmount'))
        if m.get('CostDetail') is not None:
            self.cost_detail = m.get('CostDetail')
        return self
