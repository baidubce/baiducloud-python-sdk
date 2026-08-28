"""
TollInvoiceWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TollInvoiceWordsResult(AbstractModel):
    """
    TollInvoiceWordsResult
    """

    def __init__(
        self,
        invoice_code=None,
        invoice_num=None,
        entrance=None,
        exit=None,
        ocr_date=None,
        time=None,
        fare=None,
        province=None,
        city=None,
    ):
        """
        Initialize TollInvoiceWordsResult instance.

        :param invoice_code: 发票代码
        :type invoice_code: str (optional)

        :param invoice_num: 发票号码
        :type invoice_num: str (optional)

        :param entrance: 入口
        :type entrance: str (optional)

        :param exit: 出口
        :type exit: str (optional)

        :param ocr_date: 日期
        :type ocr_date: str (optional)

        :param time: 时间
        :type time: str (optional)

        :param fare: 金额
        :type fare: str (optional)

        :param province: 省
        :type province: str (optional)

        :param city: 市
        :type city: str (optional)
        """
        super().__init__()
        self.invoice_code = invoice_code
        self.invoice_num = invoice_num
        self.entrance = entrance
        self.exit = exit
        self.ocr_date = ocr_date
        self.time = time
        self.fare = fare
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
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_num is not None:
            result['InvoiceNum'] = self.invoice_num
        if self.entrance is not None:
            result['Entrance'] = self.entrance
        if self.exit is not None:
            result['Exit'] = self.exit
        if self.ocr_date is not None:
            result['Date'] = self.ocr_date
        if self.time is not None:
            result['Time'] = self.time
        if self.fare is not None:
            result['Fare'] = self.fare
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TollInvoiceWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNum') is not None:
            self.invoice_num = m.get('InvoiceNum')
        if m.get('Entrance') is not None:
            self.entrance = m.get('Entrance')
        if m.get('Exit') is not None:
            self.exit = m.get('Exit')
        if m.get('Date') is not None:
            self.ocr_date = m.get('Date')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Fare') is not None:
            self.fare = m.get('Fare')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        return self
