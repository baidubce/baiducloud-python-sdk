"""
Request entity for CreateBidInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.billing import Billing
from baiducloud_python_sdk_bcc.models.create_cds_model import CreateCdsModel
from baiducloud_python_sdk_bcc.models.ephemeral_disk import EphemeralDisk
from baiducloud_python_sdk_bcc.models.tag_model import TagModel
from baiducloud_python_sdk_bcc.models.file_system_model import FileSystemModel


class CreateBidInstanceRequest(AbstractModel):
    """
    Request entity for CreateBidInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        spec,
        image_id,
        billing,
        bid_model,
        bid_price=None,
        cpu_count=None,
        memory_capacity_in_gb=None,
        root_disk_size_in_gb=None,
        root_disk_storage_type=None,
        create_cds_list=None,
        ephemeral_disks=None,
        network_capacity_in_mbps=None,
        internet_charge_type=None,
        eip_name=None,
        purchase_count=None,
        name=None,
        hostname=None,
        auto_seq_suffix=None,
        is_open_hostname_domain=None,
        admin_pass=None,
        keypair_id=None,
        user_data=None,
        zone_name=None,
        subnet_id=None,
        security_group_id=None,
        enterprise_security_group_id=None,
        isomerism_card=None,
        deletion_protection=None,
        relation_tag=None,
        is_open_ipv6=None,
        tags=None,
        asp_id=None,
        file_systems=None,
        is_eip_auto_related_delete=None,
        res_group_id=None,
    ):
        """
        Initialize CreateBidInstanceRequest request entity.

        :param spec: 实例规格
        :type spec: str (required)

        :param image_id: 镜像ID
        :type image_id: str (required)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param bid_model: 抢占实例出价模型，市场价: market，自定义: custom
        :type bid_model: str (required)

        :param bid_price: 抢占实例出价金额，单位：元/分钟。当bidModel=custom时有效
        :type bid_price: str (optional)

        :param cpu_count: CPU核数
        :type cpu_count: int (optional)

        :param memory_capacity_in_gb: 内存容量，单位GB
        :type memory_capacity_in_gb: int (optional)

        :param root_disk_size_in_gb: 系统盘大小，单位GB，默认40，范围[40, 2048]
        :type root_disk_size_in_gb: int (optional)

        :param root_disk_storage_type: 系统盘介质类型
        :type root_disk_storage_type: str (optional)

        :param create_cds_list: 待创建的CDS磁盘列表
        :type create_cds_list: List[CreateCdsModel] (optional)

        :param ephemeral_disks: 本地盘列表
        :type ephemeral_disks: List[EphemeralDisk] (optional)

        :param network_capacity_in_mbps: 公网带宽，单位Mbps，0~200，0表示不分配公网IP
        :type network_capacity_in_mbps: int (optional)

        :param internet_charge_type: 公网带宽计费方式
        :type internet_charge_type: str (optional)

        :param eip_name: EIP名称
        :type eip_name: str (optional)

        :param purchase_count: 批量创建的实例个数，默认为1
        :type purchase_count: int (optional)

        :param name: 虚拟机名字，批量时作为前缀
        :type name: str (optional)

        :param hostname: 虚拟机主机名
        :type hostname: str (optional)

        :param auto_seq_suffix: 是否自动生成name和hostname有序后缀
        :type auto_seq_suffix: bool (optional)

        :param is_open_hostname_domain: 是否自动生成hostname domain
        :type is_open_hostname_domain: bool (optional)

        :param admin_pass: 实例管理员密码，需加密传输
        :type admin_pass: str (optional)

        :param keypair_id: 密钥对ID
        :type keypair_id: str (optional)

        :param user_data: 用户自定义数据，Base64编码
        :type user_data: str (optional)

        :param zone_name: 可用区名称，如cn-bj-a
        :type zone_name: str (optional)

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)

        :param security_group_id: 安全组ID
        :type security_group_id: str (optional)

        :param enterprise_security_group_id: 企业安全组ID
        :type enterprise_security_group_id: str (optional)

        :param isomerism_card: 异构卡信息
        :type isomerism_card: str (optional)

        :param deletion_protection: 实例释放保护，0未开启，1开启
        :type deletion_protection: int (optional)

        :param relation_tag: 标签是否需要和已有标签键进行关联
        :type relation_tag: bool (optional)

        :param is_open_ipv6: 是否开启ipv6
        :type is_open_ipv6: bool (optional)

        :param tags: 标签列表
        :type tags: List[TagModel] (optional)

        :param asp_id: 自动快照策略ID
        :type asp_id: str (optional)

        :param file_systems: 挂载文件存储CFS列表
        :type file_systems: List[FileSystemModel] (optional)

        :param is_eip_auto_related_delete: 后付费EIP是否随抢占实例关联自动释放
        :type is_eip_auto_related_delete: bool (optional)

        :param res_group_id: 资源组ID
        :type res_group_id: str (optional)
        """
        super().__init__()
        self.spec = spec
        self.image_id = image_id
        self.billing = billing
        self.bid_model = bid_model
        self.bid_price = bid_price
        self.cpu_count = cpu_count
        self.memory_capacity_in_gb = memory_capacity_in_gb
        self.root_disk_size_in_gb = root_disk_size_in_gb
        self.root_disk_storage_type = root_disk_storage_type
        self.create_cds_list = create_cds_list
        self.ephemeral_disks = ephemeral_disks
        self.network_capacity_in_mbps = network_capacity_in_mbps
        self.internet_charge_type = internet_charge_type
        self.eip_name = eip_name
        self.purchase_count = purchase_count
        self.name = name
        self.hostname = hostname
        self.auto_seq_suffix = auto_seq_suffix
        self.is_open_hostname_domain = is_open_hostname_domain
        self.admin_pass = admin_pass
        self.keypair_id = keypair_id
        self.user_data = user_data
        self.zone_name = zone_name
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.enterprise_security_group_id = enterprise_security_group_id
        self.isomerism_card = isomerism_card
        self.deletion_protection = deletion_protection
        self.relation_tag = relation_tag
        self.is_open_ipv6 = is_open_ipv6
        self.tags = tags
        self.asp_id = asp_id
        self.file_systems = file_systems
        self.is_eip_auto_related_delete = is_eip_auto_related_delete
        self.res_group_id = res_group_id

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
        if self.spec is not None:
            result['spec'] = self.spec
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.bid_model is not None:
            result['bidModel'] = self.bid_model
        if self.bid_price is not None:
            result['bidPrice'] = self.bid_price
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.memory_capacity_in_gb is not None:
            result['memoryCapacityInGB'] = self.memory_capacity_in_gb
        if self.root_disk_size_in_gb is not None:
            result['rootDiskSizeInGb'] = self.root_disk_size_in_gb
        if self.root_disk_storage_type is not None:
            result['rootDiskStorageType'] = self.root_disk_storage_type
        if self.create_cds_list is not None:
            result['createCdsList'] = [i.to_dict() for i in self.create_cds_list]
        if self.ephemeral_disks is not None:
            result['ephemeralDisks'] = [i.to_dict() for i in self.ephemeral_disks]
        if self.network_capacity_in_mbps is not None:
            result['networkCapacityInMbps'] = self.network_capacity_in_mbps
        if self.internet_charge_type is not None:
            result['internetChargeType'] = self.internet_charge_type
        if self.eip_name is not None:
            result['eipName'] = self.eip_name
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        if self.name is not None:
            result['name'] = self.name
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.auto_seq_suffix is not None:
            result['autoSeqSuffix'] = self.auto_seq_suffix
        if self.is_open_hostname_domain is not None:
            result['isOpenHostnameDomain'] = self.is_open_hostname_domain
        if self.admin_pass is not None:
            result['adminPass'] = self.admin_pass
        if self.keypair_id is not None:
            result['keypairId'] = self.keypair_id
        if self.user_data is not None:
            result['userData'] = self.user_data
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.enterprise_security_group_id is not None:
            result['enterpriseSecurityGroupId'] = self.enterprise_security_group_id
        if self.isomerism_card is not None:
            result['isomerismCard'] = self.isomerism_card
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.relation_tag is not None:
            result['relationTag'] = self.relation_tag
        if self.is_open_ipv6 is not None:
            result['isOpenIpv6'] = self.is_open_ipv6
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.asp_id is not None:
            result['aspId'] = self.asp_id
        if self.file_systems is not None:
            result['fileSystems'] = [i.to_dict() for i in self.file_systems]
        if self.is_eip_auto_related_delete is not None:
            result['isEipAutoRelatedDelete'] = self.is_eip_auto_related_delete
        if self.res_group_id is not None:
            result['resGroupId'] = self.res_group_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateBidInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('bidModel') is not None:
            self.bid_model = m.get('bidModel')
        if m.get('bidPrice') is not None:
            self.bid_price = m.get('bidPrice')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('memoryCapacityInGB') is not None:
            self.memory_capacity_in_gb = m.get('memoryCapacityInGB')
        if m.get('rootDiskSizeInGb') is not None:
            self.root_disk_size_in_gb = m.get('rootDiskSizeInGb')
        if m.get('rootDiskStorageType') is not None:
            self.root_disk_storage_type = m.get('rootDiskStorageType')
        if m.get('createCdsList') is not None:
            self.create_cds_list = [CreateCdsModel().from_dict(i) for i in m.get('createCdsList')]
        if m.get('ephemeralDisks') is not None:
            self.ephemeral_disks = [EphemeralDisk().from_dict(i) for i in m.get('ephemeralDisks')]
        if m.get('networkCapacityInMbps') is not None:
            self.network_capacity_in_mbps = m.get('networkCapacityInMbps')
        if m.get('internetChargeType') is not None:
            self.internet_charge_type = m.get('internetChargeType')
        if m.get('eipName') is not None:
            self.eip_name = m.get('eipName')
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('autoSeqSuffix') is not None:
            self.auto_seq_suffix = m.get('autoSeqSuffix')
        if m.get('isOpenHostnameDomain') is not None:
            self.is_open_hostname_domain = m.get('isOpenHostnameDomain')
        if m.get('adminPass') is not None:
            self.admin_pass = m.get('adminPass')
        if m.get('keypairId') is not None:
            self.keypair_id = m.get('keypairId')
        if m.get('userData') is not None:
            self.user_data = m.get('userData')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('enterpriseSecurityGroupId') is not None:
            self.enterprise_security_group_id = m.get('enterpriseSecurityGroupId')
        if m.get('isomerismCard') is not None:
            self.isomerism_card = m.get('isomerismCard')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('relationTag') is not None:
            self.relation_tag = m.get('relationTag')
        if m.get('isOpenIpv6') is not None:
            self.is_open_ipv6 = m.get('isOpenIpv6')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('aspId') is not None:
            self.asp_id = m.get('aspId')
        if m.get('fileSystems') is not None:
            self.file_systems = [FileSystemModel().from_dict(i) for i in m.get('fileSystems')]
        if m.get('isEipAutoRelatedDelete') is not None:
            self.is_eip_auto_related_delete = m.get('isEipAutoRelatedDelete')
        if m.get('resGroupId') is not None:
            self.res_group_id = m.get('resGroupId')
        return self
