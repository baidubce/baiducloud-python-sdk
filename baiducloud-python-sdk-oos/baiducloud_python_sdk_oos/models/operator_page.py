"""
OperatorPage information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.operator_spec import OperatorSpec

from baiducloud_python_sdk_oos.models.category import Category


class OperatorPage(AbstractModel):
    """
    OperatorPage
    """

    def __init__(
        self,
        operators=None,
        categories=None,
        order_by=None,
        order=None,
        page_no=None,
        page_size=None,
        total_count=None,
    ):
        """
        Initialize OperatorPage instance.

        :param operators: operator 列表
        :type operators: List[OperatorSpec] (optional)

        :param categories: operator 分类列表
        :type categories: List[Category] (optional)

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param order: 排序方向 asc/desc
        :type order: str (optional)

        :param page_no: 页数
        :type page_no: int (optional)

        :param page_size: 每页展示数量
        :type page_size: int (optional)

        :param total_count: 总数量
        :type total_count: int (optional)
        """
        super().__init__()
        self.operators = operators
        self.categories = categories
        self.order_by = order_by
        self.order = order
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count

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
        if self.operators is not None:
            result['operators'] = [i.to_dict() for i in self.operators]
        if self.categories is not None:
            result['categories'] = [i.to_dict() for i in self.categories]
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OperatorPage

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('operators') is not None:
            self.operators = [OperatorSpec().from_dict(i) for i in m.get('operators')]
        if m.get('categories') is not None:
            self.categories = [Category().from_dict(i) for i in m.get('categories')]
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self
