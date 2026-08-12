"""
Request entity for GetSandboxResourcesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ax.models.sandbox_container_resource_status import SandboxContainerResourceStatus
from baiducloud_python_sdk_ax.models.sandbox_resource_condition import SandboxResourceCondition


class GetSandboxResourcesResponse(BceResponse):
    """
    GetSandboxResourcesResponse
    """

    def __init__(
        self, sandbox_id=None, runtime_type=None, status=None, containers=None, conditions=None, message=None
    ):
        """
        Initialize GetSandboxResourcesResponse response.

        :param sandbox_id: 沙箱实例 ID。
        :type sandbox_id: str (optional)

        :param runtime_type: 运行时类型。
        :type runtime_type: str (optional)

        :param status: 调整状态。
        :type status: str (optional)

        :param containers: 容器资源状态列表。
        :type containers: List[SandboxContainerResourceStatus] (optional)

        :param conditions: 资源调整条件。
        :type conditions: List[SandboxResourceCondition] (optional)

        :param message: 状态说明。
        :type message: str (optional)
        """
        super().__init__()
        self.sandbox_id = sandbox_id
        self.runtime_type = runtime_type
        self.status = status
        self.containers = containers
        self.conditions = conditions
        self.message = message

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
        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id
        if self.runtime_type is not None:
            result['runtimeType'] = self.runtime_type
        if self.status is not None:
            result['status'] = self.status
        if self.containers is not None:
            result['containers'] = [i.to_dict() for i in self.containers]
        if self.conditions is not None:
            result['conditions'] = [i.to_dict() for i in self.conditions]
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetSandboxResourcesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')
        if m.get('runtimeType') is not None:
            self.runtime_type = m.get('runtimeType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('containers') is not None:
            self.containers = [SandboxContainerResourceStatus().from_dict(i) for i in m.get('containers')]
        if m.get('conditions') is not None:
            self.conditions = [SandboxResourceCondition().from_dict(i) for i in m.get('conditions')]
        if m.get('message') is not None:
            self.message = m.get('message')
        return self
