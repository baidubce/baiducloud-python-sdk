"""
Request entity for CreateAIGatewayRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aigw.models.cluster_info import ClusterInfo
from baiducloud_python_sdk_aigw.models.tag import Tag
from baiducloud_python_sdk_aigw.models.aihc_args import AihcArgs


class CreateAIGatewayRequest(AbstractModel):
    """
    Request entity for CreateAIGatewayRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        vpc_id,
        vpc_cidr,
        subnet_id,
        gateway_type,
        x_region,
        is_internal=None,
        network_types=None,
        replicas=None,
        install_mode=None,
        description=None,
        delete_protection=None,
        src_product=None,
        account_id=None,
        workspace_id=None,
        workspace_name=None,
        blb_id=None,
        blb_ip=None,
        clusters=None,
        cprom_instance_id=None,
        cprom_bearer_token=None,
        bls_enabled=None,
        log_store_name=None,
        version=None,
        tags=None,
        resource_group_id=None,
        aihc_args=None,
    ):
        """
        Initialize CreateAIGatewayRequest request entity.

        :param name: 网关实例名称
        :type name: str (required)

        :param vpc_id: VPC ID
        :type vpc_id: str (required)

        :param vpc_cidr: VPC CIDR
        :type vpc_cidr: str (required)

        :param subnet_id: 子网 ID
        :type subnet_id: str (required)

        :param gateway_type: 网关规格：small、medium、large
        :type gateway_type: str (required)

        :param is_internal: 是否使用内网模式
        :type is_internal: str (optional)

        :param network_types: 网络类型：private、public，可多选
        :type network_types: List[str] (optional)

        :param replicas: 副本数，默认共享模式 2、独占模式 3
        :type replicas: int (optional)

        :param install_mode: 部署模式：shared 或 exclusive，默认 shared
        :type install_mode: str (optional)

        :param description: 实例描述
        :type description: str (optional)

        :param delete_protection: 删除保护，默认 true
        :type delete_protection: bool (optional)

        :param src_product: 来源产品；不同来源有额外必填字段
        :type src_product: str (optional)

        :param account_id: AgentOS 来源时必填的账号 ID
        :type account_id: str (optional)

        :param workspace_id: AgentOS 工作空间 ID
        :type workspace_id: str (optional)

        :param workspace_name: AgentOS 工作空间名称
        :type workspace_name: str (optional)

        :param blb_id: CFC 来源时必填的 BLB 长 ID
        :type blb_id: str (optional)

        :param blb_ip: BLB IP
        :type blb_ip: str (optional)

        :param clusters: 关联 CCE 集群列表
        :type clusters: List[ClusterInfo] (optional)

        :param cprom_instance_id: CProm 实例 ID，用于开启业务指标监控
        :type cprom_instance_id: str (optional)

        :param cprom_bearer_token: CProm 访问 Token
        :type cprom_bearer_token: str (optional)

        :param bls_enabled: 是否开启 BLS 日志
        :type bls_enabled: bool (optional)

        :param log_store_name: BLS 日志仓库名称
        :type log_store_name: str (optional)

        :param version: Higress 版本，不传时使用默认版本
        :type version: str (optional)

        :param tags: 实例标签列表
        :type tags: List[Tag] (optional)

        :param resource_group_id: 资源分组 ID
        :type resource_group_id: str (optional)

        :param aihc_args: aihc_args parameter
        :type aihc_args: AihcArgs (optional)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.name = name
        self.vpc_id = vpc_id
        self.vpc_cidr = vpc_cidr
        self.subnet_id = subnet_id
        self.gateway_type = gateway_type
        self.is_internal = is_internal
        self.network_types = network_types
        self.replicas = replicas
        self.install_mode = install_mode
        self.description = description
        self.delete_protection = delete_protection
        self.src_product = src_product
        self.account_id = account_id
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name
        self.blb_id = blb_id
        self.blb_ip = blb_ip
        self.clusters = clusters
        self.cprom_instance_id = cprom_instance_id
        self.cprom_bearer_token = cprom_bearer_token
        self.bls_enabled = bls_enabled
        self.log_store_name = log_store_name
        self.version = version
        self.tags = tags
        self.resource_group_id = resource_group_id
        self.aihc_args = aihc_args
        self.x_region = x_region

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
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_cidr is not None:
            result['vpcCidr'] = self.vpc_cidr
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.is_internal is not None:
            result['isInternal'] = self.is_internal
        if self.network_types is not None:
            result['networkTypes'] = self.network_types
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.install_mode is not None:
            result['installMode'] = self.install_mode
        if self.description is not None:
            result['description'] = self.description
        if self.delete_protection is not None:
            result['deleteProtection'] = self.delete_protection
        if self.src_product is not None:
            result['srcProduct'] = self.src_product
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        if self.blb_id is not None:
            result['blbId'] = self.blb_id
        if self.blb_ip is not None:
            result['blbIp'] = self.blb_ip
        if self.clusters is not None:
            result['clusters'] = [i.to_dict() for i in self.clusters]
        if self.cprom_instance_id is not None:
            result['cpromInstanceId'] = self.cprom_instance_id
        if self.cprom_bearer_token is not None:
            result['cpromBearerToken'] = self.cprom_bearer_token
        if self.bls_enabled is not None:
            result['blsEnabled'] = self.bls_enabled
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.version is not None:
            result['version'] = self.version
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.aihc_args is not None:
            result['aihcArgs'] = self.aihc_args.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAIGatewayRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcCidr') is not None:
            self.vpc_cidr = m.get('vpcCidr')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('isInternal') is not None:
            self.is_internal = m.get('isInternal')
        if m.get('networkTypes') is not None:
            self.network_types = m.get('networkTypes')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('installMode') is not None:
            self.install_mode = m.get('installMode')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('deleteProtection') is not None:
            self.delete_protection = m.get('deleteProtection')
        if m.get('srcProduct') is not None:
            self.src_product = m.get('srcProduct')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('blbIp') is not None:
            self.blb_ip = m.get('blbIp')
        if m.get('clusters') is not None:
            self.clusters = [ClusterInfo().from_dict(i) for i in m.get('clusters')]
        if m.get('cpromInstanceId') is not None:
            self.cprom_instance_id = m.get('cpromInstanceId')
        if m.get('cpromBearerToken') is not None:
            self.cprom_bearer_token = m.get('cpromBearerToken')
        if m.get('blsEnabled') is not None:
            self.bls_enabled = m.get('blsEnabled')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('aihcArgs') is not None:
            self.aihc_args = AihcArgs().from_dict(m.get('aihcArgs'))
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
