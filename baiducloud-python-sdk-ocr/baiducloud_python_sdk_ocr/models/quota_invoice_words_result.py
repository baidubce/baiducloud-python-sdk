"""
QuotaInvoiceWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QuotaInvoiceWordsResult(AbstractModel):
    """
    QuotaInvoiceWordsResult
    """

    def __init__(
        self,
        invoice_code=None,
        invoice_number=None,
        invoice_rate=None,
        location=None,
        invoice_rate_lowercase=None,
        province=None,
        city=None,
    ):
        """
        Initialize QuotaInvoiceWordsResult instance.

        :param invoice_code: 发票代码
        :type invoice_code: str (optional)

        :param invoice_number: 发票号码
        :type invoice_number: str (optional)

        :param invoice_rate: 金额
        :type invoice_rate: str (optional)

        :param location: 发票所在地
        :type location: str (optional)

        :param invoice_rate_lowercase: 发票金额小写
        :type invoice_rate_lowercase: str (optional)

        :param province: 省
        :type province: str (optional)

        :param city: 市
        :type city: str (optional)
        """
        super().__init__()
        self.invoice_code = invoice_code
        self.invoice_number = invoice_number
        self.invoice_rate = invoice_rate
        self.location = location
        self.invoice_rate_lowercase = invoice_rate_lowercase
        self.province = province
        self.city = city

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
        if self.invoice_code is not None:
            result['invoice_code'] = self.invoice_code
        if self.invoice_number is not None:
            result['invoice_number'] = self.invoice_number
        if self.invoice_rate is not None:
            result['invoice_rate'] = self.invoice_rate
        if self.location is not None:
            result['location'] = self.location
        if self.invoice_rate_lowercase is not None:
            result['invoice_rate_lowercase'] = self.invoice_rate_lowercase
        if self.province is not None:
            result['province'] = self.province
        if self.city is not None:
            result['city'] = self.city
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QuotaInvoiceWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('invoice_code') is not None:
            self.invoice_code = m.get('invoice_code')
        if m.get('invoice_number') is not None:
            self.invoice_number = m.get('invoice_number')
        if m.get('invoice_rate') is not None:
            self.invoice_rate = m.get('invoice_rate')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('invoice_rate_lowercase') is not None:
            self.invoice_rate_lowercase = m.get('invoice_rate_lowercase')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('city') is not None:
            self.city = m.get('city')
        return self
