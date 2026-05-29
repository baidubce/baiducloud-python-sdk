"""
Request entity for ListProjectRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListProjectRequest(AbstractModel):
    """
    Request entity for ListProjectRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name=None, description=None, order_by=None, order=None, page_no=None, page_size=None):
        """
        Initialize ListProjectRequest request entity.

        :param name: 指定筛选日志组名称的关键字
        :type name: str (optional)

        :param description: 指定筛选日志组描述的关键字
        :type description: str (optional)

        :param order_by: 排序字段，默认为创建时间，支持createdAt: 创建时间，updatedAt: 修改时间, name: 名称
        :type order_by: str (optional)

        :param order: 排序顺序，desc为降序，asc为升序，默认为 desc
        :type order: str (optional)

        :param page_no: 起始页码，默认为 1
        :type page_no: int (optional)

        :param page_size: 每页显示数据大小，默认为 10
        :type page_size: int (optional)
        """
        super().__init__()
        self.name = name
        self.description = description
        self.order_by = order_by
        self.order = order
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
        if self.description is not None:
            result['description'] = self.description
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
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
        :rtype: ListProjectRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
