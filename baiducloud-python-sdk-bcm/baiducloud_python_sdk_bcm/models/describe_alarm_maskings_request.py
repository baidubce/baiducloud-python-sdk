"""
Request entity for DescribeAlarmMaskingsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAlarmMaskingsRequest(AbstractModel):
    """
    Request entity for DescribeAlarmMaskingsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_no, page_size, masking_name=None, masking_id=None, order=None, order_by=None):
        """
        Initialize DescribeAlarmMaskingsRequest request entity.

        :param masking_name: 屏蔽规则名称，模糊查询
        :type masking_name: str (optional)

        :param masking_id: 屏蔽规则ID，精确查询
        :type masking_id: str (optional)

        :param order: 排序方式，asc/desc
        :type order: str (optional)

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param page_no: 页码
        :type page_no: int (required)

        :param page_size: 每页条数
        :type page_size: int (required)
        """
        super().__init__()
        self.masking_name = masking_name
        self.masking_id = masking_id
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
        if self.masking_name is not None:
            result['maskingName'] = self.masking_name
        if self.masking_id is not None:
            result['maskingId'] = self.masking_id
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
        :rtype: DescribeAlarmMaskingsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('maskingName') is not None:
            self.masking_name = m.get('maskingName')
        if m.get('maskingId') is not None:
            self.masking_id = m.get('maskingId')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
