"""
InstanceModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.rdma_nic_topo import RdmaNicTopo

from baiducloud_python_sdk_bcc.models.deploy_set_model import DeploySetModel

from baiducloud_python_sdk_bcc.models.group_info import GroupInfo

from baiducloud_python_sdk_bcc.models.nic_info import NicInfo

from baiducloud_python_sdk_bcc.models.tag import Tag

from baiducloud_python_sdk_bcc.models.volume_model import VolumeModel


class InstanceModel(AbstractModel):
    """
    InstanceModel
    """

    def __init__(
        self,
        id=None,
        source_product_id=None,
        source_product_type=None,
        serial_number=None,
        keypair_id=None,
        keypair_name=None,
        name=None,
        role_name=None,
        hostname=None,
        instance_type=None,
        spec=None,
        enable_jumbo_frame=None,
        status=None,
        desc=None,
        created_from=None,
        payment_timing=None,
        charge_status=None,
        display_charge_status=None,
        create_time=None,
        expire_time=None,
        release_time=None,
        internal_ip=None,
        public_ip=None,
        cpu_count=None,
        rdma_unit_id=None,
        rdma_pod_name=None,
        deletion_protection=None,
        rdma_nic_topo=None,
        deployset_list=None,
        res_group_infos=None,
        hosteye_type=None,
        gpu_card=None,
        gpu_video_memory=None,
        fpga_card=None,
        card_count=None,
        isomerism_card=None,
        npu_video_memory=None,
        memory_capacity_in_gb=None,
        local_disk_size_in_gb=None,
        image_id=None,
        image_type=None,
        image_name=None,
        os_version=None,
        os_arch=None,
        os_name=None,
        placement_policy=None,
        subnet_id=None,
        vpc_id=None,
        is_eip_auto_related_delete=None,
        ehc_cluster_id=None,
        deployset_id=None,
        zone_name=None,
        flavor_sub_type=None,
        product_category=None,
        repair_status=None,
        host_id=None,
        switch_id=None,
        rack_id=None,
        dedicated_host_id=None,
        auto_renew=None,
        auto_renew_period_unit=None,
        auto_renew_period=None,
        ipv6=None,
        net_eth_queue_count=None,
        eni_quota=None,
        eri_quota=None,
        rdma_type=None,
        service_components=None,
        ipv6_addresses=None,
        nic_info=None,
        eni_num=None,
        tags=None,
        volumes=None,
        network_capacity_in_mbps=None,
    ):
        """
        Initialize InstanceModel instance.

        :param id: id attribute
        :type id: str (optional)

        :param source_product_id: 来源产品ID（查询实例列表、查询指定实例详情）
        :type source_product_id: str (optional)

        :param source_product_type: 来源产品类型（查询实例列表、查询指定实例详情）
        :type source_product_type: str (optional)

        :param serial_number: 序列号（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type serial_number: str (optional)

        :param keypair_id: 密钥对ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type keypair_id: str (optional)

        :param keypair_name: 密钥对名称（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type keypair_name: str (optional)

        :param name: name attribute
        :type name: str (optional)

        :param role_name: 角色名称（查询实例列表、查询指定实例详情）
        :type role_name: str (optional)

        :param hostname: hostname attribute
        :type hostname: str (optional)

        :param instance_type: instance_type attribute
        :type instance_type: str (optional)

        :param spec: 规格（查询实例列表、查询指定实例详情）
        :type spec: str (optional)

        :param enable_jumbo_frame: 是否开启Jumbo帧，开启：true，关闭：false（查询实例列表、查询指定实例详情）
        :type enable_jumbo_frame: bool (optional)

        :param status: 实例状态（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type status: str (optional)

        :param desc: 实例描述信息（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type desc: str (optional)

        :param created_from: 创建来源（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type created_from: str (optional)

        :param payment_timing: payment_timing attribute
        :type payment_timing: str (optional)

        :param charge_status: charge_status attribute
        :type charge_status: str (optional)

        :param display_charge_status: 计费状态信息（查询指定实例详情）
        :type display_charge_status: str (optional)

        :param create_time: 创建时间（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type create_time: str (optional)

        :param expire_time: 过期时间（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type expire_time: str (optional)

        :param release_time: 释放时间（查询指定实例详情）
        :type release_time: str (optional)

        :param internal_ip: 内网IP（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type internal_ip: str (optional)

        :param public_ip: 外网IP（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type public_ip: str (optional)

        :param cpu_count: CPU(Core)个数（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type cpu_count: int (optional)

        :param rdma_unit_id: RDMA单元ID（查询实例列表、查询指定实例详情）
        :type rdma_unit_id: str (optional)

        :param rdma_pod_name: RDMA Pod名称（查询实例列表、查询指定实例详情）
        :type rdma_pod_name: str (optional)

        :param deletion_protection: 是否开启删除保护，1开启，0没开（查询实例列表、查询指定实例详情）
        :type deletion_protection: int (optional)

        :param rdma_nic_topo: RDMA高性能网络的详细连接信息（查询实例列表、查询指定实例详情）
        :type rdma_nic_topo: List[RdmaNicTopo] (optional)

        :param deployset_list: 部署集信息列表（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type deployset_list: List[DeploySetModel] (optional)

        :param res_group_infos: 实例所属的资源组信息（查询实例列表、查询指定实例详情）
        :type res_group_infos: List[GroupInfo] (optional)

        :param hosteye_type: hosteye_type attribute
        :type hosteye_type: str (optional)

        :param gpu_card: gpu_card attribute
        :type gpu_card: str (optional)

        :param gpu_video_memory: 实例的GPU显存配置信息（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type gpu_video_memory: str (optional)

        :param fpga_card: fpga_card attribute
        :type fpga_card: str (optional)

        :param card_count: card_count attribute
        :type card_count: str (optional)

        :param isomerism_card: 是否为异构计算卡（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type isomerism_card: str (optional)

        :param npu_video_memory: npu显存大小（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type npu_video_memory: str (optional)

        :param memory_capacity_in_gb: 内存容量，单位为GB（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type memory_capacity_in_gb: int (optional)

        :param local_disk_size_in_gb: local_disk_size_in_gb attribute
        :type local_disk_size_in_gb: int (optional)

        :param image_id: 镜像ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type image_id: str (optional)

        :param image_type: 镜像类型（查询实例列表、查询指定实例详情）
        :type image_type: str (optional)

        :param image_name: 镜像名称（查询实例列表、查询指定实例详情）
        :type image_name: str (optional)

        :param os_version: 操作系统版本（查询实例列表、查询指定实例详情）
        :type os_version: str (optional)

        :param os_arch: 操作系统架构（查询实例列表、查询指定实例详情）
        :type os_arch: str (optional)

        :param os_name: 操作系统名称（查询实例列表、查询指定实例详情）
        :type os_name: str (optional)

        :param placement_policy: placement_policy attribute
        :type placement_policy: str (optional)

        :param subnet_id: 子网ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type subnet_id: str (optional)

        :param vpc_id: VPC ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type vpc_id: str (optional)

        :param is_eip_auto_related_delete: 实例绑定的EIP是否随抢占实例关联自动释放，是：true，否：false（查询实例列表、查询指定实例详情）
        :type is_eip_auto_related_delete: bool (optional)

        :param ehc_cluster_id: 实例所在ehc集群id（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type ehc_cluster_id: str (optional)

        :param deployset_id: 部署集ID（查询指定实例详情、根据实例id查询实例列表）
        :type deployset_id: str (optional)

        :param zone_name: 可用区信息（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type zone_name: str (optional)

        :param flavor_sub_type: 实例规格子类型（查询实例列表、查询指定实例详情）
        :type flavor_sub_type: str (optional)

        :param product_category: 产品类别（查询实例列表、查询指定实例详情）
        :type product_category: str (optional)

        :param repair_status: repair_status attribute
        :type repair_status: str (optional)

        :param host_id: 宿主机ID（查询指定实例详情、根据实例id查询实例列表）
        :type host_id: str (optional)

        :param switch_id: 交换机ID（查询指定实例详情、根据实例id查询实例列表）
        :type switch_id: str (optional)

        :param rack_id: 机架ID（查询指定实例详情、根据实例id查询实例列表）
        :type rack_id: str (optional)

        :param dedicated_host_id: 专属服务器ID（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type dedicated_host_id: str (optional)

        :param auto_renew: auto_renew attribute
        :type auto_renew: bool (optional)

        :param auto_renew_period_unit: 自动续费周期单位（查询实例列表、查询指定实例详情）
        :type auto_renew_period_unit: str (optional)

        :param auto_renew_period: 自动续费周期（查询实例列表、查询指定实例详情）
        :type auto_renew_period: int (optional)

        :param ipv6: ipv6地址（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type ipv6: str (optional)

        :param net_eth_queue_count: 网卡队列数（查询实例列表、查询指定实例详情）
        :type net_eth_queue_count: str (optional)

        :param eni_quota: 弹性网卡配额（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type eni_quota: int (optional)

        :param eri_quota: 弹性RDMA接口配额（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type eri_quota: int (optional)

        :param rdma_type: RDMA类型（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type rdma_type: str (optional)

        :param service_components: 服务组件，Map<组件名称,组件状态>（查询实例列表、查询指定实例详情、根据实例id查询实例列表）
        :type service_components: Dict[str, str] (optional)

        :param ipv6_addresses: IPv6地址信息（查询实例列表、查询指定实例详情）
        :type ipv6_addresses: List[str] (optional)

        :param nic_info: nic_info attribute
        :type nic_info: NicInfo (optional)

        :param eni_num: 弹性网卡的数量（查询实例列表、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type eni_num: str (optional)

        :param tags: 标签信息（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type tags: List[Tag] (optional)

        :param volumes: 磁盘信息（查询实例列表、查询指定实例详情）
        :type volumes: List[VolumeModel] (optional)

        :param network_capacity_in_mbps: 公网带宽，单位为Mb（查询实例列表、查询指定实例详情、根据实例id查询实例列表、查询可关机不计费的实例列表）
        :type network_capacity_in_mbps: int (optional)
        """
        super().__init__()
        self.id = id
        self.source_product_id = source_product_id
        self.source_product_type = source_product_type
        self.serial_number = serial_number
        self.keypair_id = keypair_id
        self.keypair_name = keypair_name
        self.name = name
        self.role_name = role_name
        self.hostname = hostname
        self.instance_type = instance_type
        self.spec = spec
        self.enable_jumbo_frame = enable_jumbo_frame
        self.status = status
        self.desc = desc
        self.created_from = created_from
        self.payment_timing = payment_timing
        self.charge_status = charge_status
        self.display_charge_status = display_charge_status
        self.create_time = create_time
        self.expire_time = expire_time
        self.release_time = release_time
        self.internal_ip = internal_ip
        self.public_ip = public_ip
        self.cpu_count = cpu_count
        self.rdma_unit_id = rdma_unit_id
        self.rdma_pod_name = rdma_pod_name
        self.deletion_protection = deletion_protection
        self.rdma_nic_topo = rdma_nic_topo
        self.deployset_list = deployset_list
        self.res_group_infos = res_group_infos
        self.hosteye_type = hosteye_type
        self.gpu_card = gpu_card
        self.gpu_video_memory = gpu_video_memory
        self.fpga_card = fpga_card
        self.card_count = card_count
        self.isomerism_card = isomerism_card
        self.npu_video_memory = npu_video_memory
        self.memory_capacity_in_gb = memory_capacity_in_gb
        self.local_disk_size_in_gb = local_disk_size_in_gb
        self.image_id = image_id
        self.image_type = image_type
        self.image_name = image_name
        self.os_version = os_version
        self.os_arch = os_arch
        self.os_name = os_name
        self.placement_policy = placement_policy
        self.subnet_id = subnet_id
        self.vpc_id = vpc_id
        self.is_eip_auto_related_delete = is_eip_auto_related_delete
        self.ehc_cluster_id = ehc_cluster_id
        self.deployset_id = deployset_id
        self.zone_name = zone_name
        self.flavor_sub_type = flavor_sub_type
        self.product_category = product_category
        self.repair_status = repair_status
        self.host_id = host_id
        self.switch_id = switch_id
        self.rack_id = rack_id
        self.dedicated_host_id = dedicated_host_id
        self.auto_renew = auto_renew
        self.auto_renew_period_unit = auto_renew_period_unit
        self.auto_renew_period = auto_renew_period
        self.ipv6 = ipv6
        self.net_eth_queue_count = net_eth_queue_count
        self.eni_quota = eni_quota
        self.eri_quota = eri_quota
        self.rdma_type = rdma_type
        self.service_components = service_components
        self.ipv6_addresses = ipv6_addresses
        self.nic_info = nic_info
        self.eni_num = eni_num
        self.tags = tags
        self.volumes = volumes
        self.network_capacity_in_mbps = network_capacity_in_mbps

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
        if self.id is not None:
            result['id'] = self.id
        if self.source_product_id is not None:
            result['sourceProductId'] = self.source_product_id
        if self.source_product_type is not None:
            result['sourceProductType'] = self.source_product_type
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.keypair_id is not None:
            result['keypairId'] = self.keypair_id
        if self.keypair_name is not None:
            result['keypairName'] = self.keypair_name
        if self.name is not None:
            result['name'] = self.name
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.spec is not None:
            result['spec'] = self.spec
        if self.enable_jumbo_frame is not None:
            result['enableJumboFrame'] = self.enable_jumbo_frame
        if self.status is not None:
            result['status'] = self.status
        if self.desc is not None:
            result['desc'] = self.desc
        if self.created_from is not None:
            result['createdFrom'] = self.created_from
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.charge_status is not None:
            result['chargeStatus'] = self.charge_status
        if self.display_charge_status is not None:
            result['displayChargeStatus'] = self.display_charge_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        if self.internal_ip is not None:
            result['internalIp'] = self.internal_ip
        if self.public_ip is not None:
            result['publicIp'] = self.public_ip
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.rdma_unit_id is not None:
            result['rdmaUnitID'] = self.rdma_unit_id
        if self.rdma_pod_name is not None:
            result['rdmaPodName'] = self.rdma_pod_name
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.rdma_nic_topo is not None:
            result['rdmaNicTopo'] = [i.to_dict() for i in self.rdma_nic_topo]
        if self.deployset_list is not None:
            result['deploysetList'] = [i.to_dict() for i in self.deployset_list]
        if self.res_group_infos is not None:
            result['resGroupInfos'] = [i.to_dict() for i in self.res_group_infos]
        if self.hosteye_type is not None:
            result['hosteyeType'] = self.hosteye_type
        if self.gpu_card is not None:
            result['gpuCard'] = self.gpu_card
        if self.gpu_video_memory is not None:
            result['gpuVideoMemory'] = self.gpu_video_memory
        if self.fpga_card is not None:
            result['fpgaCard'] = self.fpga_card
        if self.card_count is not None:
            result['cardCount'] = self.card_count
        if self.isomerism_card is not None:
            result['isomerismCard'] = self.isomerism_card
        if self.npu_video_memory is not None:
            result['npuVideoMemory'] = self.npu_video_memory
        if self.memory_capacity_in_gb is not None:
            result['memoryCapacityInGB'] = self.memory_capacity_in_gb
        if self.local_disk_size_in_gb is not None:
            result['localDiskSizeInGB'] = self.local_disk_size_in_gb
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.image_type is not None:
            result['imageType'] = self.image_type
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.os_arch is not None:
            result['osArch'] = self.os_arch
        if self.os_name is not None:
            result['osName'] = self.os_name
        if self.placement_policy is not None:
            result['placementPolicy'] = self.placement_policy
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.is_eip_auto_related_delete is not None:
            result['isEipAutoRelatedDelete'] = self.is_eip_auto_related_delete
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        if self.deployset_id is not None:
            result['deploysetId'] = self.deployset_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.flavor_sub_type is not None:
            result['flavorSubType'] = self.flavor_sub_type
        if self.product_category is not None:
            result['productCategory'] = self.product_category
        if self.repair_status is not None:
            result['repairStatus'] = self.repair_status
        if self.host_id is not None:
            result['hostId'] = self.host_id
        if self.switch_id is not None:
            result['switchId'] = self.switch_id
        if self.rack_id is not None:
            result['rackId'] = self.rack_id
        if self.dedicated_host_id is not None:
            result['dedicatedHostId'] = self.dedicated_host_id
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_period_unit is not None:
            result['autoRenewPeriodUnit'] = self.auto_renew_period_unit
        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period
        if self.ipv6 is not None:
            result['ipv6'] = self.ipv6
        if self.net_eth_queue_count is not None:
            result['netEthQueueCount'] = self.net_eth_queue_count
        if self.eni_quota is not None:
            result['eniQuota'] = self.eni_quota
        if self.eri_quota is not None:
            result['eriQuota'] = self.eri_quota
        if self.rdma_type is not None:
            result['rdmaType'] = self.rdma_type
        if self.service_components is not None:
            result['serviceComponents'] = self.service_components
        if self.ipv6_addresses is not None:
            result['ipv6Addresses'] = self.ipv6_addresses
        if self.nic_info is not None:
            result['nicInfo'] = self.nic_info.to_dict()
        if self.eni_num is not None:
            result['eniNum'] = self.eni_num
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.volumes is not None:
            result['volumes'] = [i.to_dict() for i in self.volumes]
        if self.network_capacity_in_mbps is not None:
            result['networkCapacityInMbps'] = self.network_capacity_in_mbps
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('sourceProductId') is not None:
            self.source_product_id = m.get('sourceProductId')
        if m.get('sourceProductType') is not None:
            self.source_product_type = m.get('sourceProductType')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('keypairId') is not None:
            self.keypair_id = m.get('keypairId')
        if m.get('keypairName') is not None:
            self.keypair_name = m.get('keypairName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('enableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('enableJumboFrame')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('createdFrom') is not None:
            self.created_from = m.get('createdFrom')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('chargeStatus') is not None:
            self.charge_status = m.get('chargeStatus')
        if m.get('displayChargeStatus') is not None:
            self.display_charge_status = m.get('displayChargeStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        if m.get('internalIp') is not None:
            self.internal_ip = m.get('internalIp')
        if m.get('publicIp') is not None:
            self.public_ip = m.get('publicIp')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('rdmaUnitID') is not None:
            self.rdma_unit_id = m.get('rdmaUnitID')
        if m.get('rdmaPodName') is not None:
            self.rdma_pod_name = m.get('rdmaPodName')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('rdmaNicTopo') is not None:
            self.rdma_nic_topo = [RdmaNicTopo().from_dict(i) for i in m.get('rdmaNicTopo')]
        if m.get('deploysetList') is not None:
            self.deployset_list = [DeploySetModel().from_dict(i) for i in m.get('deploysetList')]
        if m.get('resGroupInfos') is not None:
            self.res_group_infos = [GroupInfo().from_dict(i) for i in m.get('resGroupInfos')]
        if m.get('hosteyeType') is not None:
            self.hosteye_type = m.get('hosteyeType')
        if m.get('gpuCard') is not None:
            self.gpu_card = m.get('gpuCard')
        if m.get('gpuVideoMemory') is not None:
            self.gpu_video_memory = m.get('gpuVideoMemory')
        if m.get('fpgaCard') is not None:
            self.fpga_card = m.get('fpgaCard')
        if m.get('cardCount') is not None:
            self.card_count = m.get('cardCount')
        if m.get('isomerismCard') is not None:
            self.isomerism_card = m.get('isomerismCard')
        if m.get('npuVideoMemory') is not None:
            self.npu_video_memory = m.get('npuVideoMemory')
        if m.get('memoryCapacityInGB') is not None:
            self.memory_capacity_in_gb = m.get('memoryCapacityInGB')
        if m.get('localDiskSizeInGB') is not None:
            self.local_disk_size_in_gb = m.get('localDiskSizeInGB')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('imageType') is not None:
            self.image_type = m.get('imageType')
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('osArch') is not None:
            self.os_arch = m.get('osArch')
        if m.get('osName') is not None:
            self.os_name = m.get('osName')
        if m.get('placementPolicy') is not None:
            self.placement_policy = m.get('placementPolicy')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('isEipAutoRelatedDelete') is not None:
            self.is_eip_auto_related_delete = m.get('isEipAutoRelatedDelete')
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        if m.get('deploysetId') is not None:
            self.deployset_id = m.get('deploysetId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('flavorSubType') is not None:
            self.flavor_sub_type = m.get('flavorSubType')
        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')
        if m.get('repairStatus') is not None:
            self.repair_status = m.get('repairStatus')
        if m.get('hostId') is not None:
            self.host_id = m.get('hostId')
        if m.get('switchId') is not None:
            self.switch_id = m.get('switchId')
        if m.get('rackId') is not None:
            self.rack_id = m.get('rackId')
        if m.get('dedicatedHostId') is not None:
            self.dedicated_host_id = m.get('dedicatedHostId')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriodUnit') is not None:
            self.auto_renew_period_unit = m.get('autoRenewPeriodUnit')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        if m.get('ipv6') is not None:
            self.ipv6 = m.get('ipv6')
        if m.get('netEthQueueCount') is not None:
            self.net_eth_queue_count = m.get('netEthQueueCount')
        if m.get('eniQuota') is not None:
            self.eni_quota = m.get('eniQuota')
        if m.get('eriQuota') is not None:
            self.eri_quota = m.get('eriQuota')
        if m.get('rdmaType') is not None:
            self.rdma_type = m.get('rdmaType')
        if m.get('serviceComponents') is not None:
            self.service_components = m.get('serviceComponents')
        if m.get('ipv6Addresses') is not None:
            self.ipv6_addresses = m.get('ipv6Addresses')
        if m.get('nicInfo') is not None:
            self.nic_info = NicInfo().from_dict(m.get('nicInfo'))
        if m.get('eniNum') is not None:
            self.eni_num = m.get('eniNum')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('volumes') is not None:
            self.volumes = [VolumeModel().from_dict(i) for i in m.get('volumes')]
        if m.get('networkCapacityInMbps') is not None:
            self.network_capacity_in_mbps = m.get('networkCapacityInMbps')
        return self
