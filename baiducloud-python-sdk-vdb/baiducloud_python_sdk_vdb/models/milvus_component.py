"""
MilvusComponent information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MilvusComponent(AbstractModel):
    """
    MilvusComponent
    """

    def __init__(self, disk_size_type=None, replicas=None, spec=None, type=None):
        """
        Initialize MilvusComponent instance.

        :param disk_size_type:
        :type disk_size_type: str (optional)

        :param replicas:
        :type replicas: int (optional)

        :param spec:
        :type spec: str (optional)

        :param type:
        :type type: str (optional)
        """
        super().__init__()
        self.disk_size_type = disk_size_type
        self.replicas = replicas
        self.spec = spec
        self.type = type

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
        if self.disk_size_type is not None:
            result['diskSizeType'] = self.disk_size_type
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.spec is not None:
            result['spec'] = self.spec
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MilvusComponent

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('diskSizeType') is not None:
            self.disk_size_type = m.get('diskSizeType')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
