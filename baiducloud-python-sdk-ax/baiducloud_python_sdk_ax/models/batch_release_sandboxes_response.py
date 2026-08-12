"""
Request entity for BatchReleaseSandboxesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ax.models.release_result import ReleaseResult


class BatchReleaseSandboxesResponse(BceResponse):
    """
    BatchReleaseSandboxesResponse
    """

    def __init__(self, results=None):
        """
        Initialize BatchReleaseSandboxesResponse response.

        :param results: 每个沙箱实例的释放结果。
        :type results: List[ReleaseResult] (optional)
        """
        super().__init__()
        self.results = results

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
        if self.results is not None:
            result['results'] = [i.to_dict() for i in self.results]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchReleaseSandboxesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('results') is not None:
            self.results = [ReleaseResult().from_dict(i) for i in m.get('results')]
        return self
