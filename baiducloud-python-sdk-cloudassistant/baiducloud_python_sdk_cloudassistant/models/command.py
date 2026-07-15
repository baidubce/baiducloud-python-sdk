"""
Command information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cloudassistant.models.parameter import Parameter


class Command(AbstractModel):
    """
    Command
    """

    def __init__(
        self,
        type=None,
        content=None,
        scope=None,
        enable_parameter=None,
        parameters=None,
        user=None,
        work_dir=None,
        exec_params=None,
        wait_on_agent_milli=None,
    ):
        """
        Initialize Command instance.

        :param type: 脚本类型
        :type type: str (optional)

        :param content: 命令脚本内容
        :type content: str (optional)

        :param scope: 命令可见范围。GLOBAL公共命令，INDIVIDUAL个人命令
        :type scope: str (optional)

        :param enable_parameter: 命令是否包含参数
        :type enable_parameter: bool (optional)

        :param parameters: 命令参数列表
        :type parameters: List[Parameter] (optional)

        :param user: 命令在虚机的执行用户
        :type user: str (optional)

        :param work_dir: 命令在虚机的执行路径
        :type work_dir: str (optional)

        :param exec_params: 命令执行时的实际参数值，仅在查询 ActionRun 详情时返回
        :type exec_params: object (optional)

        :param wait_on_agent_milli: Agent等待时间（毫秒）
        :type wait_on_agent_milli: int (optional)
        """
        super().__init__()
        self.type = type
        self.content = content
        self.scope = scope
        self.enable_parameter = enable_parameter
        self.parameters = parameters
        self.user = user
        self.work_dir = work_dir
        self.exec_params = exec_params
        self.wait_on_agent_milli = wait_on_agent_milli

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
        if self.type is not None:
            result['type'] = self.type
        if self.content is not None:
            result['content'] = self.content
        if self.scope is not None:
            result['scope'] = self.scope
        if self.enable_parameter is not None:
            result['enableParameter'] = self.enable_parameter
        if self.parameters is not None:
            result['parameters'] = [i.to_dict() for i in self.parameters]
        if self.user is not None:
            result['user'] = self.user
        if self.work_dir is not None:
            result['workDir'] = self.work_dir
        if self.exec_params is not None:
            result['execParams'] = self.exec_params
        if self.wait_on_agent_milli is not None:
            result['waitOnAgentMilli'] = self.wait_on_agent_milli
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Command

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('enableParameter') is not None:
            self.enable_parameter = m.get('enableParameter')
        if m.get('parameters') is not None:
            self.parameters = [Parameter().from_dict(i) for i in m.get('parameters')]
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('workDir') is not None:
            self.work_dir = m.get('workDir')
        if m.get('execParams') is not None:
            self.exec_params = m.get('execParams')
        if m.get('waitOnAgentMilli') is not None:
            self.wait_on_agent_milli = m.get('waitOnAgentMilli')
        return self
