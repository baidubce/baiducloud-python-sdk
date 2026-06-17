"""
Request entity for UpdateLogStoreViewRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.log_store import LogStore


class UpdateLogStoreViewRequest(AbstractModel):
    """
    Request entity for UpdateLogStoreViewRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, logstores, project=None):
        """
        Initialize UpdateLogStoreViewRequest request entity.

        :param project: 日志组名称，默认default
        :type project: str (optional)

        :param name: 日志视图名称
        :type name: str (required)

        :param logstores: 与日志视图相关联的日志集列表
        :type logstores: List[LogStore] (required)
        """
        super().__init__()
        self.project = project
        self.name = name
        self.logstores = logstores

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
        if self.project is not None:
            result['project'] = self.project
        if self.name is not None:
            result['name'] = self.name
        if self.logstores is not None:
            result['logstores'] = [i.to_dict() for i in self.logstores]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateLogStoreViewRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('logstores') is not None:
            self.logstores = [LogStore().from_dict(i) for i in m.get('logstores')]
        return self
