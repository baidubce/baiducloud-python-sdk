"""
Request entity for InstanceVersionUpgradeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceVersionUpgradeRequest(AbstractModel):
    """
    Request entity for InstanceVersionUpgradeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, kernel_version=None, is_defer=None):
        """
        Initialize InstanceVersionUpgradeRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param kernel_version: kernel_version parameter
        :type kernel_version: str (optional)

        :param is_defer: 执行时间。<li> false：立即执行<li>true：维护时间内执行
        :type is_defer: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.kernel_version = kernel_version
        self.is_defer = is_defer

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
        if self.kernel_version is not None:
            result['kernelVersion'] = self.kernel_version
        if self.is_defer is not None:
            result['isDefer'] = self.is_defer
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceVersionUpgradeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('kernelVersion') is not None:
            self.kernel_version = m.get('kernelVersion')
        if m.get('isDefer') is not None:
            self.is_defer = m.get('isDefer')
        return self
