"""
Request entity for ConnectSandboxRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ConnectSandboxRequest(AbstractModel):
    """
    Request entity for ConnectSandboxRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, sandbox_id, timeout, snapshot_id=None):
        """
        Initialize ConnectSandboxRequest request entity.

        :param sandbox_id: sandbox_id parameter
        :type sandbox_id: str (required)

        :param timeout: 续期时间，单位秒；-1 表示永久。
        :type timeout: int (required)

        :param snapshot_id: 恢复时使用的快照 ID。
        :type snapshot_id: str (optional)
        """
        super().__init__()
        self.sandbox_id = sandbox_id
        self.timeout = timeout
        self.snapshot_id = snapshot_id

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
        if self.snapshot_id is not None:
            result['snapshotID'] = self.snapshot_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ConnectSandboxRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('snapshotID') is not None:
            self.snapshot_id = m.get('snapshotID')
        return self
