"""
VatInvoiceWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord

from baiducloud_python_sdk_ocr.models.vat_invoice_row_word import VatInvoiceRowWord


class VatInvoiceWordsResult(AbstractModel):
    """
    VatInvoiceWordsResult
    """

    def __init__(
        self,
        service_type=None,
        invoice_type=None,
        invoice_type_org=None,
        invoice_code=None,
        invoice_num=None,
        invoice_code_confirm=None,
        invoice_num_confirm=None,
        invoice_num_digit=None,
        invoice_tag=None,
        machine_num=None,
        machine_code=None,
        check_code=None,
        invoice_date=None,
        purchaser_name=None,
        purchaser_register_num=None,
        purchaser_address=None,
        purchaser_bank=None,
        password=None,
        province=None,
        city=None,
        sheet_num=None,
        agent=None,
        commodity_name=None,
        commodity_type=None,
        commodity_unit=None,
        commodity_num=None,
        commodity_price=None,
        commodity_amount=None,
        commodity_tax_rate=None,
        commodity_tax=None,
        commodity_plate_num=None,
        commodity_vehicle_type=None,
        commodity_start_date=None,
        commodity_end_date=None,
        online_pay=None,
        seller_name=None,
        seller_register_num=None,
        seller_address=None,
        seller_bank=None,
        total_amount=None,
        total_tax=None,
        amount_in_words=None,
        amount_in_figuers=None,
        payee=None,
        checker=None,
        note_drawer=None,
        remarks=None,
        company_seal=None,
        seal_info=None,
        supervision_seal=None,
        supervision_seal_info=None,
        passenger_name=None,
        passenger_id_num=None,
        passenger_date=None,
        passenger_departure=None,
        passenger_arrival=None,
        passenger_class=None,
        passenger_vehicle_type=None,
        transport_type=None,
        transport_plate_num=None,
        transport_departure=None,
        transport_arrival=None,
        transport_cargo_info=None,
    ):
        """
        Initialize VatInvoiceWordsResult instance.

        :param service_type: 发票消费类型。不同消费类型输出：餐饮、电器设备、通讯、服务、日用品食品、医疗、交通、其他
        :type service_type: str (optional)

        :param invoice_type: invoice_type attribute
        :type invoice_type: str (optional)

        :param invoice_type_org: 发票名称
        :type invoice_type_org: str (optional)

        :param invoice_code: 发票代码
        :type invoice_code: str (optional)

        :param invoice_num: 发票号码
        :type invoice_num: str (optional)

        :param invoice_code_confirm: 发票代码的辅助校验码，一般业务情景可忽略
        :type invoice_code_confirm: str (optional)

        :param invoice_num_confirm: 发票号码的辅助校验码，一般业务情景可忽略
        :type invoice_num_confirm: str (optional)

        :param invoice_num_digit: 数电票号，仅针对纸质的全电发票，在密码区有数电票号码的字段输出
        :type invoice_num_digit: str (optional)

        :param invoice_tag: 增值税发票左上角标志。包含：通行费、销项负数、代开、收购、成品油、其他
        :type invoice_tag: str (optional)

        :param machine_num: 机打号码。仅增值税卷票含有此参数
        :type machine_num: str (optional)

        :param machine_code: 机器编号。仅增值税卷票含有此参数
        :type machine_code: str (optional)

        :param check_code: 校验码
        :type check_code: str (optional)

        :param invoice_date: 开票日期
        :type invoice_date: str (optional)

        :param purchaser_name: 购方名称
        :type purchaser_name: str (optional)

        :param purchaser_register_num: 购方纳税人识别号
        :type purchaser_register_num: str (optional)

        :param purchaser_address: 购方地址及电话
        :type purchaser_address: str (optional)

        :param purchaser_bank: 购方开户行及账号
        :type purchaser_bank: str (optional)

        :param password: 密码区
        :type password: str (optional)

        :param province: 省
        :type province: str (optional)

        :param city: 市
        :type city: str (optional)

        :param sheet_num: sheet_num attribute
        :type sheet_num: str (optional)

        :param agent: 是否代开
        :type agent: str (optional)

        :param commodity_name: 货物名称
        :type commodity_name: List[VatInvoiceRowWord] (optional)

        :param commodity_type: 规格型号
        :type commodity_type: List[VatInvoiceRowWord] (optional)

        :param commodity_unit: 单位
        :type commodity_unit: List[VatInvoiceRowWord] (optional)

        :param commodity_num: 数量
        :type commodity_num: List[VatInvoiceRowWord] (optional)

        :param commodity_price: 单价
        :type commodity_price: List[VatInvoiceRowWord] (optional)

        :param commodity_amount: 金额
        :type commodity_amount: List[VatInvoiceRowWord] (optional)

        :param commodity_tax_rate: 税率
        :type commodity_tax_rate: List[VatInvoiceRowWord] (optional)

        :param commodity_tax: 税额
        :type commodity_tax: List[VatInvoiceRowWord] (optional)

        :param commodity_plate_num: 车牌号。仅通行费增值税电子普通发票含有此参数
        :type commodity_plate_num: List[VatInvoiceRowWord] (optional)

        :param commodity_vehicle_type: 类型。仅通行费增值税电子普通发票含有此参数
        :type commodity_vehicle_type: List[VatInvoiceRowWord] (optional)

        :param commodity_start_date: 通行日期起。仅通行费增值税电子普通发票含有此参数
        :type commodity_start_date: List[VatInvoiceRowWord] (optional)

        :param commodity_end_date: 通行日期止。仅通行费增值税电子普通发票含有此参数
        :type commodity_end_date: List[VatInvoiceRowWord] (optional)

        :param online_pay: 电子支付标识。仅区块链发票含有此参数
        :type online_pay: str (optional)

        :param seller_name: 销售方名称
        :type seller_name: str (optional)

        :param seller_register_num: 销售方纳税人识别号
        :type seller_register_num: str (optional)

        :param seller_address: 销售方地址及电话
        :type seller_address: str (optional)

        :param seller_bank: 销售方开户行及账号
        :type seller_bank: str (optional)

        :param total_amount: 合计金额
        :type total_amount: str (optional)

        :param total_tax: 合计税额
        :type total_tax: str (optional)

        :param amount_in_words: 价税合计(大写)
        :type amount_in_words: str (optional)

        :param amount_in_figuers: 价税合计(小写)
        :type amount_in_figuers: str (optional)

        :param payee: 收款人
        :type payee: str (optional)

        :param checker: 复核
        :type checker: str (optional)

        :param note_drawer: 开票人
        :type note_drawer: str (optional)

        :param remarks: 备注
        :type remarks: str (optional)

        :param company_seal: company_seal attribute
        :type company_seal: str (optional)

        :param seal_info: 公司印章识别结果内容。当seal_tag=true时返回该字段
        :type seal_info: str (optional)

        :param supervision_seal: supervision_seal attribute
        :type supervision_seal: str (optional)

        :param supervision_seal_info: 监制印章识别结果内容。当seal_tag=true时返回该字段
        :type supervision_seal_info: str (optional)

        :param passenger_name: 出行人，仅旅客运输类发票有此参数，其余类型该参数返回为空
        :type passenger_name: List[str] (optional)

        :param passenger_id_num: 有效身份证件号，仅旅客运输类发票有此参数，其余类型该参数返回为空
        :type passenger_id_num: List[str] (optional)

        :param passenger_date: 出行日期，仅旅客运输类发票有此参数，其余类型该参数返回为空
        :type passenger_date: List[str] (optional)

        :param passenger_departure: 出发地，仅旅客运输类发票有此参数，其余类型该参数返回为空
        :type passenger_departure: List[str] (optional)

        :param passenger_arrival: 到达地，仅旅客运输类发票有此参数，其余类型该参数返回为空
        :type passenger_arrival: List[str] (optional)

        :param passenger_class: 等级，仅旅客运输类发票有此参数，其余类型该参数返回为空
        :type passenger_class: List[str] (optional)

        :param passenger_vehicle_type: 交通工具类型，仅旅客运输类发票有此参数，其余类型该参数返回为空
        :type passenger_vehicle_type: List[str] (optional)

        :param transport_type: 运输工具种类，仅货物运输类发票有此参数，其余类型该参数返回为空
        :type transport_type: List[str] (optional)

        :param transport_plate_num: 运输工具牌号，仅货物运输类发票有此参数，其余类型该参数返回为空
        :type transport_plate_num: List[str] (optional)

        :param transport_departure: 起运地，仅货物运输类发票有此参数，其余类型该参数返回为空
        :type transport_departure: List[str] (optional)

        :param transport_arrival: 到达地，仅货物运输类发票有此参数，其余类型该参数返回为空
        :type transport_arrival: List[str] (optional)

        :param transport_cargo_info: 运输货物名称，仅货物运输类发票有此参数，其余类型该参数返回为空
        :type transport_cargo_info: List[str] (optional)
        """
        super().__init__()
        self.service_type = service_type
        self.invoice_type = invoice_type
        self.invoice_type_org = invoice_type_org
        self.invoice_code = invoice_code
        self.invoice_num = invoice_num
        self.invoice_code_confirm = invoice_code_confirm
        self.invoice_num_confirm = invoice_num_confirm
        self.invoice_num_digit = invoice_num_digit
        self.invoice_tag = invoice_tag
        self.machine_num = machine_num
        self.machine_code = machine_code
        self.check_code = check_code
        self.invoice_date = invoice_date
        self.purchaser_name = purchaser_name
        self.purchaser_register_num = purchaser_register_num
        self.purchaser_address = purchaser_address
        self.purchaser_bank = purchaser_bank
        self.password = password
        self.province = province
        self.city = city
        self.sheet_num = sheet_num
        self.agent = agent
        self.commodity_name = commodity_name
        self.commodity_type = commodity_type
        self.commodity_unit = commodity_unit
        self.commodity_num = commodity_num
        self.commodity_price = commodity_price
        self.commodity_amount = commodity_amount
        self.commodity_tax_rate = commodity_tax_rate
        self.commodity_tax = commodity_tax
        self.commodity_plate_num = commodity_plate_num
        self.commodity_vehicle_type = commodity_vehicle_type
        self.commodity_start_date = commodity_start_date
        self.commodity_end_date = commodity_end_date
        self.online_pay = online_pay
        self.seller_name = seller_name
        self.seller_register_num = seller_register_num
        self.seller_address = seller_address
        self.seller_bank = seller_bank
        self.total_amount = total_amount
        self.total_tax = total_tax
        self.amount_in_words = amount_in_words
        self.amount_in_figuers = amount_in_figuers
        self.payee = payee
        self.checker = checker
        self.note_drawer = note_drawer
        self.remarks = remarks
        self.company_seal = company_seal
        self.seal_info = seal_info
        self.supervision_seal = supervision_seal
        self.supervision_seal_info = supervision_seal_info
        self.passenger_name = passenger_name
        self.passenger_id_num = passenger_id_num
        self.passenger_date = passenger_date
        self.passenger_departure = passenger_departure
        self.passenger_arrival = passenger_arrival
        self.passenger_class = passenger_class
        self.passenger_vehicle_type = passenger_vehicle_type
        self.transport_type = transport_type
        self.transport_plate_num = transport_plate_num
        self.transport_departure = transport_departure
        self.transport_arrival = transport_arrival
        self.transport_cargo_info = transport_cargo_info

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
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.invoice_type_org is not None:
            result['InvoiceTypeOrg'] = self.invoice_type_org
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_num is not None:
            result['InvoiceNum'] = self.invoice_num
        if self.invoice_code_confirm is not None:
            result['InvoiceCodeConfirm'] = self.invoice_code_confirm
        if self.invoice_num_confirm is not None:
            result['InvoiceNumConfirm'] = self.invoice_num_confirm
        if self.invoice_num_digit is not None:
            result['InvoiceNumDigit'] = self.invoice_num_digit
        if self.invoice_tag is not None:
            result['InvoiceTag'] = self.invoice_tag
        if self.machine_num is not None:
            result['MachineNum'] = self.machine_num
        if self.machine_code is not None:
            result['MachineCode'] = self.machine_code
        if self.check_code is not None:
            result['CheckCode'] = self.check_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.purchaser_name is not None:
            result['PurchaserName'] = self.purchaser_name
        if self.purchaser_register_num is not None:
            result['PurchaserRegisterNum'] = self.purchaser_register_num
        if self.purchaser_address is not None:
            result['PurchaserAddress'] = self.purchaser_address
        if self.purchaser_bank is not None:
            result['PurchaserBank'] = self.purchaser_bank
        if self.password is not None:
            result['Password'] = self.password
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.sheet_num is not None:
            result['SheetNum'] = self.sheet_num
        if self.agent is not None:
            result['Agent'] = self.agent
        if self.commodity_name is not None:
            result['CommodityName'] = [i.to_dict() for i in self.commodity_name]
        if self.commodity_type is not None:
            result['CommodityType'] = [i.to_dict() for i in self.commodity_type]
        if self.commodity_unit is not None:
            result['CommodityUnit'] = [i.to_dict() for i in self.commodity_unit]
        if self.commodity_num is not None:
            result['CommodityNum'] = [i.to_dict() for i in self.commodity_num]
        if self.commodity_price is not None:
            result['CommodityPrice'] = [i.to_dict() for i in self.commodity_price]
        if self.commodity_amount is not None:
            result['CommodityAmount'] = [i.to_dict() for i in self.commodity_amount]
        if self.commodity_tax_rate is not None:
            result['CommodityTaxRate'] = [i.to_dict() for i in self.commodity_tax_rate]
        if self.commodity_tax is not None:
            result['CommodityTax'] = [i.to_dict() for i in self.commodity_tax]
        if self.commodity_plate_num is not None:
            result['CommodityPlateNum'] = [i.to_dict() for i in self.commodity_plate_num]
        if self.commodity_vehicle_type is not None:
            result['CommodityVehicleType'] = [i.to_dict() for i in self.commodity_vehicle_type]
        if self.commodity_start_date is not None:
            result['CommodityStartDate'] = [i.to_dict() for i in self.commodity_start_date]
        if self.commodity_end_date is not None:
            result['CommodityEndDate'] = [i.to_dict() for i in self.commodity_end_date]
        if self.online_pay is not None:
            result['OnlinePay'] = self.online_pay
        if self.seller_name is not None:
            result['SellerName'] = self.seller_name
        if self.seller_register_num is not None:
            result['SellerRegisterNum'] = self.seller_register_num
        if self.seller_address is not None:
            result['SellerAddress'] = self.seller_address
        if self.seller_bank is not None:
            result['SellerBank'] = self.seller_bank
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.total_tax is not None:
            result['TotalTax'] = self.total_tax
        if self.amount_in_words is not None:
            result['AmountInWords'] = self.amount_in_words
        if self.amount_in_figuers is not None:
            result['AmountInFiguers'] = self.amount_in_figuers
        if self.payee is not None:
            result['Payee'] = self.payee
        if self.checker is not None:
            result['Checker'] = self.checker
        if self.note_drawer is not None:
            result['NoteDrawer'] = self.note_drawer
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.company_seal is not None:
            result['company_seal'] = self.company_seal
        if self.seal_info is not None:
            result['seal_info'] = self.seal_info
        if self.supervision_seal is not None:
            result['supervision_seal'] = self.supervision_seal
        if self.supervision_seal_info is not None:
            result['supervision_seal_info'] = self.supervision_seal_info
        if self.passenger_name is not None:
            result['PassengerName'] = self.passenger_name
        if self.passenger_id_num is not None:
            result['PassengerIdNum'] = self.passenger_id_num
        if self.passenger_date is not None:
            result['PassengerDate'] = self.passenger_date
        if self.passenger_departure is not None:
            result['PassengerDeparture'] = self.passenger_departure
        if self.passenger_arrival is not None:
            result['PassengerArrival'] = self.passenger_arrival
        if self.passenger_class is not None:
            result['PassengerClass'] = self.passenger_class
        if self.passenger_vehicle_type is not None:
            result['PassengerVehicleType'] = self.passenger_vehicle_type
        if self.transport_type is not None:
            result['TransportType'] = self.transport_type
        if self.transport_plate_num is not None:
            result['TransportPlateNum'] = self.transport_plate_num
        if self.transport_departure is not None:
            result['TransportDeparture'] = self.transport_departure
        if self.transport_arrival is not None:
            result['TransportArrival'] = self.transport_arrival
        if self.transport_cargo_info is not None:
            result['TransportCargoInfo'] = self.transport_cargo_info
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VatInvoiceWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('InvoiceTypeOrg') is not None:
            self.invoice_type_org = m.get('InvoiceTypeOrg')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNum') is not None:
            self.invoice_num = m.get('InvoiceNum')
        if m.get('InvoiceCodeConfirm') is not None:
            self.invoice_code_confirm = m.get('InvoiceCodeConfirm')
        if m.get('InvoiceNumConfirm') is not None:
            self.invoice_num_confirm = m.get('InvoiceNumConfirm')
        if m.get('InvoiceNumDigit') is not None:
            self.invoice_num_digit = m.get('InvoiceNumDigit')
        if m.get('InvoiceTag') is not None:
            self.invoice_tag = m.get('InvoiceTag')
        if m.get('MachineNum') is not None:
            self.machine_num = m.get('MachineNum')
        if m.get('MachineCode') is not None:
            self.machine_code = m.get('MachineCode')
        if m.get('CheckCode') is not None:
            self.check_code = m.get('CheckCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('PurchaserName') is not None:
            self.purchaser_name = m.get('PurchaserName')
        if m.get('PurchaserRegisterNum') is not None:
            self.purchaser_register_num = m.get('PurchaserRegisterNum')
        if m.get('PurchaserAddress') is not None:
            self.purchaser_address = m.get('PurchaserAddress')
        if m.get('PurchaserBank') is not None:
            self.purchaser_bank = m.get('PurchaserBank')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('SheetNum') is not None:
            self.sheet_num = m.get('SheetNum')
        if m.get('Agent') is not None:
            self.agent = m.get('Agent')
        if m.get('CommodityName') is not None:
            self.commodity_name = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityName')]
        if m.get('CommodityType') is not None:
            self.commodity_type = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityType')]
        if m.get('CommodityUnit') is not None:
            self.commodity_unit = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityUnit')]
        if m.get('CommodityNum') is not None:
            self.commodity_num = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityNum')]
        if m.get('CommodityPrice') is not None:
            self.commodity_price = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityPrice')]
        if m.get('CommodityAmount') is not None:
            self.commodity_amount = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityAmount')]
        if m.get('CommodityTaxRate') is not None:
            self.commodity_tax_rate = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityTaxRate')]
        if m.get('CommodityTax') is not None:
            self.commodity_tax = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityTax')]
        if m.get('CommodityPlateNum') is not None:
            self.commodity_plate_num = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityPlateNum')]
        if m.get('CommodityVehicleType') is not None:
            self.commodity_vehicle_type = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityVehicleType')]
        if m.get('CommodityStartDate') is not None:
            self.commodity_start_date = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityStartDate')]
        if m.get('CommodityEndDate') is not None:
            self.commodity_end_date = [VatInvoiceRowWord().from_dict(i) for i in m.get('CommodityEndDate')]
        if m.get('OnlinePay') is not None:
            self.online_pay = m.get('OnlinePay')
        if m.get('SellerName') is not None:
            self.seller_name = m.get('SellerName')
        if m.get('SellerRegisterNum') is not None:
            self.seller_register_num = m.get('SellerRegisterNum')
        if m.get('SellerAddress') is not None:
            self.seller_address = m.get('SellerAddress')
        if m.get('SellerBank') is not None:
            self.seller_bank = m.get('SellerBank')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('TotalTax') is not None:
            self.total_tax = m.get('TotalTax')
        if m.get('AmountInWords') is not None:
            self.amount_in_words = m.get('AmountInWords')
        if m.get('AmountInFiguers') is not None:
            self.amount_in_figuers = m.get('AmountInFiguers')
        if m.get('Payee') is not None:
            self.payee = m.get('Payee')
        if m.get('Checker') is not None:
            self.checker = m.get('Checker')
        if m.get('NoteDrawer') is not None:
            self.note_drawer = m.get('NoteDrawer')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('company_seal') is not None:
            self.company_seal = m.get('company_seal')
        if m.get('seal_info') is not None:
            self.seal_info = m.get('seal_info')
        if m.get('supervision_seal') is not None:
            self.supervision_seal = m.get('supervision_seal')
        if m.get('supervision_seal_info') is not None:
            self.supervision_seal_info = m.get('supervision_seal_info')
        if m.get('PassengerName') is not None:
            self.passenger_name = m.get('PassengerName')
        if m.get('PassengerIdNum') is not None:
            self.passenger_id_num = m.get('PassengerIdNum')
        if m.get('PassengerDate') is not None:
            self.passenger_date = m.get('PassengerDate')
        if m.get('PassengerDeparture') is not None:
            self.passenger_departure = m.get('PassengerDeparture')
        if m.get('PassengerArrival') is not None:
            self.passenger_arrival = m.get('PassengerArrival')
        if m.get('PassengerClass') is not None:
            self.passenger_class = m.get('PassengerClass')
        if m.get('PassengerVehicleType') is not None:
            self.passenger_vehicle_type = m.get('PassengerVehicleType')
        if m.get('TransportType') is not None:
            self.transport_type = m.get('TransportType')
        if m.get('TransportPlateNum') is not None:
            self.transport_plate_num = m.get('TransportPlateNum')
        if m.get('TransportDeparture') is not None:
            self.transport_departure = m.get('TransportDeparture')
        if m.get('TransportArrival') is not None:
            self.transport_arrival = m.get('TransportArrival')
        if m.get('TransportCargoInfo') is not None:
            self.transport_cargo_info = m.get('TransportCargoInfo')
        return self
