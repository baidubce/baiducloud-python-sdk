"""
MultipleInvoiceResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.word_only_item import WordOnlyItem

from baiducloud_python_sdk_ocr.models.result_item import ResultItem

from baiducloud_python_sdk_ocr.models.result_item import ResultItem

from baiducloud_python_sdk_ocr.models.result_item import ResultItem

from baiducloud_python_sdk_ocr.models.word_only_item import WordOnlyItem

from baiducloud_python_sdk_ocr.models.word_only_item import WordOnlyItem

from baiducloud_python_sdk_ocr.models.result_item import ResultItem

from baiducloud_python_sdk_ocr.models.result_item import ResultItem

from baiducloud_python_sdk_ocr.models.result_item import ResultItem

from baiducloud_python_sdk_ocr.models.result_item import ResultItem


class MultipleInvoiceResult(AbstractModel):
    """
    MultipleInvoiceResult
    """

    def __init__(
        self,
        invoice_code=None,
        invoice_num=None,
        invoice_date=None,
        total_amount=None,
        invoice_type=None,
        check_code=None,
        seller_name=None,
        seller_register_num=None,
        purchaser_name=None,
        purchaser_register_num=None,
    ):
        """
        Initialize MultipleInvoiceResult instance.

        :param invoice_code: 发票代码
        :type invoice_code: List[WordOnlyItem] (optional)

        :param invoice_num: 发票号码
        :type invoice_num: List[ResultItem] (optional)

        :param invoice_date: 开票日期
        :type invoice_date: List[ResultItem] (optional)

        :param total_amount: 合计金额
        :type total_amount: List[ResultItem] (optional)

        :param invoice_type: 发票类型（分类结果，不含 probability/location）
        :type invoice_type: List[WordOnlyItem] (optional)

        :param check_code: 校验码
        :type check_code: List[WordOnlyItem] (optional)

        :param seller_name: 销售方名称
        :type seller_name: List[ResultItem] (optional)

        :param seller_register_num: 销售方纳税人识别号
        :type seller_register_num: List[ResultItem] (optional)

        :param purchaser_name: 购买方名称
        :type purchaser_name: List[ResultItem] (optional)

        :param purchaser_register_num: 购买方纳税人识别号
        :type purchaser_register_num: List[ResultItem] (optional)
        """
        super().__init__()
        self.invoice_code = invoice_code
        self.invoice_num = invoice_num
        self.invoice_date = invoice_date
        self.total_amount = total_amount
        self.invoice_type = invoice_type
        self.check_code = check_code
        self.seller_name = seller_name
        self.seller_register_num = seller_register_num
        self.purchaser_name = purchaser_name
        self.purchaser_register_num = purchaser_register_num

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
            result['invoice_code'] = [i.to_dict() for i in self.invoice_code]
        if self.invoice_num is not None:
            result['invoice_num'] = [i.to_dict() for i in self.invoice_num]
        if self.invoice_date is not None:
            result['invoice_date'] = [i.to_dict() for i in self.invoice_date]
        if self.total_amount is not None:
            result['total_amount'] = [i.to_dict() for i in self.total_amount]
        if self.invoice_type is not None:
            result['invoice_type'] = [i.to_dict() for i in self.invoice_type]
        if self.check_code is not None:
            result['check_code'] = [i.to_dict() for i in self.check_code]
        if self.seller_name is not None:
            result['seller_name'] = [i.to_dict() for i in self.seller_name]
        if self.seller_register_num is not None:
            result['seller_register_num'] = [i.to_dict() for i in self.seller_register_num]
        if self.purchaser_name is not None:
            result['purchaser_name'] = [i.to_dict() for i in self.purchaser_name]
        if self.purchaser_register_num is not None:
            result['purchaser_register_num'] = [i.to_dict() for i in self.purchaser_register_num]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MultipleInvoiceResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('invoice_code') is not None:
            self.invoice_code = [WordOnlyItem().from_dict(i) for i in m.get('invoice_code')]
        if m.get('invoice_num') is not None:
            self.invoice_num = [ResultItem().from_dict(i) for i in m.get('invoice_num')]
        if m.get('invoice_date') is not None:
            self.invoice_date = [ResultItem().from_dict(i) for i in m.get('invoice_date')]
        if m.get('total_amount') is not None:
            self.total_amount = [ResultItem().from_dict(i) for i in m.get('total_amount')]
        if m.get('invoice_type') is not None:
            self.invoice_type = [WordOnlyItem().from_dict(i) for i in m.get('invoice_type')]
        if m.get('check_code') is not None:
            self.check_code = [WordOnlyItem().from_dict(i) for i in m.get('check_code')]
        if m.get('seller_name') is not None:
            self.seller_name = [ResultItem().from_dict(i) for i in m.get('seller_name')]
        if m.get('seller_register_num') is not None:
            self.seller_register_num = [ResultItem().from_dict(i) for i in m.get('seller_register_num')]
        if m.get('purchaser_name') is not None:
            self.purchaser_name = [ResultItem().from_dict(i) for i in m.get('purchaser_name')]
        if m.get('purchaser_register_num') is not None:
            self.purchaser_register_num = [ResultItem().from_dict(i) for i in m.get('purchaser_register_num')]
        return self
