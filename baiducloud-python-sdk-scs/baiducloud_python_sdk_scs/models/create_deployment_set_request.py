"""
Request entity for CreateDeploymentSetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateDeploymentSetRequest(AbstractModel):
    """
    Request entity for CreateDeploymentSetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, strategy, concurrency, desc=None):
        """
        Initialize CreateDeploymentSetRequest request entity.

        :param name: 部署集名称。
        :type name: str (required)

        :param desc: 备注。
        :type desc: str (optional)

        :param strategy: 策略。默认值：HOST_HA。
        :type strategy: str (required)

        :param concurrency: 并发度。取值范围：1-127。默认值：20。
        :type concurrency: int (required)
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
        :rtype: CreateDeploymentSetRequest

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
