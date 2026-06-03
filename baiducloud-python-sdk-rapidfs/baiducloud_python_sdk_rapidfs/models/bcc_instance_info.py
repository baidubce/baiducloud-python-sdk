"""
BccInstanceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BccInstanceInfo(AbstractModel):
    """
    BccInstanceInfo
    """

    def __init__(
        self,
        ip=None,
        bcc_id=None,
        bcc_name=None,
        vpc_id=None,
        zone=None,
        bcc_spec=None,
        status=None,
        bsm_agent_status=None,
    ):
        """
        Initialize BccInstanceInfo instance.

        :param ip: BCC 实例 IP 地址
        :type ip: str (optional)

        :param bcc_id: BCC 实例 ID
        :type bcc_id: str (optional)

        :param bcc_name: BCC 实例名称
        :type bcc_name: str (optional)

        :param vpc_id: VPC ID
        :type vpc_id: str (optional)

        :param zone: 可用区
        :type zone: str (optional)

        :param bcc_spec: BCC 规格
        :type bcc_spec: str (optional)

        :param status: status attribute
        :type status: str (optional)

        :param bsm_agent_status: BSM Agent 信息
        :type bsm_agent_status: str (optional)
        """
        super().__init__()
        self.ip = ip
        self.bcc_id = bcc_id
        self.bcc_name = bcc_name
        self.vpc_id = vpc_id
        self.zone = zone
        self.bcc_spec = bcc_spec
        self.status = status
        self.bsm_agent_status = bsm_agent_status

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.bcc_id is not None:
            result['bccId'] = self.bcc_id
        if self.bcc_name is not None:
            result['bccName'] = self.bcc_name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.zone is not None:
            result['zone'] = self.zone
        if self.bcc_spec is not None:
            result['bccSpec'] = self.bcc_spec
        if self.status is not None:
            result['status'] = self.status
        if self.bsm_agent_status is not None:
            result['bsmAgentStatus'] = self.bsm_agent_status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BccInstanceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('bccId') is not None:
            self.bcc_id = m.get('bccId')
        if m.get('bccName') is not None:
            self.bcc_name = m.get('bccName')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('bccSpec') is not None:
            self.bcc_spec = m.get('bccSpec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('bsmAgentStatus') is not None:
            self.bsm_agent_status = m.get('bsmAgentStatus')
        return self
