"""
Request entity for CreateCustomScrapeTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateCustomScrapeTaskRequest(AbstractModel):
    """
    Request entity for CreateCustomScrapeTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, agent_id, config):
        """
        Initialize CreateCustomScrapeTaskRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param agent_id: agent_id parameter
        :type agent_id: str (required)

        :param config: 抓取任务配置，示例值见请求示例
        :type config: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.agent_id = agent_id
        self.config = config

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
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateCustomScrapeTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('config') is not None:
            self.config = m.get('config')
        return self
