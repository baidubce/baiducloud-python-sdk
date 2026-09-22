"""
InstanceParam information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vdb.models.az_info import AzInfo

from baiducloud_python_sdk_vdb.models.milvus_component import MilvusComponent


class InstanceParam(AbstractModel):
    """
    InstanceParam
    """

    def __init__(
        self,
        availability_zone=None,
        az_infos=None,
        clone_data_app_backup_id=None,
        clone_data_app_id=None,
        components=None,
        data_node_num=None,
        disk_flavor=None,
        disk_type=None,
        enable_embedding=None,
        enable_encryption=None,
        engine_version=None,
        vdb_from=None,
        instance_name=None,
        instance_num=None,
        instance_type=None,
        master_node_spec=None,
        master_num=None,
        node_spec=None,
        node_type=None,
        order_id=None,
        password=None,
        port=None,
        proxy_node_spec=None,
        proxy_num=None,
        req_source=None,
        subnet_id=None,
        switch_entrance=None,
        vpc_id=None,
    ):
        """
        Initialize InstanceParam instance.

        :param availability_zone: 可用区
        :type availability_zone: str (optional)

        :param az_infos: 可用区及子网信息
        :type az_infos: List[AzInfo] (optional)

        :param clone_data_app_backup_id: 克隆源备份ID
        :type clone_data_app_backup_id: str (optional)

        :param clone_data_app_id: 克隆源实例ID
        :type clone_data_app_id: str (optional)

        :param components: 组件配置
        :type components: List[MilvusComponent] (optional)

        :param data_node_num: 数据节点数量
        :type data_node_num: int (optional)

        :param disk_flavor: 磁盘容量（GB）
        :type disk_flavor: int (optional)

        :param disk_type: 磁盘类型
        :type disk_type: str (optional)

        :param enable_embedding: 是否开启 Embedding
        :type enable_embedding: bool (optional)

        :param enable_encryption: 是否开启数据加密
        :type enable_encryption: bool (optional)

        :param engine_version: 引擎版本
        :type engine_version: str (optional)

        :param vdb_from: 请求来源（console/api）
        :type vdb_from: str (optional)

        :param instance_name: 实例名称
        :type instance_name: str (optional)

        :param instance_num: 实例数量
        :type instance_num: int (optional)

        :param instance_type: 实例类型（cluster：集群，standalone：单机）
        :type instance_type: str (optional)

        :param master_node_spec: 主节点规格
        :type master_node_spec: str (optional)

        :param master_num: 主节点数量
        :type master_num: int (optional)

        :param node_spec: 节点规格
        :type node_spec: str (optional)

        :param node_type: 节点类型
        :type node_type: str (optional)

        :param order_id: 订单ID
        :type order_id: str (optional)

        :param password: 实例密码
        :type password: str (optional)

        :param port: 端口
        :type port: int (optional)

        :param proxy_node_spec: 代理节点规格
        :type proxy_node_spec: str (optional)

        :param proxy_num: 代理节点数量
        :type proxy_num: int (optional)

        :param req_source: 请求来源
        :type req_source: str (optional)

        :param subnet_id: 子网 ID
        :type subnet_id: str (optional)

        :param switch_entrance: 是否交换原实例和克隆实例入口
        :type switch_entrance: str (optional)

        :param vpc_id: VPC ID
        :type vpc_id: str (optional)
        """
        super().__init__()
        self.availability_zone = availability_zone
        self.az_infos = az_infos
        self.clone_data_app_backup_id = clone_data_app_backup_id
        self.clone_data_app_id = clone_data_app_id
        self.components = components
        self.data_node_num = data_node_num
        self.disk_flavor = disk_flavor
        self.disk_type = disk_type
        self.enable_embedding = enable_embedding
        self.enable_encryption = enable_encryption
        self.engine_version = engine_version
        self.vdb_from = vdb_from
        self.instance_name = instance_name
        self.instance_num = instance_num
        self.instance_type = instance_type
        self.master_node_spec = master_node_spec
        self.master_num = master_num
        self.node_spec = node_spec
        self.node_type = node_type
        self.order_id = order_id
        self.password = password
        self.port = port
        self.proxy_node_spec = proxy_node_spec
        self.proxy_num = proxy_num
        self.req_source = req_source
        self.subnet_id = subnet_id
        self.switch_entrance = switch_entrance
        self.vpc_id = vpc_id

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
        if self.availability_zone is not None:
            result['availabilityZone'] = self.availability_zone
        if self.az_infos is not None:
            result['azInfos'] = [i.to_dict() for i in self.az_infos]
        if self.clone_data_app_backup_id is not None:
            result['cloneDataAppBackupId'] = self.clone_data_app_backup_id
        if self.clone_data_app_id is not None:
            result['cloneDataAppId'] = self.clone_data_app_id
        if self.components is not None:
            result['components'] = [i.to_dict() for i in self.components]
        if self.data_node_num is not None:
            result['dataNodeNum'] = self.data_node_num
        if self.disk_flavor is not None:
            result['diskFlavor'] = self.disk_flavor
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.enable_embedding is not None:
            result['enableEmbedding'] = self.enable_embedding
        if self.enable_encryption is not None:
            result['enableEncryption'] = self.enable_encryption
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.vdb_from is not None:
            result['from'] = self.vdb_from
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_num is not None:
            result['instanceNum'] = self.instance_num
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.master_node_spec is not None:
            result['masterNodeSpec'] = self.master_node_spec
        if self.master_num is not None:
            result['masterNum'] = self.master_num
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.password is not None:
            result['password'] = self.password
        if self.port is not None:
            result['port'] = self.port
        if self.proxy_node_spec is not None:
            result['proxyNodeSpec'] = self.proxy_node_spec
        if self.proxy_num is not None:
            result['proxyNum'] = self.proxy_num
        if self.req_source is not None:
            result['reqSource'] = self.req_source
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.switch_entrance is not None:
            result['switchEntrance'] = self.switch_entrance
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceParam

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('availabilityZone') is not None:
            self.availability_zone = m.get('availabilityZone')
        if m.get('azInfos') is not None:
            self.az_infos = [AzInfo().from_dict(i) for i in m.get('azInfos')]
        if m.get('cloneDataAppBackupId') is not None:
            self.clone_data_app_backup_id = m.get('cloneDataAppBackupId')
        if m.get('cloneDataAppId') is not None:
            self.clone_data_app_id = m.get('cloneDataAppId')
        if m.get('components') is not None:
            self.components = [MilvusComponent().from_dict(i) for i in m.get('components')]
        if m.get('dataNodeNum') is not None:
            self.data_node_num = m.get('dataNodeNum')
        if m.get('diskFlavor') is not None:
            self.disk_flavor = m.get('diskFlavor')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('enableEmbedding') is not None:
            self.enable_embedding = m.get('enableEmbedding')
        if m.get('enableEncryption') is not None:
            self.enable_encryption = m.get('enableEncryption')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('from') is not None:
            self.vdb_from = m.get('from')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceNum') is not None:
            self.instance_num = m.get('instanceNum')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('masterNodeSpec') is not None:
            self.master_node_spec = m.get('masterNodeSpec')
        if m.get('masterNum') is not None:
            self.master_num = m.get('masterNum')
        if m.get('nodeSpec') is not None:
            self.node_spec = m.get('nodeSpec')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('proxyNodeSpec') is not None:
            self.proxy_node_spec = m.get('proxyNodeSpec')
        if m.get('proxyNum') is not None:
            self.proxy_num = m.get('proxyNum')
        if m.get('reqSource') is not None:
            self.req_source = m.get('reqSource')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('switchEntrance') is not None:
            self.switch_entrance = m.get('switchEntrance')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self
