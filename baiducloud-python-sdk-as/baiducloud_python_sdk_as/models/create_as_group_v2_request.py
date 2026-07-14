"""
Request entity for CreateAsGroupV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_as.models.zone_info import ZoneInfo
from baiducloud_python_sdk_as.models.group_config import GroupConfig
from baiducloud_python_sdk_as.models.blb_info import BlbInfo
from baiducloud_python_sdk_as.models.node_info import NodeInfo
from baiducloud_python_sdk_as.models.eip_info import EipInfo
from baiducloud_python_sdk_as.models.eip_config import EipConfig
from baiducloud_python_sdk_as.models.billing_info import BillingInfo
from baiducloud_python_sdk_as.models.health_check_config import HealthCheckConfig
from baiducloud_python_sdk_as.models.assign_tag_info import AssignTagInfo
from baiducloud_python_sdk_as.models.cmd_config import CmdConfig
from baiducloud_python_sdk_as.models.bcc_name_config import BccNameConfig


class CreateAsGroupV2Request(AbstractModel):
    """
    Request entity for CreateAsGroupV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        group_name,
        zone_info,
        config,
        nodes,
        assign_tag_info,
        cmd_config,
        keypair_id=None,
        keypair_name=None,
        keep_image_login=None,
        blb=None,
        blb_unbind_wait_time=None,
        eip=None,
        eip_config=None,
        billing=None,
        rds=None,
        scs=None,
        health_check=None,
        expansion_strategy=None,
        shrinkage_strategy=None,
        bcc_name_config=None,
    ):
        """
        Initialize CreateAsGroupV2Request request entity.

        :param group_name: 伸缩组名称
        :type group_name: str (required)

        :param zone_info: 伸缩组所在可用区
        :type zone_info: List[ZoneInfo] (required)

        :param config: config parameter
        :type config: GroupConfig (required)

        :param keypair_id: 创建实例时使用的密钥对 ID
        :type keypair_id: str (optional)

        :param keypair_name: 创建实例时使用的密钥对名称
        :type keypair_name: str (optional)

        :param keep_image_login: 是否使用镜像预置密码，非必填，默认为0，当为1时使用预置密码，这时镜像类型必须为自定义镜像
        :type keep_image_login: int (optional)

        :param blb: 伸缩组绑定BLB，可绑定多个
        :type blb: List[BlbInfo] (optional)

        :param blb_unbind_wait_time: blb_unbind_wait_time parameter
        :type blb_unbind_wait_time: int (optional)

        :param nodes: 伸缩组扩容时节点配置
        :type nodes: List[NodeInfo] (required)

        :param eip: eip parameter
        :type eip: EipInfo (optional)

        :param eip_config: eip_config parameter
        :type eip_config: EipConfig (optional)

        :param billing: billing parameter
        :type billing: BillingInfo (optional)

        :param rds: 伸缩组绑定RDS，可绑定多个
        :type rds: List[str] (optional)

        :param scs: 伸缩组绑定SCS，可绑定多个
        :type scs: List[str] (optional)

        :param health_check: health_check parameter
        :type health_check: HealthCheckConfig (optional)

        :param expansion_strategy: expansion_strategy parameter
        :type expansion_strategy: str (optional)

        :param shrinkage_strategy: 伸缩组缩容时策略；Earlier - 删除先创建实例，Later - 删除后创建实例
        :type shrinkage_strategy: str (optional)

        :param assign_tag_info: assign_tag_info parameter
        :type assign_tag_info: AssignTagInfo (required)

        :param cmd_config: cmd_config parameter
        :type cmd_config: CmdConfig (required)

        :param bcc_name_config: bcc_name_config parameter
        :type bcc_name_config: BccNameConfig (optional)
        """
        super().__init__()
        self.group_name = group_name
        self.zone_info = zone_info
        self.config = config
        self.keypair_id = keypair_id
        self.keypair_name = keypair_name
        self.keep_image_login = keep_image_login
        self.blb = blb
        self.blb_unbind_wait_time = blb_unbind_wait_time
        self.nodes = nodes
        self.eip = eip
        self.eip_config = eip_config
        self.billing = billing
        self.rds = rds
        self.scs = scs
        self.health_check = health_check
        self.expansion_strategy = expansion_strategy
        self.shrinkage_strategy = shrinkage_strategy
        self.assign_tag_info = assign_tag_info
        self.cmd_config = cmd_config
        self.bcc_name_config = bcc_name_config

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
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.zone_info is not None:
            result['zoneInfo'] = [i.to_dict() for i in self.zone_info]
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
        if self.nodes is not None:
            result['nodes'] = [i.to_dict() for i in self.nodes]
        if self.eip is not None:
            result['eip'] = self.eip.to_dict()
        if self.eip_config is not None:
            result['eipConfig'] = self.eip_config.to_dict()
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.rds is not None:
            result['rds'] = self.rds
        if self.scs is not None:
            result['scs'] = self.scs
        if self.health_check is not None:
            result['healthCheck'] = self.health_check.to_dict()
        if self.expansion_strategy is not None:
            result['expansionStrategy'] = self.expansion_strategy
        if self.shrinkage_strategy is not None:
            result['shrinkageStrategy'] = self.shrinkage_strategy
        if self.assign_tag_info is not None:
            result['assignTagInfo'] = self.assign_tag_info.to_dict()
        if self.cmd_config is not None:
            result['cmdConfig'] = self.cmd_config.to_dict()
        if self.bcc_name_config is not None:
            result['bccNameConfig'] = self.bcc_name_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAsGroupV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('zoneInfo') is not None:
            self.zone_info = [ZoneInfo().from_dict(i) for i in m.get('zoneInfo')]
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
        if m.get('nodes') is not None:
            self.nodes = [NodeInfo().from_dict(i) for i in m.get('nodes')]
        if m.get('eip') is not None:
            self.eip = EipInfo().from_dict(m.get('eip'))
        if m.get('eipConfig') is not None:
            self.eip_config = EipConfig().from_dict(m.get('eipConfig'))
        if m.get('billing') is not None:
            self.billing = BillingInfo().from_dict(m.get('billing'))
        if m.get('rds') is not None:
            self.rds = m.get('rds')
        if m.get('scs') is not None:
            self.scs = m.get('scs')
        if m.get('healthCheck') is not None:
            self.health_check = HealthCheckConfig().from_dict(m.get('healthCheck'))
        if m.get('expansionStrategy') is not None:
            self.expansion_strategy = m.get('expansionStrategy')
        if m.get('shrinkageStrategy') is not None:
            self.shrinkage_strategy = m.get('shrinkageStrategy')
        if m.get('assignTagInfo') is not None:
            self.assign_tag_info = AssignTagInfo().from_dict(m.get('assignTagInfo'))
        if m.get('cmdConfig') is not None:
            self.cmd_config = CmdConfig().from_dict(m.get('cmdConfig'))
        if m.get('bccNameConfig') is not None:
            self.bcc_name_config = BccNameConfig().from_dict(m.get('bccNameConfig'))
        return self
