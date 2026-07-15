"""
Request entity for BatchGetAgentRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cloudassistant.models.host import Host


class BatchGetAgentRequest(AbstractModel):
    """
    Request entity for BatchGetAgentRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, hosts):
        """
        Initialize BatchGetAgentRequest request entity.

        :param hosts: 虚机列表
        :type hosts: List[Host] (required)
        """
        super().__init__()
        self.hosts = hosts

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
        if self.hosts is not None:
            result['hosts'] = [i.to_dict() for i in self.hosts]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchGetAgentRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('hosts') is not None:
            self.hosts = [Host().from_dict(i) for i in m.get('hosts')]
        return self
