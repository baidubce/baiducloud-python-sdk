"""
MedicalStatementWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.medical_statement_field_value import MedicalStatementFieldValue

from baiducloud_python_sdk_ocr.models.medical_statement_field_value import MedicalStatementFieldValue

from baiducloud_python_sdk_ocr.models.medical_statement_field_value import MedicalStatementFieldValue

from baiducloud_python_sdk_ocr.models.medical_statement_field_value import MedicalStatementFieldValue

from baiducloud_python_sdk_ocr.models.medical_statement_field_value import MedicalStatementFieldValue

from baiducloud_python_sdk_ocr.models.medical_statement_field_value import MedicalStatementFieldValue


class MedicalStatementWordsResult(AbstractModel):
    """
    MedicalStatementWordsResult
    """

    def __init__(
        self,
        admission_date=None,
        discharge_date=None,
        name=None,
        amount_in_figuers=None,
        self_payment_amount=None,
        medical_insurance_amount=None,
    ):
        """
        Initialize MedicalStatementWordsResult instance.

        :param admission_date: admission_date attribute
        :type admission_date: MedicalStatementFieldValue (optional)

        :param discharge_date: discharge_date attribute
        :type discharge_date: MedicalStatementFieldValue (optional)

        :param name: name attribute
        :type name: MedicalStatementFieldValue (optional)

        :param amount_in_figuers: amount_in_figuers attribute
        :type amount_in_figuers: MedicalStatementFieldValue (optional)

        :param self_payment_amount: self_payment_amount attribute
        :type self_payment_amount: MedicalStatementFieldValue (optional)

        :param medical_insurance_amount: medical_insurance_amount attribute
        :type medical_insurance_amount: MedicalStatementFieldValue (optional)
        """
        super().__init__()
        self.admission_date = admission_date
        self.discharge_date = discharge_date
        self.name = name
        self.amount_in_figuers = amount_in_figuers
        self.self_payment_amount = self_payment_amount
        self.medical_insurance_amount = medical_insurance_amount

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
        if self.admission_date is not None:
            result['AdmissionDate'] = self.admission_date.to_dict()
        if self.discharge_date is not None:
            result['DischargeDate'] = self.discharge_date.to_dict()
        if self.name is not None:
            result['Name'] = self.name.to_dict()
        if self.amount_in_figuers is not None:
            result['AmountInFiguers'] = self.amount_in_figuers.to_dict()
        if self.self_payment_amount is not None:
            result['SelfPaymentAmount'] = self.self_payment_amount.to_dict()
        if self.medical_insurance_amount is not None:
            result['MedicalInsuranceAmount'] = self.medical_insurance_amount.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalStatementWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('AdmissionDate') is not None:
            self.admission_date = MedicalStatementFieldValue().from_dict(m.get('AdmissionDate'))
        if m.get('DischargeDate') is not None:
            self.discharge_date = MedicalStatementFieldValue().from_dict(m.get('DischargeDate'))
        if m.get('Name') is not None:
            self.name = MedicalStatementFieldValue().from_dict(m.get('Name'))
        if m.get('AmountInFiguers') is not None:
            self.amount_in_figuers = MedicalStatementFieldValue().from_dict(m.get('AmountInFiguers'))
        if m.get('SelfPaymentAmount') is not None:
            self.self_payment_amount = MedicalStatementFieldValue().from_dict(m.get('SelfPaymentAmount'))
        if m.get('MedicalInsuranceAmount') is not None:
            self.medical_insurance_amount = MedicalStatementFieldValue().from_dict(m.get('MedicalInsuranceAmount'))
        return self
