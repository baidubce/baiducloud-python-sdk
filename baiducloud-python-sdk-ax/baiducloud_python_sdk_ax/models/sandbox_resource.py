"""
SandboxResource information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SandboxResource(AbstractModel):
    """
    SandboxResource
    """

    def __init__(self, cpu=None, memory=None):
        """
        Initialize SandboxResource instance.

        :param cpu: CPU 资源量。
        :type cpu: str (optional)

        :param memory: 内存资源量。
        :type memory: str (optional)
        """
        super().__init__()
        self.cpu = cpu
        self.memory = memory

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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SandboxResource

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        return self
