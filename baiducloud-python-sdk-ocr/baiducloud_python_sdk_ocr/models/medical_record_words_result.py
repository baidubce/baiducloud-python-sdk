"""
MedicalRecordWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue

from baiducloud_python_sdk_ocr.models.medical_record_field_value import MedicalRecordFieldValue


class MedicalRecordWordsResult(AbstractModel):
    """
    MedicalRecordWordsResult
    """

    def __init__(
        self,
        record_num=None,
        name=None,
        sex=None,
        birthday=None,
        age=None,
        career=None,
        marital_status=None,
        nation=None,
        id=None,
        nationality=None,
        admission_department=None,
        discharge_department=None,
        hospital_day=None,
        allergy=None,
        blood_type=None,
    ):
        """
        Initialize MedicalRecordWordsResult instance.

        :param record_num: record_num attribute
        :type record_num: MedicalRecordFieldValue (optional)

        :param name: name attribute
        :type name: MedicalRecordFieldValue (optional)

        :param sex: sex attribute
        :type sex: MedicalRecordFieldValue (optional)

        :param birthday: birthday attribute
        :type birthday: MedicalRecordFieldValue (optional)

        :param age: age attribute
        :type age: MedicalRecordFieldValue (optional)

        :param career: career attribute
        :type career: MedicalRecordFieldValue (optional)

        :param marital_status: marital_status attribute
        :type marital_status: MedicalRecordFieldValue (optional)

        :param nation: nation attribute
        :type nation: MedicalRecordFieldValue (optional)

        :param id: id attribute
        :type id: MedicalRecordFieldValue (optional)

        :param nationality: nationality attribute
        :type nationality: MedicalRecordFieldValue (optional)

        :param admission_department: admission_department attribute
        :type admission_department: MedicalRecordFieldValue (optional)

        :param discharge_department: discharge_department attribute
        :type discharge_department: MedicalRecordFieldValue (optional)

        :param hospital_day: hospital_day attribute
        :type hospital_day: MedicalRecordFieldValue (optional)

        :param allergy: allergy attribute
        :type allergy: MedicalRecordFieldValue (optional)

        :param blood_type: blood_type attribute
        :type blood_type: MedicalRecordFieldValue (optional)
        """
        super().__init__()
        self.record_num = record_num
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.age = age
        self.career = career
        self.marital_status = marital_status
        self.nation = nation
        self.id = id
        self.nationality = nationality
        self.admission_department = admission_department
        self.discharge_department = discharge_department
        self.hospital_day = hospital_day
        self.allergy = allergy
        self.blood_type = blood_type

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
        if self.record_num is not None:
            result['RecordNum'] = self.record_num.to_dict()
        if self.name is not None:
            result['Name'] = self.name.to_dict()
        if self.sex is not None:
            result['Sex'] = self.sex.to_dict()
        if self.birthday is not None:
            result['Birthday'] = self.birthday.to_dict()
        if self.age is not None:
            result['Age'] = self.age.to_dict()
        if self.career is not None:
            result['Career'] = self.career.to_dict()
        if self.marital_status is not None:
            result['MaritalStatus'] = self.marital_status.to_dict()
        if self.nation is not None:
            result['Nation'] = self.nation.to_dict()
        if self.id is not None:
            result['ID'] = self.id.to_dict()
        if self.nationality is not None:
            result['Nationality'] = self.nationality.to_dict()
        if self.admission_department is not None:
            result['AdmissionDepartment'] = self.admission_department.to_dict()
        if self.discharge_department is not None:
            result['DischargeDepartment'] = self.discharge_department.to_dict()
        if self.hospital_day is not None:
            result['HospitalDay'] = self.hospital_day.to_dict()
        if self.allergy is not None:
            result['Allergy'] = self.allergy.to_dict()
        if self.blood_type is not None:
            result['BloodType'] = self.blood_type.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalRecordWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('RecordNum') is not None:
            self.record_num = MedicalRecordFieldValue().from_dict(m.get('RecordNum'))
        if m.get('Name') is not None:
            self.name = MedicalRecordFieldValue().from_dict(m.get('Name'))
        if m.get('Sex') is not None:
            self.sex = MedicalRecordFieldValue().from_dict(m.get('Sex'))
        if m.get('Birthday') is not None:
            self.birthday = MedicalRecordFieldValue().from_dict(m.get('Birthday'))
        if m.get('Age') is not None:
            self.age = MedicalRecordFieldValue().from_dict(m.get('Age'))
        if m.get('Career') is not None:
            self.career = MedicalRecordFieldValue().from_dict(m.get('Career'))
        if m.get('MaritalStatus') is not None:
            self.marital_status = MedicalRecordFieldValue().from_dict(m.get('MaritalStatus'))
        if m.get('Nation') is not None:
            self.nation = MedicalRecordFieldValue().from_dict(m.get('Nation'))
        if m.get('ID') is not None:
            self.id = MedicalRecordFieldValue().from_dict(m.get('ID'))
        if m.get('Nationality') is not None:
            self.nationality = MedicalRecordFieldValue().from_dict(m.get('Nationality'))
        if m.get('AdmissionDepartment') is not None:
            self.admission_department = MedicalRecordFieldValue().from_dict(m.get('AdmissionDepartment'))
        if m.get('DischargeDepartment') is not None:
            self.discharge_department = MedicalRecordFieldValue().from_dict(m.get('DischargeDepartment'))
        if m.get('HospitalDay') is not None:
            self.hospital_day = MedicalRecordFieldValue().from_dict(m.get('HospitalDay'))
        if m.get('Allergy') is not None:
            self.allergy = MedicalRecordFieldValue().from_dict(m.get('Allergy'))
        if m.get('BloodType') is not None:
            self.blood_type = MedicalRecordFieldValue().from_dict(m.get('BloodType'))
        return self
