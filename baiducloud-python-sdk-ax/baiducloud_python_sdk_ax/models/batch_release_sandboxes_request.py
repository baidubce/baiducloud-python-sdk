"""
Request entity for BatchReleaseSandboxesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchReleaseSandboxesRequest(AbstractModel):
    """
    Request entity for BatchReleaseSandboxesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, sandbox_ids):
        """
        Initialize BatchReleaseSandboxesRequest request entity.

        :param sandbox_ids: 要释放的沙箱实例 ID 列表，最多 100 个。
        :type sandbox_ids: List[str] (required)
        """
        super().__init__()
        self.sandbox_ids = sandbox_ids

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
        if self.sandbox_ids is not None:
            result['sandboxIds'] = self.sandbox_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchReleaseSandboxesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxIds') is not None:
            self.sandbox_ids = m.get('sandboxIds')
        return self
