"""
InstanceQuota information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceQuota(AbstractModel):
    """
    InstanceQuota
    """

    def __init__(self, repo=None, chart=None, namespace=None, vpc=None):
        """
        Initialize InstanceQuota instance.

        :param repo: 镜像仓库个数限额
        :type repo: int (optional)

        :param chart: Chart 个数限额
        :type chart: int (optional)

        :param namespace: 命名空间个数限额
        :type namespace: int (optional)

        :param vpc: 可关联私有网络个数限额
        :type vpc: int (optional)
        """
        super().__init__()
        self.repo = repo
        self.chart = chart
        self.namespace = namespace
        self.vpc = vpc

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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceQuota

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
        return self
