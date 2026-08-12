"""
Request entity for SetSandboxTimeoutRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SetSandboxTimeoutRequest(AbstractModel):
    """
    Request entity for SetSandboxTimeoutRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, sandbox_id, timeout):
        """
        Initialize SetSandboxTimeoutRequest request entity.

        :param sandbox_id: sandbox_id parameter
        :type sandbox_id: str (required)

        :param timeout: 从当前时间起的存活时间，单位秒。
        :type timeout: int (required)
        """
        super().__init__()
        self.sandbox_id = sandbox_id
        self.timeout = timeout

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
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SetSandboxTimeoutRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self
