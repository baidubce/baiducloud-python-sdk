"""
ContainerDetailModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bci.models.port import Port

from baiducloud_python_sdk_bci.models.volume_mount import VolumeMount

from baiducloud_python_sdk_bci.models.environment import Environment

from baiducloud_python_sdk_bci.models.container_status import ContainerStatus

from baiducloud_python_sdk_bci.models.container_status import ContainerStatus


class ContainerDetailModel(AbstractModel):
    """
    ContainerDetailModel
    """

    def __init__(
        self,
        name=None,
        image=None,
        cpu=None,
        gpu=None,
        memory=None,
        working_dir=None,
        image_pull_policy=None,
        commands=None,
        args=None,
        ports=None,
        volume_mounts=None,
        envs=None,
        create_time=None,
        update_time=None,
        delete_time=None,
        previous_state=None,
        current_state=None,
        ready=None,
        restart_count=None,
    ):
        """
        Initialize ContainerDetailModel instance.

        :param name: 容器名称
        :type name: str (optional)

        :param image: 容器镜像
        :type image: str (optional)

        :param cpu: cpu数量
        :type cpu: float (optional)

        :param gpu: gpu数量
        :type gpu: float (optional)

        :param memory: 内存大小
        :type memory: float (optional)

        :param working_dir: 容器工作目录
        :type working_dir: str (optional)

        :param image_pull_policy: 镜像拉取策略
        :type image_pull_policy: str (optional)

        :param commands: 容器启动命令
        :type commands: List[str] (optional)

        :param args: 容器启动参数
        :type args: List[str] (optional)

        :param ports: 容器内端口信息
        :type ports: List[Port] (optional)

        :param volume_mounts: 容器存储卷信息
        :type volume_mounts: List[VolumeMount] (optional)

        :param envs: 容器环境变量列表
        :type envs: List[Environment] (optional)

        :param create_time: 容器创建时间
        :type create_time: str (optional)

        :param update_time: 容器更新时间
        :type update_time: str (optional)

        :param delete_time: 容器删除时间
        :type delete_time: str (optional)

        :param previous_state: previous_state attribute
        :type previous_state: ContainerStatus (optional)

        :param current_state: current_state attribute
        :type current_state: ContainerStatus (optional)

        :param ready: 是否已通过就绪探针
        :type ready: bool (optional)

        :param restart_count: 重启次数
        :type restart_count: int (optional)
        """
        super().__init__()
        self.name = name
        self.image = image
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory
        self.working_dir = working_dir
        self.image_pull_policy = image_pull_policy
        self.commands = commands
        self.args = args
        self.ports = ports
        self.volume_mounts = volume_mounts
        self.envs = envs
        self.create_time = create_time
        self.update_time = update_time
        self.delete_time = delete_time
        self.previous_state = previous_state
        self.current_state = current_state
        self.ready = ready
        self.restart_count = restart_count

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
        if self.name is not None:
            result['name'] = self.name
        if self.image is not None:
            result['image'] = self.image
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.gpu is not None:
            result['gpu'] = self.gpu
        if self.memory is not None:
            result['memory'] = self.memory
        if self.working_dir is not None:
            result['workingDir'] = self.working_dir
        if self.image_pull_policy is not None:
            result['imagePullPolicy'] = self.image_pull_policy
        if self.commands is not None:
            result['commands'] = self.commands
        if self.args is not None:
            result['args'] = self.args
        if self.ports is not None:
            result['ports'] = [i.to_dict() for i in self.ports]
        if self.volume_mounts is not None:
            result['volumeMounts'] = [i.to_dict() for i in self.volume_mounts]
        if self.envs is not None:
            result['envs'] = [i.to_dict() for i in self.envs]
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.delete_time is not None:
            result['deleteTime'] = self.delete_time
        if self.previous_state is not None:
            result['previousState'] = self.previous_state.to_dict()
        if self.current_state is not None:
            result['currentState'] = self.current_state.to_dict()
        if self.ready is not None:
            result['ready'] = self.ready
        if self.restart_count is not None:
            result['restartCount'] = self.restart_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ContainerDetailModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('workingDir') is not None:
            self.working_dir = m.get('workingDir')
        if m.get('imagePullPolicy') is not None:
            self.image_pull_policy = m.get('imagePullPolicy')
        if m.get('commands') is not None:
            self.commands = m.get('commands')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('ports') is not None:
            self.ports = [Port().from_dict(i) for i in m.get('ports')]
        if m.get('volumeMounts') is not None:
            self.volume_mounts = [VolumeMount().from_dict(i) for i in m.get('volumeMounts')]
        if m.get('envs') is not None:
            self.envs = [Environment().from_dict(i) for i in m.get('envs')]
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('deleteTime') is not None:
            self.delete_time = m.get('deleteTime')
        if m.get('previousState') is not None:
            self.previous_state = ContainerStatus().from_dict(m.get('previousState'))
        if m.get('currentState') is not None:
            self.current_state = ContainerStatus().from_dict(m.get('currentState'))
        if m.get('ready') is not None:
            self.ready = m.get('ready')
        if m.get('restartCount') is not None:
            self.restart_count = m.get('restartCount')
        return self
