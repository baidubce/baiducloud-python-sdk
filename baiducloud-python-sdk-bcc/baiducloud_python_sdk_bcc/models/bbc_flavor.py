"""
BbcFlavor information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BbcFlavor(AbstractModel):
    """
    BbcFlavor
    """

    def __init__(
        self,
        cpu_count=None,
        memory_capacity_in_gb=None,
        ephemeral_disk_count=None,
        ephemeral_disk_type=None,
        gpu_card_count=None,
        fpga_card_type=None,
        fpga_card_count=None,
        product_type=None,
        spec=None,
        spec_id=None,
        enable_jumbo_frame=None,
        cpu_model=None,
        cpu_ghz=None,
        network_bandwidth=None,
        network_package=None,
        net_eth_queue_count=None,
        net_eth_max_queue_count=None,
        eni_quota=None,
        eri_quota=None,
        rdma_type=None,
        rdma_net_card_count=None,
        rdma_net_bandwidth=None,
        system_disk_type=None,
        data_disk_type=None,
        nic_ipv4_quota=None,
        nic_ipv6_quota=None,
        volume_count=None,
        gpu_card_type=None,
    ):
        """
        Initialize BbcFlavor instance.

        :param cpu_count: cpu数量
        :type cpu_count: int (optional)

        :param memory_capacity_in_gb: 内存容量（单位：GB）
        :type memory_capacity_in_gb: int (optional)

        :param ephemeral_disk_count: 本地数据盘数量
        :type ephemeral_disk_count: str (optional)

        :param ephemeral_disk_type: 本地数据盘类型
        :type ephemeral_disk_type: str (optional)

        :param gpu_card_count: gpu卡数量
        :type gpu_card_count: str (optional)

        :param fpga_card_type: fpga卡类型
        :type fpga_card_type: str (optional)

        :param fpga_card_count: fpga卡数量
        :type fpga_card_count: str (optional)

        :param product_type: 支持计费类型（PrePaid：包年包月；PostPaid：按量付费；both：包年包月/按量付费）
        :type product_type: str (optional)

        :param spec: 实例套餐规格
        :type spec: str (optional)

        :param spec_id: 实例套餐规格类型
        :type spec_id: str (optional)

        :param enable_jumbo_frame: 实例套餐是否支持开启Jumbo帧，开启:true，关闭:false
        :type enable_jumbo_frame: bool (optional)

        :param cpu_model: 处理器型号
        :type cpu_model: str (optional)

        :param cpu_ghz: 处理器主频
        :type cpu_ghz: str (optional)

        :param network_bandwidth: 内网带宽(Gbps)
        :type network_bandwidth: str (optional)

        :param network_package: 网络收发包
        :type network_package: str (optional)

        :param net_eth_queue_count: 套餐网卡队列数
        :type net_eth_queue_count: str (optional)

        :param net_eth_max_queue_count: 套餐网卡最大支持的队列数
        :type net_eth_max_queue_count: str (optional)

        :param eni_quota: ENI最大数量（配额）
        :type eni_quota: int (optional)

        :param eri_quota: ERI最大数量（配额）
        :type eri_quota: int (optional)

        :param rdma_type: rdma类型，RoCE或IB
        :type rdma_type: str (optional)

        :param rdma_net_card_count: rdma网卡数量
        :type rdma_net_card_count: int (optional)

        :param rdma_net_bandwidth: rdma网卡带宽(Gbps)
        :type rdma_net_bandwidth: int (optional)

        :param system_disk_type: system_disk_type attribute
        :type system_disk_type: List[str] (optional)

        :param data_disk_type: data_disk_type attribute
        :type data_disk_type: List[str] (optional)

        :param nic_ipv4_quota: 单网卡IPv4地址数量（配额）
        :type nic_ipv4_quota: int (optional)

        :param nic_ipv6_quota: 单网卡IPv6地址数量（配额）
        :type nic_ipv6_quota: int (optional)

        :param volume_count: CDS数量
        :type volume_count: int (optional)

        :param gpu_card_type: gpu卡类型
        :type gpu_card_type: str (optional)
        """
        super().__init__()
        self.cpu_count = cpu_count
        self.memory_capacity_in_gb = memory_capacity_in_gb
        self.ephemeral_disk_count = ephemeral_disk_count
        self.ephemeral_disk_type = ephemeral_disk_type
        self.gpu_card_count = gpu_card_count
        self.fpga_card_type = fpga_card_type
        self.fpga_card_count = fpga_card_count
        self.product_type = product_type
        self.spec = spec
        self.spec_id = spec_id
        self.enable_jumbo_frame = enable_jumbo_frame
        self.cpu_model = cpu_model
        self.cpu_ghz = cpu_ghz
        self.network_bandwidth = network_bandwidth
        self.network_package = network_package
        self.net_eth_queue_count = net_eth_queue_count
        self.net_eth_max_queue_count = net_eth_max_queue_count
        self.eni_quota = eni_quota
        self.eri_quota = eri_quota
        self.rdma_type = rdma_type
        self.rdma_net_card_count = rdma_net_card_count
        self.rdma_net_bandwidth = rdma_net_bandwidth
        self.system_disk_type = system_disk_type
        self.data_disk_type = data_disk_type
        self.nic_ipv4_quota = nic_ipv4_quota
        self.nic_ipv6_quota = nic_ipv6_quota
        self.volume_count = volume_count
        self.gpu_card_type = gpu_card_type

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
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.memory_capacity_in_gb is not None:
            result['memoryCapacityInGB'] = self.memory_capacity_in_gb
        if self.ephemeral_disk_count is not None:
            result['ephemeralDiskCount'] = self.ephemeral_disk_count
        if self.ephemeral_disk_type is not None:
            result['ephemeralDiskType'] = self.ephemeral_disk_type
        if self.gpu_card_count is not None:
            result['gpuCardCount'] = self.gpu_card_count
        if self.fpga_card_type is not None:
            result['fpgaCardType'] = self.fpga_card_type
        if self.fpga_card_count is not None:
            result['fpgaCardCount'] = self.fpga_card_count
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.spec is not None:
            result['spec'] = self.spec
        if self.spec_id is not None:
            result['specId'] = self.spec_id
        if self.enable_jumbo_frame is not None:
            result['enableJumboFrame'] = self.enable_jumbo_frame
        if self.cpu_model is not None:
            result['cpuModel'] = self.cpu_model
        if self.cpu_ghz is not None:
            result['cpuGHz'] = self.cpu_ghz
        if self.network_bandwidth is not None:
            result['networkBandwidth'] = self.network_bandwidth
        if self.network_package is not None:
            result['networkPackage'] = self.network_package
        if self.net_eth_queue_count is not None:
            result['netEthQueueCount'] = self.net_eth_queue_count
        if self.net_eth_max_queue_count is not None:
            result['netEthMaxQueueCount'] = self.net_eth_max_queue_count
        if self.eni_quota is not None:
            result['eniQuota'] = self.eni_quota
        if self.eri_quota is not None:
            result['eriQuota'] = self.eri_quota
        if self.rdma_type is not None:
            result['rdmaType'] = self.rdma_type
        if self.rdma_net_card_count is not None:
            result['rdmaNetCardCount'] = self.rdma_net_card_count
        if self.rdma_net_bandwidth is not None:
            result['rdmaNetBandwidth'] = self.rdma_net_bandwidth
        if self.system_disk_type is not None:
            result['systemDiskType'] = self.system_disk_type
        if self.data_disk_type is not None:
            result['dataDiskType'] = self.data_disk_type
        if self.nic_ipv4_quota is not None:
            result['nicIpv4Quota'] = self.nic_ipv4_quota
        if self.nic_ipv6_quota is not None:
            result['nicIpv6Quota'] = self.nic_ipv6_quota
        if self.volume_count is not None:
            result['volumeCount'] = self.volume_count
        if self.gpu_card_type is not None:
            result['gpuCardType'] = self.gpu_card_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BbcFlavor

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('memoryCapacityInGB') is not None:
            self.memory_capacity_in_gb = m.get('memoryCapacityInGB')
        if m.get('ephemeralDiskCount') is not None:
            self.ephemeral_disk_count = m.get('ephemeralDiskCount')
        if m.get('ephemeralDiskType') is not None:
            self.ephemeral_disk_type = m.get('ephemeralDiskType')
        if m.get('gpuCardCount') is not None:
            self.gpu_card_count = m.get('gpuCardCount')
        if m.get('fpgaCardType') is not None:
            self.fpga_card_type = m.get('fpgaCardType')
        if m.get('fpgaCardCount') is not None:
            self.fpga_card_count = m.get('fpgaCardCount')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('specId') is not None:
            self.spec_id = m.get('specId')
        if m.get('enableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('enableJumboFrame')
        if m.get('cpuModel') is not None:
            self.cpu_model = m.get('cpuModel')
        if m.get('cpuGHz') is not None:
            self.cpu_ghz = m.get('cpuGHz')
        if m.get('networkBandwidth') is not None:
            self.network_bandwidth = m.get('networkBandwidth')
        if m.get('networkPackage') is not None:
            self.network_package = m.get('networkPackage')
        if m.get('netEthQueueCount') is not None:
            self.net_eth_queue_count = m.get('netEthQueueCount')
        if m.get('netEthMaxQueueCount') is not None:
            self.net_eth_max_queue_count = m.get('netEthMaxQueueCount')
        if m.get('eniQuota') is not None:
            self.eni_quota = m.get('eniQuota')
        if m.get('eriQuota') is not None:
            self.eri_quota = m.get('eriQuota')
        if m.get('rdmaType') is not None:
            self.rdma_type = m.get('rdmaType')
        if m.get('rdmaNetCardCount') is not None:
            self.rdma_net_card_count = m.get('rdmaNetCardCount')
        if m.get('rdmaNetBandwidth') is not None:
            self.rdma_net_bandwidth = m.get('rdmaNetBandwidth')
        if m.get('systemDiskType') is not None:
            self.system_disk_type = m.get('systemDiskType')
        if m.get('dataDiskType') is not None:
            self.data_disk_type = m.get('dataDiskType')
        if m.get('nicIpv4Quota') is not None:
            self.nic_ipv4_quota = m.get('nicIpv4Quota')
        if m.get('nicIpv6Quota') is not None:
            self.nic_ipv6_quota = m.get('nicIpv6Quota')
        if m.get('volumeCount') is not None:
            self.volume_count = m.get('volumeCount')
        if m.get('gpuCardType') is not None:
            self.gpu_card_type = m.get('gpuCardType')
        return self
