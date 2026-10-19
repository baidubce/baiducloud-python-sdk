"""
Request entity for UpdateAutomaticStorageExpansionConfigurationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateAutomaticStorageExpansionConfigurationRequest(AbstractModel):
    """
    Request entity for UpdateAutomaticStorageExpansionConfigurationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, action, free_space_threshold=None, disk_max_limit=None):
        """
        Initialize UpdateAutomaticStorageExpansionConfigurationRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param action: action parameter
        :type action: str (required)

        :param free_space_threshold: 可用空间阈值, 单位%。当action为open时，为必传参数，仅允许实例在启用存储自动扩容时修改
        :type free_space_threshold: int (optional)

        :param disk_max_limit: disk_max_limit parameter
        :type disk_max_limit: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.action = action
        self.free_space_threshold = free_space_threshold
        self.disk_max_limit = disk_max_limit

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
        if self.free_space_threshold is not None:
            result['freeSpaceThreshold'] = self.free_space_threshold
        if self.disk_max_limit is not None:
            result['diskMaxLimit'] = self.disk_max_limit
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAutomaticStorageExpansionConfigurationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('freeSpaceThreshold') is not None:
            self.free_space_threshold = m.get('freeSpaceThreshold')
        if m.get('diskMaxLimit') is not None:
            self.disk_max_limit = m.get('diskMaxLimit')
        return self
