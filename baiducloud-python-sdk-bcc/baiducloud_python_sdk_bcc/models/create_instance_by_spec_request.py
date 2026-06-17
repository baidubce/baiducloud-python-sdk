"""
Request entity for CreateInstanceBySpecRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.create_cds_model import CreateCdsModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel
from baiducloud_python_sdk_bcc.models.file_system_model import FileSystemModel
from baiducloud_python_sdk_bcc.models.ephemeral_disk import EphemeralDisk
from baiducloud_python_sdk_bcc.models.billing import Billing


class CreateInstanceBySpecRequest(AbstractModel):
    """
    Request entity for CreateInstanceBySpecRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image_id,
        spec,
        zone_name,
        billing,
        keep_image_login=None,
        bcc_create_with_script=None,
        name=None,
        cpu_thread_config=None,
        numa_config=None,
        enable_delete_protection=None,
        hostname=None,
        auto_seq_suffix=None,
        is_open_hostname_domain=None,
        admin_pass=None,
        keypair_id=None,
        asp_id=None,
        spec_id=None,
        enable_jumbo_frame=None,
        user_data=None,
        deletion_protection=None,
        auto_renew_time_unit=None,
        auto_renew_time=None,
        hosteye_type=None,
        enable_numa=None,
        data_partition_type=None,
        root_partition_type=None,
        cds_auto_renew=None,
        create_cds_list=None,
        role_name=None,
        bid_model=None,
        bid_price=None,
        root_disk_size_in_gb=None,
        root_disk_extra_io=None,
        root_disk_storage_type=None,
        network_capacity_in_mbps=None,
        ehc_cluster_id=None,
        purchase_count=None,
        purchase_min_count=None,
        dedicated_host_id=None,
        relation_tag=None,
        tags=None,
        file_systems=None,
        ephemeral_disks=None,
        security_group_id=None,
        enterprise_security_group_id=None,
        security_group_ids=None,
        enterprise_security_group_ids=None,
        subnet_id=None,
        deploy_id=None,
        deploy_id_list=None,
        eni_ids=None,
        disable_root_disk_serial=None,
        internal_ips=None,
        res_group_id=None,
        is_eip_auto_related_delete=None,
        network_purchase_type=None,
        instance_type=None,
        internet_charge_type=None,
        eip_name=None,
        is_open_host_eye=None,
        enable_ht=None,
        is_open_ipv6=None,
    ):
        """
        Initialize CreateInstanceBySpecRequest request entity.

        :param keep_image_login: keep_image_login parameter
        :type keep_image_login: bool (optional)

        :param bcc_create_with_script: 在创建BCC实例时执行的自动化脚本
        :type bcc_create_with_script: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param cpu_thread_config: cpu_thread_config parameter
        :type cpu_thread_config: str (optional)

        :param numa_config: numa_config parameter
        :type numa_config: str (optional)

        :param enable_delete_protection: 是否开启删除保护功能
        :type enable_delete_protection: bool (optional)

        :param hostname: hostname parameter
        :type hostname: str (optional)

        :param auto_seq_suffix: 是否自动生成name和hostname有序后缀（可选参数） 是:true 否:false
        :type auto_seq_suffix: bool (optional)

        :param is_open_hostname_domain: 是否自动生成hostname domain（可选参数） 是:true 否:false
        :type is_open_hostname_domain: bool (optional)

        :param admin_pass: admin_pass parameter
        :type admin_pass: str (optional)

        :param keypair_id: 待创建实例所要绑定的密钥对ID
        :type keypair_id: str (optional)

        :param asp_id: 自动快照策略ID
        :type asp_id: str (optional)

        :param spec_id: 规格族
        :type spec_id: str (optional)

        :param enable_jumbo_frame: 是否开启Jumbo帧，默认值false，开启:true，关闭:false。注意:只有支持Jumbo帧的套餐才能开启
        :type enable_jumbo_frame: bool (optional)

        :param user_data: user_data parameter
        :type user_data: str (optional)

        :param deletion_protection: 实例释放保护，默认0未开启，1开启，开启后禁止手动释放虚机
        :type deletion_protection: str (optional)

        :param auto_renew_time_unit: 若开启自动续费，则需传值，不开启为空。按月付费或者按年付费 月是\"month\",年是\"year\"
        :type auto_renew_time_unit: str (optional)

        :param auto_renew_time: 若开启自动续费，则需传值，不开启为空。自动续费的时间 按月是1-9 按年是 1-5
        :type auto_renew_time: int (optional)

        :param hosteye_type: hosteye_type parameter
        :type hosteye_type: str (optional)

        :param enable_numa: 控制是否启用NUMA优化功能
        :type enable_numa: bool (optional)

        :param data_partition_type: 数据盘文件格式,可选值：xfs，ext4
        :type data_partition_type: str (optional)

        :param root_partition_type: 系统盘文件格式,可选值：xfs，ext4
        :type root_partition_type: str (optional)

        :param cds_auto_renew: 【此参数废弃，cds自动续费和bcc保持一致】cds是否自动续费 是:true 否:false
        :type cds_auto_renew: bool (optional)

        :param create_cds_list: 待创建的CDS磁盘列表
        :type create_cds_list: List[CreateCdsModel] (optional)

        :param image_id: 待创建虚拟机实例的镜像ID，可通过调用查询镜像列表接口选择获取所需镜像ID。
        :type image_id: str (required)

        :param spec: 待创建虚拟机实例的套餐规格例bcc.g7.c2m8，通过使用实例套餐规格列表接口来查看可使用实例套餐及套餐规格。
        :type spec: str (required)

        :param role_name: 角色名称
        :type role_name: str (optional)

        :param bid_model: 抢占实例出价模型， 市场价: \"market\" 自定义：\"custom\"。参考BidModel
        :type bid_model: str (optional)

        :param bid_price: bid_price parameter
        :type bid_price: str (optional)

        :param root_disk_size_in_gb: root_disk_size_in_gb parameter
        :type root_disk_size_in_gb: int (optional)

        :param root_disk_extra_io: 配置根磁盘的额外IO性能
        :type root_disk_extra_io: str (optional)

        :param root_disk_storage_type: 待创建虚拟机实例系统盘介质，默认使用高性能云磁盘（hp1），可指定系统盘磁盘类型可参见StorageType。
        :type root_disk_storage_type: str (optional)

        :param network_capacity_in_mbps: network_capacity_in_mbps parameter
        :type network_capacity_in_mbps: int (optional)

        :param ehc_cluster_id: 创建roce实例时可选参数，若为空则使用默认EHC集群
        :type ehc_cluster_id: str (optional)

        :param purchase_count: 批量创建（购买）的虚拟机实例个数，必须为大于0的整数，可选参数，缺省为1
        :type purchase_count: int (optional)

        :param purchase_min_count: 批量创建（购买）的虚拟机实例最小个数
        :type purchase_min_count: int (optional)

        :param dedicated_host_id: 专属服务器id，指定虚机置放位置时指定该值。
        :type dedicated_host_id: str (optional)

        :param relation_tag: 其关联资源CDS（数据盘）、EIP、快照、快照链是否统一加标签，默认为false。
        :type relation_tag: bool (optional)

        :param tags: 待创建的标签列表
        :type tags: List[TagModel] (optional)

        :param file_systems: 指定实例要挂载的cfs文件系统列表
        :type file_systems: List[FileSystemModel] (optional)

        :param ephemeral_disks: ephemeral_disks parameter
        :type ephemeral_disks: List[EphemeralDisk] (optional)

        :param security_group_id: 已废弃，指定securityGroup信息，为空时将使用默认安全组
        :type security_group_id: str (optional)

        :param enterprise_security_group_id: 指定企业安全组
        :type enterprise_security_group_id: str (optional)

        :param security_group_ids: 指定securityGroup信息列表，为空时将使用默认安全组
        :type security_group_ids: List[str] (optional)

        :param enterprise_security_group_ids: 指定企业安全组信息列表，不为空时，securityGroupIds无效，为空时将使用默认安全组
        :type enterprise_security_group_ids: List[str] (optional)

        :param subnet_id: 指定subnet信息，为空时将使用默认子网
        :type subnet_id: str (optional)

        :param deploy_id: 指定实例所在的部署集id
        :type deploy_id: str (optional)

        :param deploy_id_list: 指定实例所在的部署集id列表
        :type deploy_id_list: List[str] (optional)

        :param eni_ids: eni_ids parameter
        :type eni_ids: List[str] (optional)

        :param disable_root_disk_serial: 创建实例时是否隐藏系统盘SN,默认false。 true:隐藏 fase:不隐藏
        :type disable_root_disk_serial: str (optional)

        :param zone_name: zone_name parameter
        :type zone_name: str (required)

        :param internal_ips: 内网IP列表
        :type internal_ips: List[str] (optional)

        :param res_group_id: 指定实例要绑定的资源组id
        :type res_group_id: str (optional)

        :param is_eip_auto_related_delete: is_eip_auto_related_delete parameter
        :type is_eip_auto_related_delete: bool (optional)

        :param network_purchase_type: EIP线路类型，包含标准BGP（BGP）和增强BGP（BGP_S），默认标准BGP
        :type network_purchase_type: str (optional)

        :param instance_type: 待创建虚拟机实例的类型，具体可选类型参见InstanceType，为空时使用默认虚机类型
        :type instance_type: str (optional)

        :param internet_charge_type: internet_charge_type parameter
        :type internet_charge_type: str (optional)

        :param eip_name: 公网IP名称，长度1～65个字节，字母开头，可包含字母数字-_/.字符。若不传该参数，服务会自动生成name。
        :type eip_name: str (optional)

        :param is_open_host_eye: 是否开启主机安全，true:开启，false：关闭；不传默认开启
        :type is_open_host_eye: bool (optional)

        :param enable_ht: 是否开启Ht,ebc使用，默认值true, true:开启，false:关闭
        :type enable_ht: bool (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param is_open_ipv6: is_open_ipv6 parameter
        :type is_open_ipv6: bool (optional)
        """
        super().__init__()
        self.keep_image_login = keep_image_login
        self.bcc_create_with_script = bcc_create_with_script
        self.name = name
        self.cpu_thread_config = cpu_thread_config
        self.numa_config = numa_config
        self.enable_delete_protection = enable_delete_protection
        self.hostname = hostname
        self.auto_seq_suffix = auto_seq_suffix
        self.is_open_hostname_domain = is_open_hostname_domain
        self.admin_pass = admin_pass
        self.keypair_id = keypair_id
        self.asp_id = asp_id
        self.spec_id = spec_id
        self.enable_jumbo_frame = enable_jumbo_frame
        self.user_data = user_data
        self.deletion_protection = deletion_protection
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time
        self.hosteye_type = hosteye_type
        self.enable_numa = enable_numa
        self.data_partition_type = data_partition_type
        self.root_partition_type = root_partition_type
        self.cds_auto_renew = cds_auto_renew
        self.create_cds_list = create_cds_list
        self.image_id = image_id
        self.spec = spec
        self.role_name = role_name
        self.bid_model = bid_model
        self.bid_price = bid_price
        self.root_disk_size_in_gb = root_disk_size_in_gb
        self.root_disk_extra_io = root_disk_extra_io
        self.root_disk_storage_type = root_disk_storage_type
        self.network_capacity_in_mbps = network_capacity_in_mbps
        self.ehc_cluster_id = ehc_cluster_id
        self.purchase_count = purchase_count
        self.purchase_min_count = purchase_min_count
        self.dedicated_host_id = dedicated_host_id
        self.relation_tag = relation_tag
        self.tags = tags
        self.file_systems = file_systems
        self.ephemeral_disks = ephemeral_disks
        self.security_group_id = security_group_id
        self.enterprise_security_group_id = enterprise_security_group_id
        self.security_group_ids = security_group_ids
        self.enterprise_security_group_ids = enterprise_security_group_ids
        self.subnet_id = subnet_id
        self.deploy_id = deploy_id
        self.deploy_id_list = deploy_id_list
        self.eni_ids = eni_ids
        self.disable_root_disk_serial = disable_root_disk_serial
        self.zone_name = zone_name
        self.internal_ips = internal_ips
        self.res_group_id = res_group_id
        self.is_eip_auto_related_delete = is_eip_auto_related_delete
        self.network_purchase_type = network_purchase_type
        self.instance_type = instance_type
        self.internet_charge_type = internet_charge_type
        self.eip_name = eip_name
        self.is_open_host_eye = is_open_host_eye
        self.enable_ht = enable_ht
        self.billing = billing
        self.is_open_ipv6 = is_open_ipv6

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
        if self.keep_image_login is not None:
            result['keepImageLogin'] = self.keep_image_login
        if self.bcc_create_with_script is not None:
            result['bccCreateWithScript'] = self.bcc_create_with_script
        if self.name is not None:
            result['name'] = self.name
        if self.cpu_thread_config is not None:
            result['cpuThreadConfig'] = self.cpu_thread_config
        if self.numa_config is not None:
            result['numaConfig'] = self.numa_config
        if self.enable_delete_protection is not None:
            result['enableDeleteProtection'] = self.enable_delete_protection
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
        if self.asp_id is not None:
            result['aspId'] = self.asp_id
        if self.spec_id is not None:
            result['specId'] = self.spec_id
        if self.enable_jumbo_frame is not None:
            result['enableJumboFrame'] = self.enable_jumbo_frame
        if self.user_data is not None:
            result['userData'] = self.user_data
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.hosteye_type is not None:
            result['hosteyeType'] = self.hosteye_type
        if self.enable_numa is not None:
            result['enableNuma'] = self.enable_numa
        if self.data_partition_type is not None:
            result['dataPartitionType'] = self.data_partition_type
        if self.root_partition_type is not None:
            result['rootPartitionType'] = self.root_partition_type
        if self.cds_auto_renew is not None:
            result['cdsAutoRenew'] = self.cds_auto_renew
        if self.create_cds_list is not None:
            result['createCdsList'] = [i.to_dict() for i in self.create_cds_list]
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.spec is not None:
            result['spec'] = self.spec
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.bid_model is not None:
            result['bidModel'] = self.bid_model
        if self.bid_price is not None:
            result['bidPrice'] = self.bid_price
        if self.root_disk_size_in_gb is not None:
            result['rootDiskSizeInGb'] = self.root_disk_size_in_gb
        if self.root_disk_extra_io is not None:
            result['rootDiskExtraIo'] = self.root_disk_extra_io
        if self.root_disk_storage_type is not None:
            result['rootDiskStorageType'] = self.root_disk_storage_type
        if self.network_capacity_in_mbps is not None:
            result['networkCapacityInMbps'] = self.network_capacity_in_mbps
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        if self.purchase_min_count is not None:
            result['purchaseMinCount'] = self.purchase_min_count
        if self.dedicated_host_id is not None:
            result['dedicatedHostId'] = self.dedicated_host_id
        if self.relation_tag is not None:
            result['relationTag'] = self.relation_tag
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.file_systems is not None:
            result['fileSystems'] = [i.to_dict() for i in self.file_systems]
        if self.ephemeral_disks is not None:
            result['ephemeralDisks'] = [i.to_dict() for i in self.ephemeral_disks]
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.enterprise_security_group_id is not None:
            result['enterpriseSecurityGroupId'] = self.enterprise_security_group_id
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.enterprise_security_group_ids is not None:
            result['enterpriseSecurityGroupIds'] = self.enterprise_security_group_ids
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.deploy_id is not None:
            result['deployId'] = self.deploy_id
        if self.deploy_id_list is not None:
            result['deployIdList'] = self.deploy_id_list
        if self.eni_ids is not None:
            result['eniIds'] = self.eni_ids
        if self.disable_root_disk_serial is not None:
            result['disableRootDiskSerial'] = self.disable_root_disk_serial
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.internal_ips is not None:
            result['internalIps'] = self.internal_ips
        if self.res_group_id is not None:
            result['resGroupId'] = self.res_group_id
        if self.is_eip_auto_related_delete is not None:
            result['isEipAutoRelatedDelete'] = self.is_eip_auto_related_delete
        if self.network_purchase_type is not None:
            result['networkPurchaseType'] = self.network_purchase_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['internetChargeType'] = self.internet_charge_type
        if self.eip_name is not None:
            result['eipName'] = self.eip_name
        if self.is_open_host_eye is not None:
            result['isOpenHostEye'] = self.is_open_host_eye
        if self.enable_ht is not None:
            result['enableHt'] = self.enable_ht
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.is_open_ipv6 is not None:
            result['isOpenIpv6'] = self.is_open_ipv6
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateInstanceBySpecRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keepImageLogin') is not None:
            self.keep_image_login = m.get('keepImageLogin')
        if m.get('bccCreateWithScript') is not None:
            self.bcc_create_with_script = m.get('bccCreateWithScript')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cpuThreadConfig') is not None:
            self.cpu_thread_config = m.get('cpuThreadConfig')
        if m.get('numaConfig') is not None:
            self.numa_config = m.get('numaConfig')
        if m.get('enableDeleteProtection') is not None:
            self.enable_delete_protection = m.get('enableDeleteProtection')
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
        if m.get('aspId') is not None:
            self.asp_id = m.get('aspId')
        if m.get('specId') is not None:
            self.spec_id = m.get('specId')
        if m.get('enableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('enableJumboFrame')
        if m.get('userData') is not None:
            self.user_data = m.get('userData')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('hosteyeType') is not None:
            self.hosteye_type = m.get('hosteyeType')
        if m.get('enableNuma') is not None:
            self.enable_numa = m.get('enableNuma')
        if m.get('dataPartitionType') is not None:
            self.data_partition_type = m.get('dataPartitionType')
        if m.get('rootPartitionType') is not None:
            self.root_partition_type = m.get('rootPartitionType')
        if m.get('cdsAutoRenew') is not None:
            self.cds_auto_renew = m.get('cdsAutoRenew')
        if m.get('createCdsList') is not None:
            self.create_cds_list = [CreateCdsModel().from_dict(i) for i in m.get('createCdsList')]
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('bidModel') is not None:
            self.bid_model = m.get('bidModel')
        if m.get('bidPrice') is not None:
            self.bid_price = m.get('bidPrice')
        if m.get('rootDiskSizeInGb') is not None:
            self.root_disk_size_in_gb = m.get('rootDiskSizeInGb')
        if m.get('rootDiskExtraIo') is not None:
            self.root_disk_extra_io = m.get('rootDiskExtraIo')
        if m.get('rootDiskStorageType') is not None:
            self.root_disk_storage_type = m.get('rootDiskStorageType')
        if m.get('networkCapacityInMbps') is not None:
            self.network_capacity_in_mbps = m.get('networkCapacityInMbps')
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        if m.get('purchaseMinCount') is not None:
            self.purchase_min_count = m.get('purchaseMinCount')
        if m.get('dedicatedHostId') is not None:
            self.dedicated_host_id = m.get('dedicatedHostId')
        if m.get('relationTag') is not None:
            self.relation_tag = m.get('relationTag')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('fileSystems') is not None:
            self.file_systems = [FileSystemModel().from_dict(i) for i in m.get('fileSystems')]
        if m.get('ephemeralDisks') is not None:
            self.ephemeral_disks = [EphemeralDisk().from_dict(i) for i in m.get('ephemeralDisks')]
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('enterpriseSecurityGroupId') is not None:
            self.enterprise_security_group_id = m.get('enterpriseSecurityGroupId')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('enterpriseSecurityGroupIds') is not None:
            self.enterprise_security_group_ids = m.get('enterpriseSecurityGroupIds')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('deployId') is not None:
            self.deploy_id = m.get('deployId')
        if m.get('deployIdList') is not None:
            self.deploy_id_list = m.get('deployIdList')
        if m.get('eniIds') is not None:
            self.eni_ids = m.get('eniIds')
        if m.get('disableRootDiskSerial') is not None:
            self.disable_root_disk_serial = m.get('disableRootDiskSerial')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('internalIps') is not None:
            self.internal_ips = m.get('internalIps')
        if m.get('resGroupId') is not None:
            self.res_group_id = m.get('resGroupId')
        if m.get('isEipAutoRelatedDelete') is not None:
            self.is_eip_auto_related_delete = m.get('isEipAutoRelatedDelete')
        if m.get('networkPurchaseType') is not None:
            self.network_purchase_type = m.get('networkPurchaseType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetChargeType') is not None:
            self.internet_charge_type = m.get('internetChargeType')
        if m.get('eipName') is not None:
            self.eip_name = m.get('eipName')
        if m.get('isOpenHostEye') is not None:
            self.is_open_host_eye = m.get('isOpenHostEye')
        if m.get('enableHt') is not None:
            self.enable_ht = m.get('enableHt')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('isOpenIpv6') is not None:
            self.is_open_ipv6 = m.get('isOpenIpv6')
        return self
