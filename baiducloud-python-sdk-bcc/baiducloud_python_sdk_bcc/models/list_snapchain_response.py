"""
Request entity for ListSnapchainResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.snapchain_model import SnapchainModel


class ListSnapchainResponse(BceResponse):
    """
    ListSnapchainResponse
    """

    def __init__(
        self, order_by=None, total_count=None, page_size=None, page_no=None, is_truncated=None, snapchains=None
    ):
        """
        Initialize ListSnapchainResponse response.

        :param order_by: 排序属性
        :type order_by: str (optional)

        :param total_count: 快照链总数
        :type total_count: int (optional)

        :param page_size: 该页容量
        :type page_size: int (optional)

        :param page_no: 页数
        :type page_no: int (optional)

        :param is_truncated: true表示后面还有数据，false表示已经是最后一页
        :type is_truncated: bool (optional)

        :param snapchains: 快照链信息，由 SnapchainModel 组成的集合
        :type snapchains: List[SnapchainModel] (optional)
        """
        super().__init__()
        self.order_by = order_by
        self.total_count = total_count
        self.page_size = page_size
        self.page_no = page_no
        self.is_truncated = is_truncated
        self.snapchains = snapchains

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.snapchains is not None:
            result['snapchains'] = [i.to_dict() for i in self.snapchains]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListSnapchainResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('snapchains') is not None:
            self.snapchains = [SnapchainModel().from_dict(i) for i in m.get('snapchains')]
        return self
