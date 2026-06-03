"""
InstanceStatistic information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceStatistic(AbstractModel):
    """
    InstanceStatistic
    """

    def __init__(self, repo=None, chart=None, namespace=None, vpc=None, storage=None):
        """
        Initialize InstanceStatistic instance.

        :param repo: 镜像仓库个数
        :type repo: int (optional)

        :param chart: Chart 个数
        :type chart: int (optional)

        :param namespace: 命名空间个数
        :type namespace: int (optional)

        :param vpc: 已关联私有网络个数
        :type vpc: int (optional)

        :param storage: BOS 存储空间大小，单位：字节
        :type storage: int (optional)
        """
        super().__init__()
        self.repo = repo
        self.chart = chart
        self.namespace = namespace
        self.vpc = vpc
        self.storage = storage

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
        if self.repo is not None:
            result['repo'] = self.repo
        if self.chart is not None:
            result['chart'] = self.chart
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.vpc is not None:
            result['vpc'] = self.vpc
        if self.storage is not None:
            result['storage'] = self.storage
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceStatistic

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('repo') is not None:
            self.repo = m.get('repo')
        if m.get('chart') is not None:
            self.chart = m.get('chart')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('vpc') is not None:
            self.vpc = m.get('vpc')
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        return self
