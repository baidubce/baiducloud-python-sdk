"""
Request entity for GetPriceForCreateInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetPriceForCreateInstanceRequest(AbstractModel):
    """
    Request entity for GetPriceForCreateInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        engine=None,
        cluster_type=None,
        node_type=None,
        cache_instance_type=None,
        shard_num=None,
        replication_num=None,
        instance_num=None,
        disk_type=None,
        disk_flavor=None,
        charge_type=None,
        period=None,
        time_unit=None,
    ):
        """
        Initialize GetPriceForCreateInstanceRequest request entity.

        :param engine: 引擎类型。默认值为2。取值范围如下： <br>  Redis内存型: 2 <br>  Reids 容量型: 3
        :type engine: int (optional)

        :param cluster_type: cluster_type parameter
        :type cluster_type: str (optional)

        :param node_type: node_type parameter
        :type node_type: str (optional)

        :param cache_instance_type: Memcache的节点规格。单位GB。<br>取值范围：1、2、4、8、16、32、64。
        :type cache_instance_type: int (optional)

        :param shard_num: 分片个数，默认为1
        :type shard_num: int (optional)

        :param replication_num: replication_num parameter
        :type replication_num: int (optional)

        :param instance_num: 购买数量，默认为1
        :type instance_num: int (optional)

        :param disk_type: 存储磁盘类型，购买Reids 容量型(原 PegaDB)时有效 。默认值为cloud_hp1。
        :type disk_type: str (optional)

        :param disk_flavor: 单分片存储磁盘容量大小，购买Reids 容量型(原 PegaDB)时为必填项。
        :type disk_flavor: int (optional)

        :param charge_type: charge_type parameter
        :type charge_type: str (optional)

        :param period: 计费周期。计费类型为包年包月时必填，单位为月，默认为1
        :type period: int (optional)

        :param time_unit: time_unit parameter
        :type time_unit: str (optional)
        """
        super().__init__()
        self.engine = engine
        self.cluster_type = cluster_type
        self.node_type = node_type
        self.cache_instance_type = cache_instance_type
        self.shard_num = shard_num
        self.replication_num = replication_num
        self.instance_num = instance_num
        self.disk_type = disk_type
        self.disk_flavor = disk_flavor
        self.charge_type = charge_type
        self.period = period
        self.time_unit = time_unit

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
        if self.engine is not None:
            result['engine'] = self.engine
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.cache_instance_type is not None:
            result['cacheInstanceType'] = self.cache_instance_type
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.replication_num is not None:
            result['replicationNum'] = self.replication_num
        if self.instance_num is not None:
            result['instanceNum'] = self.instance_num
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.disk_flavor is not None:
            result['diskFlavor'] = self.disk_flavor
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.period is not None:
            result['period'] = self.period
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPriceForCreateInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('cacheInstanceType') is not None:
            self.cache_instance_type = m.get('cacheInstanceType')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('replicationNum') is not None:
            self.replication_num = m.get('replicationNum')
        if m.get('instanceNum') is not None:
            self.instance_num = m.get('instanceNum')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('diskFlavor') is not None:
            self.disk_flavor = m.get('diskFlavor')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        return self
