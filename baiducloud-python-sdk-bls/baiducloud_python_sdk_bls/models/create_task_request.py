"""
Request entity for CreateTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.task_config import TaskConfig
from baiducloud_python_sdk_bls.models.host import Host
from baiducloud_python_sdk_bls.models.tag import Tag


class CreateTaskRequest(AbstractModel):
    """
    Request entity for CreateTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, config, hosts=None, tags=None):
        """
        Initialize CreateTaskRequest request entity.

        :param name: 传输任务名字
        :type name: str (required)

        :param config: config parameter
        :type config: TaskConfig (required)

        :param hosts: 运行任务的主机列表
        :type hosts: List[Host] (optional)

        :param tags: 待创建的标签列表，具体参数格式参见下述
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.name = name
        self.config = config
        self.hosts = hosts
        self.tags = tags

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
        if self.name is not None:
            result['name'] = self.name
        if self.config is not None:
            result['config'] = self.config.to_dict()
        if self.hosts is not None:
            result['hosts'] = [i.to_dict() for i in self.hosts]
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('config') is not None:
            self.config = TaskConfig().from_dict(m.get('config'))
        if m.get('hosts') is not None:
            self.hosts = [Host().from_dict(i) for i in m.get('hosts')]
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
