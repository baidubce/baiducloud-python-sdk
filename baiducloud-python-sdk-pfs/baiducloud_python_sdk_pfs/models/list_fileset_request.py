"""
Request entity for ListFilesetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListFilesetRequest(AbstractModel):
    """
    Request entity for ListFilesetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        manner,
        fileset_id=None,
        fileset_name=None,
        order=None,
        order_by=None,
        page_no=None,
        page_size=None,
    ):
        """
        Initialize ListFilesetRequest request entity.

        :param instance_id: fileset所属PFS实例的短id
        :type instance_id: str (required)

        :param fileset_id: 基于filesetId进行过滤
        :type fileset_id: str (optional)

        :param fileset_name: 基于filesetName进行过滤
        :type fileset_name: str (optional)

        :param manner: 只支持page
        :type manner: str (required)

        :param order: 排序，desc倒序，asc正序
        :type order: str (optional)

        :param order_by: orderBy，默认createTime
        :type order_by: str (optional)

        :param page_no: 默认1
        :type page_no: int (optional)

        :param page_size: 默认10
        :type page_size: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.fileset_id = fileset_id
        self.fileset_name = fileset_name
        self.manner = manner
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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.fileset_id is not None:
            result['filesetId'] = self.fileset_id
        if self.fileset_name is not None:
            result['filesetName'] = self.fileset_name
        if self.manner is not None:
            result['manner'] = self.manner
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
        :rtype: ListFilesetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('filesetId') is not None:
            self.fileset_id = m.get('filesetId')
        if m.get('filesetName') is not None:
            self.fileset_name = m.get('filesetName')
        if m.get('manner') is not None:
            self.manner = m.get('manner')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
