"""
Node information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.as_eip import AsEip

from baiducloud_python_sdk_as.models.tag_info import TagInfo


class Node(AbstractModel):
    """
    Node
    """

    def __init__(
        self,
        instance_id=None,
        instance_uuid=None,
        instance_name=None,
        floating_ip=None,
        internal_ip=None,
        status=None,
        payment=None,
        cpu_count=None,
        memory_capacity_in_gb=None,
        instance_type=None,
        sys_disk_in_gb=None,
        create_time=None,
        eip=None,
        subnet_type=None,
        is_protected=None,
        node_type=None,
        tags=None,
        group_id=None,
        is_managed=None,
        internal_spec=None,
        logical_zone=None,
    ):
        """
        Initialize Node instance.

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param instance_uuid: 实例UUID
        :type instance_uuid: str (optional)

        :param instance_name: 实例名称
        :type instance_name: str (optional)

        :param floating_ip: 浮动IP
        :type floating_ip: str (optional)

        :param internal_ip: 内网IP
        :type internal_ip: str (optional)

        :param status: 状态
        :type status: str (optional)

        :param payment: 付费方式
        :type payment: str (optional)

        :param cpu_count: cpu数量
        :type cpu_count: int (optional)

        :param memory_capacity_in_gb: 内存大小
        :type memory_capacity_in_gb: int (optional)

        :param instance_type: 实例类型
        :type instance_type: str (optional)

        :param sys_disk_in_gb: 系统盘大小
        :type sys_disk_in_gb: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param eip: eip attribute
        :type eip: AsEip (optional)

        :param subnet_type: 子网类型
        :type subnet_type: str (optional)

        :param is_protected: 是否受保护节点
        :type is_protected: bool (optional)

        :param node_type: 节点类型
        :type node_type: str (optional)

        :param tags: 标签列表
        :type tags: List[TagInfo] (optional)

        :param group_id: 分组ID
        :type group_id: str (optional)

        :param is_managed: 是否由系统托管
        :type is_managed: bool (optional)

        :param internal_spec: 内部规格标识
        :type internal_spec: str (optional)

        :param logical_zone: 逻辑区域标识
        :type logical_zone: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.instance_uuid = instance_uuid
        self.instance_name = instance_name
        self.floating_ip = floating_ip
        self.internal_ip = internal_ip
        self.status = status
        self.payment = payment
        self.cpu_count = cpu_count
        self.memory_capacity_in_gb = memory_capacity_in_gb
        self.instance_type = instance_type
        self.sys_disk_in_gb = sys_disk_in_gb
        self.create_time = create_time
        self.eip = eip
        self.subnet_type = subnet_type
        self.is_protected = is_protected
        self.node_type = node_type
        self.tags = tags
        self.group_id = group_id
        self.is_managed = is_managed
        self.internal_spec = internal_spec
        self.logical_zone = logical_zone

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_uuid is not None:
            result['instanceUuid'] = self.instance_uuid
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.floating_ip is not None:
            result['floatingIp'] = self.floating_ip
        if self.internal_ip is not None:
            result['internalIp'] = self.internal_ip
        if self.status is not None:
            result['status'] = self.status
        if self.payment is not None:
            result['payment'] = self.payment
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.memory_capacity_in_gb is not None:
            result['memoryCapacityInGB'] = self.memory_capacity_in_gb
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.sys_disk_in_gb is not None:
            result['sysDiskInGB'] = self.sys_disk_in_gb
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.eip is not None:
            result['eip'] = self.eip.to_dict()
        if self.subnet_type is not None:
            result['subnetType'] = self.subnet_type
        if self.is_protected is not None:
            result['isProtected'] = self.is_protected
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed
        if self.internal_spec is not None:
            result['internalSpec'] = self.internal_spec
        if self.logical_zone is not None:
            result['logicalZone'] = self.logical_zone
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Node

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceUuid') is not None:
            self.instance_uuid = m.get('instanceUuid')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('floatingIp') is not None:
            self.floating_ip = m.get('floatingIp')
        if m.get('internalIp') is not None:
            self.internal_ip = m.get('internalIp')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('payment') is not None:
            self.payment = m.get('payment')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('memoryCapacityInGB') is not None:
            self.memory_capacity_in_gb = m.get('memoryCapacityInGB')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('sysDiskInGB') is not None:
            self.sys_disk_in_gb = m.get('sysDiskInGB')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('eip') is not None:
            self.eip = AsEip().from_dict(m.get('eip'))
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('isProtected') is not None:
            self.is_protected = m.get('isProtected')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('tags') is not None:
            self.tags = [TagInfo().from_dict(i) for i in m.get('tags')]
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')
        if m.get('internalSpec') is not None:
            self.internal_spec = m.get('internalSpec')
        if m.get('logicalZone') is not None:
            self.logical_zone = m.get('logicalZone')
        return self
