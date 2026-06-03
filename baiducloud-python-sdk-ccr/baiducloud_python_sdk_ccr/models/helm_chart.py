"""
HelmChart information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HelmChart(AbstractModel):
    """
    HelmChart
    """

    def __init__(
        self,
        name=None,
        total_versions=None,
        latest_version=None,
        home=None,
        icon=None,
        deprecated=None,
        created=None,
        updated=None,
    ):
        """
        Initialize HelmChart instance.

        :param name: Chart 名称
        :type name: str (optional)

        :param total_versions: 版本个数
        :type total_versions: int (optional)

        :param latest_version: 最新版本号
        :type latest_version: str (optional)

        :param home: Chart 主页的 URL 地址
        :type home: str (optional)

        :param icon: Chart 图标的地址
        :type icon: str (optional)

        :param deprecated: 是否弃用
        :type deprecated: bool (optional)

        :param created: 创建时间
        :type created: str (optional)

        :param updated: 更新时间
        :type updated: str (optional)
        """
        super().__init__()
        self.name = name
        self.total_versions = total_versions
        self.latest_version = latest_version
        self.home = home
        self.icon = icon
        self.deprecated = deprecated
        self.created = created
        self.updated = updated

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
        if self.name is not None:
            result['name'] = self.name
        if self.total_versions is not None:
            result['totalVersions'] = self.total_versions
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.home is not None:
            result['home'] = self.home
        if self.icon is not None:
            result['icon'] = self.icon
        if self.deprecated is not None:
            result['deprecated'] = self.deprecated
        if self.created is not None:
            result['created'] = self.created
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HelmChart

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalVersions') is not None:
            self.total_versions = m.get('totalVersions')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('home') is not None:
            self.home = m.get('home')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('deprecated') is not None:
            self.deprecated = m.get('deprecated')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self
