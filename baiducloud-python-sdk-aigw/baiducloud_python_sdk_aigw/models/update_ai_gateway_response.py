"""
Request entity for UpdateAIGatewayResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class UpdateAIGatewayResponse(BceResponse):
    """
    UpdateAIGatewayResponse
    """

    def __init__(
        self,
        instance_id=None,
        name=None,
        description=None,
        delete_protection=None,
        public_accessible=None,
        replicas=None,
        update_time=None,
    ):
        """
        Initialize UpdateAIGatewayResponse response.

        :param instance_id: 网关实例 ID
        :type instance_id: str (optional)

        :param name: 更新后的名称
        :type name: str (optional)

        :param description: 更新后的描述
        :type description: str (optional)

        :param delete_protection: 删除保护状态
        :type delete_protection: bool (optional)

        :param public_accessible: 公网访问状态
        :type public_accessible: bool (optional)

        :param replicas: 更新后的副本数
        :type replicas: int (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.name = name
        self.description = description
        self.delete_protection = delete_protection
        self.public_accessible = public_accessible
        self.replicas = replicas
        self.update_time = update_time

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
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.delete_protection is not None:
            result['deleteProtection'] = self.delete_protection
        if self.public_accessible is not None:
            result['publicAccessible'] = self.public_accessible
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAIGatewayResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('deleteProtection') is not None:
            self.delete_protection = m.get('deleteProtection')
        if m.get('publicAccessible') is not None:
            self.public_accessible = m.get('publicAccessible')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
