"""
Topology information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.read_replica_id_mapping import ReadReplicaIdMapping

from baiducloud_python_sdk_rds.models.master_id_mapping import MasterIdMapping

from baiducloud_python_sdk_rds.models.read_replica_id_mapping import ReadReplicaIdMapping

from baiducloud_python_sdk_rds.models.read_replica_id_mapping import ReadReplicaIdMapping


class Topology(AbstractModel):
    """
    Topology
    """

    def __init__(
        self,
        master=None,
        read_replica=None,
        rdsproxy=None,
        read_replica_id_mapping=None,
        master_id_mapping=None,
        rdsproxy_id_mapping=None,
        rdsproxy_id_mappings=None,
    ):
        """
        Initialize Topology instance.

        :param master: 主实例列表。
        :type master: List[str] (optional)

        :param read_replica: 只读实列列表。
        :type read_replica: List[str] (optional)

        :param rdsproxy: 代理实例列表。
        :type rdsproxy: List[str] (optional)

        :param read_replica_id_mapping: 只读实例映射。
        :type read_replica_id_mapping: List[ReadReplicaIdMapping] (optional)

        :param master_id_mapping: master_id_mapping attribute
        :type master_id_mapping: MasterIdMapping (optional)

        :param rdsproxy_id_mapping: rdsproxy_id_mapping attribute
        :type rdsproxy_id_mapping: ReadReplicaIdMapping (optional)

        :param rdsproxy_id_mappings: 代理实例映射列表。
        :type rdsproxy_id_mappings: List[ReadReplicaIdMapping] (optional)
        """
        super().__init__()
        self.master = master
        self.read_replica = read_replica
        self.rdsproxy = rdsproxy
        self.read_replica_id_mapping = read_replica_id_mapping
        self.master_id_mapping = master_id_mapping
        self.rdsproxy_id_mapping = rdsproxy_id_mapping
        self.rdsproxy_id_mappings = rdsproxy_id_mappings

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
        if self.master is not None:
            result['master'] = self.master
        if self.read_replica is not None:
            result['readReplica'] = self.read_replica
        if self.rdsproxy is not None:
            result['rdsproxy'] = self.rdsproxy
        if self.read_replica_id_mapping is not None:
            result['readReplicaIdMapping'] = [i.to_dict() for i in self.read_replica_id_mapping]
        if self.master_id_mapping is not None:
            result['masterIdMapping'] = self.master_id_mapping.to_dict()
        if self.rdsproxy_id_mapping is not None:
            result['rdsproxyIdMapping'] = self.rdsproxy_id_mapping.to_dict()
        if self.rdsproxy_id_mappings is not None:
            result['rdsproxyIdMappings'] = [i.to_dict() for i in self.rdsproxy_id_mappings]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Topology

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('master') is not None:
            self.master = m.get('master')
        if m.get('readReplica') is not None:
            self.read_replica = m.get('readReplica')
        if m.get('rdsproxy') is not None:
            self.rdsproxy = m.get('rdsproxy')
        if m.get('readReplicaIdMapping') is not None:
            self.read_replica_id_mapping = [ReadReplicaIdMapping().from_dict(i) for i in m.get('readReplicaIdMapping')]
        if m.get('masterIdMapping') is not None:
            self.master_id_mapping = MasterIdMapping().from_dict(m.get('masterIdMapping'))
        if m.get('rdsproxyIdMapping') is not None:
            self.rdsproxy_id_mapping = ReadReplicaIdMapping().from_dict(m.get('rdsproxyIdMapping'))
        if m.get('rdsproxyIdMappings') is not None:
            self.rdsproxy_id_mappings = [ReadReplicaIdMapping().from_dict(i) for i in m.get('rdsproxyIdMappings')]
        return self
