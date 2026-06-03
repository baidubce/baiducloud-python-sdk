"""
ArtifactScanOverview information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ArtifactScanOverview(AbstractModel):
    """
    ArtifactScanOverview
    """

    def __init__(
        self, description=None, fix_version=None, id=None, links=None, package=None, severity=None, version=None
    ):
        """
        Initialize ArtifactScanOverview instance.

        :param description: 缺陷简介
        :type description: str (optional)

        :param fix_version: 修复版本
        :type fix_version: str (optional)

        :param id: 缺陷码
        :type id: str (optional)

        :param links: 缺陷详情页面链接
        :type links: List[str] (optional)

        :param package: 组件
        :type package: str (optional)

        :param severity: 严重程度
        :type severity: str (optional)

        :param version: 当前版本
        :type version: str (optional)
        """
        super().__init__()
        self.description = description
        self.fix_version = fix_version
        self.id = id
        self.links = links
        self.package = package
        self.severity = severity
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
        if self.description is not None:
            result['description'] = self.description
        if self.fix_version is not None:
            result['fixVersion'] = self.fix_version
        if self.id is not None:
            result['id'] = self.id
        if self.links is not None:
            result['links'] = self.links
        if self.package is not None:
            result['package'] = self.package
        if self.severity is not None:
            result['severity'] = self.severity
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
        :rtype: ArtifactScanOverview

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('fixVersion') is not None:
            self.fix_version = m.get('fixVersion')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('links') is not None:
            self.links = m.get('links')
        if m.get('package') is not None:
            self.package = m.get('package')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self
