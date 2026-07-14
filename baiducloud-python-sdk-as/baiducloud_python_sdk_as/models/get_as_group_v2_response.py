"""
Request entity for GetAsGroupV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_as.models.vpc_info import VpcInfo
from baiducloud_python_sdk_as.models.group_config import GroupConfig
from baiducloud_python_sdk_as.models.blb_info import BlbInfo
from baiducloud_python_sdk_as.models.tag_info import TagInfo
from baiducloud_python_sdk_as.models.cmd_config import CmdConfig
from baiducloud_python_sdk_as.models.bcc_name_config import BccNameConfig
from baiducloud_python_sdk_as.models.eip_config import EipConfig
from baiducloud_python_sdk_as.models.health_check_config import HealthCheckConfig


class GetAsGroupV2Response(BceResponse):
    """
    GetAsGroupV2Response
    """

    def __init__(
        self,
        group_id=None,
        group_name=None,
        region=None,
        status=None,
        vpc_info=None,
        zone_info=None,
        config=None,
        keypair_id=None,
        keypair_name=None,
        keep_image_login=None,
        blb=None,
        blb_unbind_wait_time=None,
        node_num=None,
        create_time=None,
        rds_ids=None,
        scs_ids=None,
        expansion_strategy=None,
        shrinkage_strategy=None,
        relation_tag=None,
        tags=None,
        cmd_config=None,
        bcc_name_config=None,
        eip_config=None,
        health_check=None,
    ):
        """
        Initialize GetAsGroupV2Response response.

        :param group_id: 伸缩组ID
        :type group_id: str (optional)

        :param group_name: 伸缩组名称
        :type group_name: str (optional)

        :param region: 伸缩组Region
        :type region: str (optional)

        :param status: 伸缩组状态
        :type status: str (optional)

        :param vpc_info: vpc_info field
        :type vpc_info: VpcInfo (optional)

        :param zone_info: 伸缩组可用区信息
        :type zone_info: List[object] (optional)

        :param config: config field
        :type config: GroupConfig (optional)

        :param keypair_id: 创建实例时使用的密钥对ID，非必填
        :type keypair_id: str (optional)

        :param keypair_name: 创建实例时使用的密钥对名称，非必填
        :type keypair_name: str (optional)

        :param keep_image_login: 是否使用镜像预置密码
        :type keep_image_login: bool (optional)

        :param blb: 伸缩组绑定BLB，可绑定多个
        :type blb: List[BlbInfo] (optional)

        :param blb_unbind_wait_time: BLB等待时间
        :type blb_unbind_wait_time: int (optional)

        :param node_num: 伸缩组节点
        :type node_num: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param rds_ids: rds的id
        :type rds_ids: str (optional)

        :param scs_ids: scs的id
        :type scs_ids: str (optional)

        :param expansion_strategy: 伸缩组扩容策略
        :type expansion_strategy: str (optional)

        :param shrinkage_strategy: 伸缩组缩容策略
        :type shrinkage_strategy: str (optional)

        :param relation_tag: 是否绑定标签
        :type relation_tag: bool (optional)

        :param tags: 伸缩组绑定标签
        :type tags: List[TagInfo] (optional)

        :param cmd_config: cmd_config field
        :type cmd_config: CmdConfig (optional)

        :param bcc_name_config: bcc_name_config field
        :type bcc_name_config: BccNameConfig (optional)

        :param eip_config: eip_config field
        :type eip_config: EipConfig (optional)

        :param health_check: health_check field
        :type health_check: HealthCheckConfig (optional)
        """
        super().__init__()
        self.group_id = group_id
        self.group_name = group_name
        self.region = region
        self.status = status
        self.vpc_info = vpc_info
        self.zone_info = zone_info
        self.config = config
        self.keypair_id = keypair_id
        self.keypair_name = keypair_name
        self.keep_image_login = keep_image_login
        self.blb = blb
        self.blb_unbind_wait_time = blb_unbind_wait_time
        self.node_num = node_num
        self.create_time = create_time
        self.rds_ids = rds_ids
        self.scs_ids = scs_ids
        self.expansion_strategy = expansion_strategy
        self.shrinkage_strategy = shrinkage_strategy
        self.relation_tag = relation_tag
        self.tags = tags
        self.cmd_config = cmd_config
        self.bcc_name_config = bcc_name_config
        self.eip_config = eip_config
        self.health_check = health_check

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
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_dict()
        if self.zone_info is not None:
            result['zoneInfo'] = self.zone_info
        if self.config is not None:
            result['config'] = self.config.to_dict()
        if self.keypair_id is not None:
            result['keypairId'] = self.keypair_id
        if self.keypair_name is not None:
            result['keypairName'] = self.keypair_name
        if self.keep_image_login is not None:
            result['keepImageLogin'] = self.keep_image_login
        if self.blb is not None:
            result['blb'] = [i.to_dict() for i in self.blb]
        if self.blb_unbind_wait_time is not None:
            result['blbUnbindWaitTime'] = self.blb_unbind_wait_time
        if self.node_num is not None:
            result['nodeNum'] = self.node_num
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.rds_ids is not None:
            result['rdsIds'] = self.rds_ids
        if self.scs_ids is not None:
            result['scsIds'] = self.scs_ids
        if self.expansion_strategy is not None:
            result['expansionStrategy'] = self.expansion_strategy
        if self.shrinkage_strategy is not None:
            result['shrinkageStrategy'] = self.shrinkage_strategy
        if self.relation_tag is not None:
            result['relationTag'] = self.relation_tag
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.cmd_config is not None:
            result['cmdConfig'] = self.cmd_config.to_dict()
        if self.bcc_name_config is not None:
            result['bccNameConfig'] = self.bcc_name_config.to_dict()
        if self.eip_config is not None:
            result['eipConfig'] = self.eip_config.to_dict()
        if self.health_check is not None:
            result['healthCheck'] = self.health_check.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetAsGroupV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
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
        if m.get('vpcInfo') is not None:
            self.vpc_info = VpcInfo().from_dict(m.get('vpcInfo'))
        if m.get('zoneInfo') is not None:
            self.zone_info = m.get('zoneInfo')
        if m.get('config') is not None:
            self.config = GroupConfig().from_dict(m.get('config'))
        if m.get('keypairId') is not None:
            self.keypair_id = m.get('keypairId')
        if m.get('keypairName') is not None:
            self.keypair_name = m.get('keypairName')
        if m.get('keepImageLogin') is not None:
            self.keep_image_login = m.get('keepImageLogin')
        if m.get('blb') is not None:
            self.blb = [BlbInfo().from_dict(i) for i in m.get('blb')]
        if m.get('blbUnbindWaitTime') is not None:
            self.blb_unbind_wait_time = m.get('blbUnbindWaitTime')
        if m.get('nodeNum') is not None:
            self.node_num = m.get('nodeNum')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('rdsIds') is not None:
            self.rds_ids = m.get('rdsIds')
        if m.get('scsIds') is not None:
            self.scs_ids = m.get('scsIds')
        if m.get('expansionStrategy') is not None:
            self.expansion_strategy = m.get('expansionStrategy')
        if m.get('shrinkageStrategy') is not None:
            self.shrinkage_strategy = m.get('shrinkageStrategy')
        if m.get('relationTag') is not None:
            self.relation_tag = m.get('relationTag')
        if m.get('tags') is not None:
            self.tags = [TagInfo().from_dict(i) for i in m.get('tags')]
        if m.get('cmdConfig') is not None:
            self.cmd_config = CmdConfig().from_dict(m.get('cmdConfig'))
        if m.get('bccNameConfig') is not None:
            self.bcc_name_config = BccNameConfig().from_dict(m.get('bccNameConfig'))
        if m.get('eipConfig') is not None:
            self.eip_config = EipConfig().from_dict(m.get('eipConfig'))
        if m.get('healthCheck') is not None:
            self.health_check = HealthCheckConfig().from_dict(m.get('healthCheck'))
        return self
