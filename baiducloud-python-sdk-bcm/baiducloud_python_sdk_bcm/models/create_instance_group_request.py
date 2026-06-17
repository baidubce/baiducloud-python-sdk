"""
Request entity for CreateInstanceGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.instance_group_instance import InstanceGroupInstance


class CreateInstanceGroupRequest(AbstractModel):
    """
    Request entity for CreateInstanceGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, scope, resource_type, name, instances):
        """
        Initialize CreateInstanceGroupRequest request entity.

        :param scope: 云产品类型
        :type scope: str (required)

        :param resource_type: 资源类型
        :type resource_type: str (required)

        :param name: 实例组名称
        :type name: str (required)

        :param instances: 实例列表
        :type instances: List[InstanceGroupInstance] (required)
        """
        super().__init__()
        self.scope = scope
        self.resource_type = resource_type
        self.name = name
        self.instances = instances

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
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.name is not None:
            result['name'] = self.name
        if self.instances is not None:
            result['instances'] = [i.to_dict() for i in self.instances]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateInstanceGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instances') is not None:
            self.instances = [InstanceGroupInstance().from_dict(i) for i in m.get('instances')]
        return self
