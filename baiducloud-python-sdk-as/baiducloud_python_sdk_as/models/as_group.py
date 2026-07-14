"""
AsGroup information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.tag_info import TagInfo

from baiducloud_python_sdk_as.models.group_config import GroupConfig

from baiducloud_python_sdk_as.models.blb_info import BlbInfo

from baiducloud_python_sdk_as.models.health_check_state import HealthCheckState


class AsGroup(AbstractModel):
    """
    AsGroup
    """

    def __init__(
        self,
        group_id=None,
        group_name=None,
        region=None,
        status=None,
        tags=None,
        relation_tag=None,
        vpc_id=None,
        zone_info=None,
        config=None,
        blb=None,
        node_num=None,
        rule_count=None,
        create_time=None,
        health_check_state=None,
    ):
        """
        Initialize AsGroup instance.

        :param group_id: 伸缩组id
        :type group_id: str (optional)

        :param group_name: 伸缩组名称
        :type group_name: str (optional)

        :param region: 分区
        :type region: str (optional)

        :param status: 状态
        :type status: str (optional)

        :param tags: 标签信息
        :type tags: List[TagInfo] (optional)

        :param relation_tag: 是否绑定标签
        :type relation_tag: bool (optional)

        :param vpc_id: vpc的id
        :type vpc_id: str (optional)

        :param zone_info: 伸缩组所在可用区
        :type zone_info: List[object] (optional)

        :param config: config attribute
        :type config: GroupConfig (optional)

        :param blb: 伸缩组绑定BLB，可绑定多个
        :type blb: List[BlbInfo] (optional)

        :param node_num: 节点数量
        :type node_num: int (optional)

        :param rule_count: 规则数量
        :type rule_count: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param health_check_state: health_check_state attribute
        :type health_check_state: HealthCheckState (optional)
        """
        super().__init__()
        self.group_id = group_id
        self.group_name = group_name
        self.region = region
        self.status = status
        self.tags = tags
        self.relation_tag = relation_tag
        self.vpc_id = vpc_id
        self.zone_info = zone_info
        self.config = config
        self.blb = blb
        self.node_num = node_num
        self.rule_count = rule_count
        self.create_time = create_time
        self.health_check_state = health_check_state

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
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.relation_tag is not None:
            result['relationTag'] = self.relation_tag
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.zone_info is not None:
            result['zoneInfo'] = self.zone_info
        if self.config is not None:
            result['config'] = self.config.to_dict()
        if self.blb is not None:
            result['blb'] = [i.to_dict() for i in self.blb]
        if self.node_num is not None:
            result['nodeNum'] = self.node_num
        if self.rule_count is not None:
            result['ruleCount'] = self.rule_count
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.health_check_state is not None:
            result['healthCheckState'] = self.health_check_state.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AsGroup

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tags') is not None:
            self.tags = [TagInfo().from_dict(i) for i in m.get('tags')]
        if m.get('relationTag') is not None:
            self.relation_tag = m.get('relationTag')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneInfo') is not None:
            self.zone_info = m.get('zoneInfo')
        if m.get('config') is not None:
            self.config = GroupConfig().from_dict(m.get('config'))
        if m.get('blb') is not None:
            self.blb = [BlbInfo().from_dict(i) for i in m.get('blb')]
        if m.get('nodeNum') is not None:
            self.node_num = m.get('nodeNum')
        if m.get('ruleCount') is not None:
            self.rule_count = m.get('ruleCount')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('healthCheckState') is not None:
            self.health_check_state = HealthCheckState().from_dict(m.get('healthCheckState'))
        return self
