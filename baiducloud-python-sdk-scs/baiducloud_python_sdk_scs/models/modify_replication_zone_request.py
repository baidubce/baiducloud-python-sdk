"""
Request entity for ModifyReplicationZoneRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.replication_item import ReplicationItem


class ModifyReplicationZoneRequest(AbstractModel):
    """
    Request entity for ModifyReplicationZoneRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, is_defer, replication_info):
        """
        Initialize ModifyReplicationZoneRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param is_defer: 是否维护时间内执行。 <li>true：维护时间内执行 <li>false：立即执行
        :type is_defer: bool (required)

        :param replication_info: 副本信息。需全量的副本信息，可以修改可用区和子网。
        :type replication_info: List[ReplicationItem] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.is_defer = is_defer
        self.replication_info = replication_info

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
        if self.is_defer is not None:
            result['isDefer'] = self.is_defer
        if self.replication_info is not None:
            result['replicationInfo'] = [i.to_dict() for i in self.replication_info]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyReplicationZoneRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDefer') is not None:
            self.is_defer = m.get('isDefer')
        if m.get('replicationInfo') is not None:
            self.replication_info = [ReplicationItem().from_dict(i) for i in m.get('replicationInfo')]
        return self
