"""
Request entity for DescribeJobsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_aihc.models.job_item import JobItem


class DescribeJobsResponse(BceResponse):
    """
    DescribeJobsResponse
    """

    def __init__(self, request_id=None, total_count=None, jobs=None):
        """
        Initialize DescribeJobsResponse response.

        :param request_id: 请求ID，用于标识每个请求的唯一性
        :type request_id: str (optional)

        :param total_count: 返回任务总数
        :type total_count: int (optional)

        :param jobs: 成功请求时的返回结果
        :type jobs: List[JobItem] (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.total_count = total_count
        self.jobs = jobs

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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.jobs is not None:
            result['jobs'] = [i.to_dict() for i in self.jobs]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeJobsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('jobs') is not None:
            self.jobs = [JobItem().from_dict(i) for i in m.get('jobs')]
        return self
