"""
ReservedInstanceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class ReservedInstanceInfo(AbstractModel):
    """
    ReservedInstanceInfo
    """

    def __init__(
        self,
        reserved_instance_id=None,
        reserved_instance_uuid=None,
        reserved_instance_name=None,
        scope=None,
        zone_name=None,
        logical_zone=None,
        spec=None,
        reserved_type=None,
        offering_type=None,
        os_type=None,
        reserved_instance_status=None,
        instance_count=None,
        effective_time=None,
        expire_time=None,
        transfer_in_time=None,
        auto_renew=None,
        renew_time_unit=None,
        renew_time=None,
        next_renew_time=None,
        flavor_sub_type=None,
        product_category=None,
        is_need_ehc_cluster=None,
        tags=None,
        instance_id=None,
        instance_ids=None,
        instance_name=None,
        instance_names=None,
        transfer_in=None,
        grantor_user_id=None,
        time_granularity=None,
        reserved_instance_time=None,
        ehc_cluster_id=None,
    ):
        """
        Initialize ReservedInstanceInfo instance.

        :param reserved_instance_id: 预留实例券id（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type reserved_instance_id: str (optional)

        :param reserved_instance_uuid: 预留实例券长id（查询预留实例券、预留实例券转出列表返回）
        :type reserved_instance_uuid: str (optional)

        :param reserved_instance_name: 预留实例券名称（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type reserved_instance_name: str (optional)

        :param scope: 预留实例券生效范围（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type scope: str (optional)

        :param zone_name: 预留实例券可用区（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type zone_name: str (optional)

        :param logical_zone: 逻辑可用区（查询预留实例券、预留实例券转出列表返回）
        :type logical_zone: str (optional)

        :param spec: 预留实例券实例规格（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type spec: str (optional)

        :param reserved_type: 预留实例券类型（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type reserved_type: str (optional)

        :param offering_type: 预留实例券付费方式（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type offering_type: str (optional)

        :param os_type: 预留实例券镜像类型（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type os_type: str (optional)

        :param reserved_instance_status: 预留实例券状态（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type reserved_instance_status: str (optional)

        :param instance_count: 预留实例券实例数量（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type instance_count: int (optional)

        :param effective_time: 预留实例券生效时间（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type effective_time: str (optional)

        :param expire_time: 预留实例券过期时间（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type expire_time: str (optional)

        :param transfer_in_time: 转入时间（查询预留实例券、预留实例券转出列表返回）
        :type transfer_in_time: str (optional)

        :param auto_renew: 预留实例券是否开启自动续费（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type auto_renew: bool (optional)

        :param renew_time_unit: 预留实例券自动续费单位（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type renew_time_unit: str (optional)

        :param renew_time: 预留实例券续费时长（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type renew_time: int (optional)

        :param next_renew_time: 预留实例券下次自动续费时间（查询预留实例券、预留实例券转出列表、预留实例券转入列表返回）
        :type next_renew_time: str (optional)

        :param flavor_sub_type: 规格子类型（查询预留实例券、预留实例券转出列表返回）
        :type flavor_sub_type: str (optional)

        :param product_category: 产品类别类别（查询预留实例券、预留实例券转出列表返回）
        :type product_category: str (optional)

        :param is_need_ehc_cluster: 是否需要EHC集群（查询预留实例券、预留实例券转出列表返回）
        :type is_need_ehc_cluster: bool (optional)

        :param tags: 标签信息（查询预留实例券返回）
        :type tags: List[TagModel] (optional)

        :param instance_id: 抵扣实例ID（查询预留实例券、预留实例券转出列表返回）
        :type instance_id: str (optional)

        :param instance_ids: 实例ID列表（查询预留实例券返回）
        :type instance_ids: List[str] (optional)

        :param instance_name: 抵扣实例名称（查询预留实例券、预留实例券转出列表返回）
        :type instance_name: str (optional)

        :param instance_names: 抵扣实例名称（查询预留实例券返回）
        :type instance_names: List[str] (optional)

        :param transfer_in: 是否已转入（查询预留实例券返回）
        :type transfer_in: bool (optional)

        :param grantor_user_id: 授予者用户ID（查询预留实例券返回）
        :type grantor_user_id: str (optional)

        :param time_granularity: 时间粒度（查询预留实例券返回）
        :type time_granularity: str (optional)

        :param reserved_instance_time: 预留实例时间（查询预留实例券返回）
        :type reserved_instance_time: int (optional)

        :param ehc_cluster_id: 预留实例券所在ehc集群id（查询预留实例券返回）
        :type ehc_cluster_id: str (optional)
        """
        super().__init__()
        self.reserved_instance_id = reserved_instance_id
        self.reserved_instance_uuid = reserved_instance_uuid
        self.reserved_instance_name = reserved_instance_name
        self.scope = scope
        self.zone_name = zone_name
        self.logical_zone = logical_zone
        self.spec = spec
        self.reserved_type = reserved_type
        self.offering_type = offering_type
        self.os_type = os_type
        self.reserved_instance_status = reserved_instance_status
        self.instance_count = instance_count
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.transfer_in_time = transfer_in_time
        self.auto_renew = auto_renew
        self.renew_time_unit = renew_time_unit
        self.renew_time = renew_time
        self.next_renew_time = next_renew_time
        self.flavor_sub_type = flavor_sub_type
        self.product_category = product_category
        self.is_need_ehc_cluster = is_need_ehc_cluster
        self.tags = tags
        self.instance_id = instance_id
        self.instance_ids = instance_ids
        self.instance_name = instance_name
        self.instance_names = instance_names
        self.transfer_in = transfer_in
        self.grantor_user_id = grantor_user_id
        self.time_granularity = time_granularity
        self.reserved_instance_time = reserved_instance_time
        self.ehc_cluster_id = ehc_cluster_id

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
        if self.reserved_instance_id is not None:
            result['reservedInstanceId'] = self.reserved_instance_id
        if self.reserved_instance_uuid is not None:
            result['reservedInstanceUuid'] = self.reserved_instance_uuid
        if self.reserved_instance_name is not None:
            result['reservedInstanceName'] = self.reserved_instance_name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.logical_zone is not None:
            result['logicalZone'] = self.logical_zone
        if self.spec is not None:
            result['spec'] = self.spec
        if self.reserved_type is not None:
            result['reservedType'] = self.reserved_type
        if self.offering_type is not None:
            result['offeringType'] = self.offering_type
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.reserved_instance_status is not None:
            result['reservedInstanceStatus'] = self.reserved_instance_status
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count
        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.transfer_in_time is not None:
            result['transferInTime'] = self.transfer_in_time
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.renew_time_unit is not None:
            result['renewTimeUnit'] = self.renew_time_unit
        if self.renew_time is not None:
            result['renewTime'] = self.renew_time
        if self.next_renew_time is not None:
            result['nextRenewTime'] = self.next_renew_time
        if self.flavor_sub_type is not None:
            result['flavorSubType'] = self.flavor_sub_type
        if self.product_category is not None:
            result['productCategory'] = self.product_category
        if self.is_need_ehc_cluster is not None:
            result['isNeedEhcCluster'] = self.is_need_ehc_cluster
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_names is not None:
            result['instanceNames'] = self.instance_names
        if self.transfer_in is not None:
            result['transferIn'] = self.transfer_in
        if self.grantor_user_id is not None:
            result['grantorUserId'] = self.grantor_user_id
        if self.time_granularity is not None:
            result['timeGranularity'] = self.time_granularity
        if self.reserved_instance_time is not None:
            result['reservedInstanceTime'] = self.reserved_instance_time
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReservedInstanceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstanceId') is not None:
            self.reserved_instance_id = m.get('reservedInstanceId')
        if m.get('reservedInstanceUuid') is not None:
            self.reserved_instance_uuid = m.get('reservedInstanceUuid')
        if m.get('reservedInstanceName') is not None:
            self.reserved_instance_name = m.get('reservedInstanceName')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('logicalZone') is not None:
            self.logical_zone = m.get('logicalZone')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('reservedType') is not None:
            self.reserved_type = m.get('reservedType')
        if m.get('offeringType') is not None:
            self.offering_type = m.get('offeringType')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('reservedInstanceStatus') is not None:
            self.reserved_instance_status = m.get('reservedInstanceStatus')
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')
        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('transferInTime') is not None:
            self.transfer_in_time = m.get('transferInTime')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('renewTimeUnit') is not None:
            self.renew_time_unit = m.get('renewTimeUnit')
        if m.get('renewTime') is not None:
            self.renew_time = m.get('renewTime')
        if m.get('nextRenewTime') is not None:
            self.next_renew_time = m.get('nextRenewTime')
        if m.get('flavorSubType') is not None:
            self.flavor_sub_type = m.get('flavorSubType')
        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')
        if m.get('isNeedEhcCluster') is not None:
            self.is_need_ehc_cluster = m.get('isNeedEhcCluster')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceNames') is not None:
            self.instance_names = m.get('instanceNames')
        if m.get('transferIn') is not None:
            self.transfer_in = m.get('transferIn')
        if m.get('grantorUserId') is not None:
            self.grantor_user_id = m.get('grantorUserId')
        if m.get('timeGranularity') is not None:
            self.time_granularity = m.get('timeGranularity')
        if m.get('reservedInstanceTime') is not None:
            self.reserved_instance_time = m.get('reservedInstanceTime')
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        return self
