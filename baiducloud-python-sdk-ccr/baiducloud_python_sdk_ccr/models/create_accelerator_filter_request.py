"""
Request entity for CreateAcceleratorFilterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_ccr.models.accelerator_filter import AcceleratorFilter


class CreateAcceleratorFilterRequest(AbstractModel):
    """
    Request entity for CreateAcceleratorFilterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, filters, name, description=None):
        """
        Initialize CreateAcceleratorFilterRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param description: 备注
        :type description: str (optional)

        :param filters: 触发规则
        :type filters: List[AcceleratorFilter] (required)

        :param name: 镜像按需加载规则名称
        :type name: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.description = description
        self.filters = filters
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
        if self.description is not None:
            result['description'] = self.description
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
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
        :rtype: CreateAcceleratorFilterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('filters') is not None:
            self.filters = [AcceleratorFilter().from_dict(i) for i in m.get('filters')]
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
