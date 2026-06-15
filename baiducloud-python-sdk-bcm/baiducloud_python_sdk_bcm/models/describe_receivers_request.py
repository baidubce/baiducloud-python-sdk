"""
Request entity for DescribeReceiversRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeReceiversRequest(AbstractModel):
    """
    Request entity for DescribeReceiversRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, type, page_no, page_size, name=None):
        """
        Initialize DescribeReceiversRequest request entity.

        :param type: 对象类型，可选值：USER（单用户）/ USER_GROUP（用户组）
        :type type: str (required)

        :param name: 用户名或用户组名，支持部分匹配
        :type name: str (optional)

        :param page_no: 页号，从1开始
        :type page_no: int (required)

        :param page_size: 页大小
        :type page_size: int (required)
        """
        super().__init__()
        self.type = type
        self.name = name
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
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
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
        :rtype: DescribeReceiversRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
