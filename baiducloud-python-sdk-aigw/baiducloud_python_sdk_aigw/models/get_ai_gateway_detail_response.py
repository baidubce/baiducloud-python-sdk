"""
Request entity for GetAIGatewayDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_aigw.models.vpc_endpoint import VpcEndpoint
from baiducloud_python_sdk_aigw.models.tag import Tag
from baiducloud_python_sdk_aigw.models.aihc_args import AihcArgs


class GetAIGatewayDetailResponse(BceResponse):
    """
    GetAIGatewayDetailResponse
    """

    def __init__(
        self,
        instance_id=None,
        name=None,
        ingress_status=None,
        internal_ip=None,
        external_ip=None,
        create_time=None,
        region=None,
        replicas=None,
        install_mode=None,
        vpc_cidr=None,
        vpc_id=None,
        subnet_id=None,
        gateway_type=None,
        public_accessible=None,
        delete_protection=None,
        description=None,
        namespace=None,
        enable_ingress=None,
        enable_all_ingress_classes=None,
        enable_all_namespaces=None,
        ingress_classes=None,
        watch_namespaces=None,
        ba_endpoint=None,
        associated_cluster=None,
        src_product=None,
        blb_long_id=None,
        waf_id=None,
        waf_enable=None,
        private_domain_name=None,
        public_domain_name=None,
        network_type=None,
        domain_status=None,
        security_group_id=None,
        tags=None,
        version=None,
        aihc_args=None,
    ):
        """
        Initialize GetAIGatewayDetailResponse response.

        :param instance_id: 网关实例 ID
        :type instance_id: str (optional)

        :param name: 实例名称
        :type name: str (optional)

        :param ingress_status: 网关状态
        :type ingress_status: str (optional)

        :param internal_ip: 内网 IP
        :type internal_ip: str (optional)

        :param external_ip: 公网 IP
        :type external_ip: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param region: 地域
        :type region: str (optional)

        :param replicas: 副本数
        :type replicas: int (optional)

        :param install_mode: 部署模式
        :type install_mode: str (optional)

        :param vpc_cidr: VPC CIDR
        :type vpc_cidr: str (optional)

        :param vpc_id: VPC ID
        :type vpc_id: str (optional)

        :param subnet_id: 子网 ID
        :type subnet_id: str (optional)

        :param gateway_type: 网关规格
        :type gateway_type: str (optional)

        :param public_accessible: 是否公网可访问
        :type public_accessible: bool (optional)

        :param delete_protection: 是否开启删除保护
        :type delete_protection: bool (optional)

        :param description: 实例描述
        :type description: str (optional)

        :param namespace: 网关命名空间
        :type namespace: str (optional)

        :param enable_ingress: 是否开启 Ingress
        :type enable_ingress: bool (optional)

        :param enable_all_ingress_classes: 是否监听全部 IngressClass
        :type enable_all_ingress_classes: bool (optional)

        :param enable_all_namespaces: 是否监听全部命名空间
        :type enable_all_namespaces: bool (optional)

        :param ingress_classes: IngressClass 列表
        :type ingress_classes: List[str] (optional)

        :param watch_namespaces: 监听命名空间列表
        :type watch_namespaces: List[str] (optional)

        :param ba_endpoint: ba_endpoint field
        :type ba_endpoint: VpcEndpoint (optional)

        :param associated_cluster: 关联集群
        :type associated_cluster: str (optional)

        :param src_product: 来源产品
        :type src_product: str (optional)

        :param blb_long_id: BLB 长 ID
        :type blb_long_id: str (optional)

        :param waf_id: WAF ID
        :type waf_id: str (optional)

        :param waf_enable: WAF 是否开启
        :type waf_enable: bool (optional)

        :param private_domain_name: 默认私网域名
        :type private_domain_name: str (optional)

        :param public_domain_name: 默认公网域名
        :type public_domain_name: str (optional)

        :param network_type: 网络类型
        :type network_type: str (optional)

        :param domain_status: 域名状态
        :type domain_status: str (optional)

        :param security_group_id: 安全组 ID
        :type security_group_id: str (optional)

        :param tags: 实例标签
        :type tags: List[Tag] (optional)

        :param version: Higress 版本
        :type version: str (optional)

        :param aihc_args: aihc_args field
        :type aihc_args: AihcArgs (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.name = name
        self.ingress_status = ingress_status
        self.internal_ip = internal_ip
        self.external_ip = external_ip
        self.create_time = create_time
        self.region = region
        self.replicas = replicas
        self.install_mode = install_mode
        self.vpc_cidr = vpc_cidr
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.gateway_type = gateway_type
        self.public_accessible = public_accessible
        self.delete_protection = delete_protection
        self.description = description
        self.namespace = namespace
        self.enable_ingress = enable_ingress
        self.enable_all_ingress_classes = enable_all_ingress_classes
        self.enable_all_namespaces = enable_all_namespaces
        self.ingress_classes = ingress_classes
        self.watch_namespaces = watch_namespaces
        self.ba_endpoint = ba_endpoint
        self.associated_cluster = associated_cluster
        self.src_product = src_product
        self.blb_long_id = blb_long_id
        self.waf_id = waf_id
        self.waf_enable = waf_enable
        self.private_domain_name = private_domain_name
        self.public_domain_name = public_domain_name
        self.network_type = network_type
        self.domain_status = domain_status
        self.security_group_id = security_group_id
        self.tags = tags
        self.version = version
        self.aihc_args = aihc_args

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.name is not None:
            result['name'] = self.name
        if self.ingress_status is not None:
            result['ingressStatus'] = self.ingress_status
        if self.internal_ip is not None:
            result['internalIP'] = self.internal_ip
        if self.external_ip is not None:
            result['externalIP'] = self.external_ip
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.region is not None:
            result['region'] = self.region
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.install_mode is not None:
            result['installMode'] = self.install_mode
        if self.vpc_cidr is not None:
            result['vpcCidr'] = self.vpc_cidr
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.public_accessible is not None:
            result['publicAccessible'] = self.public_accessible
        if self.delete_protection is not None:
            result['deleteProtection'] = self.delete_protection
        if self.description is not None:
            result['description'] = self.description
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.enable_ingress is not None:
            result['enableIngress'] = self.enable_ingress
        if self.enable_all_ingress_classes is not None:
            result['enableAllIngressClasses'] = self.enable_all_ingress_classes
        if self.enable_all_namespaces is not None:
            result['enableAllNamespaces'] = self.enable_all_namespaces
        if self.ingress_classes is not None:
            result['ingressClasses'] = self.ingress_classes
        if self.watch_namespaces is not None:
            result['watchNamespaces'] = self.watch_namespaces
        if self.ba_endpoint is not None:
            result['baEndpoint'] = self.ba_endpoint.to_dict()
        if self.associated_cluster is not None:
            result['associatedCluster'] = self.associated_cluster
        if self.src_product is not None:
            result['srcProduct'] = self.src_product
        if self.blb_long_id is not None:
            result['blbLongId'] = self.blb_long_id
        if self.waf_id is not None:
            result['wafId'] = self.waf_id
        if self.waf_enable is not None:
            result['wafEnable'] = self.waf_enable
        if self.private_domain_name is not None:
            result['privateDomainName'] = self.private_domain_name
        if self.public_domain_name is not None:
            result['publicDomainName'] = self.public_domain_name
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.domain_status is not None:
            result['domainStatus'] = self.domain_status
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.version is not None:
            result['version'] = self.version
        if self.aihc_args is not None:
            result['aihcArgs'] = self.aihc_args.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetAIGatewayDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ingressStatus') is not None:
            self.ingress_status = m.get('ingressStatus')
        if m.get('internalIP') is not None:
            self.internal_ip = m.get('internalIP')
        if m.get('externalIP') is not None:
            self.external_ip = m.get('externalIP')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('installMode') is not None:
            self.install_mode = m.get('installMode')
        if m.get('vpcCidr') is not None:
            self.vpc_cidr = m.get('vpcCidr')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('publicAccessible') is not None:
            self.public_accessible = m.get('publicAccessible')
        if m.get('deleteProtection') is not None:
            self.delete_protection = m.get('deleteProtection')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('enableIngress') is not None:
            self.enable_ingress = m.get('enableIngress')
        if m.get('enableAllIngressClasses') is not None:
            self.enable_all_ingress_classes = m.get('enableAllIngressClasses')
        if m.get('enableAllNamespaces') is not None:
            self.enable_all_namespaces = m.get('enableAllNamespaces')
        if m.get('ingressClasses') is not None:
            self.ingress_classes = m.get('ingressClasses')
        if m.get('watchNamespaces') is not None:
            self.watch_namespaces = m.get('watchNamespaces')
        if m.get('baEndpoint') is not None:
            self.ba_endpoint = VpcEndpoint().from_dict(m.get('baEndpoint'))
        if m.get('associatedCluster') is not None:
            self.associated_cluster = m.get('associatedCluster')
        if m.get('srcProduct') is not None:
            self.src_product = m.get('srcProduct')
        if m.get('blbLongId') is not None:
            self.blb_long_id = m.get('blbLongId')
        if m.get('wafId') is not None:
            self.waf_id = m.get('wafId')
        if m.get('wafEnable') is not None:
            self.waf_enable = m.get('wafEnable')
        if m.get('privateDomainName') is not None:
            self.private_domain_name = m.get('privateDomainName')
        if m.get('publicDomainName') is not None:
            self.public_domain_name = m.get('publicDomainName')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('domainStatus') is not None:
            self.domain_status = m.get('domainStatus')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('aihcArgs') is not None:
            self.aihc_args = AihcArgs().from_dict(m.get('aihcArgs'))
        return self
