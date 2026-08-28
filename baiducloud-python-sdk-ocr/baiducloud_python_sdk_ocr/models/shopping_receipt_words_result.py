"""
ShoppingReceiptWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.table import Table


class ShoppingReceiptWordsResult(AbstractModel):
    """
    ShoppingReceiptWordsResult
    """

    def __init__(
        self,
        shop_name=None,
        receipt_num=None,
        machine_num=None,
        employee_num=None,
        consumption_date=None,
        consumption_time=None,
        total_amount=None,
        change=None,
        currency=None,
        paid_amount=None,
        discount=None,
        print_date=None,
        print_time=None,
        table_row_num=None,
        table=None,
    ):
        """
        Initialize ShoppingReceiptWordsResult instance.

        :param shop_name: 店名/超市名字
        :type shop_name: str (optional)

        :param receipt_num: 小票号码
        :type receipt_num: str (optional)

        :param machine_num: 机器编号
        :type machine_num: str (optional)

        :param employee_num: 工号
        :type employee_num: str (optional)

        :param consumption_date: 消费日期
        :type consumption_date: str (optional)

        :param consumption_time: 消费时间
        :type consumption_time: str (optional)

        :param total_amount: 总金额
        :type total_amount: str (optional)

        :param change: 找零
        :type change: str (optional)

        :param currency: 币种
        :type currency: str (optional)

        :param paid_amount: 实收金额
        :type paid_amount: str (optional)

        :param discount: 优惠/折扣
        :type discount: str (optional)

        :param print_date: 打印日期
        :type print_date: str (optional)

        :param print_time: 打印时间
        :type print_time: str (optional)

        :param table_row_num: 商品明细行数，表示Table中的object个数
        :type table_row_num: int (optional)

        :param table: 消费明细区域
        :type table: List[Table] (optional)
        """
        super().__init__()
        self.shop_name = shop_name
        self.receipt_num = receipt_num
        self.machine_num = machine_num
        self.employee_num = employee_num
        self.consumption_date = consumption_date
        self.consumption_time = consumption_time
        self.total_amount = total_amount
        self.change = change
        self.currency = currency
        self.paid_amount = paid_amount
        self.discount = discount
        self.print_date = print_date
        self.print_time = print_time
        self.table_row_num = table_row_num
        self.table = table

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
        if self.shop_name is not None:
            result['shop_name'] = self.shop_name
        if self.receipt_num is not None:
            result['receipt_num'] = self.receipt_num
        if self.machine_num is not None:
            result['machine_num'] = self.machine_num
        if self.employee_num is not None:
            result['employee_num'] = self.employee_num
        if self.consumption_date is not None:
            result['consumption_date'] = self.consumption_date
        if self.consumption_time is not None:
            result['consumption_time'] = self.consumption_time
        if self.total_amount is not None:
            result['total_amount'] = self.total_amount
        if self.change is not None:
            result['change'] = self.change
        if self.currency is not None:
            result['currency'] = self.currency
        if self.paid_amount is not None:
            result['paid_amount'] = self.paid_amount
        if self.discount is not None:
            result['discount'] = self.discount
        if self.print_date is not None:
            result['print_date'] = self.print_date
        if self.print_time is not None:
            result['print_time'] = self.print_time
        if self.table_row_num is not None:
            result['table_row_num'] = self.table_row_num
        if self.table is not None:
            result['table'] = [i.to_dict() for i in self.table]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ShoppingReceiptWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('shop_name') is not None:
            self.shop_name = m.get('shop_name')
        if m.get('receipt_num') is not None:
            self.receipt_num = m.get('receipt_num')
        if m.get('machine_num') is not None:
            self.machine_num = m.get('machine_num')
        if m.get('employee_num') is not None:
            self.employee_num = m.get('employee_num')
        if m.get('consumption_date') is not None:
            self.consumption_date = m.get('consumption_date')
        if m.get('consumption_time') is not None:
            self.consumption_time = m.get('consumption_time')
        if m.get('total_amount') is not None:
            self.total_amount = m.get('total_amount')
        if m.get('change') is not None:
            self.change = m.get('change')
        if m.get('currency') is not None:
            self.currency = m.get('currency')
        if m.get('paid_amount') is not None:
            self.paid_amount = m.get('paid_amount')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('print_date') is not None:
            self.print_date = m.get('print_date')
        if m.get('print_time') is not None:
            self.print_time = m.get('print_time')
        if m.get('table_row_num') is not None:
            self.table_row_num = m.get('table_row_num')
        if m.get('table') is not None:
            self.table = [Table().from_dict(i) for i in m.get('table')]
        return self
