"""
Request entity for GetReservedInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetReservedInstanceRequest(AbstractModel):
    """
    Request entity for GetReservedInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        marker=None,
        max_keys=None,
        reserved_instance_ids=None,
        reserved_instance_name=None,
        zone_name=None,
        reserved_instance_status=None,
        spec=None,
        offering_type=None,
        os_type=None,
        instance_id=None,
        instance_name=None,
        is_deduct=None,
        ehc_cluster_id=None,
        sort_key=None,
        sort_dir=None,
        reserved_instance_source=None,
        scope=None,
    ):
        """
        Initialize GetReservedInstanceRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param reserved_instance_ids: 预留实例券的id集合
        :type reserved_instance_ids: List[str] (optional)

        :param reserved_instance_name: 实例券的名称
        :type reserved_instance_name: str (optional)

        :param zone_name: 可用区，例如：cn-bj-a
        :type zone_name: str (optional)

        :param reserved_instance_status: 预留实例券的状态
        :type reserved_instance_status: str (optional)

        :param spec: 实例规格，例如：bcc.g4.c2m8
        :type spec: str (optional)

        :param offering_type: FullyPrepay：全预付
        :type offering_type: str (optional)

        :param os_type: 支持的镜像类型，all/linux/windows
        :type os_type: str (optional)

        :param instance_id: 抵扣实例ID
        :type instance_id: str (optional)

        :param instance_name: 实例名称
        :type instance_name: str (optional)

        :param is_deduct: 是否有抵扣实例：true/false
        :type is_deduct: bool (optional)

        :param ehc_cluster_id: ehc集群id
        :type ehc_cluster_id: str (optional)

        :param sort_key: 排序字段：osType/instanceCount/effectiveTime/expireTime
        :type sort_key: str (optional)

        :param sort_dir: 排序方式：desc/asc
        :type sort_dir: str (optional)

        :param reserved_instance_source: 预留实例券来源
        :type reserved_instance_source: str (optional)

        :param scope: 生效范围
        :type scope: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.reserved_instance_ids = reserved_instance_ids
        self.reserved_instance_name = reserved_instance_name
        self.zone_name = zone_name
        self.reserved_instance_status = reserved_instance_status
        self.spec = spec
        self.offering_type = offering_type
        self.os_type = os_type
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.is_deduct = is_deduct
        self.ehc_cluster_id = ehc_cluster_id
        self.sort_key = sort_key
        self.sort_dir = sort_dir
        self.reserved_instance_source = reserved_instance_source
        self.scope = scope

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
        if self.reserved_instance_ids is not None:
            result['reservedInstanceIds'] = self.reserved_instance_ids
        if self.reserved_instance_name is not None:
            result['reservedInstanceName'] = self.reserved_instance_name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.reserved_instance_status is not None:
            result['reservedInstanceStatus'] = self.reserved_instance_status
        if self.spec is not None:
            result['spec'] = self.spec
        if self.offering_type is not None:
            result['offeringType'] = self.offering_type
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.is_deduct is not None:
            result['isDeduct'] = self.is_deduct
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        if self.sort_dir is not None:
            result['sortDir'] = self.sort_dir
        if self.reserved_instance_source is not None:
            result['reservedInstanceSource'] = self.reserved_instance_source
        if self.scope is not None:
            result['scope'] = self.scope
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetReservedInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('reservedInstanceIds') is not None:
            self.reserved_instance_ids = m.get('reservedInstanceIds')
        if m.get('reservedInstanceName') is not None:
            self.reserved_instance_name = m.get('reservedInstanceName')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('reservedInstanceStatus') is not None:
            self.reserved_instance_status = m.get('reservedInstanceStatus')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('offeringType') is not None:
            self.offering_type = m.get('offeringType')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('isDeduct') is not None:
            self.is_deduct = m.get('isDeduct')
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        if m.get('sortDir') is not None:
            self.sort_dir = m.get('sortDir')
        if m.get('reservedInstanceSource') is not None:
            self.reserved_instance_source = m.get('reservedInstanceSource')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        return self
