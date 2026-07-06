"""
Request entity for DescribeJobLogsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DescribeJobLogsResponse(BceResponse):
    """
    DescribeJobLogsResponse
    """

    def __init__(self, request_id=None, job_id=None, pod_name=None, logs=None, next_marker=None):
        """
        Initialize DescribeJobLogsResponse response.

        :param request_id: 请求ID
        :type request_id: str (optional)

        :param job_id: 任务ID
        :type job_id: str (optional)

        :param pod_name: Pod名称
        :type pod_name: str (optional)

        :param logs: 日志条目
        :type logs: List[str] (optional)

        :param next_marker: 下次查询的日志标识符
        :type next_marker: str (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.job_id = job_id
        self.pod_name = pod_name
        self.logs = logs
        self.next_marker = next_marker

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
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.pod_name is not None:
            result['podName'] = self.pod_name
        if self.logs is not None:
            result['logs'] = self.logs
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeJobLogsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('podName') is not None:
            self.pod_name = m.get('podName')
        if m.get('logs') is not None:
            self.logs = m.get('logs')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        return self
