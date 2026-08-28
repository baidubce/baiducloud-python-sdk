"""
BirthCertificateResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.baby_birthday import BabyBirthday

from baiducloud_python_sdk_ocr.models.birth_province import BirthProvince

from baiducloud_python_sdk_ocr.models.birth_city import BirthCity

from baiducloud_python_sdk_ocr.models.birth_county import BirthCounty

from baiducloud_python_sdk_ocr.models.birth_weight import BirthWeight

from baiducloud_python_sdk_ocr.models.birth_length import BirthLength

from baiducloud_python_sdk_ocr.models.gestational_age import GestationalAge

from baiducloud_python_sdk_ocr.models.baby_name import BabyName

from baiducloud_python_sdk_ocr.models.baby_sex import BabySex

from baiducloud_python_sdk_ocr.models.code import Code

from baiducloud_python_sdk_ocr.models.hospital import Hospital

from baiducloud_python_sdk_ocr.models.father_name import FatherName

from baiducloud_python_sdk_ocr.models.father_id import FatherID

from baiducloud_python_sdk_ocr.models.father_nationality import FatherNationality

from baiducloud_python_sdk_ocr.models.father_ethnic import FatherEthnic

from baiducloud_python_sdk_ocr.models.father_address import FatherAddress

from baiducloud_python_sdk_ocr.models.father_age import FatherAge

from baiducloud_python_sdk_ocr.models.mother_name import MotherName

from baiducloud_python_sdk_ocr.models.mother_id import MotherID

from baiducloud_python_sdk_ocr.models.mother_nationality import MotherNationality

from baiducloud_python_sdk_ocr.models.mother_ethnic import MotherEthnic

from baiducloud_python_sdk_ocr.models.mother_address import MotherAddress

from baiducloud_python_sdk_ocr.models.mother_age import MotherAge


class BirthCertificateResult(AbstractModel):
    """
    BirthCertificateResult
    """

    def __init__(
        self,
        baby_birthday=None,
        birth_province=None,
        birth_city=None,
        birth_county=None,
        birth_weight=None,
        birth_length=None,
        gestational_age=None,
        baby_name=None,
        baby_sex=None,
        code=None,
        hospital=None,
        father_name=None,
        father_id=None,
        father_nationality=None,
        father_ethnic=None,
        father_address=None,
        father_age=None,
        mother_name=None,
        mother_id=None,
        mother_nationality=None,
        mother_ethnic=None,
        mother_address=None,
        mother_age=None,
    ):
        """
        Initialize BirthCertificateResult instance.

        :param baby_birthday: baby_birthday attribute
        :type baby_birthday: BabyBirthday (optional)

        :param birth_province: birth_province attribute
        :type birth_province: BirthProvince (optional)

        :param birth_city: birth_city attribute
        :type birth_city: BirthCity (optional)

        :param birth_county: birth_county attribute
        :type birth_county: BirthCounty (optional)

        :param birth_weight: birth_weight attribute
        :type birth_weight: BirthWeight (optional)

        :param birth_length: birth_length attribute
        :type birth_length: BirthLength (optional)

        :param gestational_age: gestational_age attribute
        :type gestational_age: GestationalAge (optional)

        :param baby_name: baby_name attribute
        :type baby_name: BabyName (optional)

        :param baby_sex: baby_sex attribute
        :type baby_sex: BabySex (optional)

        :param code: code attribute
        :type code: Code (optional)

        :param hospital: hospital attribute
        :type hospital: Hospital (optional)

        :param father_name: father_name attribute
        :type father_name: FatherName (optional)

        :param father_id: father_id attribute
        :type father_id: FatherID (optional)

        :param father_nationality: father_nationality attribute
        :type father_nationality: FatherNationality (optional)

        :param father_ethnic: father_ethnic attribute
        :type father_ethnic: FatherEthnic (optional)

        :param father_address: father_address attribute
        :type father_address: FatherAddress (optional)

        :param father_age: father_age attribute
        :type father_age: FatherAge (optional)

        :param mother_name: mother_name attribute
        :type mother_name: MotherName (optional)

        :param mother_id: mother_id attribute
        :type mother_id: MotherID (optional)

        :param mother_nationality: mother_nationality attribute
        :type mother_nationality: MotherNationality (optional)

        :param mother_ethnic: mother_ethnic attribute
        :type mother_ethnic: MotherEthnic (optional)

        :param mother_address: mother_address attribute
        :type mother_address: MotherAddress (optional)

        :param mother_age: mother_age attribute
        :type mother_age: MotherAge (optional)
        """
        super().__init__()
        self.baby_birthday = baby_birthday
        self.birth_province = birth_province
        self.birth_city = birth_city
        self.birth_county = birth_county
        self.birth_weight = birth_weight
        self.birth_length = birth_length
        self.gestational_age = gestational_age
        self.baby_name = baby_name
        self.baby_sex = baby_sex
        self.code = code
        self.hospital = hospital
        self.father_name = father_name
        self.father_id = father_id
        self.father_nationality = father_nationality
        self.father_ethnic = father_ethnic
        self.father_address = father_address
        self.father_age = father_age
        self.mother_name = mother_name
        self.mother_id = mother_id
        self.mother_nationality = mother_nationality
        self.mother_ethnic = mother_ethnic
        self.mother_address = mother_address
        self.mother_age = mother_age

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
        if self.baby_birthday is not None:
            result['BabyBirthday'] = self.baby_birthday.to_dict()
        if self.birth_province is not None:
            result['BirthProvince'] = self.birth_province.to_dict()
        if self.birth_city is not None:
            result['BirthCity'] = self.birth_city.to_dict()
        if self.birth_county is not None:
            result['BirthCounty'] = self.birth_county.to_dict()
        if self.birth_weight is not None:
            result['BirthWeight'] = self.birth_weight.to_dict()
        if self.birth_length is not None:
            result['BirthLength'] = self.birth_length.to_dict()
        if self.gestational_age is not None:
            result['GestationalAge'] = self.gestational_age.to_dict()
        if self.baby_name is not None:
            result['BabyName'] = self.baby_name.to_dict()
        if self.baby_sex is not None:
            result['BabySex'] = self.baby_sex.to_dict()
        if self.code is not None:
            result['Code'] = self.code.to_dict()
        if self.hospital is not None:
            result['Hospital'] = self.hospital.to_dict()
        if self.father_name is not None:
            result['FatherName'] = self.father_name.to_dict()
        if self.father_id is not None:
            result['FatherID'] = self.father_id.to_dict()
        if self.father_nationality is not None:
            result['FatherNationality'] = self.father_nationality.to_dict()
        if self.father_ethnic is not None:
            result['FatherEthnic'] = self.father_ethnic.to_dict()
        if self.father_address is not None:
            result['FatherAddress'] = self.father_address.to_dict()
        if self.father_age is not None:
            result['FatherAge'] = self.father_age.to_dict()
        if self.mother_name is not None:
            result['MotherName'] = self.mother_name.to_dict()
        if self.mother_id is not None:
            result['MotherID'] = self.mother_id.to_dict()
        if self.mother_nationality is not None:
            result['MotherNationality'] = self.mother_nationality.to_dict()
        if self.mother_ethnic is not None:
            result['MotherEthnic'] = self.mother_ethnic.to_dict()
        if self.mother_address is not None:
            result['MotherAddress'] = self.mother_address.to_dict()
        if self.mother_age is not None:
            result['MotherAge'] = self.mother_age.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BirthCertificateResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('BabyBirthday') is not None:
            self.baby_birthday = BabyBirthday().from_dict(m.get('BabyBirthday'))
        if m.get('BirthProvince') is not None:
            self.birth_province = BirthProvince().from_dict(m.get('BirthProvince'))
        if m.get('BirthCity') is not None:
            self.birth_city = BirthCity().from_dict(m.get('BirthCity'))
        if m.get('BirthCounty') is not None:
            self.birth_county = BirthCounty().from_dict(m.get('BirthCounty'))
        if m.get('BirthWeight') is not None:
            self.birth_weight = BirthWeight().from_dict(m.get('BirthWeight'))
        if m.get('BirthLength') is not None:
            self.birth_length = BirthLength().from_dict(m.get('BirthLength'))
        if m.get('GestationalAge') is not None:
            self.gestational_age = GestationalAge().from_dict(m.get('GestationalAge'))
        if m.get('BabyName') is not None:
            self.baby_name = BabyName().from_dict(m.get('BabyName'))
        if m.get('BabySex') is not None:
            self.baby_sex = BabySex().from_dict(m.get('BabySex'))
        if m.get('Code') is not None:
            self.code = Code().from_dict(m.get('Code'))
        if m.get('Hospital') is not None:
            self.hospital = Hospital().from_dict(m.get('Hospital'))
        if m.get('FatherName') is not None:
            self.father_name = FatherName().from_dict(m.get('FatherName'))
        if m.get('FatherID') is not None:
            self.father_id = FatherID().from_dict(m.get('FatherID'))
        if m.get('FatherNationality') is not None:
            self.father_nationality = FatherNationality().from_dict(m.get('FatherNationality'))
        if m.get('FatherEthnic') is not None:
            self.father_ethnic = FatherEthnic().from_dict(m.get('FatherEthnic'))
        if m.get('FatherAddress') is not None:
            self.father_address = FatherAddress().from_dict(m.get('FatherAddress'))
        if m.get('FatherAge') is not None:
            self.father_age = FatherAge().from_dict(m.get('FatherAge'))
        if m.get('MotherName') is not None:
            self.mother_name = MotherName().from_dict(m.get('MotherName'))
        if m.get('MotherID') is not None:
            self.mother_id = MotherID().from_dict(m.get('MotherID'))
        if m.get('MotherNationality') is not None:
            self.mother_nationality = MotherNationality().from_dict(m.get('MotherNationality'))
        if m.get('MotherEthnic') is not None:
            self.mother_ethnic = MotherEthnic().from_dict(m.get('MotherEthnic'))
        if m.get('MotherAddress') is not None:
            self.mother_address = MotherAddress().from_dict(m.get('MotherAddress'))
        if m.get('MotherAge') is not None:
            self.mother_age = MotherAge().from_dict(m.get('MotherAge'))
        return self
