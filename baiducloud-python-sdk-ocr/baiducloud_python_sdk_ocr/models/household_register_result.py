"""
HouseholdRegisterResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem

from baiducloud_python_sdk_ocr.models.household_word_item import HouseholdWordItem


class HouseholdRegisterResult(AbstractModel):
    """
    HouseholdRegisterResult
    """

    def __init__(
        self,
        household_num=None,
        name=None,
        relationship=None,
        sex=None,
        birth_address=None,
        nation=None,
        birthday=None,
        card_no=None,
        former_name=None,
        hometown=None,
        other_address=None,
        belief=None,
        height=None,
        blood_type=None,
        education=None,
        marital_status=None,
        veteran_status=None,
        work_address=None,
        career=None,
        wwto_city=None,
        ww_here=None,
        ocr_date=None,
        household_type=None,
        householder_name=None,
        address=None,
        issue_date=None,
    ):
        """
        Initialize HouseholdRegisterResult instance.

        :param household_num: household_num attribute
        :type household_num: HouseholdWordItem (optional)

        :param name: name attribute
        :type name: HouseholdWordItem (optional)

        :param relationship: relationship attribute
        :type relationship: HouseholdWordItem (optional)

        :param sex: sex attribute
        :type sex: HouseholdWordItem (optional)

        :param birth_address: birth_address attribute
        :type birth_address: HouseholdWordItem (optional)

        :param nation: nation attribute
        :type nation: HouseholdWordItem (optional)

        :param birthday: birthday attribute
        :type birthday: HouseholdWordItem (optional)

        :param card_no: card_no attribute
        :type card_no: HouseholdWordItem (optional)

        :param former_name: former_name attribute
        :type former_name: HouseholdWordItem (optional)

        :param hometown: hometown attribute
        :type hometown: HouseholdWordItem (optional)

        :param other_address: other_address attribute
        :type other_address: HouseholdWordItem (optional)

        :param belief: belief attribute
        :type belief: HouseholdWordItem (optional)

        :param height: height attribute
        :type height: HouseholdWordItem (optional)

        :param blood_type: blood_type attribute
        :type blood_type: HouseholdWordItem (optional)

        :param education: education attribute
        :type education: HouseholdWordItem (optional)

        :param marital_status: marital_status attribute
        :type marital_status: HouseholdWordItem (optional)

        :param veteran_status: veteran_status attribute
        :type veteran_status: HouseholdWordItem (optional)

        :param work_address: work_address attribute
        :type work_address: HouseholdWordItem (optional)

        :param career: career attribute
        :type career: HouseholdWordItem (optional)

        :param wwto_city: wwto_city attribute
        :type wwto_city: HouseholdWordItem (optional)

        :param ww_here: ww_here attribute
        :type ww_here: HouseholdWordItem (optional)

        :param ocr_date: ocr_date attribute
        :type ocr_date: HouseholdWordItem (optional)

        :param household_type: household_type attribute
        :type household_type: HouseholdWordItem (optional)

        :param householder_name: householder_name attribute
        :type householder_name: HouseholdWordItem (optional)

        :param address: address attribute
        :type address: HouseholdWordItem (optional)

        :param issue_date: issue_date attribute
        :type issue_date: HouseholdWordItem (optional)
        """
        super().__init__()
        self.household_num = household_num
        self.name = name
        self.relationship = relationship
        self.sex = sex
        self.birth_address = birth_address
        self.nation = nation
        self.birthday = birthday
        self.card_no = card_no
        self.former_name = former_name
        self.hometown = hometown
        self.other_address = other_address
        self.belief = belief
        self.height = height
        self.blood_type = blood_type
        self.education = education
        self.marital_status = marital_status
        self.veteran_status = veteran_status
        self.work_address = work_address
        self.career = career
        self.wwto_city = wwto_city
        self.ww_here = ww_here
        self.ocr_date = ocr_date
        self.household_type = household_type
        self.householder_name = householder_name
        self.address = address
        self.issue_date = issue_date

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
        if self.household_num is not None:
            result['HouseholdNum'] = self.household_num.to_dict()
        if self.name is not None:
            result['Name'] = self.name.to_dict()
        if self.relationship is not None:
            result['Relationship'] = self.relationship.to_dict()
        if self.sex is not None:
            result['Sex'] = self.sex.to_dict()
        if self.birth_address is not None:
            result['BirthAddress'] = self.birth_address.to_dict()
        if self.nation is not None:
            result['Nation'] = self.nation.to_dict()
        if self.birthday is not None:
            result['Birthday'] = self.birthday.to_dict()
        if self.card_no is not None:
            result['CardNo'] = self.card_no.to_dict()
        if self.former_name is not None:
            result['FormerName'] = self.former_name.to_dict()
        if self.hometown is not None:
            result['Hometown'] = self.hometown.to_dict()
        if self.other_address is not None:
            result['OtherAddress'] = self.other_address.to_dict()
        if self.belief is not None:
            result['Belief'] = self.belief.to_dict()
        if self.height is not None:
            result['Height'] = self.height.to_dict()
        if self.blood_type is not None:
            result['BloodType'] = self.blood_type.to_dict()
        if self.education is not None:
            result['Education'] = self.education.to_dict()
        if self.marital_status is not None:
            result['MaritalStatus'] = self.marital_status.to_dict()
        if self.veteran_status is not None:
            result['VeteranStatus'] = self.veteran_status.to_dict()
        if self.work_address is not None:
            result['WorkAddress'] = self.work_address.to_dict()
        if self.career is not None:
            result['Career'] = self.career.to_dict()
        if self.wwto_city is not None:
            result['WWToCity'] = self.wwto_city.to_dict()
        if self.ww_here is not None:
            result['WWHere'] = self.ww_here.to_dict()
        if self.ocr_date is not None:
            result['Date'] = self.ocr_date.to_dict()
        if self.household_type is not None:
            result['HouseholdType'] = self.household_type.to_dict()
        if self.householder_name is not None:
            result['HouseholderName'] = self.householder_name.to_dict()
        if self.address is not None:
            result['Address'] = self.address.to_dict()
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HouseholdRegisterResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('HouseholdNum') is not None:
            self.household_num = HouseholdWordItem().from_dict(m.get('HouseholdNum'))
        if m.get('Name') is not None:
            self.name = HouseholdWordItem().from_dict(m.get('Name'))
        if m.get('Relationship') is not None:
            self.relationship = HouseholdWordItem().from_dict(m.get('Relationship'))
        if m.get('Sex') is not None:
            self.sex = HouseholdWordItem().from_dict(m.get('Sex'))
        if m.get('BirthAddress') is not None:
            self.birth_address = HouseholdWordItem().from_dict(m.get('BirthAddress'))
        if m.get('Nation') is not None:
            self.nation = HouseholdWordItem().from_dict(m.get('Nation'))
        if m.get('Birthday') is not None:
            self.birthday = HouseholdWordItem().from_dict(m.get('Birthday'))
        if m.get('CardNo') is not None:
            self.card_no = HouseholdWordItem().from_dict(m.get('CardNo'))
        if m.get('FormerName') is not None:
            self.former_name = HouseholdWordItem().from_dict(m.get('FormerName'))
        if m.get('Hometown') is not None:
            self.hometown = HouseholdWordItem().from_dict(m.get('Hometown'))
        if m.get('OtherAddress') is not None:
            self.other_address = HouseholdWordItem().from_dict(m.get('OtherAddress'))
        if m.get('Belief') is not None:
            self.belief = HouseholdWordItem().from_dict(m.get('Belief'))
        if m.get('Height') is not None:
            self.height = HouseholdWordItem().from_dict(m.get('Height'))
        if m.get('BloodType') is not None:
            self.blood_type = HouseholdWordItem().from_dict(m.get('BloodType'))
        if m.get('Education') is not None:
            self.education = HouseholdWordItem().from_dict(m.get('Education'))
        if m.get('MaritalStatus') is not None:
            self.marital_status = HouseholdWordItem().from_dict(m.get('MaritalStatus'))
        if m.get('VeteranStatus') is not None:
            self.veteran_status = HouseholdWordItem().from_dict(m.get('VeteranStatus'))
        if m.get('WorkAddress') is not None:
            self.work_address = HouseholdWordItem().from_dict(m.get('WorkAddress'))
        if m.get('Career') is not None:
            self.career = HouseholdWordItem().from_dict(m.get('Career'))
        if m.get('WWToCity') is not None:
            self.wwto_city = HouseholdWordItem().from_dict(m.get('WWToCity'))
        if m.get('WWHere') is not None:
            self.ww_here = HouseholdWordItem().from_dict(m.get('WWHere'))
        if m.get('Date') is not None:
            self.ocr_date = HouseholdWordItem().from_dict(m.get('Date'))
        if m.get('HouseholdType') is not None:
            self.household_type = HouseholdWordItem().from_dict(m.get('HouseholdType'))
        if m.get('HouseholderName') is not None:
            self.householder_name = HouseholdWordItem().from_dict(m.get('HouseholderName'))
        if m.get('Address') is not None:
            self.address = HouseholdWordItem().from_dict(m.get('Address'))
        if m.get('IssueDate') is not None:
            self.issue_date = HouseholdWordItem().from_dict(m.get('IssueDate'))
        return self
