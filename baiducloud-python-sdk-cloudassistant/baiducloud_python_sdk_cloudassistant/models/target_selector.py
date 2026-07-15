"""
TargetSelector information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cloudassistant.models.tag import Tag

from baiducloud_python_sdk_cloudassistant.models.target_import import TargetImport


class TargetSelector(AbstractModel):
    """
    TargetSelector
    """

    def __init__(self, instance_type=None, tags=None, import_instances=None):
        """
        Initialize TargetSelector instance.

        :param instance_type: 实例类型。枚举值：BCC，BBC
        :type instance_type: str (optional)

        :param tags: 实例标签列表
        :type tags: List[Tag] (optional)

        :param import_instances: import_instances attribute
        :type import_instances: TargetImport (optional)
        """
        super().__init__()
        self.instance_type = instance_type
        self.tags = tags
        self.import_instances = import_instances

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
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.import_instances is not None:
            result['importInstances'] = self.import_instances.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TargetSelector

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('importInstances') is not None:
            self.import_instances = TargetImport().from_dict(m.get('importInstances'))
        return self
