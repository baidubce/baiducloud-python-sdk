"""
Pod information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aihc.models.env import Env


class Pod(AbstractModel):
    """
    Pod
    """

    def __init__(
        self,
        pod_ip=None,
        node_name=None,
        creation_at=None,
        uid=None,
        name=None,
        status=None,
        replica_type=None,
        restart_count=None,
        envs=None,
        finished_at=None,
        reason=None,
    ):
        """
        Initialize Pod instance.

        :param pod_ip: Pod IP
        :type pod_ip: str (optional)

        :param node_name: 任务pod所在节点的名称
        :type node_name: str (optional)

        :param creation_at: Pod创建时间
        :type creation_at: str (optional)

        :param uid: Pod的id
        :type uid: str (optional)

        :param name: 任务Pod名称
        :type name: str (optional)

        :param status: status attribute
        :type status: str (optional)

        :param replica_type: 任务Pod的副本类型，pytorch中包含master和worker两种副本类型
        :type replica_type: str (optional)

        :param restart_count: 任务Pod重启次数
        :type restart_count: int (optional)

        :param envs: Pod环境变量
        :type envs: List[Env] (optional)

        :param finished_at: Pod完成时间
        :type finished_at: str (optional)

        :param reason: Pod失败原因
        :type reason: str (optional)
        """
        super().__init__()
        self.pod_ip = pod_ip
        self.node_name = node_name
        self.creation_at = creation_at
        self.uid = uid
        self.name = name
        self.status = status
        self.replica_type = replica_type
        self.restart_count = restart_count
        self.envs = envs
        self.finished_at = finished_at
        self.reason = reason

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
        if self.pod_ip is not None:
            result['PodIP'] = self.pod_ip
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.creation_at is not None:
            result['creationAt'] = self.creation_at
        if self.uid is not None:
            result['uid'] = self.uid
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.replica_type is not None:
            result['replicaType'] = self.replica_type
        if self.restart_count is not None:
            result['restartCount'] = self.restart_count
        if self.envs is not None:
            result['envs'] = [i.to_dict() for i in self.envs]
        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Pod

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('PodIP') is not None:
            self.pod_ip = m.get('PodIP')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('creationAt') is not None:
            self.creation_at = m.get('creationAt')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('replicaType') is not None:
            self.replica_type = m.get('replicaType')
        if m.get('restartCount') is not None:
            self.restart_count = m.get('restartCount')
        if m.get('envs') is not None:
            self.envs = [Env().from_dict(i) for i in m.get('envs')]
        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self
