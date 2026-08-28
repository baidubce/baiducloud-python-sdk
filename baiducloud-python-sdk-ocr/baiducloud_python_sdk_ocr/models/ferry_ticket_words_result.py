"""
FerryTicketWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FerryTicketWordsResult(AbstractModel):
    """
    FerryTicketWordsResult
    """

    def __init__(
        self,
        invoice_type=None,
        invoice_code=None,
        invoice_num=None,
        starting_station=None,
        destination_station=None,
        fare=None,
        invoice_date=None,
        bar_code=None,
        bar_code_num=None,
        city=None,
        invoice_title=None,
        province=None,
        qr_code=None,
        time=None,
        ticket_time=None,
        ticket_date=None,
        id_card=None,
        passenger_name=None,
    ):
        """
        Initialize FerryTicketWordsResult instance.

        :param invoice_type: 发票类型
        :type invoice_type: str (optional)

        :param invoice_code: 发票代码
        :type invoice_code: str (optional)

        :param invoice_num: 发票号码
        :type invoice_num: str (optional)

        :param starting_station: 出发地点
        :type starting_station: str (optional)

        :param destination_station: 到达地点
        :type destination_station: str (optional)

        :param fare: 总金额
        :type fare: str (optional)

        :param invoice_date: 开票日期
        :type invoice_date: str (optional)

        :param bar_code: 条形码识别结果
        :type bar_code: str (optional)

        :param bar_code_num: 条形码编号
        :type bar_code_num: str (optional)

        :param city: 城市
        :type city: str (optional)

        :param invoice_title: 发票标题
        :type invoice_title: str (optional)

        :param province: 省份
        :type province: str (optional)

        :param qr_code: 二维码识别结果
        :type qr_code: str (optional)

        :param time: 时间
        :type time: str (optional)

        :param ticket_time: 乘船时间
        :type ticket_time: str (optional)

        :param ticket_date: 乘船日期
        :type ticket_date: str (optional)

        :param id_card: 身份证号
        :type id_card: str (optional)

        :param passenger_name: 乘客姓名
        :type passenger_name: str (optional)
        """
        super().__init__()
        self.invoice_type = invoice_type
        self.invoice_code = invoice_code
        self.invoice_num = invoice_num
        self.starting_station = starting_station
        self.destination_station = destination_station
        self.fare = fare
        self.invoice_date = invoice_date
        self.bar_code = bar_code
        self.bar_code_num = bar_code_num
        self.city = city
        self.invoice_title = invoice_title
        self.province = province
        self.qr_code = qr_code
        self.time = time
        self.ticket_time = ticket_time
        self.ticket_date = ticket_date
        self.id_card = id_card
        self.passenger_name = passenger_name

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
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_num is not None:
            result['InvoiceNum'] = self.invoice_num
        if self.starting_station is not None:
            result['StartingStation'] = self.starting_station
        if self.destination_station is not None:
            result['DestinationStation'] = self.destination_station
        if self.fare is not None:
            result['Fare'] = self.fare
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.bar_code is not None:
            result['BarCode'] = self.bar_code
        if self.bar_code_num is not None:
            result['BarCodeNum'] = self.bar_code_num
        if self.city is not None:
            result['City'] = self.city
        if self.invoice_title is not None:
            result['InvoiceTitle'] = self.invoice_title
        if self.province is not None:
            result['Province'] = self.province
        if self.qr_code is not None:
            result['QrCode'] = self.qr_code
        if self.time is not None:
            result['Time'] = self.time
        if self.ticket_time is not None:
            result['TicketTime'] = self.ticket_time
        if self.ticket_date is not None:
            result['TicketDate'] = self.ticket_date
        if self.id_card is not None:
            result['IdCard'] = self.id_card
        if self.passenger_name is not None:
            result['PassengerName'] = self.passenger_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FerryTicketWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNum') is not None:
            self.invoice_num = m.get('InvoiceNum')
        if m.get('StartingStation') is not None:
            self.starting_station = m.get('StartingStation')
        if m.get('DestinationStation') is not None:
            self.destination_station = m.get('DestinationStation')
        if m.get('Fare') is not None:
            self.fare = m.get('Fare')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('BarCode') is not None:
            self.bar_code = m.get('BarCode')
        if m.get('BarCodeNum') is not None:
            self.bar_code_num = m.get('BarCodeNum')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('InvoiceTitle') is not None:
            self.invoice_title = m.get('InvoiceTitle')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('QrCode') is not None:
            self.qr_code = m.get('QrCode')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TicketTime') is not None:
            self.ticket_time = m.get('TicketTime')
        if m.get('TicketDate') is not None:
            self.ticket_date = m.get('TicketDate')
        if m.get('IdCard') is not None:
            self.id_card = m.get('IdCard')
        if m.get('PassengerName') is not None:
            self.passenger_name = m.get('PassengerName')
        return self
