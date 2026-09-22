"""
Request entity for GePriceForResizeInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GePriceForResizeInstanceRequest(AbstractModel):
    """
    Request entity for GePriceForResizeInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        client_token,
        instance_id,
        node_type=None,
        shard_num=None,
        replication_num=None,
        disk_flavor=None,
        charge_type=None,
        period=None,
        change_type=None,
    ):
        """
        Initialize GePriceForResizeInstanceRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (required)

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param node_type: node_type parameter
        :type node_type: str (optional)

        :param shard_num: 分片个数，默认为1
        :type shard_num: int (optional)

        :param replication_num: 副本数量，默认为1。<br/>Redis内存型和Redis容量型此字段有效。
        :type replication_num: int (optional)

        :param disk_flavor: 单分片容量，单位GB。<br/>  Redis容量型此字段有效。
        :type disk_flavor: int (optional)

        :param charge_type: 计费类型。预付费prepay/后付费postpay,计费类型需与原实例相同
        :type charge_type: str (optional)

        :param period: 计费周期。计费类型为预付费必填,单位为月
        :type period: int (optional)

        :param change_type: 变更类型。<br/>modifyType：Redis标准版变配为集群版时的询价标识，此时为必填字段。
        :type change_type: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.instance_id = instance_id
        self.node_type = node_type
        self.shard_num = shard_num
        self.replication_num = replication_num
        self.disk_flavor = disk_flavor
        self.charge_type = charge_type
        self.period = period
        self.change_type = change_type

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
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.replication_num is not None:
            result['replicationNum'] = self.replication_num
        if self.disk_flavor is not None:
            result['diskFlavor'] = self.disk_flavor
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.period is not None:
            result['period'] = self.period
        if self.change_type is not None:
            result['changeType'] = self.change_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GePriceForResizeInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('replicationNum') is not None:
            self.replication_num = m.get('replicationNum')
        if m.get('diskFlavor') is not None:
            self.disk_flavor = m.get('diskFlavor')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('changeType') is not None:
            self.change_type = m.get('changeType')
        return self
