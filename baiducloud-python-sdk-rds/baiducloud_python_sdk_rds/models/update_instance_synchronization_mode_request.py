"""
Request entity for UpdateInstanceSynchronizationModeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateInstanceSynchronizationModeRequest(AbstractModel):
    """
    Request entity for UpdateInstanceSynchronizationModeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, sync_mode):
        """
        Initialize UpdateInstanceSynchronizationModeRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param sync_mode: 同步模式（异步复制：Async，半同步复制：Semi\\_sync）
        :type sync_mode: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.sync_mode = sync_mode

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
        if self.sync_mode is not None:
            result['syncMode'] = self.sync_mode
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateInstanceSynchronizationModeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('syncMode') is not None:
            self.sync_mode = m.get('syncMode')
        return self
