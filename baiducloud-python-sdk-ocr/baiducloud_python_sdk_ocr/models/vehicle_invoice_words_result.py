"""
VehicleInvoiceWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VehicleInvoiceWordsResult(AbstractModel):
    """
    VehicleInvoiceWordsResult
    """

    def __init__(
        self,
        invoice_header=None,
        invoice_code=None,
        invoice_num=None,
        printed_code=None,
        printed_num=None,
        invoice_date=None,
        machine_code=None,
        purchaser=None,
        purchaser_code=None,
        vehicle_type=None,
        manu_model=None,
        origin=None,
        certificate_num=None,
        engine_num=None,
        vin_num=None,
        price_tax=None,
        price_tax_low=None,
        saler=None,
        saler_phone=None,
        saler_code=None,
        saler_account_num=None,
        saler_address=None,
        saler_bank=None,
        tax_rate=None,
        tax=None,
        tax_author=None,
        tax_author_code=None,
        price=None,
        limit_passenger=None,
        toonage=None,
        sheet_num=None,
        drawer=None,
        remarks=None,
        import_certificate_num=None,
        tax_payment_voucher_no=None,
        inspection_form_num=None,
        tax_code=None,
        invoice_num_digit=None,
    ):
        """
        Initialize VehicleInvoiceWordsResult instance.

        :param invoice_header: 发票标题
        :type invoice_header: str (optional)

        :param invoice_code: 发票代码
        :type invoice_code: str (optional)

        :param invoice_num: 发票号码
        :type invoice_num: str (optional)

        :param printed_code: 机打代码
        :type printed_code: str (optional)

        :param printed_num: 机打号码
        :type printed_num: str (optional)

        :param invoice_date: 开票日期
        :type invoice_date: str (optional)

        :param machine_code: 机器编号
        :type machine_code: str (optional)

        :param purchaser: 购买方名称
        :type purchaser: str (optional)

        :param purchaser_code: 购买方身份证号码/组织机构代码
        :type purchaser_code: str (optional)

        :param vehicle_type: 车辆类型
        :type vehicle_type: str (optional)

        :param manu_model: 厂牌型号
        :type manu_model: str (optional)

        :param origin: 产地
        :type origin: str (optional)

        :param certificate_num: 合格证号
        :type certificate_num: str (optional)

        :param engine_num: 发动机号码
        :type engine_num: str (optional)

        :param vin_num: 车架号码
        :type vin_num: str (optional)

        :param price_tax: 价税合计
        :type price_tax: str (optional)

        :param price_tax_low: 价税合计小写
        :type price_tax_low: str (optional)

        :param saler: 销货单位名称
        :type saler: str (optional)

        :param saler_phone: 销货单位电话
        :type saler_phone: str (optional)

        :param saler_code: 销货单位纳税人识别号
        :type saler_code: str (optional)

        :param saler_account_num: 销货单位账号
        :type saler_account_num: str (optional)

        :param saler_address: 销货单位地址
        :type saler_address: str (optional)

        :param saler_bank: 销货单位开户银行
        :type saler_bank: str (optional)

        :param tax_rate: 税率
        :type tax_rate: str (optional)

        :param tax: 税额
        :type tax: str (optional)

        :param tax_author: 主管税务机关
        :type tax_author: str (optional)

        :param tax_author_code: 主管税务机关代码
        :type tax_author_code: str (optional)

        :param price: 不含税价格
        :type price: str (optional)

        :param limit_passenger: 限乘人数
        :type limit_passenger: str (optional)

        :param toonage: 吨位
        :type toonage: str (optional)

        :param sheet_num: 联次
        :type sheet_num: str (optional)

        :param drawer: 开票人
        :type drawer: str (optional)

        :param remarks: 备注
        :type remarks: str (optional)

        :param import_certificate_num: 进口证明书号
        :type import_certificate_num: str (optional)

        :param tax_payment_voucher_no: 完整凭税编号
        :type tax_payment_voucher_no: str (optional)

        :param inspection_form_num: 商检单号
        :type inspection_form_num: str (optional)

        :param tax_code: 税控码
        :type tax_code: str (optional)

        :param invoice_num_digit: 发票号码（数字）
        :type invoice_num_digit: str (optional)
        """
        super().__init__()
        self.invoice_header = invoice_header
        self.invoice_code = invoice_code
        self.invoice_num = invoice_num
        self.printed_code = printed_code
        self.printed_num = printed_num
        self.invoice_date = invoice_date
        self.machine_code = machine_code
        self.purchaser = purchaser
        self.purchaser_code = purchaser_code
        self.vehicle_type = vehicle_type
        self.manu_model = manu_model
        self.origin = origin
        self.certificate_num = certificate_num
        self.engine_num = engine_num
        self.vin_num = vin_num
        self.price_tax = price_tax
        self.price_tax_low = price_tax_low
        self.saler = saler
        self.saler_phone = saler_phone
        self.saler_code = saler_code
        self.saler_account_num = saler_account_num
        self.saler_address = saler_address
        self.saler_bank = saler_bank
        self.tax_rate = tax_rate
        self.tax = tax
        self.tax_author = tax_author
        self.tax_author_code = tax_author_code
        self.price = price
        self.limit_passenger = limit_passenger
        self.toonage = toonage
        self.sheet_num = sheet_num
        self.drawer = drawer
        self.remarks = remarks
        self.import_certificate_num = import_certificate_num
        self.tax_payment_voucher_no = tax_payment_voucher_no
        self.inspection_form_num = inspection_form_num
        self.tax_code = tax_code
        self.invoice_num_digit = invoice_num_digit

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
        if self.invoice_header is not None:
            result['InvoiceHeader'] = self.invoice_header
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_num is not None:
            result['InvoiceNum'] = self.invoice_num
        if self.printed_code is not None:
            result['PrintedCode'] = self.printed_code
        if self.printed_num is not None:
            result['PrintedNum'] = self.printed_num
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.machine_code is not None:
            result['MachineCode'] = self.machine_code
        if self.purchaser is not None:
            result['Purchaser'] = self.purchaser
        if self.purchaser_code is not None:
            result['PurchaserCode'] = self.purchaser_code
        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type
        if self.manu_model is not None:
            result['ManuModel'] = self.manu_model
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.certificate_num is not None:
            result['CertificateNum'] = self.certificate_num
        if self.engine_num is not None:
            result['EngineNum'] = self.engine_num
        if self.vin_num is not None:
            result['VinNum'] = self.vin_num
        if self.price_tax is not None:
            result['PriceTax'] = self.price_tax
        if self.price_tax_low is not None:
            result['PriceTaxLow'] = self.price_tax_low
        if self.saler is not None:
            result['Saler'] = self.saler
        if self.saler_phone is not None:
            result['SalerPhone'] = self.saler_phone
        if self.saler_code is not None:
            result['SalerCode'] = self.saler_code
        if self.saler_account_num is not None:
            result['SalerAccountNum'] = self.saler_account_num
        if self.saler_address is not None:
            result['SalerAddress'] = self.saler_address
        if self.saler_bank is not None:
            result['SalerBank'] = self.saler_bank
        if self.tax_rate is not None:
            result['TaxRate'] = self.tax_rate
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.tax_author is not None:
            result['TaxAuthor'] = self.tax_author
        if self.tax_author_code is not None:
            result['TaxAuthorCode'] = self.tax_author_code
        if self.price is not None:
            result['Price'] = self.price
        if self.limit_passenger is not None:
            result['LimitPassenger'] = self.limit_passenger
        if self.toonage is not None:
            result['toonage'] = self.toonage
        if self.sheet_num is not None:
            result['sheet-num'] = self.sheet_num
        if self.drawer is not None:
            result['drawer'] = self.drawer
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.import_certificate_num is not None:
            result['import-certificate-num'] = self.import_certificate_num
        if self.tax_payment_voucher_no is not None:
            result['tax-payment-voucher-no'] = self.tax_payment_voucher_no
        if self.inspection_form_num is not None:
            result['inspection-form-num'] = self.inspection_form_num
        if self.tax_code is not None:
            result['tax-code'] = self.tax_code
        if self.invoice_num_digit is not None:
            result['InvoiceNumDigit'] = self.invoice_num_digit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VehicleInvoiceWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('InvoiceHeader') is not None:
            self.invoice_header = m.get('InvoiceHeader')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNum') is not None:
            self.invoice_num = m.get('InvoiceNum')
        if m.get('PrintedCode') is not None:
            self.printed_code = m.get('PrintedCode')
        if m.get('PrintedNum') is not None:
            self.printed_num = m.get('PrintedNum')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('MachineCode') is not None:
            self.machine_code = m.get('MachineCode')
        if m.get('Purchaser') is not None:
            self.purchaser = m.get('Purchaser')
        if m.get('PurchaserCode') is not None:
            self.purchaser_code = m.get('PurchaserCode')
        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')
        if m.get('ManuModel') is not None:
            self.manu_model = m.get('ManuModel')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('CertificateNum') is not None:
            self.certificate_num = m.get('CertificateNum')
        if m.get('EngineNum') is not None:
            self.engine_num = m.get('EngineNum')
        if m.get('VinNum') is not None:
            self.vin_num = m.get('VinNum')
        if m.get('PriceTax') is not None:
            self.price_tax = m.get('PriceTax')
        if m.get('PriceTaxLow') is not None:
            self.price_tax_low = m.get('PriceTaxLow')
        if m.get('Saler') is not None:
            self.saler = m.get('Saler')
        if m.get('SalerPhone') is not None:
            self.saler_phone = m.get('SalerPhone')
        if m.get('SalerCode') is not None:
            self.saler_code = m.get('SalerCode')
        if m.get('SalerAccountNum') is not None:
            self.saler_account_num = m.get('SalerAccountNum')
        if m.get('SalerAddress') is not None:
            self.saler_address = m.get('SalerAddress')
        if m.get('SalerBank') is not None:
            self.saler_bank = m.get('SalerBank')
        if m.get('TaxRate') is not None:
            self.tax_rate = m.get('TaxRate')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('TaxAuthor') is not None:
            self.tax_author = m.get('TaxAuthor')
        if m.get('TaxAuthorCode') is not None:
            self.tax_author_code = m.get('TaxAuthorCode')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('LimitPassenger') is not None:
            self.limit_passenger = m.get('LimitPassenger')
        if m.get('toonage') is not None:
            self.toonage = m.get('toonage')
        if m.get('sheet-num') is not None:
            self.sheet_num = m.get('sheet-num')
        if m.get('drawer') is not None:
            self.drawer = m.get('drawer')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('import-certificate-num') is not None:
            self.import_certificate_num = m.get('import-certificate-num')
        if m.get('tax-payment-voucher-no') is not None:
            self.tax_payment_voucher_no = m.get('tax-payment-voucher-no')
        if m.get('inspection-form-num') is not None:
            self.inspection_form_num = m.get('inspection-form-num')
        if m.get('tax-code') is not None:
            self.tax_code = m.get('tax-code')
        if m.get('InvoiceNumDigit') is not None:
            self.invoice_num_digit = m.get('InvoiceNumDigit')
        return self
