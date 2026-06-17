"""
Request entity for CreateReservedInstancesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class CreateReservedInstancesRequest(AbstractModel):
    """
    Request entity for CreateReservedInstancesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        zone_name,
        spec,
        offering_type,
        reserved_instance_time,
        reserved_instance_name=None,
        scope=None,
        instance_count=None,
        reserved_instance_count=None,
        reserved_instance_time_unit=None,
        auto_renew=None,
        auto_renew_time_unit=None,
        auto_renew_time=None,
        effective_time=None,
        tags=None,
        ticket_id=None,
        ehc_cluster_id=None,
    ):
        """
        Initialize CreateReservedInstancesRequest request entity.

        :param reserved_instance_name: reserved_instance_name parameter
        :type reserved_instance_name: str (optional)

        :param scope: 实例券的可用范围；默认：AZ
        :type scope: str (optional)

        :param zone_name: 可用区，例如cn-bj-a
        :type zone_name: str (required)

        :param spec: 实例规格，例如bcc.g4.c2m8
        :type spec: str (required)

        :param offering_type: 默认值全预付：FullyPrepay
        :type offering_type: str (required)

        :param instance_count: 实例数量，默认为1，不可变更
        :type instance_count: int (optional)

        :param reserved_instance_count: 预留实例券数量，默认1，不能超过配额，默认配额20，若需要更多配额，请联系工单（可链接）申请
        :type reserved_instance_count: int (optional)

        :param reserved_instance_time: 预留实例券购买时长，支持3，6，9，12，24，36个月
        :type reserved_instance_time: int (required)

        :param reserved_instance_time_unit: 预留实例券购买时长单位，默认为month，不可变更
        :type reserved_instance_time_unit: str (optional)

        :param auto_renew: 自动续费开关，默认为false
        :type auto_renew: bool (optional)

        :param auto_renew_time_unit: 预留实例券自动续费时长单位,默认为month，不可变更
        :type auto_renew_time_unit: str (optional)

        :param auto_renew_time: auto_renew_time parameter
        :type auto_renew_time: int (optional)

        :param effective_time: effective_time parameter
        :type effective_time: str (optional)

        :param tags: 标签信息（查询预留实例券返回）
        :type tags: List[TagModel] (optional)

        :param ticket_id: 代金券id
        :type ticket_id: str (optional)

        :param ehc_cluster_id: 创建roce预留实例券时可选参数，若为空则使用默认EHC集群
        :type ehc_cluster_id: str (optional)
        """
        super().__init__()
        self.reserved_instance_name = reserved_instance_name
        self.scope = scope
        self.zone_name = zone_name
        self.spec = spec
        self.offering_type = offering_type
        self.instance_count = instance_count
        self.reserved_instance_count = reserved_instance_count
        self.reserved_instance_time = reserved_instance_time
        self.reserved_instance_time_unit = reserved_instance_time_unit
        self.auto_renew = auto_renew
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time
        self.effective_time = effective_time
        self.tags = tags
        self.ticket_id = ticket_id
        self.ehc_cluster_id = ehc_cluster_id

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
        if self.reserved_instance_name is not None:
            result['reservedInstanceName'] = self.reserved_instance_name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.spec is not None:
            result['spec'] = self.spec
        if self.offering_type is not None:
            result['offeringType'] = self.offering_type
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count
        if self.reserved_instance_count is not None:
            result['reservedInstanceCount'] = self.reserved_instance_count
        if self.reserved_instance_time is not None:
            result['reservedInstanceTime'] = self.reserved_instance_time
        if self.reserved_instance_time_unit is not None:
            result['reservedInstanceTimeUnit'] = self.reserved_instance_time_unit
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.ticket_id is not None:
            result['ticketId'] = self.ticket_id
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateReservedInstancesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstanceName') is not None:
            self.reserved_instance_name = m.get('reservedInstanceName')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('offeringType') is not None:
            self.offering_type = m.get('offeringType')
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')
        if m.get('reservedInstanceCount') is not None:
            self.reserved_instance_count = m.get('reservedInstanceCount')
        if m.get('reservedInstanceTime') is not None:
            self.reserved_instance_time = m.get('reservedInstanceTime')
        if m.get('reservedInstanceTimeUnit') is not None:
            self.reserved_instance_time_unit = m.get('reservedInstanceTimeUnit')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('ticketId') is not None:
            self.ticket_id = m.get('ticketId')
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        return self
