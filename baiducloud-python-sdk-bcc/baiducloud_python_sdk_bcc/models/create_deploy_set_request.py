"""
Request entity for CreateDeploySetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateDeploySetRequest(AbstractModel):
    """
    Request entity for CreateDeploySetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name=None, desc=None, strategy=None, concurrency=None):
        """
        Initialize CreateDeploySetRequest request entity.

        :param name: 部署集名字
        :type name: str (optional)

        :param desc: desc parameter
        :type desc: str (optional)

        :param strategy: 部署集策略（HOST_HA:宿主机, RACK_HA:机架, TOR_HA:交换机）
        :type strategy: str (optional)

        :param concurrency: 部署集并发度
        :type concurrency: int (optional)
        """
        super().__init__()
        self.name = name
        self.desc = desc
        self.strategy = strategy
        self.concurrency = concurrency

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
        if self.desc is not None:
            result['desc'] = self.desc
        if self.strategy is not None:
            result['strategy'] = self.strategy
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDeploySetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        return self
