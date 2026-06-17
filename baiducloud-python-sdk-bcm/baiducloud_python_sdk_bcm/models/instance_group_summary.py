"""
InstanceGroupSummary information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceGroupSummary(AbstractModel):
    """
    InstanceGroupSummary
    """

    def __init__(self, id=None, name=None, scope=None, resource_type=None, instance_count=None):
        """
        Initialize InstanceGroupSummary instance.

        :param id: 实例组ID
        :type id: str (optional)

        :param name: 实例组名称
        :type name: str (optional)

        :param scope: 云产品类型
        :type scope: str (optional)

        :param resource_type: 资源类型
        :type resource_type: str (optional)

        :param instance_count: 实例个数
        :type instance_count: int (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.scope = scope
        self.resource_type = resource_type
        self.instance_count = instance_count

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceGroupSummary

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')
        return self
