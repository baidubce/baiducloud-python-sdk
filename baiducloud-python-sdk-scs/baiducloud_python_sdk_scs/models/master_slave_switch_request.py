"""
Request entity for MasterSlaveSwitchRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.switch_master_slave_shard import SwitchMasterSlaveShard


class MasterSlaveSwitchRequest(AbstractModel):
    """
    Request entity for MasterSlaveSwitchRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, shards):
        """
        Initialize MasterSlaveSwitchRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param shards: 切换的分片列表。
        :type shards: List[SwitchMasterSlaveShard] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.shards = shards

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
        if self.shards is not None:
            result['shards'] = [i.to_dict() for i in self.shards]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MasterSlaveSwitchRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('shards') is not None:
            self.shards = [SwitchMasterSlaveShard().from_dict(i) for i in m.get('shards')]
        return self
