"""
MedicalInvoiceWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_field_value import MedicalInvoiceFieldValue

from baiducloud_python_sdk_ocr.models.medical_invoice_region_supplement_item import MedicalInvoiceRegionSupplementItem


class MedicalInvoiceWordsResult(AbstractModel):
    """
    MedicalInvoiceWordsResult
    """

    def __init__(
        self,
        business_num=None,
        invoice_num=None,
        hospital_num=None,
        hospital_name=None,
        record_num=None,
        hospital_day=None,
        admission_date=None,
        discharge_date=None,
        discharge_department=None,
        name=None,
        sex=None,
        hospital_type=None,
        social_security_num=None,
        insurance_type=None,
        charging_unit=None,
        payee=None,
        ocr_date=None,
        amount_in_words=None,
        amount_in_figuers=None,
        insurance_payment=None,
        personal_payment=None,
        prepay_amount=None,
        payment_amount=None,
        refund_amount=None,
        clinic_num=None,
        cost_categories=None,
        cost_detail=None,
        region_supplement=None,
    ):
        """
        Initialize MedicalInvoiceWordsResult instance.

        :param business_num: business_num attribute
        :type business_num: MedicalInvoiceFieldValue (optional)

        :param invoice_num: invoice_num attribute
        :type invoice_num: MedicalInvoiceFieldValue (optional)

        :param hospital_num: hospital_num attribute
        :type hospital_num: MedicalInvoiceFieldValue (optional)

        :param hospital_name: hospital_name attribute
        :type hospital_name: MedicalInvoiceFieldValue (optional)

        :param record_num: record_num attribute
        :type record_num: MedicalInvoiceFieldValue (optional)

        :param hospital_day: hospital_day attribute
        :type hospital_day: MedicalInvoiceFieldValue (optional)

        :param admission_date: admission_date attribute
        :type admission_date: MedicalInvoiceFieldValue (optional)

        :param discharge_date: discharge_date attribute
        :type discharge_date: MedicalInvoiceFieldValue (optional)

        :param discharge_department: discharge_department attribute
        :type discharge_department: MedicalInvoiceFieldValue (optional)

        :param name: name attribute
        :type name: MedicalInvoiceFieldValue (optional)

        :param sex: sex attribute
        :type sex: MedicalInvoiceFieldValue (optional)

        :param hospital_type: hospital_type attribute
        :type hospital_type: MedicalInvoiceFieldValue (optional)

        :param social_security_num: social_security_num attribute
        :type social_security_num: MedicalInvoiceFieldValue (optional)

        :param insurance_type: insurance_type attribute
        :type insurance_type: MedicalInvoiceFieldValue (optional)

        :param charging_unit: charging_unit attribute
        :type charging_unit: MedicalInvoiceFieldValue (optional)

        :param payee: payee attribute
        :type payee: MedicalInvoiceFieldValue (optional)

        :param ocr_date: ocr_date attribute
        :type ocr_date: MedicalInvoiceFieldValue (optional)

        :param amount_in_words: amount_in_words attribute
        :type amount_in_words: MedicalInvoiceFieldValue (optional)

        :param amount_in_figuers: amount_in_figuers attribute
        :type amount_in_figuers: MedicalInvoiceFieldValue (optional)

        :param insurance_payment: insurance_payment attribute
        :type insurance_payment: MedicalInvoiceFieldValue (optional)

        :param personal_payment: personal_payment attribute
        :type personal_payment: MedicalInvoiceFieldValue (optional)

        :param prepay_amount: prepay_amount attribute
        :type prepay_amount: MedicalInvoiceFieldValue (optional)

        :param payment_amount: payment_amount attribute
        :type payment_amount: MedicalInvoiceFieldValue (optional)

        :param refund_amount: refund_amount attribute
        :type refund_amount: MedicalInvoiceFieldValue (optional)

        :param clinic_num: clinic_num attribute
        :type clinic_num: MedicalInvoiceFieldValue (optional)

        :param cost_categories: 项目大类：治疗费、检查费等项目大类
        :type cost_categories: List[List[MedicalInvoiceCostCategoryItem]] (optional)

        :param cost_detail: 明细类别：药物/检查的明细类别
        :type cost_detail: List[List[MedicalInvoiceCostDetailItem]] (optional)

        :param region_supplement: 地区字段：根据省市返回该地区特有的字段
        :type region_supplement: List[MedicalInvoiceRegionSupplementItem] (optional)
        """
        super().__init__()
        self.business_num = business_num
        self.invoice_num = invoice_num
        self.hospital_num = hospital_num
        self.hospital_name = hospital_name
        self.record_num = record_num
        self.hospital_day = hospital_day
        self.admission_date = admission_date
        self.discharge_date = discharge_date
        self.discharge_department = discharge_department
        self.name = name
        self.sex = sex
        self.hospital_type = hospital_type
        self.social_security_num = social_security_num
        self.insurance_type = insurance_type
        self.charging_unit = charging_unit
        self.payee = payee
        self.ocr_date = ocr_date
        self.amount_in_words = amount_in_words
        self.amount_in_figuers = amount_in_figuers
        self.insurance_payment = insurance_payment
        self.personal_payment = personal_payment
        self.prepay_amount = prepay_amount
        self.payment_amount = payment_amount
        self.refund_amount = refund_amount
        self.clinic_num = clinic_num
        self.cost_categories = cost_categories
        self.cost_detail = cost_detail
        self.region_supplement = region_supplement

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
        if self.business_num is not None:
            result['BusinessNum'] = self.business_num.to_dict()
        if self.invoice_num is not None:
            result['InvoiceNum'] = self.invoice_num.to_dict()
        if self.hospital_num is not None:
            result['HospitalNum'] = self.hospital_num.to_dict()
        if self.hospital_name is not None:
            result['HospitalName'] = self.hospital_name.to_dict()
        if self.record_num is not None:
            result['RecordNum'] = self.record_num.to_dict()
        if self.hospital_day is not None:
            result['HospitalDay'] = self.hospital_day.to_dict()
        if self.admission_date is not None:
            result['AdmissionDate'] = self.admission_date.to_dict()
        if self.discharge_date is not None:
            result['DischargeDate'] = self.discharge_date.to_dict()
        if self.discharge_department is not None:
            result['DischargeDepartment'] = self.discharge_department.to_dict()
        if self.name is not None:
            result['Name'] = self.name.to_dict()
        if self.sex is not None:
            result['Sex'] = self.sex.to_dict()
        if self.hospital_type is not None:
            result['HospitalType'] = self.hospital_type.to_dict()
        if self.social_security_num is not None:
            result['SocialSecurityNum'] = self.social_security_num.to_dict()
        if self.insurance_type is not None:
            result['InsuranceType'] = self.insurance_type.to_dict()
        if self.charging_unit is not None:
            result['ChargingUnit'] = self.charging_unit.to_dict()
        if self.payee is not None:
            result['Payee'] = self.payee.to_dict()
        if self.ocr_date is not None:
            result['Date'] = self.ocr_date.to_dict()
        if self.amount_in_words is not None:
            result['AmountInWords'] = self.amount_in_words.to_dict()
        if self.amount_in_figuers is not None:
            result['AmountInFiguers'] = self.amount_in_figuers.to_dict()
        if self.insurance_payment is not None:
            result['InsurancePayment'] = self.insurance_payment.to_dict()
        if self.personal_payment is not None:
            result['PersonalPayment'] = self.personal_payment.to_dict()
        if self.prepay_amount is not None:
            result['PrepayAmount'] = self.prepay_amount.to_dict()
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount.to_dict()
        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount.to_dict()
        if self.clinic_num is not None:
            result['ClinicNum'] = self.clinic_num.to_dict()
        if self.cost_categories is not None:
            result['CostCategories'] = self.cost_categories
        if self.cost_detail is not None:
            result['CostDetail'] = self.cost_detail
        if self.region_supplement is not None:
            result['RegionSupplement'] = [i.to_dict() for i in self.region_supplement]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalInvoiceWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('BusinessNum') is not None:
            self.business_num = MedicalInvoiceFieldValue().from_dict(m.get('BusinessNum'))
        if m.get('InvoiceNum') is not None:
            self.invoice_num = MedicalInvoiceFieldValue().from_dict(m.get('InvoiceNum'))
        if m.get('HospitalNum') is not None:
            self.hospital_num = MedicalInvoiceFieldValue().from_dict(m.get('HospitalNum'))
        if m.get('HospitalName') is not None:
            self.hospital_name = MedicalInvoiceFieldValue().from_dict(m.get('HospitalName'))
        if m.get('RecordNum') is not None:
            self.record_num = MedicalInvoiceFieldValue().from_dict(m.get('RecordNum'))
        if m.get('HospitalDay') is not None:
            self.hospital_day = MedicalInvoiceFieldValue().from_dict(m.get('HospitalDay'))
        if m.get('AdmissionDate') is not None:
            self.admission_date = MedicalInvoiceFieldValue().from_dict(m.get('AdmissionDate'))
        if m.get('DischargeDate') is not None:
            self.discharge_date = MedicalInvoiceFieldValue().from_dict(m.get('DischargeDate'))
        if m.get('DischargeDepartment') is not None:
            self.discharge_department = MedicalInvoiceFieldValue().from_dict(m.get('DischargeDepartment'))
        if m.get('Name') is not None:
            self.name = MedicalInvoiceFieldValue().from_dict(m.get('Name'))
        if m.get('Sex') is not None:
            self.sex = MedicalInvoiceFieldValue().from_dict(m.get('Sex'))
        if m.get('HospitalType') is not None:
            self.hospital_type = MedicalInvoiceFieldValue().from_dict(m.get('HospitalType'))
        if m.get('SocialSecurityNum') is not None:
            self.social_security_num = MedicalInvoiceFieldValue().from_dict(m.get('SocialSecurityNum'))
        if m.get('InsuranceType') is not None:
            self.insurance_type = MedicalInvoiceFieldValue().from_dict(m.get('InsuranceType'))
        if m.get('ChargingUnit') is not None:
            self.charging_unit = MedicalInvoiceFieldValue().from_dict(m.get('ChargingUnit'))
        if m.get('Payee') is not None:
            self.payee = MedicalInvoiceFieldValue().from_dict(m.get('Payee'))
        if m.get('Date') is not None:
            self.ocr_date = MedicalInvoiceFieldValue().from_dict(m.get('Date'))
        if m.get('AmountInWords') is not None:
            self.amount_in_words = MedicalInvoiceFieldValue().from_dict(m.get('AmountInWords'))
        if m.get('AmountInFiguers') is not None:
            self.amount_in_figuers = MedicalInvoiceFieldValue().from_dict(m.get('AmountInFiguers'))
        if m.get('InsurancePayment') is not None:
            self.insurance_payment = MedicalInvoiceFieldValue().from_dict(m.get('InsurancePayment'))
        if m.get('PersonalPayment') is not None:
            self.personal_payment = MedicalInvoiceFieldValue().from_dict(m.get('PersonalPayment'))
        if m.get('PrepayAmount') is not None:
            self.prepay_amount = MedicalInvoiceFieldValue().from_dict(m.get('PrepayAmount'))
        if m.get('PaymentAmount') is not None:
            self.payment_amount = MedicalInvoiceFieldValue().from_dict(m.get('PaymentAmount'))
        if m.get('RefundAmount') is not None:
            self.refund_amount = MedicalInvoiceFieldValue().from_dict(m.get('RefundAmount'))
        if m.get('ClinicNum') is not None:
            self.clinic_num = MedicalInvoiceFieldValue().from_dict(m.get('ClinicNum'))
        if m.get('CostCategories') is not None:
            self.cost_categories = m.get('CostCategories')
        if m.get('CostDetail') is not None:
            self.cost_detail = m.get('CostDetail')
        if m.get('RegionSupplement') is not None:
            self.region_supplement = [
                MedicalInvoiceRegionSupplementItem().from_dict(i) for i in m.get('RegionSupplement')
            ]
        return self
