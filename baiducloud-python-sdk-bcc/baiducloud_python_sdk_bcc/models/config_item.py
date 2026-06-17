"""
ConfigItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ConfigItem(AbstractModel):
    """
    ConfigItem
    """

    def __init__(self, cpu=None, memory=None, type=None, spec_id=None, spec=None, zone_name=None):
        """
        Initialize ConfigItem instance.

        :param cpu: cpu个数
        :type cpu: int (optional)

        :param memory: 内存大小
        :type memory: int (optional)

        :param type: 实例类型，具体可选类型参见InstanceType
        :type type: str (optional)

        :param spec_id: 实例规格类型
        :type spec_id: str (optional)

        :param spec: 实例规格
        :type spec: str (optional)

        :param zone_name: 可用区名称
        :type zone_name: str (optional)
        """
        super().__init__()
        self.cpu = cpu
        self.memory = memory
        self.type = type
        self.spec_id = spec_id
        self.spec = spec
        self.zone_name = zone_name

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
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.memory is not None:
            result['memory'] = self.memory
        if self.type is not None:
            result['type'] = self.type
        if self.spec_id is not None:
            result['specId'] = self.spec_id
        if self.spec is not None:
            result['spec'] = self.spec
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ConfigItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('specId') is not None:
            self.spec_id = m.get('specId')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self
