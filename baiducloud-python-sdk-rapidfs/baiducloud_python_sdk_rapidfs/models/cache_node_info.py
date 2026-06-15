"""
CacheNodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rapidfs.models.disk_info import DiskInfo

from baiducloud_python_sdk_rapidfs.models.bcc_cache_node_info import BCCCacheNodeInfo

from baiducloud_python_sdk_rapidfs.models.idc_cache_node_info import IDCCacheNodeInfo

from baiducloud_python_sdk_rapidfs.models.cce_cache_node_info import CCECacheNodeInfo

from baiducloud_python_sdk_rapidfs.models.k8_s_cache_node_info import K8SCacheNodeInfo

from baiducloud_python_sdk_rapidfs.models.aihc_cache_node_info import AIHCCacheNodeInfo


class CacheNodeInfo(AbstractModel):
    """
    CacheNodeInfo
    """

    def __init__(
        self,
        cache_node_id=None,
        instance_id=None,
        type=None,
        ip=None,
        status=None,
        connection_status=None,
        description=None,
        create_time=None,
        report_time=None,
        capacity_mi_b=None,
        capacity_used_mi_b=None,
        capacity_used_percentage=None,
        config=None,
        disk_infos=None,
        deploy_path=None,
        bcc_info=None,
        idc_info=None,
        cce_info=None,
        k8s_info=None,
        aihc_info=None,
    ):
        """
        Initialize CacheNodeInfo instance.

        :param cache_node_id: 缓存节点唯一 ID
        :type cache_node_id: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (optional)

        :param type: type attribute
        :type type: str (optional)

        :param ip: 缓存节点 IP 地址
        :type ip: str (optional)

        :param status: 节点状态，见 CacheNodeStatus
        :type status: str (optional)

        :param connection_status: 连接状态，见 CacheNodeConnectionStatus
        :type connection_status: str (optional)

        :param description: 描述信息
        :type description: str (optional)

        :param create_time: 创建时间，例如 2026-06-01T23:00:10Z
        :type create_time: str (optional)

        :param report_time: 缓存节点最近一次心跳上报时间，例如 2026-06-01T23:00:10Z
        :type report_time: str (optional)

        :param capacity_mi_b: 总容量，单位 MiB
        :type capacity_mi_b: int (optional)

        :param capacity_used_mi_b: 已使用容量，单位 MiB
        :type capacity_used_mi_b: int (optional)

        :param capacity_used_percentage: 容量使用百分比
        :type capacity_used_percentage: float (optional)

        :param config: config attribute
        :type config: str (optional)

        :param disk_infos: 磁盘信息列表
        :type disk_infos: List[DiskInfo] (optional)

        :param deploy_path: 缓存节点服务部署路径
        :type deploy_path: str (optional)

        :param bcc_info: bcc_info attribute
        :type bcc_info: BCCCacheNodeInfo (optional)

        :param idc_info: idc_info attribute
        :type idc_info: IDCCacheNodeInfo (optional)

        :param cce_info: cce_info attribute
        :type cce_info: CCECacheNodeInfo (optional)

        :param k8s_info: k8s_info attribute
        :type k8s_info: K8SCacheNodeInfo (optional)

        :param aihc_info: aihc_info attribute
        :type aihc_info: AIHCCacheNodeInfo (optional)
        """
        super().__init__()
        self.cache_node_id = cache_node_id
        self.instance_id = instance_id
        self.type = type
        self.ip = ip
        self.status = status
        self.connection_status = connection_status
        self.description = description
        self.create_time = create_time
        self.report_time = report_time
        self.capacity_mi_b = capacity_mi_b
        self.capacity_used_mi_b = capacity_used_mi_b
        self.capacity_used_percentage = capacity_used_percentage
        self.config = config
        self.disk_infos = disk_infos
        self.deploy_path = deploy_path
        self.bcc_info = bcc_info
        self.idc_info = idc_info
        self.cce_info = cce_info
        self.k8s_info = k8s_info
        self.aihc_info = aihc_info

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
        if self.cache_node_id is not None:
            result['cacheNodeId'] = self.cache_node_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.type is not None:
            result['type'] = self.type
        if self.ip is not None:
            result['ip'] = self.ip
        if self.status is not None:
            result['status'] = self.status
        if self.connection_status is not None:
            result['connectionStatus'] = self.connection_status
        if self.description is not None:
            result['description'] = self.description
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.report_time is not None:
            result['reportTime'] = self.report_time
        if self.capacity_mi_b is not None:
            result['capacityMiB'] = self.capacity_mi_b
        if self.capacity_used_mi_b is not None:
            result['capacityUsedMiB'] = self.capacity_used_mi_b
        if self.capacity_used_percentage is not None:
            result['capacityUsedPercentage'] = self.capacity_used_percentage
        if self.config is not None:
            result['config'] = self.config
        if self.disk_infos is not None:
            result['diskInfos'] = [i.to_dict() for i in self.disk_infos]
        if self.deploy_path is not None:
            result['deployPath'] = self.deploy_path
        if self.bcc_info is not None:
            result['bccInfo'] = self.bcc_info.to_dict()
        if self.idc_info is not None:
            result['idcInfo'] = self.idc_info.to_dict()
        if self.cce_info is not None:
            result['cceInfo'] = self.cce_info.to_dict()
        if self.k8s_info is not None:
            result['k8sInfo'] = self.k8s_info.to_dict()
        if self.aihc_info is not None:
            result['aihcInfo'] = self.aihc_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CacheNodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cacheNodeId') is not None:
            self.cache_node_id = m.get('cacheNodeId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('connectionStatus') is not None:
            self.connection_status = m.get('connectionStatus')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('reportTime') is not None:
            self.report_time = m.get('reportTime')
        if m.get('capacityMiB') is not None:
            self.capacity_mi_b = m.get('capacityMiB')
        if m.get('capacityUsedMiB') is not None:
            self.capacity_used_mi_b = m.get('capacityUsedMiB')
        if m.get('capacityUsedPercentage') is not None:
            self.capacity_used_percentage = m.get('capacityUsedPercentage')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('diskInfos') is not None:
            self.disk_infos = [DiskInfo().from_dict(i) for i in m.get('diskInfos')]
        if m.get('deployPath') is not None:
            self.deploy_path = m.get('deployPath')
        if m.get('bccInfo') is not None:
            self.bcc_info = BCCCacheNodeInfo().from_dict(m.get('bccInfo'))
        if m.get('idcInfo') is not None:
            self.idc_info = IDCCacheNodeInfo().from_dict(m.get('idcInfo'))
        if m.get('cceInfo') is not None:
            self.cce_info = CCECacheNodeInfo().from_dict(m.get('cceInfo'))
        if m.get('k8sInfo') is not None:
            self.k8s_info = K8SCacheNodeInfo().from_dict(m.get('k8sInfo'))
        if m.get('aihcInfo') is not None:
            self.aihc_info = AIHCCacheNodeInfo().from_dict(m.get('aihcInfo'))
        return self
