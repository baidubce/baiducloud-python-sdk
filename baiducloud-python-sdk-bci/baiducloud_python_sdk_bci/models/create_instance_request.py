"""
Request entity for CreateInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bci.models.tag import Tag
from baiducloud_python_sdk_bci.models.image_registry_credential import ImageRegistryCredential
from baiducloud_python_sdk_bci.models.container import Container
from baiducloud_python_sdk_bci.models.container import Container
from baiducloud_python_sdk_bci.models.volume import Volume


class CreateInstanceRequest(AbstractModel):
    """
    Request entity for CreateInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        security_group_ids,
        subnet_ids,
        containers,
        volume,
        client_token=None,
        zone_name=None,
        restart_policy=None,
        eip_ip=None,
        auto_create_eip=None,
        eip_name=None,
        eip_route_type=None,
        eip_bandwidth_in_mbps=None,
        eip_billing_method=None,
        gpu_type=None,
        termination_grace_period_seconds=None,
        host_name=None,
        tags=None,
        image_registry_credentials=None,
        init_containers=None,
    ):
        """
        Initialize CreateInstanceRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: BCI实例名称（容器组名称），长度2-252，由字母数字、\"-\"或\".\"组成，必须以字母数字开头和结尾
        :type name: str (required)

        :param zone_name: 可用区名称
        :type zone_name: str (optional)

        :param security_group_ids: 安全组ID，所有安全组、子网应属于同一VPC，上限10
        :type security_group_ids: List[str] (required)

        :param subnet_ids: 子网ID，属于同一VPC，不可重复，上限10
        :type subnet_ids: List[str] (required)

        :param restart_policy: 重启策略：Always（默认）、Never、OnFailure
        :type restart_policy: str (optional)

        :param eip_ip: 弹性公网IP
        :type eip_ip: str (optional)

        :param auto_create_eip: 是否自动创建EIP并绑定，仅eipIp为空时生效，默认false
        :type auto_create_eip: bool (optional)

        :param eip_name: 弹性公网名称，autoCreateEip为true时生效，默认\"eip\"
        :type eip_name: str (optional)

        :param eip_route_type: EIP线路类型：BGP（标准）或BGP_S（增强），默认BGP
        :type eip_route_type: str (optional)

        :param eip_bandwidth_in_mbps: 公网带宽(Mbps)，标准BGP 1-500，增强BGP 100-5000，按流量计费标准BGP 1-200，默认100
        :type eip_bandwidth_in_mbps: int (optional)

        :param eip_billing_method: 计费方式：ByTraffic（按流量，默认）、ByBandwidth（按带宽）、ByPeak95（按增强95）
        :type eip_billing_method: str (optional)

        :param gpu_type: GPU资源型号，目前仅支持Nvidia A10 PCIE
        :type gpu_type: str (optional)

        :param termination_grace_period_seconds: 程序缓冲时间，用于关闭前操作
        :type termination_grace_period_seconds: int (optional)

        :param host_name: 主机名称
        :type host_name: str (optional)

        :param tags: 用户标签列表
        :type tags: List[Tag] (optional)

        :param image_registry_credentials: 镜像仓库凭证信息
        :type image_registry_credentials: List[ImageRegistryCredential] (optional)

        :param containers: 业务容器组
        :type containers: List[Container] (required)

        :param init_containers: Init容器
        :type init_containers: List[Container] (optional)

        :param volume: volume parameter
        :type volume: Volume (required)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.zone_name = zone_name
        self.security_group_ids = security_group_ids
        self.subnet_ids = subnet_ids
        self.restart_policy = restart_policy
        self.eip_ip = eip_ip
        self.auto_create_eip = auto_create_eip
        self.eip_name = eip_name
        self.eip_route_type = eip_route_type
        self.eip_bandwidth_in_mbps = eip_bandwidth_in_mbps
        self.eip_billing_method = eip_billing_method
        self.gpu_type = gpu_type
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.host_name = host_name
        self.tags = tags
        self.image_registry_credentials = image_registry_credentials
        self.containers = containers
        self.init_containers = init_containers
        self.volume = volume

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
        if self.name is not None:
            result['name'] = self.name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.subnet_ids is not None:
            result['subnetIds'] = self.subnet_ids
        if self.restart_policy is not None:
            result['restartPolicy'] = self.restart_policy
        if self.eip_ip is not None:
            result['eipIp'] = self.eip_ip
        if self.auto_create_eip is not None:
            result['autoCreateEip'] = self.auto_create_eip
        if self.eip_name is not None:
            result['eipName'] = self.eip_name
        if self.eip_route_type is not None:
            result['eipRouteType'] = self.eip_route_type
        if self.eip_bandwidth_in_mbps is not None:
            result['eipBandwidthInMbps'] = self.eip_bandwidth_in_mbps
        if self.eip_billing_method is not None:
            result['eipBillingMethod'] = self.eip_billing_method
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        if self.termination_grace_period_seconds is not None:
            result['terminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.image_registry_credentials is not None:
            result['imageRegistryCredentials'] = [i.to_dict() for i in self.image_registry_credentials]
        if self.containers is not None:
            result['containers'] = [i.to_dict() for i in self.containers]
        if self.init_containers is not None:
            result['initContainers'] = [i.to_dict() for i in self.init_containers]
        if self.volume is not None:
            result['volume'] = self.volume.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('subnetIds') is not None:
            self.subnet_ids = m.get('subnetIds')
        if m.get('restartPolicy') is not None:
            self.restart_policy = m.get('restartPolicy')
        if m.get('eipIp') is not None:
            self.eip_ip = m.get('eipIp')
        if m.get('autoCreateEip') is not None:
            self.auto_create_eip = m.get('autoCreateEip')
        if m.get('eipName') is not None:
            self.eip_name = m.get('eipName')
        if m.get('eipRouteType') is not None:
            self.eip_route_type = m.get('eipRouteType')
        if m.get('eipBandwidthInMbps') is not None:
            self.eip_bandwidth_in_mbps = m.get('eipBandwidthInMbps')
        if m.get('eipBillingMethod') is not None:
            self.eip_billing_method = m.get('eipBillingMethod')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        if m.get('terminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('terminationGracePeriodSeconds')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('imageRegistryCredentials') is not None:
            self.image_registry_credentials = [
                ImageRegistryCredential().from_dict(i) for i in m.get('imageRegistryCredentials')
            ]
        if m.get('containers') is not None:
            self.containers = [Container().from_dict(i) for i in m.get('containers')]
        if m.get('initContainers') is not None:
            self.init_containers = [Container().from_dict(i) for i in m.get('initContainers')]
        if m.get('volume') is not None:
            self.volume = Volume().from_dict(m.get('volume'))
        return self
