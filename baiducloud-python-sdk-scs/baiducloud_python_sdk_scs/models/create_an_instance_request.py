"""
Request entity for CreateAnInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.billing import Billing
from baiducloud_python_sdk_scs.models.replication_map import ReplicationMap
from baiducloud_python_sdk_scs.models.tag import Tag


class CreateAnInstanceRequest(AbstractModel):
    """
    Request entity for CreateAnInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        billing,
        instance_name,
        node_type,
        port,
        engine_version,
        purchase_count,
        proxy_num,
        cluster_type,
        client_token=None,
        engine=None,
        store_type=None,
        enable_read_only=None,
        shard_num=None,
        disk_flavor=None,
        disk_type=None,
        vpc_id=None,
        replication_info=None,
        auto_renew_time_unit=None,
        auto_renew_time=None,
        bgw_group_id=None,
        client_auth=None,
        tags=None,
        conf_tpl=None,
        resource_group_id=None,
        auto_backup_config=None,
        deploy_id_list=None,
    ):
        """
        Initialize CreateAnInstanceRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param instance_name: instance_name parameter
        :type instance_name: str (required)

        :param node_type: node_type parameter
        :type node_type: str (required)

        :param port: 端口号可选1025-7041、7043-22221、22223-65534，创建后支持更改
        :type port: int (required)

        :param engine: 引擎类型，默认值为2。 redis内存型:2；Redis容量型:3
        :type engine: int (optional)

        :param engine_version: engine_version parameter
        :type engine_version: str (required)

        :param store_type: 存储类型，默认为0。高性能内存:0、容量型存储：3
        :type store_type: int (optional)

        :param enable_read_only: 副本只读，默认值为2。 打开：1、关闭：2
        :type enable_read_only: int (optional)

        :param purchase_count: 购买个数，最大不超过10，默认1
        :type purchase_count: int (required)

        :param shard_num: 分片个数，默认值为1
        :type shard_num: int (optional)

        :param proxy_num: 代理节点数，目前支持的取值：主从版：0<br>集群版：代理节点数=分片个数<br>集群版分片数为1时，代理节点数量为2
        :type proxy_num: int (required)

        :param cluster_type: 集群类型：<br/>企业版集群：\"cluster\"<br/>主从版：\"master\\_slave\"<br>
        :type cluster_type: str (required)

        :param disk_flavor: 单分片存储空间,引擎类型为3，即为Redis容量型(原PegaDB)时传入
        :type disk_flavor: int (optional)

        :param disk_type: 存储类型:目前支持 \"cds\"
        :type disk_type: str (optional)

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (optional)

        :param replication_info: replication_info parameter
        :type replication_info: List[ReplicationMap] (optional)

        :param auto_renew_time_unit: 按月付费或者按年付费 月是\"month\"，年是\"year\"
        :type auto_renew_time_unit: str (optional)

        :param auto_renew_time: 自动续费的时间 按月是1-9 按年是 1-3
        :type auto_renew_time: int (optional)

        :param bgw_group_id: blb专属集群Id。该参数不传，默认为共享集群。
        :type bgw_group_id: str (optional)

        :param client_auth: client_auth parameter
        :type client_auth: str (optional)

        :param tags: 标签键值对列表
        :type tags: List[Tag] (optional)

        :param conf_tpl: 指定的参数模版ID
        :type conf_tpl: str (optional)

        :param resource_group_id: resource_group_id parameter
        :type resource_group_id: str (optional)

        :param auto_backup_config: auto_backup_config parameter
        :type auto_backup_config: str (optional)

        :param deploy_id_list: deploy_id_list parameter
        :type deploy_id_list: List[str] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.billing = billing
        self.instance_name = instance_name
        self.node_type = node_type
        self.port = port
        self.engine = engine
        self.engine_version = engine_version
        self.store_type = store_type
        self.enable_read_only = enable_read_only
        self.purchase_count = purchase_count
        self.shard_num = shard_num
        self.proxy_num = proxy_num
        self.cluster_type = cluster_type
        self.disk_flavor = disk_flavor
        self.disk_type = disk_type
        self.vpc_id = vpc_id
        self.replication_info = replication_info
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time
        self.bgw_group_id = bgw_group_id
        self.client_auth = client_auth
        self.tags = tags
        self.conf_tpl = conf_tpl
        self.resource_group_id = resource_group_id
        self.auto_backup_config = auto_backup_config
        self.deploy_id_list = deploy_id_list

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
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.port is not None:
            result['port'] = self.port
        if self.engine is not None:
            result['engine'] = self.engine
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.store_type is not None:
            result['storeType'] = self.store_type
        if self.enable_read_only is not None:
            result['enableReadOnly'] = self.enable_read_only
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.proxy_num is not None:
            result['proxyNum'] = self.proxy_num
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.disk_flavor is not None:
            result['diskFlavor'] = self.disk_flavor
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.replication_info is not None:
            result['replicationInfo'] = [i.to_dict() for i in self.replication_info]
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.bgw_group_id is not None:
            result['bgwGroupId'] = self.bgw_group_id
        if self.client_auth is not None:
            result['clientAuth'] = self.client_auth
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.conf_tpl is not None:
            result['confTpl'] = self.conf_tpl
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.auto_backup_config is not None:
            result['autoBackupConfig'] = self.auto_backup_config
        if self.deploy_id_list is not None:
            result['deployIdList'] = self.deploy_id_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAnInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        if m.get('enableReadOnly') is not None:
            self.enable_read_only = m.get('enableReadOnly')
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('proxyNum') is not None:
            self.proxy_num = m.get('proxyNum')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('diskFlavor') is not None:
            self.disk_flavor = m.get('diskFlavor')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('replicationInfo') is not None:
            self.replication_info = [ReplicationMap().from_dict(i) for i in m.get('replicationInfo')]
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('bgwGroupId') is not None:
            self.bgw_group_id = m.get('bgwGroupId')
        if m.get('clientAuth') is not None:
            self.client_auth = m.get('clientAuth')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('confTpl') is not None:
            self.conf_tpl = m.get('confTpl')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('autoBackupConfig') is not None:
            self.auto_backup_config = m.get('autoBackupConfig')
        if m.get('deployIdList') is not None:
            self.deploy_id_list = m.get('deployIdList')
        return self
