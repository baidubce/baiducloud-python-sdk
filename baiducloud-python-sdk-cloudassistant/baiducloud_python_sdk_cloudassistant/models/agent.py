"""
Agent information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cloudassistant.models.host import Host


class Agent(AbstractModel):
    """
    Agent
    """

    def __init__(self, host=None, state=None, version=None):
        """
        Initialize Agent instance.

        :param host: host attribute
        :type host: Host (optional)

        :param state: bsm-agent状态。枚举值：ONLINE（在线），OFFLINE（离线）
        :type state: str (optional)

        :param version: bsm-agent版本号，如4.2.0.1
        :type version: str (optional)
        """
        super().__init__()
        self.host = host
        self.state = state
        self.version = version

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
        if self.host is not None:
            result['host'] = self.host.to_dict()
        if self.state is not None:
            result['state'] = self.state
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Agent

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('host') is not None:
            self.host = Host().from_dict(m.get('host'))
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self
