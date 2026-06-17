"""
LogStore information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.extend import Extend


class LogStore(AbstractModel):
    """
    LogStore
    """

    def __init__(self, project=None, log_store_name=None, log_store_id=None, region=None, name=None, extends=None):
        """
        Initialize LogStore instance.

        :param project: 日志集所属的日志组名称
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)

        :param log_store_id: 监控对象ID
        :type log_store_id: str (optional)

        :param region: 日志集所在的区域
        :type region: str (optional)

        :param name: 日志集的名称
        :type name: str (optional)

        :param extends: 允许对日志集中的索引列进行别名
        :type extends: List[Extend] (optional)
        """
        super().__init__()
        self.project = project
        self.log_store_name = log_store_name
        self.log_store_id = log_store_id
        self.region = region
        self.name = name
        self.extends = extends

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
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.log_store_id is not None:
            result['logStoreId'] = self.log_store_id
        if self.region is not None:
            result['region'] = self.region
        if self.name is not None:
            result['name'] = self.name
        if self.extends is not None:
            result['extends'] = [i.to_dict() for i in self.extends]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogStore

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('logStoreId') is not None:
            self.log_store_id = m.get('logStoreId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('extends') is not None:
            self.extends = [Extend().from_dict(i) for i in m.get('extends')]
        return self
