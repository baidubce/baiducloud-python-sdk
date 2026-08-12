"""
Request entity for CreateSandboxSnapshotRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateSandboxSnapshotRequest(AbstractModel):
    """
    Request entity for CreateSandboxSnapshotRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, sandbox_id, name):
        """
        Initialize CreateSandboxSnapshotRequest request entity.

        :param sandbox_id: sandbox_id parameter
        :type sandbox_id: str (required)

        :param name: 快照模板名称，同时作为模板 ID。
        :type name: str (required)
        """
        super().__init__()
        self.sandbox_id = sandbox_id
        self.name = name

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
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSandboxSnapshotRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
