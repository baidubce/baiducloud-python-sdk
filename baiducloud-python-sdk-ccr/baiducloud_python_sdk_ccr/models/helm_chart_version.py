"""
HelmChartVersion information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HelmChartVersion(AbstractModel):
    """
    HelmChartVersion
    """

    def __init__(
        self,
        name=None,
        description=None,
        api_version=None,
        app_version=None,
        version=None,
        urls=None,
        digest=None,
        engine=None,
        home=None,
        icon=None,
        sources=None,
        created=None,
        deprecated=None,
        removed=None,
        maintainers=None,
    ):
        """
        Initialize HelmChartVersion instance.

        :param name: Chart 包的名称
        :type name: str (optional)

        :param description: 描述信息
        :type description: str (optional)

        :param api_version: API 版本号
        :type api_version: str (optional)

        :param app_version: 包含的应用程序版本
        :type app_version: str (optional)

        :param version: Chart 包版本号
        :type version: str (optional)

        :param urls: Chart 包文件的 URL 列表
        :type urls: List[str] (optional)

        :param digest: Chart 摘要
        :type digest: str (optional)

        :param engine: 模板引擎名称
        :type engine: str (optional)

        :param home: Chart 主页的 URL 地址
        :type home: str (optional)

        :param icon: Chart 图标的地址
        :type icon: str (optional)

        :param sources: Chart 包含的源代码 URL 列表
        :type sources: List[str] (optional)

        :param created: 版本创建时间
        :type created: str (optional)

        :param deprecated: 是否弃用
        :type deprecated: bool (optional)

        :param removed: 是否删除
        :type removed: bool (optional)

        :param maintainers: 维护者信息
        :type maintainers: List[str] (optional)
        """
        super().__init__()
        self.name = name
        self.description = description
        self.api_version = api_version
        self.app_version = app_version
        self.version = version
        self.urls = urls
        self.digest = digest
        self.engine = engine
        self.home = home
        self.icon = icon
        self.sources = sources
        self.created = created
        self.deprecated = deprecated
        self.removed = removed
        self.maintainers = maintainers

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
        if self.description is not None:
            result['description'] = self.description
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.version is not None:
            result['version'] = self.version
        if self.urls is not None:
            result['urls'] = self.urls
        if self.digest is not None:
            result['digest'] = self.digest
        if self.engine is not None:
            result['engine'] = self.engine
        if self.home is not None:
            result['home'] = self.home
        if self.icon is not None:
            result['icon'] = self.icon
        if self.sources is not None:
            result['sources'] = self.sources
        if self.created is not None:
            result['created'] = self.created
        if self.deprecated is not None:
            result['deprecated'] = self.deprecated
        if self.removed is not None:
            result['removed'] = self.removed
        if self.maintainers is not None:
            result['maintainers'] = self.maintainers
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HelmChartVersion

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('urls') is not None:
            self.urls = m.get('urls')
        if m.get('digest') is not None:
            self.digest = m.get('digest')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('home') is not None:
            self.home = m.get('home')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('sources') is not None:
            self.sources = m.get('sources')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('deprecated') is not None:
            self.deprecated = m.get('deprecated')
        if m.get('removed') is not None:
            self.removed = m.get('removed')
        if m.get('maintainers') is not None:
            self.maintainers = m.get('maintainers')
        return self
