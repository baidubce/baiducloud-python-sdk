"""
Request entity for ModifyJobResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ModifyJobResponse(BceResponse):
    """
    ModifyJobResponse
    """

    def __init__(self, job_id=None, request_id=None):
        """
        Initialize ModifyJobResponse response.

        :param job_id: 成功请求时的返回结果，任务id
        :type job_id: str (optional)

        :param request_id: 请求ID，用于标译每个请求的唯一性
        :type request_id: str (optional)
        """
        super().__init__()
        self.job_id = job_id
        self.request_id = request_id

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
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyJobResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self
