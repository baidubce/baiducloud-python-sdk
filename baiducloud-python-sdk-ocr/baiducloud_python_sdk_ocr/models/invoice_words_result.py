"""
InvoiceWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.invoice_row_word import InvoiceRowWord

from baiducloud_python_sdk_ocr.models.invoice_row_word import InvoiceRowWord

from baiducloud_python_sdk_ocr.models.invoice_row_word import InvoiceRowWord

from baiducloud_python_sdk_ocr.models.invoice_row_word import InvoiceRowWord

from baiducloud_python_sdk_ocr.models.invoice_row_word import InvoiceRowWord


class InvoiceWordsResult(AbstractModel):
    """
    InvoiceWordsResult
    """

    def __init__(
        self,
        invoice_type=None,
        invoice_code=None,
        invoice_num=None,
        invoice_date=None,
        amount_in_figuers=None,
        amount_in_words=None,
        commodity_name=None,
        commodity_unit=None,
        commodity_price=None,
        commodity_num=None,
        commodity_amount=None,
        industry_sort=None,
        machine_num=None,
        check_code=None,
        seller_name=None,
        seller_register_num=None,
        purchaser_name=None,
        purchaser_register_num=None,
        total_tax=None,
        province=None,
        city=None,
        time=None,
        sheet_num=None,
    ):
        """
        Initialize InvoiceWordsResult instance.

        :param invoice_type: 发票类型
        :type invoice_type: str (optional)

        :param invoice_code: 发票代码
        :type invoice_code: str (optional)

        :param invoice_num: 发票号码
        :type invoice_num: str (optional)

        :param invoice_date: 开票日期
        :type invoice_date: str (optional)

        :param amount_in_figuers: 合计金额小写
        :type amount_in_figuers: str (optional)

        :param amount_in_words: 合计金额大写
        :type amount_in_words: str (optional)

        :param commodity_name: 商品名称
        :type commodity_name: List[InvoiceRowWord] (optional)

        :param commodity_unit: 商品单位
        :type commodity_unit: List[InvoiceRowWord] (optional)

        :param commodity_price: 商品单价
        :type commodity_price: List[InvoiceRowWord] (optional)

        :param commodity_num: 商品数量
        :type commodity_num: List[InvoiceRowWord] (optional)

        :param commodity_amount: 商品金额
        :type commodity_amount: List[InvoiceRowWord] (optional)

        :param industry_sort: 行业分类
        :type industry_sort: str (optional)

        :param machine_num: 机打号码
        :type machine_num: str (optional)

        :param check_code: 校验码
        :type check_code: str (optional)

        :param seller_name: 销售方名称
        :type seller_name: str (optional)

        :param seller_register_num: 销售方纳税人识别号
        :type seller_register_num: str (optional)

        :param purchaser_name: 购买方名称
        :type purchaser_name: str (optional)

        :param purchaser_register_num: 购买方纳税人识别号
        :type purchaser_register_num: str (optional)

        :param total_tax: 合计税额
        :type total_tax: str (optional)

        :param province: 省
        :type province: str (optional)

        :param city: 市
        :type city: str (optional)

        :param time: 时间
        :type time: str (optional)

        :param sheet_num: 联次
        :type sheet_num: str (optional)
        """
        super().__init__()
        self.invoice_type = invoice_type
        self.invoice_code = invoice_code
        self.invoice_num = invoice_num
        self.invoice_date = invoice_date
        self.amount_in_figuers = amount_in_figuers
        self.amount_in_words = amount_in_words
        self.commodity_name = commodity_name
        self.commodity_unit = commodity_unit
        self.commodity_price = commodity_price
        self.commodity_num = commodity_num
        self.commodity_amount = commodity_amount
        self.industry_sort = industry_sort
        self.machine_num = machine_num
        self.check_code = check_code
        self.seller_name = seller_name
        self.seller_register_num = seller_register_num
        self.purchaser_name = purchaser_name
        self.purchaser_register_num = purchaser_register_num
        self.total_tax = total_tax
        self.province = province
        self.city = city
        self.time = time
        self.sheet_num = sheet_num

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
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.amount_in_figuers is not None:
            result['AmountInFiguers'] = self.amount_in_figuers
        if self.amount_in_words is not None:
            result['AmountInWords'] = self.amount_in_words
        if self.commodity_name is not None:
            result['CommodityName'] = [i.to_dict() for i in self.commodity_name]
        if self.commodity_unit is not None:
            result['CommodityUnit'] = [i.to_dict() for i in self.commodity_unit]
        if self.commodity_price is not None:
            result['CommodityPrice'] = [i.to_dict() for i in self.commodity_price]
        if self.commodity_num is not None:
            result['CommodityNum'] = [i.to_dict() for i in self.commodity_num]
        if self.commodity_amount is not None:
            result['CommodityAmount'] = [i.to_dict() for i in self.commodity_amount]
        if self.industry_sort is not None:
            result['IndustrySort'] = self.industry_sort
        if self.machine_num is not None:
            result['MachineNum'] = self.machine_num
        if self.check_code is not None:
            result['CheckCode'] = self.check_code
        if self.seller_name is not None:
            result['SellerName'] = self.seller_name
        if self.seller_register_num is not None:
            result['SellerRegisterNum'] = self.seller_register_num
        if self.purchaser_name is not None:
            result['PurchaserName'] = self.purchaser_name
        if self.purchaser_register_num is not None:
            result['PurchaserRegisterNum'] = self.purchaser_register_num
        if self.total_tax is not None:
            result['TotalTax'] = self.total_tax
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.time is not None:
            result['Time'] = self.time
        if self.sheet_num is not None:
            result['SheetNum'] = self.sheet_num
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InvoiceWordsResult

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
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('AmountInFiguers') is not None:
            self.amount_in_figuers = m.get('AmountInFiguers')
        if m.get('AmountInWords') is not None:
            self.amount_in_words = m.get('AmountInWords')
        if m.get('CommodityName') is not None:
            self.commodity_name = [InvoiceRowWord().from_dict(i) for i in m.get('CommodityName')]
        if m.get('CommodityUnit') is not None:
            self.commodity_unit = [InvoiceRowWord().from_dict(i) for i in m.get('CommodityUnit')]
        if m.get('CommodityPrice') is not None:
            self.commodity_price = [InvoiceRowWord().from_dict(i) for i in m.get('CommodityPrice')]
        if m.get('CommodityNum') is not None:
            self.commodity_num = [InvoiceRowWord().from_dict(i) for i in m.get('CommodityNum')]
        if m.get('CommodityAmount') is not None:
            self.commodity_amount = [InvoiceRowWord().from_dict(i) for i in m.get('CommodityAmount')]
        if m.get('IndustrySort') is not None:
            self.industry_sort = m.get('IndustrySort')
        if m.get('MachineNum') is not None:
            self.machine_num = m.get('MachineNum')
        if m.get('CheckCode') is not None:
            self.check_code = m.get('CheckCode')
        if m.get('SellerName') is not None:
            self.seller_name = m.get('SellerName')
        if m.get('SellerRegisterNum') is not None:
            self.seller_register_num = m.get('SellerRegisterNum')
        if m.get('PurchaserName') is not None:
            self.purchaser_name = m.get('PurchaserName')
        if m.get('PurchaserRegisterNum') is not None:
            self.purchaser_register_num = m.get('PurchaserRegisterNum')
        if m.get('TotalTax') is not None:
            self.total_tax = m.get('TotalTax')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('SheetNum') is not None:
            self.sheet_num = m.get('SheetNum')
        return self
