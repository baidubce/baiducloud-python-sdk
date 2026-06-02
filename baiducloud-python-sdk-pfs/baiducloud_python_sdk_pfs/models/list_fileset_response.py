"""
Request entity for ListFilesetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.fileset_model import FilesetModel


class ListFilesetResponse(BceResponse):
    """
    ListFilesetResponse
    """

    def __init__(
        self,
        request_id=None,
        result=None,
        page_no=None,
        page_size=None,
        total_count=None,
        max_fileset_num=None,
        max_files_quota=None,
        min_files_quota=None,
    ):
        """
        Initialize ListFilesetResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type request_id: str (optional)

        :param result: fileset列表
        :type result: List[FilesetModel] (optional)

        :param page_no: 页数
        :type page_no: int (optional)

        :param page_size: 页大小
        :type page_size: int (optional)

        :param total_count: 返回fileset list的总数量
        :type total_count: int (optional)

        :param max_fileset_num: 该用户可创建的fileset最大数量
        :type max_fileset_num: int (optional)

        :param max_files_quota: 该用户可设置的fileset最大文件数配额
        :type max_files_quota: int (optional)

        :param min_files_quota: 该用户可设置的fileset最小文件数配额
        :type min_files_quota: int (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.result = result
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.max_fileset_num = max_fileset_num
        self.max_files_quota = max_files_quota
        self.min_files_quota = min_files_quota

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.max_fileset_num is not None:
            result['maxFilesetNum'] = self.max_fileset_num
        if self.max_files_quota is not None:
            result['maxFilesQuota'] = self.max_files_quota
        if self.min_files_quota is not None:
            result['minFilesQuota'] = self.min_files_quota
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListFilesetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = [FilesetModel().from_dict(i) for i in m.get('result')]
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('maxFilesetNum') is not None:
            self.max_fileset_num = m.get('maxFilesetNum')
        if m.get('maxFilesQuota') is not None:
            self.max_files_quota = m.get('maxFilesQuota')
        if m.get('minFilesQuota') is not None:
            self.min_files_quota = m.get('minFilesQuota')
        return self
