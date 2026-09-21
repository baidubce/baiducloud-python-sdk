"""
Request entity for InstanceDetailUsingGETResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vdb.models.vdb_auto_renew_rule import VdbAutoRenewRule
from baiducloud_python_sdk_vdb.models.az_info import AzInfo
from baiducloud_python_sdk_vdb.models.milvus_component import MilvusComponent
from baiducloud_python_sdk_vdb.models.data_node import DataNode
from baiducloud_python_sdk_vdb.models.log_service import LogService
from baiducloud_python_sdk_vdb.models.logging_service import LoggingService
from baiducloud_python_sdk_vdb.models.milvus_node import MilvusNode
from baiducloud_python_sdk_vdb.models.proxy import Proxy
from baiducloud_python_sdk_vdb.models.subnet import Subnet
from baiducloud_python_sdk_vdb.models.target_package import TargetPackage


class InstanceDetailUsingGETResponse(BceResponse):
    """
    InstanceDetailUsingGETResponse
    """

    def __init__(
        self,
        auto_renew_rule=None,
        availability_zone=None,
        az_infos=None,
        bcm_cycle=None,
        components=None,
        create_time=None,
        data_node_num=None,
        data_nodes=None,
        data_status=None,
        disk_type=None,
        domain=None,
        eip=None,
        enable_embedding=None,
        enable_encryption=None,
        enable_tde=None,
        engine_minor_version=None,
        engine_type=None,
        engine_version=None,
        expire_date=None,
        instance_expire_time=None,
        instance_id=None,
        instance_name=None,
        instance_type=None,
        ip=None,
        log_service=None,
        logging_services=None,
        node_spec=None,
        nodes=None,
        order_status=None,
        package_version=None,
        port=None,
        product_type=None,
        proxies=None,
        proxy_node_spec=None,
        proxy_num=None,
        status=None,
        subnets=None,
        support_embedding=None,
        target_package=None,
        total_disk_capacity_in_gb=None,
        total_mem_capacity_in_gb=None,
        upgradable=None,
        used_disk_capacity_in_gb=None,
        used_mem_capacity_in_gb=None,
        vip=None,
        vpc_cidr=None,
        vpc_id=None,
        vpc_name=None,
    ):
        """
        Initialize InstanceDetailUsingGETResponse response.

        :param auto_renew_rule: auto_renew_rule field
        :type auto_renew_rule: VdbAutoRenewRule (optional)

        :param availability_zone: availability_zone field
        :type availability_zone: str (optional)

        :param az_infos: az_infos field
        :type az_infos: List[AzInfo] (optional)

        :param bcm_cycle: bcm_cycle field
        :type bcm_cycle: int (optional)

        :param components: components field
        :type components: List[MilvusComponent] (optional)

        :param create_time: create_time field
        :type create_time: str (optional)

        :param data_node_num: data_node_num field
        :type data_node_num: int (optional)

        :param data_nodes: data_nodes field
        :type data_nodes: List[DataNode] (optional)

        :param data_status: data_status field
        :type data_status: str (optional)

        :param disk_type: disk_type field
        :type disk_type: str (optional)

        :param domain: domain field
        :type domain: str (optional)

        :param eip: eip field
        :type eip: str (optional)

        :param enable_embedding: enable_embedding field
        :type enable_embedding: bool (optional)

        :param enable_encryption: enable_encryption field
        :type enable_encryption: bool (optional)

        :param enable_tde: enable_tde field
        :type enable_tde: str (optional)

        :param engine_minor_version: engine_minor_version field
        :type engine_minor_version: str (optional)

        :param engine_type: engine_type field
        :type engine_type: str (optional)

        :param engine_version: engine_version field
        :type engine_version: str (optional)

        :param expire_date: expire_date field
        :type expire_date: int (optional)

        :param instance_expire_time: instance_expire_time field
        :type instance_expire_time: str (optional)

        :param instance_id: instance_id field
        :type instance_id: str (optional)

        :param instance_name: instance_name field
        :type instance_name: str (optional)

        :param instance_type: instance_type field
        :type instance_type: str (optional)

        :param ip: ip field
        :type ip: str (optional)

        :param log_service: log_service field
        :type log_service: LogService (optional)

        :param logging_services: logging_services field
        :type logging_services: List[LoggingService] (optional)

        :param node_spec: node_spec field
        :type node_spec: str (optional)

        :param nodes: nodes field
        :type nodes: List[MilvusNode] (optional)

        :param order_status: order_status field
        :type order_status: str (optional)

        :param package_version: package_version field
        :type package_version: str (optional)

        :param port: port field
        :type port: int (optional)

        :param product_type: product_type field
        :type product_type: str (optional)

        :param proxies: proxies field
        :type proxies: List[Proxy] (optional)

        :param proxy_node_spec: proxy_node_spec field
        :type proxy_node_spec: str (optional)

        :param proxy_num: proxy_num field
        :type proxy_num: int (optional)

        :param status: status field
        :type status: str (optional)

        :param subnets: subnets field
        :type subnets: List[Subnet] (optional)

        :param support_embedding: support_embedding field
        :type support_embedding: bool (optional)

        :param target_package: target_package field
        :type target_package: TargetPackage (optional)

        :param total_disk_capacity_in_gb: total_disk_capacity_in_gb field
        :type total_disk_capacity_in_gb: int (optional)

        :param total_mem_capacity_in_gb: total_mem_capacity_in_gb field
        :type total_mem_capacity_in_gb: int (optional)

        :param upgradable: upgradable field
        :type upgradable: bool (optional)

        :param used_disk_capacity_in_gb: used_disk_capacity_in_gb field
        :type used_disk_capacity_in_gb: float (optional)

        :param used_mem_capacity_in_gb: used_mem_capacity_in_gb field
        :type used_mem_capacity_in_gb: float (optional)

        :param vip: vip field
        :type vip: str (optional)

        :param vpc_cidr: vpc_cidr field
        :type vpc_cidr: str (optional)

        :param vpc_id: vpc_id field
        :type vpc_id: str (optional)

        :param vpc_name: vpc_name field
        :type vpc_name: str (optional)
        """
        super().__init__()
        self.auto_renew_rule = auto_renew_rule
        self.availability_zone = availability_zone
        self.az_infos = az_infos
        self.bcm_cycle = bcm_cycle
        self.components = components
        self.create_time = create_time
        self.data_node_num = data_node_num
        self.data_nodes = data_nodes
        self.data_status = data_status
        self.disk_type = disk_type
        self.domain = domain
        self.eip = eip
        self.enable_embedding = enable_embedding
        self.enable_encryption = enable_encryption
        self.enable_tde = enable_tde
        self.engine_minor_version = engine_minor_version
        self.engine_type = engine_type
        self.engine_version = engine_version
        self.expire_date = expire_date
        self.instance_expire_time = instance_expire_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.ip = ip
        self.log_service = log_service
        self.logging_services = logging_services
        self.node_spec = node_spec
        self.nodes = nodes
        self.order_status = order_status
        self.package_version = package_version
        self.port = port
        self.product_type = product_type
        self.proxies = proxies
        self.proxy_node_spec = proxy_node_spec
        self.proxy_num = proxy_num
        self.status = status
        self.subnets = subnets
        self.support_embedding = support_embedding
        self.target_package = target_package
        self.total_disk_capacity_in_gb = total_disk_capacity_in_gb
        self.total_mem_capacity_in_gb = total_mem_capacity_in_gb
        self.upgradable = upgradable
        self.used_disk_capacity_in_gb = used_disk_capacity_in_gb
        self.used_mem_capacity_in_gb = used_mem_capacity_in_gb
        self.vip = vip
        self.vpc_cidr = vpc_cidr
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.auto_renew_rule is not None:
            result['autoRenewRule'] = self.auto_renew_rule.to_dict()
        if self.availability_zone is not None:
            result['availabilityZone'] = self.availability_zone
        if self.az_infos is not None:
            result['azInfos'] = [i.to_dict() for i in self.az_infos]
        if self.bcm_cycle is not None:
            result['bcmCycle'] = self.bcm_cycle
        if self.components is not None:
            result['components'] = [i.to_dict() for i in self.components]
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_node_num is not None:
            result['dataNodeNum'] = self.data_node_num
        if self.data_nodes is not None:
            result['dataNodes'] = [i.to_dict() for i in self.data_nodes]
        if self.data_status is not None:
            result['dataStatus'] = self.data_status
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.domain is not None:
            result['domain'] = self.domain
        if self.eip is not None:
            result['eip'] = self.eip
        if self.enable_embedding is not None:
            result['enableEmbedding'] = self.enable_embedding
        if self.enable_encryption is not None:
            result['enableEncryption'] = self.enable_encryption
        if self.enable_tde is not None:
            result['enableTDE'] = self.enable_tde
        if self.engine_minor_version is not None:
            result['engineMinorVersion'] = self.engine_minor_version
        if self.engine_type is not None:
            result['engineType'] = self.engine_type
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date
        if self.instance_expire_time is not None:
            result['instanceExpireTime'] = self.instance_expire_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.ip is not None:
            result['ip'] = self.ip
        if self.log_service is not None:
            result['logService'] = self.log_service.to_dict()
        if self.logging_services is not None:
            result['loggingServices'] = [i.to_dict() for i in self.logging_services]
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec
        if self.nodes is not None:
            result['nodes'] = [i.to_dict() for i in self.nodes]
        if self.order_status is not None:
            result['orderStatus'] = self.order_status
        if self.package_version is not None:
            result['packageVersion'] = self.package_version
        if self.port is not None:
            result['port'] = self.port
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.proxies is not None:
            result['proxies'] = [i.to_dict() for i in self.proxies]
        if self.proxy_node_spec is not None:
            result['proxyNodeSpec'] = self.proxy_node_spec
        if self.proxy_num is not None:
            result['proxyNum'] = self.proxy_num
        if self.status is not None:
            result['status'] = self.status
        if self.subnets is not None:
            result['subnets'] = [i.to_dict() for i in self.subnets]
        if self.support_embedding is not None:
            result['supportEmbedding'] = self.support_embedding
        if self.target_package is not None:
            result['targetPackage'] = self.target_package.to_dict()
        if self.total_disk_capacity_in_gb is not None:
            result['totalDiskCapacityInGB'] = self.total_disk_capacity_in_gb
        if self.total_mem_capacity_in_gb is not None:
            result['totalMemCapacityInGB'] = self.total_mem_capacity_in_gb
        if self.upgradable is not None:
            result['upgradable'] = self.upgradable
        if self.used_disk_capacity_in_gb is not None:
            result['usedDiskCapacityInGB'] = self.used_disk_capacity_in_gb
        if self.used_mem_capacity_in_gb is not None:
            result['usedMemCapacityInGB'] = self.used_mem_capacity_in_gb
        if self.vip is not None:
            result['vip'] = self.vip
        if self.vpc_cidr is not None:
            result['vpcCidr'] = self.vpc_cidr
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['vpcName'] = self.vpc_name
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceDetailUsingGETResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('autoRenewRule') is not None:
            self.auto_renew_rule = VdbAutoRenewRule().from_dict(m.get('autoRenewRule'))
        if m.get('availabilityZone') is not None:
            self.availability_zone = m.get('availabilityZone')
        if m.get('azInfos') is not None:
            self.az_infos = [AzInfo().from_dict(i) for i in m.get('azInfos')]
        if m.get('bcmCycle') is not None:
            self.bcm_cycle = m.get('bcmCycle')
        if m.get('components') is not None:
            self.components = [MilvusComponent().from_dict(i) for i in m.get('components')]
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataNodeNum') is not None:
            self.data_node_num = m.get('dataNodeNum')
        if m.get('dataNodes') is not None:
            self.data_nodes = [DataNode().from_dict(i) for i in m.get('dataNodes')]
        if m.get('dataStatus') is not None:
            self.data_status = m.get('dataStatus')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('enableEmbedding') is not None:
            self.enable_embedding = m.get('enableEmbedding')
        if m.get('enableEncryption') is not None:
            self.enable_encryption = m.get('enableEncryption')
        if m.get('enableTDE') is not None:
            self.enable_tde = m.get('enableTDE')
        if m.get('engineMinorVersion') is not None:
            self.engine_minor_version = m.get('engineMinorVersion')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')
        if m.get('instanceExpireTime') is not None:
            self.instance_expire_time = m.get('instanceExpireTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('logService') is not None:
            self.log_service = LogService().from_dict(m.get('logService'))
        if m.get('loggingServices') is not None:
            self.logging_services = [LoggingService().from_dict(i) for i in m.get('loggingServices')]
        if m.get('nodeSpec') is not None:
            self.node_spec = m.get('nodeSpec')
        if m.get('nodes') is not None:
            self.nodes = [MilvusNode().from_dict(i) for i in m.get('nodes')]
        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')
        if m.get('packageVersion') is not None:
            self.package_version = m.get('packageVersion')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('proxies') is not None:
            self.proxies = [Proxy().from_dict(i) for i in m.get('proxies')]
        if m.get('proxyNodeSpec') is not None:
            self.proxy_node_spec = m.get('proxyNodeSpec')
        if m.get('proxyNum') is not None:
            self.proxy_num = m.get('proxyNum')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subnets') is not None:
            self.subnets = [Subnet().from_dict(i) for i in m.get('subnets')]
        if m.get('supportEmbedding') is not None:
            self.support_embedding = m.get('supportEmbedding')
        if m.get('targetPackage') is not None:
            self.target_package = TargetPackage().from_dict(m.get('targetPackage'))
        if m.get('totalDiskCapacityInGB') is not None:
            self.total_disk_capacity_in_gb = m.get('totalDiskCapacityInGB')
        if m.get('totalMemCapacityInGB') is not None:
            self.total_mem_capacity_in_gb = m.get('totalMemCapacityInGB')
        if m.get('upgradable') is not None:
            self.upgradable = m.get('upgradable')
        if m.get('usedDiskCapacityInGB') is not None:
            self.used_disk_capacity_in_gb = m.get('usedDiskCapacityInGB')
        if m.get('usedMemCapacityInGB') is not None:
            self.used_mem_capacity_in_gb = m.get('usedMemCapacityInGB')
        if m.get('vip') is not None:
            self.vip = m.get('vip')
        if m.get('vpcCidr') is not None:
            self.vpc_cidr = m.get('vpcCidr')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcName') is not None:
            self.vpc_name = m.get('vpcName')
        return self
