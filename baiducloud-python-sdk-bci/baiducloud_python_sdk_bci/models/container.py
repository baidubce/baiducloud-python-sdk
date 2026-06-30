"""
Container information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bci.models.volume_mount import VolumeMount

from baiducloud_python_sdk_bci.models.port import Port

from baiducloud_python_sdk_bci.models.environment import Environment

from baiducloud_python_sdk_bci.models.probe import Probe

from baiducloud_python_sdk_bci.models.probe import Probe

from baiducloud_python_sdk_bci.models.probe import Probe

from baiducloud_python_sdk_bci.models.container_security_context import ContainerSecurityContext


class Container(AbstractModel):
    """
    Container
    """

    def __init__(
        self,
        name=None,
        image=None,
        memory=None,
        cpu=None,
        gpu=None,
        working_dir=None,
        image_pull_policy=None,
        commands=None,
        args=None,
        volume_mounts=None,
        ports=None,
        environment_vars=None,
        liveness_probe=None,
        readiness_probe=None,
        startup_probe=None,
        stdin=None,
        stdin_once=None,
        tty=None,
        security_context=None,
    ):
        """
        Initialize Container instance.

        :param name: 容器名，1-40字符，由字母数字、\"-\"或\".\"组成
        :type name: str (optional)

        :param image: 镜像
        :type image: str (optional)

        :param memory: 内存（GiB），不可超过实例总内存
        :type memory: float (optional)

        :param cpu: CPU（核），不可超过实例总核数
        :type cpu: float (optional)

        :param gpu: 容器使用GPU个数
        :type gpu: float (optional)

        :param working_dir: 容器工作目录
        :type working_dir: str (optional)

        :param image_pull_policy: 镜像拉取策略：Always、IfNotPresent、Never
        :type image_pull_policy: str (optional)

        :param commands: 容器启动命令
        :type commands: List[str] (optional)

        :param args: 容器启动参数
        :type args: List[str] (optional)

        :param volume_mounts: 数据卷挂载信息
        :type volume_mounts: List[VolumeMount] (optional)

        :param ports: 容器内端口信息
        :type ports: List[Port] (optional)

        :param environment_vars: 环境变量
        :type environment_vars: List[Environment] (optional)

        :param liveness_probe: liveness_probe attribute
        :type liveness_probe: Probe (optional)

        :param readiness_probe: readiness_probe attribute
        :type readiness_probe: Probe (optional)

        :param startup_probe: startup_probe attribute
        :type startup_probe: Probe (optional)

        :param stdin: 是否分配标准输入缓冲区，默认false
        :type stdin: bool (optional)

        :param stdin_once: 标准输入流多会话是否保持开启，默认false
        :type stdin_once: bool (optional)

        :param tty: 是否开启交互（/bin/bash时需设为true），默认false
        :type tty: bool (optional)

        :param security_context: security_context attribute
        :type security_context: ContainerSecurityContext (optional)
        """
        super().__init__()
        self.name = name
        self.image = image
        self.memory = memory
        self.cpu = cpu
        self.gpu = gpu
        self.working_dir = working_dir
        self.image_pull_policy = image_pull_policy
        self.commands = commands
        self.args = args
        self.volume_mounts = volume_mounts
        self.ports = ports
        self.environment_vars = environment_vars
        self.liveness_probe = liveness_probe
        self.readiness_probe = readiness_probe
        self.startup_probe = startup_probe
        self.stdin = stdin
        self.stdin_once = stdin_once
        self.tty = tty
        self.security_context = security_context

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
        if self.memory is not None:
            result['memory'] = self.memory
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.gpu is not None:
            result['gpu'] = self.gpu
        if self.working_dir is not None:
            result['workingDir'] = self.working_dir
        if self.image_pull_policy is not None:
            result['imagePullPolicy'] = self.image_pull_policy
        if self.commands is not None:
            result['commands'] = self.commands
        if self.args is not None:
            result['args'] = self.args
        if self.volume_mounts is not None:
            result['volumeMounts'] = [i.to_dict() for i in self.volume_mounts]
        if self.ports is not None:
            result['ports'] = [i.to_dict() for i in self.ports]
        if self.environment_vars is not None:
            result['environmentVars'] = [i.to_dict() for i in self.environment_vars]
        if self.liveness_probe is not None:
            result['livenessProbe'] = self.liveness_probe.to_dict()
        if self.readiness_probe is not None:
            result['readinessProbe'] = self.readiness_probe.to_dict()
        if self.startup_probe is not None:
            result['startupProbe'] = self.startup_probe.to_dict()
        if self.stdin is not None:
            result['stdin'] = self.stdin
        if self.stdin_once is not None:
            result['stdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['tty'] = self.tty
        if self.security_context is not None:
            result['securityContext'] = self.security_context.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Container

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')
        if m.get('workingDir') is not None:
            self.working_dir = m.get('workingDir')
        if m.get('imagePullPolicy') is not None:
            self.image_pull_policy = m.get('imagePullPolicy')
        if m.get('commands') is not None:
            self.commands = m.get('commands')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('volumeMounts') is not None:
            self.volume_mounts = [VolumeMount().from_dict(i) for i in m.get('volumeMounts')]
        if m.get('ports') is not None:
            self.ports = [Port().from_dict(i) for i in m.get('ports')]
        if m.get('environmentVars') is not None:
            self.environment_vars = [Environment().from_dict(i) for i in m.get('environmentVars')]
        if m.get('livenessProbe') is not None:
            self.liveness_probe = Probe().from_dict(m.get('livenessProbe'))
        if m.get('readinessProbe') is not None:
            self.readiness_probe = Probe().from_dict(m.get('readinessProbe'))
        if m.get('startupProbe') is not None:
            self.startup_probe = Probe().from_dict(m.get('startupProbe'))
        if m.get('stdin') is not None:
            self.stdin = m.get('stdin')
        if m.get('stdinOnce') is not None:
            self.stdin_once = m.get('stdinOnce')
        if m.get('tty') is not None:
            self.tty = m.get('tty')
        if m.get('securityContext') is not None:
            self.security_context = ContainerSecurityContext().from_dict(m.get('securityContext'))
        return self
