"""
Request entity for DescribeNotifyTemplatesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeNotifyTemplatesRequest(AbstractModel):
    """
    Request entity for DescribeNotifyTemplatesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_no, page_size, name=None, policy_id=None, order=None, order_by=None):
        """
        Initialize DescribeNotifyTemplatesRequest request entity.

        :param name: 按通知模板名称筛选，支持部分匹配
        :type name: str (optional)

        :param policy_id: 策略ID，查询被该策略使用的通知模板
        :type policy_id: str (optional)

        :param order: 排序顺序，默认值：desc，可选值：desc / asc
        :type order: str (optional)

        :param order_by: 排序字段，默认值：updatedTime，可选值：updatedTime / createdTime
        :type order_by: str (optional)

        :param page_no: 页号，从1开始
        :type page_no: int (required)

        :param page_size: 页大小，取值范围：[1, 100]
        :type page_size: int (required)
        """
        super().__init__()
        self.name = name
        self.policy_id = policy_id
        self.order = order
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.order is not None:
            result['order'] = self.order
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeNotifyTemplatesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
