"""
NodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class NodeInfo(AbstractModel):
    """
    NodeInfo
    """

    def __init__(
        self,
        node_id=None,
        node_name=None,
        internal_ip=None,
        zone_name=None,
        vpc_id=None,
        vpc_name=None,
        instance_id_list=None,
        node_status=None,
        node_type=None,
        mount_status=None,
        passwd=None,
        mt_name=None,
        mt_id=None,
        mt_path=None,
    ):
        """
        Initialize NodeInfo instance.

        :param node_id: 客户端节点短ID（BBC ID/AIHC ID/HPAS ID）
        :type node_id: str (optional)

        :param node_name: 客户端节点名称
        :type node_name: str (optional)

        :param internal_ip: 客户端节点内网IP(AIHC不展示)
        :type internal_ip: str (optional)

        :param zone_name: 可用区（cn-gz-d）
        :type zone_name: str (optional)

        :param vpc_id: vpc id
        :type vpc_id: str (optional)

        :param vpc_name: vpc name
        :type vpc_name: str (optional)

        :param instance_id_list: 节点挂载后端集群list
        :type instance_id_list: List[str] (optional)

        :param node_status: node_status attribute
        :type node_status: str (optional)

        :param node_type: BBC/BCC/AIHC/HPAS
        :type node_type: str (optional)

        :param mount_status: mount_status attribute
        :type mount_status: str (optional)

        :param passwd: 节点密码
        :type passwd: str (optional)

        :param mt_name: 挂载服务名称
        :type mt_name: str (optional)

        :param mt_id: 挂载服务id
        :type mt_id: str (optional)

        :param mt_path: 节点的挂载路径
        :type mt_path: str (optional)
        """
        super().__init__()
        self.node_id = node_id
        self.node_name = node_name
        self.internal_ip = internal_ip
        self.zone_name = zone_name
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.instance_id_list = instance_id_list
        self.node_status = node_status
        self.node_type = node_type
        self.mount_status = mount_status
        self.passwd = passwd
        self.mt_name = mt_name
        self.mt_id = mt_id
        self.mt_path = mt_path

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
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.internal_ip is not None:
            result['internalIp'] = self.internal_ip
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['vpcName'] = self.vpc_name
        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list
        if self.node_status is not None:
            result['nodeStatus'] = self.node_status
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.mount_status is not None:
            result['mountStatus'] = self.mount_status
        if self.passwd is not None:
            result['passwd'] = self.passwd
        if self.mt_name is not None:
            result['mtName'] = self.mt_name
        if self.mt_id is not None:
            result['mtId'] = self.mt_id
        if self.mt_path is not None:
            result['mtPath'] = self.mt_path
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('internalIp') is not None:
            self.internal_ip = m.get('internalIp')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcName') is not None:
            self.vpc_name = m.get('vpcName')
        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')
        if m.get('nodeStatus') is not None:
            self.node_status = m.get('nodeStatus')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('mountStatus') is not None:
            self.mount_status = m.get('mountStatus')
        if m.get('passwd') is not None:
            self.passwd = m.get('passwd')
        if m.get('mtName') is not None:
            self.mt_name = m.get('mtName')
        if m.get('mtId') is not None:
            self.mt_id = m.get('mtId')
        if m.get('mtPath') is not None:
            self.mt_path = m.get('mtPath')
        return self
