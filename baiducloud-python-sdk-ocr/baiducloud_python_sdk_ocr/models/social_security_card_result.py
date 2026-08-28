"""
SocialSecurityCardResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.social_security_card_field import SocialSecurityCardField

from baiducloud_python_sdk_ocr.models.social_security_card_field import SocialSecurityCardField

from baiducloud_python_sdk_ocr.models.social_security_card_field import SocialSecurityCardField

from baiducloud_python_sdk_ocr.models.social_security_card_field import SocialSecurityCardField

from baiducloud_python_sdk_ocr.models.social_security_card_field import SocialSecurityCardField

from baiducloud_python_sdk_ocr.models.social_security_card_field import SocialSecurityCardField

from baiducloud_python_sdk_ocr.models.social_security_card_field import SocialSecurityCardField

from baiducloud_python_sdk_ocr.models.social_security_card_field import SocialSecurityCardField


class SocialSecurityCardResult(AbstractModel):
    """
    SocialSecurityCardResult
    """

    def __init__(
        self,
        card_number=None,
        name=None,
        sex=None,
        birth_date=None,
        social_security_number=None,
        issue_date=None,
        bank_card_number=None,
        expiry_date=None,
    ):
        """
        Initialize SocialSecurityCardResult instance.

        :param card_number: card_number attribute
        :type card_number: SocialSecurityCardField (optional)

        :param name: name attribute
        :type name: SocialSecurityCardField (optional)

        :param sex: sex attribute
        :type sex: SocialSecurityCardField (optional)

        :param birth_date: birth_date attribute
        :type birth_date: SocialSecurityCardField (optional)

        :param social_security_number: social_security_number attribute
        :type social_security_number: SocialSecurityCardField (optional)

        :param issue_date: issue_date attribute
        :type issue_date: SocialSecurityCardField (optional)

        :param bank_card_number: bank_card_number attribute
        :type bank_card_number: SocialSecurityCardField (optional)

        :param expiry_date: expiry_date attribute
        :type expiry_date: SocialSecurityCardField (optional)
        """
        super().__init__()
        self.card_number = card_number
        self.name = name
        self.sex = sex
        self.birth_date = birth_date
        self.social_security_number = social_security_number
        self.issue_date = issue_date
        self.bank_card_number = bank_card_number
        self.expiry_date = expiry_date

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
        if self.card_number is not None:
            result['card_number'] = self.card_number.to_dict()
        if self.name is not None:
            result['name'] = self.name.to_dict()
        if self.sex is not None:
            result['sex'] = self.sex.to_dict()
        if self.birth_date is not None:
            result['birth_date'] = self.birth_date.to_dict()
        if self.social_security_number is not None:
            result['social_security_number'] = self.social_security_number.to_dict()
        if self.issue_date is not None:
            result['issue_date'] = self.issue_date.to_dict()
        if self.bank_card_number is not None:
            result['bank_card_number'] = self.bank_card_number.to_dict()
        if self.expiry_date is not None:
            result['expiry_date'] = self.expiry_date.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SocialSecurityCardResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('card_number') is not None:
            self.card_number = SocialSecurityCardField().from_dict(m.get('card_number'))
        if m.get('name') is not None:
            self.name = SocialSecurityCardField().from_dict(m.get('name'))
        if m.get('sex') is not None:
            self.sex = SocialSecurityCardField().from_dict(m.get('sex'))
        if m.get('birth_date') is not None:
            self.birth_date = SocialSecurityCardField().from_dict(m.get('birth_date'))
        if m.get('social_security_number') is not None:
            self.social_security_number = SocialSecurityCardField().from_dict(m.get('social_security_number'))
        if m.get('issue_date') is not None:
            self.issue_date = SocialSecurityCardField().from_dict(m.get('issue_date'))
        if m.get('bank_card_number') is not None:
            self.bank_card_number = SocialSecurityCardField().from_dict(m.get('bank_card_number'))
        if m.get('expiry_date') is not None:
            self.expiry_date = SocialSecurityCardField().from_dict(m.get('expiry_date'))
        return self
