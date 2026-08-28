"""
TrainTicketWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TrainTicketWordsResult(AbstractModel):
    """
    TrainTicketWordsResult
    """

    def __init__(
        self,
        ticket_num=None,
        starting_station=None,
        train_num=None,
        destination_station=None,
        ocr_date=None,
        ticket_rates=None,
        seat_category=None,
        name=None,
        id_num=None,
        serial_number=None,
        sales_station=None,
        time=None,
        seat_num=None,
        refund_flag=None,
        invoice_num=None,
        invoice_date=None,
        fare=None,
        tax_rate=None,
        tax=None,
        elec_ticket_num=None,
        service_type=None,
    ):
        """
        Initialize TrainTicketWordsResult instance.

        :param ticket_num: 车票号
        :type ticket_num: str (optional)

        :param starting_station: 始发站
        :type starting_station: str (optional)

        :param train_num: 车次号
        :type train_num: str (optional)

        :param destination_station: 到达站
        :type destination_station: str (optional)

        :param ocr_date: 出发日期
        :type ocr_date: str (optional)

        :param ticket_rates: 车票金额
        :type ticket_rates: str (optional)

        :param seat_category: 席别
        :type seat_category: str (optional)

        :param name: 乘客姓名
        :type name: str (optional)

        :param id_num: 身份证号
        :type id_num: str (optional)

        :param serial_number: 序列号
        :type serial_number: str (optional)

        :param sales_station: 售站
        :type sales_station: str (optional)

        :param time: 时间
        :type time: str (optional)

        :param seat_num: 座位号
        :type seat_num: str (optional)

        :param refund_flag: 退票标识，仅在输入为电子火车票时返回该字段
        :type refund_flag: str (optional)

        :param invoice_num: 发票号码，仅在输入为电子火车票时返回该字段
        :type invoice_num: str (optional)

        :param invoice_date: 开票日期，仅在输入为电子火车票时返回该字段
        :type invoice_date: str (optional)

        :param fare: 不含税金额，仅在输入为电子火车票时返回该字段
        :type fare: str (optional)

        :param tax_rate: 税率，仅在输入为电子火车票时返回该字段
        :type tax_rate: str (optional)

        :param tax: 税额，仅在输入为电子火车票时返回该字段
        :type tax: str (optional)

        :param elec_ticket_num: 电子客票号，仅在输入为电子火车票时返回该字段
        :type elec_ticket_num: str (optional)

        :param service_type: 服务类型
        :type service_type: str (optional)
        """
        super().__init__()
        self.ticket_num = ticket_num
        self.starting_station = starting_station
        self.train_num = train_num
        self.destination_station = destination_station
        self.ocr_date = ocr_date
        self.ticket_rates = ticket_rates
        self.seat_category = seat_category
        self.name = name
        self.id_num = id_num
        self.serial_number = serial_number
        self.sales_station = sales_station
        self.time = time
        self.seat_num = seat_num
        self.refund_flag = refund_flag
        self.invoice_num = invoice_num
        self.invoice_date = invoice_date
        self.fare = fare
        self.tax_rate = tax_rate
        self.tax = tax
        self.elec_ticket_num = elec_ticket_num
        self.service_type = service_type

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
        if self.ticket_num is not None:
            result['ticket_num'] = self.ticket_num
        if self.starting_station is not None:
            result['starting_station'] = self.starting_station
        if self.train_num is not None:
            result['train_num'] = self.train_num
        if self.destination_station is not None:
            result['destination_station'] = self.destination_station
        if self.ocr_date is not None:
            result['date'] = self.ocr_date
        if self.ticket_rates is not None:
            result['ticket_rates'] = self.ticket_rates
        if self.seat_category is not None:
            result['seat_category'] = self.seat_category
        if self.name is not None:
            result['name'] = self.name
        if self.id_num is not None:
            result['id_num'] = self.id_num
        if self.serial_number is not None:
            result['serial_number'] = self.serial_number
        if self.sales_station is not None:
            result['sales_station'] = self.sales_station
        if self.time is not None:
            result['time'] = self.time
        if self.seat_num is not None:
            result['seat_num'] = self.seat_num
        if self.refund_flag is not None:
            result['refund_flag'] = self.refund_flag
        if self.invoice_num is not None:
            result['invoice_num'] = self.invoice_num
        if self.invoice_date is not None:
            result['invoice_date'] = self.invoice_date
        if self.fare is not None:
            result['fare'] = self.fare
        if self.tax_rate is not None:
            result['tax_rate'] = self.tax_rate
        if self.tax is not None:
            result['tax'] = self.tax
        if self.elec_ticket_num is not None:
            result['elec_ticket_num'] = self.elec_ticket_num
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TrainTicketWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ticket_num') is not None:
            self.ticket_num = m.get('ticket_num')
        if m.get('starting_station') is not None:
            self.starting_station = m.get('starting_station')
        if m.get('train_num') is not None:
            self.train_num = m.get('train_num')
        if m.get('destination_station') is not None:
            self.destination_station = m.get('destination_station')
        if m.get('date') is not None:
            self.ocr_date = m.get('date')
        if m.get('ticket_rates') is not None:
            self.ticket_rates = m.get('ticket_rates')
        if m.get('seat_category') is not None:
            self.seat_category = m.get('seat_category')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id_num') is not None:
            self.id_num = m.get('id_num')
        if m.get('serial_number') is not None:
            self.serial_number = m.get('serial_number')
        if m.get('sales_station') is not None:
            self.sales_station = m.get('sales_station')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('seat_num') is not None:
            self.seat_num = m.get('seat_num')
        if m.get('refund_flag') is not None:
            self.refund_flag = m.get('refund_flag')
        if m.get('invoice_num') is not None:
            self.invoice_num = m.get('invoice_num')
        if m.get('invoice_date') is not None:
            self.invoice_date = m.get('invoice_date')
        if m.get('fare') is not None:
            self.fare = m.get('fare')
        if m.get('tax_rate') is not None:
            self.tax_rate = m.get('tax_rate')
        if m.get('tax') is not None:
            self.tax = m.get('tax')
        if m.get('elec_ticket_num') is not None:
            self.elec_ticket_num = m.get('elec_ticket_num')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self
