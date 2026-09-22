"""
ListItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_scs.models.cluster_item import ClusterItem


class ListItem(AbstractModel):
    """
    ListItem
    """

    def __init__(
        self,
        sync_group_show_id=None,
        sync_group_name=None,
        status=None,
        cluster_num=None,
        node_type=None,
        net_conn=None,
        confilct_resolution=None,
        sync_group_create_time=None,
        same_spec=None,
        same_shard_num=None,
        cluster=None,
        user_name=None,
        update_status=None,
        extra=None,
        user_type=None,
    ):
        """
        Initialize ListItem instance.

        :param sync_group_show_id: 实例组ID。
        :type sync_group_show_id: str (optional)

        :param sync_group_name: 实例组名称。
        :type sync_group_name: str (optional)

        :param status: 实例组状态。
        :type status: str (optional)

        :param cluster_num: 实例组中成员集群的数量。
        :type cluster_num: int (optional)

        :param node_type: 实例组中成员集群的规格。
        :type node_type: str (optional)

        :param net_conn: 网络联通状态。忽略该字段。
        :type net_conn: str (optional)

        :param confilct_resolution: 冲突解决办法。忽略该字段。
        :type confilct_resolution: str (optional)

        :param sync_group_create_time: 多活实例组创建时间。
        :type sync_group_create_time: str (optional)

        :param same_spec: 实例组中所有成员的规格是否一致。
        :type same_spec: bool (optional)

        :param same_shard_num: 实例组中所有成员的分片数量是否一致。
        :type same_shard_num: bool (optional)

        :param cluster: 多活组列表数据。
        :type cluster: List[ClusterItem] (optional)

        :param user_name: 账号名称。
        :type user_name: str (optional)

        :param update_status: 账号状态。0：正常可用；1：创建中；2：修改中；4：删除中；
        :type update_status: int (optional)

        :param extra: 备注信息。
        :type extra: str (optional)

        :param user_type: 账号权限。1：读写；2：只读；
        :type user_type: int (optional)
        """
        super().__init__()
        self.sync_group_show_id = sync_group_show_id
        self.sync_group_name = sync_group_name
        self.status = status
        self.cluster_num = cluster_num
        self.node_type = node_type
        self.net_conn = net_conn
        self.confilct_resolution = confilct_resolution
        self.sync_group_create_time = sync_group_create_time
        self.same_spec = same_spec
        self.same_shard_num = same_shard_num
        self.cluster = cluster
        self.user_name = user_name
        self.update_status = update_status
        self.extra = extra
        self.user_type = user_type

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
        if self.sync_group_show_id is not None:
            result['syncGroupShowId'] = self.sync_group_show_id
        if self.sync_group_name is not None:
            result['syncGroupName'] = self.sync_group_name
        if self.status is not None:
            result['status'] = self.status
        if self.cluster_num is not None:
            result['clusterNum'] = self.cluster_num
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.net_conn is not None:
            result['netConn'] = self.net_conn
        if self.confilct_resolution is not None:
            result['confilctResolution'] = self.confilct_resolution
        if self.sync_group_create_time is not None:
            result['syncGroupCreateTime'] = self.sync_group_create_time
        if self.same_spec is not None:
            result['sameSpec'] = self.same_spec
        if self.same_shard_num is not None:
            result['sameShardNum'] = self.same_shard_num
        if self.cluster is not None:
            result['cluster'] = [i.to_dict() for i in self.cluster]
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.update_status is not None:
            result['updateStatus'] = self.update_status
        if self.extra is not None:
            result['extra'] = self.extra
        if self.user_type is not None:
            result['userType'] = self.user_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('syncGroupShowId') is not None:
            self.sync_group_show_id = m.get('syncGroupShowId')
        if m.get('syncGroupName') is not None:
            self.sync_group_name = m.get('syncGroupName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('clusterNum') is not None:
            self.cluster_num = m.get('clusterNum')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('netConn') is not None:
            self.net_conn = m.get('netConn')
        if m.get('confilctResolution') is not None:
            self.confilct_resolution = m.get('confilctResolution')
        if m.get('syncGroupCreateTime') is not None:
            self.sync_group_create_time = m.get('syncGroupCreateTime')
        if m.get('sameSpec') is not None:
            self.same_spec = m.get('sameSpec')
        if m.get('sameShardNum') is not None:
            self.same_shard_num = m.get('sameShardNum')
        if m.get('cluster') is not None:
            self.cluster = [ClusterItem().from_dict(i) for i in m.get('cluster')]
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('updateStatus') is not None:
            self.update_status = m.get('updateStatus')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        return self
