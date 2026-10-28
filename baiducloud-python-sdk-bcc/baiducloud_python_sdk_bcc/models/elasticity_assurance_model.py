"""
ElasticityAssuranceModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.tag import Tag

from baiducloud_python_sdk_bcc.models.instance_model import InstanceModel


class ElasticityAssuranceModel(AbstractModel):
    """
    ElasticityAssuranceModel
    """

    def __init__(
        self,
        elasticity_assurance_id=None,
        elasticity_assurance_name=None,
        spec=None,
        status=None,
        zone_name=None,
        capacity=None,
        used_capacity=None,
        available_capacity=None,
        create_time=None,
        expire_time=None,
        auto_renew=None,
        auto_renew_period=None,
        tags=None,
        instances=None,
    ):
        """
        Initialize ElasticityAssuranceModel instance.

        :param elasticity_assurance_id: 弹性保障短ID
        :type elasticity_assurance_id: str (optional)

        :param elasticity_assurance_name: 弹性保障名称
        :type elasticity_assurance_name: str (optional)

        :param spec: 实例规格
        :type spec: str (optional)

        :param status: 弹性保障状态，如CREATING/ACTIVE
        :type status: str (optional)

        :param zone_name: 逻辑可用区
        :type zone_name: str (optional)

        :param capacity: 购买的总保障容量，单位为台
        :type capacity: int (optional)

        :param used_capacity: 当前已匹配的后付费实例数量
        :type used_capacity: int (optional)

        :param available_capacity: 当前剩余保障容量
        :type available_capacity: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param expire_time: 到期时间
        :type expire_time: str (optional)

        :param auto_renew: 是否开启自动续费
        :type auto_renew: bool (optional)

        :param auto_renew_period: 自动续费时长，单位为月；未开启时为空
        :type auto_renew_period: int (optional)

        :param tags: 标签列表
        :type tags: List[Tag] (optional)

        :param instances: 当前关联的按量实例列表
        :type instances: List[InstanceModel] (optional)
        """
        super().__init__()
        self.elasticity_assurance_id = elasticity_assurance_id
        self.elasticity_assurance_name = elasticity_assurance_name
        self.spec = spec
        self.status = status
        self.zone_name = zone_name
        self.capacity = capacity
        self.used_capacity = used_capacity
        self.available_capacity = available_capacity
        self.create_time = create_time
        self.expire_time = expire_time
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.tags = tags
        self.instances = instances

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
        if self.elasticity_assurance_id is not None:
            result['elasticityAssuranceId'] = self.elasticity_assurance_id
        if self.elasticity_assurance_name is not None:
            result['ElasticityAssuranceName'] = self.elasticity_assurance_name
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.used_capacity is not None:
            result['usedCapacity'] = self.used_capacity
        if self.available_capacity is not None:
            result['availableCapacity'] = self.available_capacity
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.instances is not None:
            result['instances'] = [i.to_dict() for i in self.instances]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ElasticityAssuranceModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('elasticityAssuranceId') is not None:
            self.elasticity_assurance_id = m.get('elasticityAssuranceId')
        if m.get('ElasticityAssuranceName') is not None:
            self.elasticity_assurance_name = m.get('ElasticityAssuranceName')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('usedCapacity') is not None:
            self.used_capacity = m.get('usedCapacity')
        if m.get('availableCapacity') is not None:
            self.available_capacity = m.get('availableCapacity')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('instances') is not None:
            self.instances = [InstanceModel().from_dict(i) for i in m.get('instances')]
        return self
