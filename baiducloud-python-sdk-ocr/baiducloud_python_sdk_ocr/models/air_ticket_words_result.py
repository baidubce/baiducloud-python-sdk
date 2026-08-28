"""
AirTicketWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem

from baiducloud_python_sdk_ocr.models.air_ticket_word_item import AirTicketWordItem


class AirTicketWordsResult(AbstractModel):
    """
    AirTicketWordsResult
    """

    def __init__(
        self,
        invoice_type_org=None,
        name=None,
        starting_station=None,
        destination_station=None,
        flight=None,
        ocr_date=None,
        ticket_number=None,
        fare=None,
        dev_fund=None,
        fuel_surcharge=None,
        other_tax=None,
        ticket_rates=None,
        issued_date=None,
        id_num=None,
        carrier=None,
        time=None,
        issued_by=None,
        serial_number=None,
        insurance=None,
        fare_basis=None,
        ocr_class=None,
        agent_code=None,
        endorsement=None,
        allow=None,
        ck=None,
        effective_date=None,
        expiration_date=None,
        invoice_num=None,
        commodity_tax_rate=None,
        commodity_tax=None,
        purchaser_name=None,
        purchaser_register_num=None,
        identification=None,
        invoice_status=None,
        tip=None,
        service_type=None,
    ):
        """
        Initialize AirTicketWordsResult instance.

        :param invoice_type_org: 发票名称
        :type invoice_type_org: str (optional)

        :param name: 姓名
        :type name: List[AirTicketWordItem] (optional)

        :param starting_station: 始发站
        :type starting_station: List[AirTicketWordItem] (optional)

        :param destination_station: 目的站
        :type destination_station: List[AirTicketWordItem] (optional)

        :param flight: 航班号
        :type flight: List[AirTicketWordItem] (optional)

        :param ocr_date: 日期
        :type ocr_date: List[AirTicketWordItem] (optional)

        :param ticket_number: 电子客票号码
        :type ticket_number: List[AirTicketWordItem] (optional)

        :param fare: 票价
        :type fare: List[AirTicketWordItem] (optional)

        :param dev_fund: 民航发展基金/机建费
        :type dev_fund: List[AirTicketWordItem] (optional)

        :param fuel_surcharge: 燃油附加费
        :type fuel_surcharge: List[AirTicketWordItem] (optional)

        :param other_tax: 其他税费
        :type other_tax: List[AirTicketWordItem] (optional)

        :param ticket_rates: 合计金额
        :type ticket_rates: List[AirTicketWordItem] (optional)

        :param issued_date: 填开日期
        :type issued_date: List[AirTicketWordItem] (optional)

        :param id_num: 身份证号
        :type id_num: List[AirTicketWordItem] (optional)

        :param carrier: 承运人
        :type carrier: List[AirTicketWordItem] (optional)

        :param time: 时间
        :type time: List[AirTicketWordItem] (optional)

        :param issued_by: 填开单位
        :type issued_by: List[AirTicketWordItem] (optional)

        :param serial_number: 印刷序号
        :type serial_number: List[AirTicketWordItem] (optional)

        :param insurance: 保险费
        :type insurance: List[AirTicketWordItem] (optional)

        :param fare_basis: 客票级别
        :type fare_basis: List[AirTicketWordItem] (optional)

        :param ocr_class: 座位等级
        :type ocr_class: List[AirTicketWordItem] (optional)

        :param agent_code: 销售单位号
        :type agent_code: List[AirTicketWordItem] (optional)

        :param endorsement: 签注
        :type endorsement: List[AirTicketWordItem] (optional)

        :param allow: 免费行李
        :type allow: List[AirTicketWordItem] (optional)

        :param ck: 验证码
        :type ck: List[AirTicketWordItem] (optional)

        :param effective_date: 客票生效日期
        :type effective_date: List[AirTicketWordItem] (optional)

        :param expiration_date: 有效期截止日期
        :type expiration_date: List[AirTicketWordItem] (optional)

        :param invoice_num: 发票号码
        :type invoice_num: List[AirTicketWordItem] (optional)

        :param commodity_tax_rate: 增值税税率
        :type commodity_tax_rate: List[AirTicketWordItem] (optional)

        :param commodity_tax: 增值税税额
        :type commodity_tax: List[AirTicketWordItem] (optional)

        :param purchaser_name: 购买方名称
        :type purchaser_name: List[AirTicketWordItem] (optional)

        :param purchaser_register_num: 统一社会信用代码/纳税人识别号
        :type purchaser_register_num: List[AirTicketWordItem] (optional)

        :param identification: 国内国际标识
        :type identification: List[AirTicketWordItem] (optional)

        :param invoice_status: 开票状态
        :type invoice_status: List[AirTicketWordItem] (optional)

        :param tip: 提示信息
        :type tip: List[AirTicketWordItem] (optional)

        :param service_type: 服务类型
        :type service_type: List[AirTicketWordItem] (optional)
        """
        super().__init__()
        self.invoice_type_org = invoice_type_org
        self.name = name
        self.starting_station = starting_station
        self.destination_station = destination_station
        self.flight = flight
        self.ocr_date = ocr_date
        self.ticket_number = ticket_number
        self.fare = fare
        self.dev_fund = dev_fund
        self.fuel_surcharge = fuel_surcharge
        self.other_tax = other_tax
        self.ticket_rates = ticket_rates
        self.issued_date = issued_date
        self.id_num = id_num
        self.carrier = carrier
        self.time = time
        self.issued_by = issued_by
        self.serial_number = serial_number
        self.insurance = insurance
        self.fare_basis = fare_basis
        self.ocr_class = ocr_class
        self.agent_code = agent_code
        self.endorsement = endorsement
        self.allow = allow
        self.ck = ck
        self.effective_date = effective_date
        self.expiration_date = expiration_date
        self.invoice_num = invoice_num
        self.commodity_tax_rate = commodity_tax_rate
        self.commodity_tax = commodity_tax
        self.purchaser_name = purchaser_name
        self.purchaser_register_num = purchaser_register_num
        self.identification = identification
        self.invoice_status = invoice_status
        self.tip = tip
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
        if self.invoice_type_org is not None:
            result['invoice_type_org'] = self.invoice_type_org
        if self.name is not None:
            result['name'] = [i.to_dict() for i in self.name]
        if self.starting_station is not None:
            result['starting_station'] = [i.to_dict() for i in self.starting_station]
        if self.destination_station is not None:
            result['destination_station'] = [i.to_dict() for i in self.destination_station]
        if self.flight is not None:
            result['flight'] = [i.to_dict() for i in self.flight]
        if self.ocr_date is not None:
            result['date'] = [i.to_dict() for i in self.ocr_date]
        if self.ticket_number is not None:
            result['ticket_number'] = [i.to_dict() for i in self.ticket_number]
        if self.fare is not None:
            result['fare'] = [i.to_dict() for i in self.fare]
        if self.dev_fund is not None:
            result['dev_fund'] = [i.to_dict() for i in self.dev_fund]
        if self.fuel_surcharge is not None:
            result['fuel_surcharge'] = [i.to_dict() for i in self.fuel_surcharge]
        if self.other_tax is not None:
            result['other_tax'] = [i.to_dict() for i in self.other_tax]
        if self.ticket_rates is not None:
            result['ticket_rates'] = [i.to_dict() for i in self.ticket_rates]
        if self.issued_date is not None:
            result['issued_date'] = [i.to_dict() for i in self.issued_date]
        if self.id_num is not None:
            result['id_num'] = [i.to_dict() for i in self.id_num]
        if self.carrier is not None:
            result['carrier'] = [i.to_dict() for i in self.carrier]
        if self.time is not None:
            result['time'] = [i.to_dict() for i in self.time]
        if self.issued_by is not None:
            result['issued_by'] = [i.to_dict() for i in self.issued_by]
        if self.serial_number is not None:
            result['serial_number'] = [i.to_dict() for i in self.serial_number]
        if self.insurance is not None:
            result['insurance'] = [i.to_dict() for i in self.insurance]
        if self.fare_basis is not None:
            result['fare_basis'] = [i.to_dict() for i in self.fare_basis]
        if self.ocr_class is not None:
            result['class'] = [i.to_dict() for i in self.ocr_class]
        if self.agent_code is not None:
            result['agent_code'] = [i.to_dict() for i in self.agent_code]
        if self.endorsement is not None:
            result['endorsement'] = [i.to_dict() for i in self.endorsement]
        if self.allow is not None:
            result['allow'] = [i.to_dict() for i in self.allow]
        if self.ck is not None:
            result['ck'] = [i.to_dict() for i in self.ck]
        if self.effective_date is not None:
            result['effective_date'] = [i.to_dict() for i in self.effective_date]
        if self.expiration_date is not None:
            result['expiration_date'] = [i.to_dict() for i in self.expiration_date]
        if self.invoice_num is not None:
            result['invoice_num'] = [i.to_dict() for i in self.invoice_num]
        if self.commodity_tax_rate is not None:
            result['commodity_tax_rate'] = [i.to_dict() for i in self.commodity_tax_rate]
        if self.commodity_tax is not None:
            result['commodity_tax'] = [i.to_dict() for i in self.commodity_tax]
        if self.purchaser_name is not None:
            result['purchaser_name'] = [i.to_dict() for i in self.purchaser_name]
        if self.purchaser_register_num is not None:
            result['purchaser_register_num'] = [i.to_dict() for i in self.purchaser_register_num]
        if self.identification is not None:
            result['identification'] = [i.to_dict() for i in self.identification]
        if self.invoice_status is not None:
            result['invoice_status'] = [i.to_dict() for i in self.invoice_status]
        if self.tip is not None:
            result['tip'] = [i.to_dict() for i in self.tip]
        if self.service_type is not None:
            result['ServiceType'] = [i.to_dict() for i in self.service_type]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AirTicketWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('invoice_type_org') is not None:
            self.invoice_type_org = m.get('invoice_type_org')
        if m.get('name') is not None:
            self.name = [AirTicketWordItem().from_dict(i) for i in m.get('name')]
        if m.get('starting_station') is not None:
            self.starting_station = [AirTicketWordItem().from_dict(i) for i in m.get('starting_station')]
        if m.get('destination_station') is not None:
            self.destination_station = [AirTicketWordItem().from_dict(i) for i in m.get('destination_station')]
        if m.get('flight') is not None:
            self.flight = [AirTicketWordItem().from_dict(i) for i in m.get('flight')]
        if m.get('date') is not None:
            self.ocr_date = [AirTicketWordItem().from_dict(i) for i in m.get('date')]
        if m.get('ticket_number') is not None:
            self.ticket_number = [AirTicketWordItem().from_dict(i) for i in m.get('ticket_number')]
        if m.get('fare') is not None:
            self.fare = [AirTicketWordItem().from_dict(i) for i in m.get('fare')]
        if m.get('dev_fund') is not None:
            self.dev_fund = [AirTicketWordItem().from_dict(i) for i in m.get('dev_fund')]
        if m.get('fuel_surcharge') is not None:
            self.fuel_surcharge = [AirTicketWordItem().from_dict(i) for i in m.get('fuel_surcharge')]
        if m.get('other_tax') is not None:
            self.other_tax = [AirTicketWordItem().from_dict(i) for i in m.get('other_tax')]
        if m.get('ticket_rates') is not None:
            self.ticket_rates = [AirTicketWordItem().from_dict(i) for i in m.get('ticket_rates')]
        if m.get('issued_date') is not None:
            self.issued_date = [AirTicketWordItem().from_dict(i) for i in m.get('issued_date')]
        if m.get('id_num') is not None:
            self.id_num = [AirTicketWordItem().from_dict(i) for i in m.get('id_num')]
        if m.get('carrier') is not None:
            self.carrier = [AirTicketWordItem().from_dict(i) for i in m.get('carrier')]
        if m.get('time') is not None:
            self.time = [AirTicketWordItem().from_dict(i) for i in m.get('time')]
        if m.get('issued_by') is not None:
            self.issued_by = [AirTicketWordItem().from_dict(i) for i in m.get('issued_by')]
        if m.get('serial_number') is not None:
            self.serial_number = [AirTicketWordItem().from_dict(i) for i in m.get('serial_number')]
        if m.get('insurance') is not None:
            self.insurance = [AirTicketWordItem().from_dict(i) for i in m.get('insurance')]
        if m.get('fare_basis') is not None:
            self.fare_basis = [AirTicketWordItem().from_dict(i) for i in m.get('fare_basis')]
        if m.get('class') is not None:
            self.ocr_class = [AirTicketWordItem().from_dict(i) for i in m.get('class')]
        if m.get('agent_code') is not None:
            self.agent_code = [AirTicketWordItem().from_dict(i) for i in m.get('agent_code')]
        if m.get('endorsement') is not None:
            self.endorsement = [AirTicketWordItem().from_dict(i) for i in m.get('endorsement')]
        if m.get('allow') is not None:
            self.allow = [AirTicketWordItem().from_dict(i) for i in m.get('allow')]
        if m.get('ck') is not None:
            self.ck = [AirTicketWordItem().from_dict(i) for i in m.get('ck')]
        if m.get('effective_date') is not None:
            self.effective_date = [AirTicketWordItem().from_dict(i) for i in m.get('effective_date')]
        if m.get('expiration_date') is not None:
            self.expiration_date = [AirTicketWordItem().from_dict(i) for i in m.get('expiration_date')]
        if m.get('invoice_num') is not None:
            self.invoice_num = [AirTicketWordItem().from_dict(i) for i in m.get('invoice_num')]
        if m.get('commodity_tax_rate') is not None:
            self.commodity_tax_rate = [AirTicketWordItem().from_dict(i) for i in m.get('commodity_tax_rate')]
        if m.get('commodity_tax') is not None:
            self.commodity_tax = [AirTicketWordItem().from_dict(i) for i in m.get('commodity_tax')]
        if m.get('purchaser_name') is not None:
            self.purchaser_name = [AirTicketWordItem().from_dict(i) for i in m.get('purchaser_name')]
        if m.get('purchaser_register_num') is not None:
            self.purchaser_register_num = [AirTicketWordItem().from_dict(i) for i in m.get('purchaser_register_num')]
        if m.get('identification') is not None:
            self.identification = [AirTicketWordItem().from_dict(i) for i in m.get('identification')]
        if m.get('invoice_status') is not None:
            self.invoice_status = [AirTicketWordItem().from_dict(i) for i in m.get('invoice_status')]
        if m.get('tip') is not None:
            self.tip = [AirTicketWordItem().from_dict(i) for i in m.get('tip')]
        if m.get('ServiceType') is not None:
            self.service_type = [AirTicketWordItem().from_dict(i) for i in m.get('ServiceType')]
        return self
