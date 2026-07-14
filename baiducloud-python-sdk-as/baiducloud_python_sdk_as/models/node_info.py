"""
NodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.billing_info import BillingInfo

from baiducloud_python_sdk_as.models.ephemeral_disk import EphemeralDisk

from baiducloud_python_sdk_as.models.cds_info import CdsInfo


class NodeInfo(AbstractModel):
    """
    NodeInfo
    """

    def __init__(
        self,
        spec=None,
        cpu_count=None,
        memory_capacity_in_gb=None,
        sys_disk_type=None,
        sys_disk_in_gb=None,
        billing=None,
        bid_model=None,
        bid_price=None,
        ephemeral_disks=None,
        instance_type=None,
        gpu_card=None,
        gpu_count=None,
        fpga_card=None,
        fpga_count=None,
        contains_fpga=None,
        kunlun_card=None,
        kunlun_count=None,
        image_type=None,
        image_id=None,
        image_name=None,
        os_type=None,
        os_name=None,
        os_version=None,
        os_arch=None,
        security_group_id=None,
        admin_pass=None,
        admin_pass_type=None,
        security_group_name=None,
        total_count=None,
        asp_id=None,
        cds=None,
        zone_subnet=None,
        user_data=None,
        priorities=None,
        template_id=None,
    ):
        """
        Initialize NodeInfo instance.

        :param spec: 套餐规格
        :type spec: str (optional)

        :param cpu_count: CPU数量
        :type cpu_count: int (optional)

        :param memory_capacity_in_gb: 磁盘容量
        :type memory_capacity_in_gb: int (optional)

        :param sys_disk_type: 系统盘类型
        :type sys_disk_type: str (optional)

        :param sys_disk_in_gb: 系统盘大小
        :type sys_disk_in_gb: int (optional)

        :param billing: billing attribute
        :type billing: BillingInfo (optional)

        :param bid_model: 抢占式实例释放策略：市场价释放-market，自定义释放价格-custom
        :type bid_model: str (optional)

        :param bid_price: 自定义释放时，价格值
        :type bid_price: str (optional)

        :param ephemeral_disks: 本地盘信息
        :type ephemeral_disks: List[EphemeralDisk] (optional)

        :param instance_type: 实例类型
        :type instance_type: str (optional)

        :param gpu_card: gpu卡属性
        :type gpu_card: str (optional)

        :param gpu_count: gpu数量
        :type gpu_count: int (optional)

        :param fpga_card: fpga卡属性
        :type fpga_card: str (optional)

        :param fpga_count: fpga卡数量
        :type fpga_count: int (optional)

        :param contains_fpga: 是否包含fpga卡
        :type contains_fpga: bool (optional)

        :param kunlun_card: 昆仑卡属性
        :type kunlun_card: str (optional)

        :param kunlun_count: 昆仑卡数量
        :type kunlun_count: int (optional)

        :param image_type: 实例镜像类型
        :type image_type: str (optional)

        :param image_id: 实例镜像ID
        :type image_id: str (optional)

        :param image_name: 实例镜像名称
        :type image_name: str (optional)

        :param os_type: 操作系统类型
        :type os_type: str (optional)

        :param os_name: 操作系统名称
        :type os_name: str (optional)

        :param os_version: 操作系统版本
        :type os_version: str (optional)

        :param os_arch: 操作系统架构
        :type os_arch: str (optional)

        :param security_group_id: 安全组ID
        :type security_group_id: str (optional)

        :param admin_pass: 密码
        :type admin_pass: str (optional)

        :param admin_pass_type: 密码类型: \"0\"(随机); \"1\"(用户自定义)
        :type admin_pass_type: str (optional)

        :param security_group_name: 安全组名称
        :type security_group_name: str (optional)

        :param total_count: 总数量
        :type total_count: int (optional)

        :param asp_id: 子网类型
        :type asp_id: str (optional)

        :param cds: 本地存储信息
        :type cds: List[CdsInfo] (optional)

        :param zone_subnet: zone_subnet attribute
        :type zone_subnet: str (optional)

        :param user_data: 用户高级配置能力
        :type user_data: str (optional)

        :param priorities: 模板顺序
        :type priorities: int (optional)

        :param template_id: 所属模板的ID
        :type template_id: str (optional)
        """
        super().__init__()
        self.spec = spec
        self.cpu_count = cpu_count
        self.memory_capacity_in_gb = memory_capacity_in_gb
        self.sys_disk_type = sys_disk_type
        self.sys_disk_in_gb = sys_disk_in_gb
        self.billing = billing
        self.bid_model = bid_model
        self.bid_price = bid_price
        self.ephemeral_disks = ephemeral_disks
        self.instance_type = instance_type
        self.gpu_card = gpu_card
        self.gpu_count = gpu_count
        self.fpga_card = fpga_card
        self.fpga_count = fpga_count
        self.contains_fpga = contains_fpga
        self.kunlun_card = kunlun_card
        self.kunlun_count = kunlun_count
        self.image_type = image_type
        self.image_id = image_id
        self.image_name = image_name
        self.os_type = os_type
        self.os_name = os_name
        self.os_version = os_version
        self.os_arch = os_arch
        self.security_group_id = security_group_id
        self.admin_pass = admin_pass
        self.admin_pass_type = admin_pass_type
        self.security_group_name = security_group_name
        self.total_count = total_count
        self.asp_id = asp_id
        self.cds = cds
        self.zone_subnet = zone_subnet
        self.user_data = user_data
        self.priorities = priorities
        self.template_id = template_id

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
        if self.spec is not None:
            result['spec'] = self.spec
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.memory_capacity_in_gb is not None:
            result['memoryCapacityInGB'] = self.memory_capacity_in_gb
        if self.sys_disk_type is not None:
            result['sysDiskType'] = self.sys_disk_type
        if self.sys_disk_in_gb is not None:
            result['sysDiskInGB'] = self.sys_disk_in_gb
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.bid_model is not None:
            result['bidModel'] = self.bid_model
        if self.bid_price is not None:
            result['bidPrice'] = self.bid_price
        if self.ephemeral_disks is not None:
            result['ephemeralDisks'] = [i.to_dict() for i in self.ephemeral_disks]
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.gpu_card is not None:
            result['gpuCard'] = self.gpu_card
        if self.gpu_count is not None:
            result['gpuCount'] = self.gpu_count
        if self.fpga_card is not None:
            result['fpgaCard'] = self.fpga_card
        if self.fpga_count is not None:
            result['fpgaCount'] = self.fpga_count
        if self.contains_fpga is not None:
            result['containsFpga'] = self.contains_fpga
        if self.kunlun_card is not None:
            result['kunlunCard'] = self.kunlun_card
        if self.kunlun_count is not None:
            result['kunlunCount'] = self.kunlun_count
        if self.image_type is not None:
            result['imageType'] = self.image_type
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.os_name is not None:
            result['osName'] = self.os_name
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.os_arch is not None:
            result['osArch'] = self.os_arch
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.admin_pass is not None:
            result['adminPass'] = self.admin_pass
        if self.admin_pass_type is not None:
            result['adminPassType'] = self.admin_pass_type
        if self.security_group_name is not None:
            result['securityGroupName'] = self.security_group_name
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.asp_id is not None:
            result['aspId'] = self.asp_id
        if self.cds is not None:
            result['cds'] = [i.to_dict() for i in self.cds]
        if self.zone_subnet is not None:
            result['zoneSubnet'] = self.zone_subnet
        if self.user_data is not None:
            result['userData'] = self.user_data
        if self.priorities is not None:
            result['priorities'] = self.priorities
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('memoryCapacityInGB') is not None:
            self.memory_capacity_in_gb = m.get('memoryCapacityInGB')
        if m.get('sysDiskType') is not None:
            self.sys_disk_type = m.get('sysDiskType')
        if m.get('sysDiskInGB') is not None:
            self.sys_disk_in_gb = m.get('sysDiskInGB')
        if m.get('billing') is not None:
            self.billing = BillingInfo().from_dict(m.get('billing'))
        if m.get('bidModel') is not None:
            self.bid_model = m.get('bidModel')
        if m.get('bidPrice') is not None:
            self.bid_price = m.get('bidPrice')
        if m.get('ephemeralDisks') is not None:
            self.ephemeral_disks = [EphemeralDisk().from_dict(i) for i in m.get('ephemeralDisks')]
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('gpuCard') is not None:
            self.gpu_card = m.get('gpuCard')
        if m.get('gpuCount') is not None:
            self.gpu_count = m.get('gpuCount')
        if m.get('fpgaCard') is not None:
            self.fpga_card = m.get('fpgaCard')
        if m.get('fpgaCount') is not None:
            self.fpga_count = m.get('fpgaCount')
        if m.get('containsFpga') is not None:
            self.contains_fpga = m.get('containsFpga')
        if m.get('kunlunCard') is not None:
            self.kunlun_card = m.get('kunlunCard')
        if m.get('kunlunCount') is not None:
            self.kunlun_count = m.get('kunlunCount')
        if m.get('imageType') is not None:
            self.image_type = m.get('imageType')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('osName') is not None:
            self.os_name = m.get('osName')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('osArch') is not None:
            self.os_arch = m.get('osArch')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('adminPass') is not None:
            self.admin_pass = m.get('adminPass')
        if m.get('adminPassType') is not None:
            self.admin_pass_type = m.get('adminPassType')
        if m.get('securityGroupName') is not None:
            self.security_group_name = m.get('securityGroupName')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('aspId') is not None:
            self.asp_id = m.get('aspId')
        if m.get('cds') is not None:
            self.cds = [CdsInfo().from_dict(i) for i in m.get('cds')]
        if m.get('zoneSubnet') is not None:
            self.zone_subnet = m.get('zoneSubnet')
        if m.get('userData') is not None:
            self.user_data = m.get('userData')
        if m.get('priorities') is not None:
            self.priorities = m.get('priorities')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self
