"""
Request entity for DeleteInstanceGroupInstancesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.instance_group_instance import InstanceGroupInstance


class DeleteInstanceGroupInstancesRequest(AbstractModel):
    """
    Request entity for DeleteInstanceGroupInstancesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, instances):
        """
        Initialize DeleteInstanceGroupInstancesRequest request entity.

        :param id: 实例组ID
        :type id: str (required)

        :param instances: 待删除的实例列表
        :type instances: List[InstanceGroupInstance] (required)
        """
        super().__init__()
        self.id = id
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
        if self.id is not None:
            result['id'] = self.id
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
        :rtype: DeleteInstanceGroupInstancesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instances') is not None:
            self.instances = [InstanceGroupInstance().from_dict(i) for i in m.get('instances')]
        return self
