"""
Request entity for CreateAIGatewayResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAIGatewayResponse(BceResponse):
    """
    CreateAIGatewayResponse
    """

    def __init__(self, instance_id=None, request_id=None, task_id=None, security_group_id=None):
        """
        Initialize CreateAIGatewayResponse response.

        :param instance_id: 新创建的网关实例 ID
        :type instance_id: str (optional)

        :param request_id: 请求 ID
        :type request_id: str (optional)

        :param task_id: 异步创建任务 ID
        :type task_id: str (optional)

        :param security_group_id: 创建或复用的安全组 ID
        :type security_group_id: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.request_id = request_id
        self.task_id = task_id
        self.security_group_id = security_group_id

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAIGatewayResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        return self
