"""
BusTicketWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BusTicketWordsResult(AbstractModel):
    """
    BusTicketWordsResult
    """

    def __init__(
        self,
        invoice_code=None,
        invoice_num=None,
        ocr_date=None,
        time=None,
        starting_station=None,
        fare=None,
        id_num=None,
        destination_station=None,
        name=None,
    ):
        """
        Initialize BusTicketWordsResult instance.

        :param invoice_code: 发票代码
        :type invoice_code: str (optional)

        :param invoice_num: 发票号码
        :type invoice_num: str (optional)

        :param ocr_date: 日期
        :type ocr_date: str (optional)

        :param time: 时间
        :type time: str (optional)

        :param starting_station: 出发站
        :type starting_station: str (optional)

        :param fare: 金额
        :type fare: str (optional)

        :param id_num: 身份证号
        :type id_num: str (optional)

        :param destination_station: 到达站
        :type destination_station: str (optional)

        :param name: 姓名
        :type name: str (optional)
        """
        super().__init__()
        self.invoice_code = invoice_code
        self.invoice_num = invoice_num
        self.ocr_date = ocr_date
        self.time = time
        self.starting_station = starting_station
        self.fare = fare
        self.id_num = id_num
        self.destination_station = destination_station
        self.name = name

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
        if self.ocr_date is not None:
            result['Date'] = self.ocr_date
        if self.time is not None:
            result['Time'] = self.time
        if self.starting_station is not None:
            result['StartingStation'] = self.starting_station
        if self.fare is not None:
            result['Fare'] = self.fare
        if self.id_num is not None:
            result['IdNum'] = self.id_num
        if self.destination_station is not None:
            result['DestinationStation'] = self.destination_station
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BusTicketWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNum') is not None:
            self.invoice_num = m.get('InvoiceNum')
        if m.get('Date') is not None:
            self.ocr_date = m.get('Date')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('StartingStation') is not None:
            self.starting_station = m.get('StartingStation')
        if m.get('Fare') is not None:
            self.fare = m.get('Fare')
        if m.get('IdNum') is not None:
            self.id_num = m.get('IdNum')
        if m.get('DestinationStation') is not None:
            self.destination_station = m.get('DestinationStation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self
