"""
BankcardResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.bank_card_number_location import BankCardNumberLocation

from baiducloud_python_sdk_ocr.models.card_quality import CardQuality


class BankcardResult(AbstractModel):
    """
    BankcardResult
    """

    def __init__(
        self,
        bank_card_number=None,
        valid_date=None,
        bank_card_type=None,
        bank_name=None,
        holder_name=None,
        bank_card_number_location=None,
        card_quality=None,
    ):
        """
        Initialize BankcardResult instance.

        :param bank_card_number: 银行卡卡号
        :type bank_card_number: str (optional)

        :param valid_date: 有效期
        :type valid_date: str (optional)

        :param bank_card_type: 银行卡类型
        :type bank_card_type: int (optional)

        :param bank_name: 银行名
        :type bank_name: str (optional)

        :param holder_name: 持卡人姓名
        :type holder_name: str (optional)

        :param bank_card_number_location: bank_card_number_location attribute
        :type bank_card_number_location: BankCardNumberLocation (optional)

        :param card_quality: card_quality attribute
        :type card_quality: CardQuality (optional)
        """
        super().__init__()
        self.bank_card_number = bank_card_number
        self.valid_date = valid_date
        self.bank_card_type = bank_card_type
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.bank_card_number_location = bank_card_number_location
        self.card_quality = card_quality

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
        if self.bank_card_number is not None:
            result['bank_card_number'] = self.bank_card_number
        if self.valid_date is not None:
            result['valid_date'] = self.valid_date
        if self.bank_card_type is not None:
            result['bank_card_type'] = self.bank_card_type
        if self.bank_name is not None:
            result['bank_name'] = self.bank_name
        if self.holder_name is not None:
            result['holder_name'] = self.holder_name
        if self.bank_card_number_location is not None:
            result['bank_card_number_location'] = self.bank_card_number_location.to_dict()
        if self.card_quality is not None:
            result['card_quality'] = self.card_quality.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BankcardResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bank_card_number') is not None:
            self.bank_card_number = m.get('bank_card_number')
        if m.get('valid_date') is not None:
            self.valid_date = m.get('valid_date')
        if m.get('bank_card_type') is not None:
            self.bank_card_type = m.get('bank_card_type')
        if m.get('bank_name') is not None:
            self.bank_name = m.get('bank_name')
        if m.get('holder_name') is not None:
            self.holder_name = m.get('holder_name')
        if m.get('bank_card_number_location') is not None:
            self.bank_card_number_location = BankCardNumberLocation().from_dict(m.get('bank_card_number_location'))
        if m.get('card_quality') is not None:
            self.card_quality = CardQuality().from_dict(m.get('card_quality'))
        return self
