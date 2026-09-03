"""
Request entity for UpdateAIGatewayRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aigw.models.tag import Tag


class UpdateAIGatewayRequest(AbstractModel):
    """
    Request entity for UpdateAIGatewayRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        x_region,
        name=None,
        description=None,
        delete_protection=None,
        public_accessible=None,
        replicas=None,
        network_types=None,
        tags=None,
    ):
        """
        Initialize UpdateAIGatewayRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param name: 实例名称
        :type name: str (optional)

        :param description: 实例描述
        :type description: str (optional)

        :param delete_protection: 是否开启删除保护
        :type delete_protection: bool (optional)

        :param public_accessible: 是否允许公网访问
        :type public_accessible: bool (optional)

        :param replicas: 副本数，服务端校验范围为 2-5
        :type replicas: int (optional)

        :param network_types: 网络类型：private、public，可多选
        :type network_types: List[str] (optional)

        :param tags: 标签列表；不传表示不修改，空数组表示清空
        :type tags: List[Tag] (optional)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.name = name
        self.description = description
        self.delete_protection = delete_protection
        self.public_accessible = public_accessible
        self.replicas = replicas
        self.network_types = network_types
        self.tags = tags
        self.x_region = x_region

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
        if self.description is not None:
            result['description'] = self.description
        if self.delete_protection is not None:
            result['deleteProtection'] = self.delete_protection
        if self.public_accessible is not None:
            result['publicAccessible'] = self.public_accessible
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.network_types is not None:
            result['networkTypes'] = self.network_types
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAIGatewayRequest

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
        if m.get('networkTypes') is not None:
            self.network_types = m.get('networkTypes')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
