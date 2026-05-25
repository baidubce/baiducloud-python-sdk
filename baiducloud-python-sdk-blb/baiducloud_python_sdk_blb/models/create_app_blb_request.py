"""
Request entity for CreateAppBlbRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.tag_model import TagModel
from baiducloud_python_sdk_blb.models.billing_for_create import BillingForCreate


class CreateAppBlbRequest(AbstractModel):
    """
    Request entity for CreateAppBlbRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        subnet_id,
        vpc_id,
        client_token=None,
        name=None,
        type=None,
        desc=None,
        address=None,
        eip=None,
        tags=None,
        billing=None,
        performance_level=None,
        auto_renew_length=None,
        auto_renew_time_unit=None,
        resource_group_id=None,
        allow_delete=None,
        allow_modify=None,
        modification_protection_reason=None,
        allocate_ipv6=None,
    ):
        """
        Initialize CreateAppBlbRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param type: LoaBalancer的类型，此处取值\"application\"(默认)
        :type type: str (optional)

        :param desc: LoadBalancer实例的描述，便于用户添加更详细的描述信息。长度0~450个字节，支持中文。默认为空
        :type desc: str (optional)

        :param subnet_id: LoadBalancer实例所属子网
        :type subnet_id: str (required)

        :param vpc_id: LoadBalancer实例vip所属VPC的vpcShortId
        :type vpc_id: str (required)

        :param address: 指定负载均衡实例的私网IP地址，该地址必须包含在子网网段下。
        :type address: str (optional)

        :param eip: 绑定已有的eip。取值为eip的IP地址
        :type eip: str (optional)

        :param tags: 待创建的标签键值对列表
        :type tags: List[TagModel] (optional)

        :param billing: billing parameter
        :type billing: BillingForCreate (optional)

        :param performance_level: performance_level parameter
        :type performance_level: str (optional)

        :param auto_renew_length: auto_renew_length parameter
        :type auto_renew_length: int (optional)

        :param auto_renew_time_unit: 支持创建BLB同时开通自动续费，取值为 month 获 year （默认 month）
        :type auto_renew_time_unit: str (optional)

        :param resource_group_id: 支持创建BLB同时绑定资源分组id
        :type resource_group_id: str (optional)

        :param allow_delete: 是否允许删除。缺省值为true，代表允许删除
        :type allow_delete: bool (optional)

        :param allow_modify: allow_modify parameter
        :type allow_modify: bool (optional)

        :param modification_protection_reason: 不允许修改的原因,最多支持128个字符
        :type modification_protection_reason: str (optional)

        :param allocate_ipv6: 是否分配ipv6地址。true代表分配ipv6地址，false代表不分配ipv6地址
        :type allocate_ipv6: bool (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.type = type
        self.desc = desc
        self.subnet_id = subnet_id
        self.vpc_id = vpc_id
        self.address = address
        self.eip = eip
        self.tags = tags
        self.billing = billing
        self.performance_level = performance_level
        self.auto_renew_length = auto_renew_length
        self.auto_renew_time_unit = auto_renew_time_unit
        self.resource_group_id = resource_group_id
        self.allow_delete = allow_delete
        self.allow_modify = allow_modify
        self.modification_protection_reason = modification_protection_reason
        self.allocate_ipv6 = allocate_ipv6

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
        if self.type is not None:
            result['type'] = self.type
        if self.desc is not None:
            result['desc'] = self.desc
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.address is not None:
            result['address'] = self.address
        if self.eip is not None:
            result['eip'] = self.eip
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level
        if self.auto_renew_length is not None:
            result['autoRenewLength'] = self.auto_renew_length
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.allow_delete is not None:
            result['allowDelete'] = self.allow_delete
        if self.allow_modify is not None:
            result['allowModify'] = self.allow_modify
        if self.modification_protection_reason is not None:
            result['modificationProtectionReason'] = self.modification_protection_reason
        if self.allocate_ipv6 is not None:
            result['allocateIpv6'] = self.allocate_ipv6
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAppBlbRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('billing') is not None:
            self.billing = BillingForCreate().from_dict(m.get('billing'))
        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')
        if m.get('autoRenewLength') is not None:
            self.auto_renew_length = m.get('autoRenewLength')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('allowDelete') is not None:
            self.allow_delete = m.get('allowDelete')
        if m.get('allowModify') is not None:
            self.allow_modify = m.get('allowModify')
        if m.get('modificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('modificationProtectionReason')
        if m.get('allocateIpv6') is not None:
            self.allocate_ipv6 = m.get('allocateIpv6')
        return self
