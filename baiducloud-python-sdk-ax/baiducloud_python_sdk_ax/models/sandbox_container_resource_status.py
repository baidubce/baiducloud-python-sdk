"""
SandboxContainerResourceStatus information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ax.models.sandbox_resource import SandboxResource

from baiducloud_python_sdk_ax.models.sandbox_resource import SandboxResource

from baiducloud_python_sdk_ax.models.sandbox_resource import SandboxResource


class SandboxContainerResourceStatus(AbstractModel):
    """
    SandboxContainerResourceStatus
    """

    def __init__(self, name=None, desired=None, allocated=None, current=None):
        """
        Initialize SandboxContainerResourceStatus instance.

        :param name: 容器名称。
        :type name: str (optional)

        :param desired: desired attribute
        :type desired: SandboxResource (optional)

        :param allocated: allocated attribute
        :type allocated: SandboxResource (optional)

        :param current: current attribute
        :type current: SandboxResource (optional)
        """
        super().__init__()
        self.name = name
        self.desired = desired
        self.allocated = allocated
        self.current = current

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
        if self.name is not None:
            result['name'] = self.name
        if self.desired is not None:
            result['desired'] = self.desired.to_dict()
        if self.allocated is not None:
            result['allocated'] = self.allocated.to_dict()
        if self.current is not None:
            result['current'] = self.current.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SandboxContainerResourceStatus

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desired') is not None:
            self.desired = SandboxResource().from_dict(m.get('desired'))
        if m.get('allocated') is not None:
            self.allocated = SandboxResource().from_dict(m.get('allocated'))
        if m.get('current') is not None:
            self.current = SandboxResource().from_dict(m.get('current'))
        return self
