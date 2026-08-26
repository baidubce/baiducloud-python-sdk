"""
ResourceCatalog information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.resource_catalog_item import ResourceCatalogItem


class ResourceCatalog(AbstractModel):
    """
    ResourceCatalog
    """

    def __init__(self, scope=None, scope_label=None, resources=None, regions=None):
        """
        Initialize ResourceCatalog instance.

        :param scope: 云产品标识，可作为指标查询接口的scope参数
        :type scope: str (optional)

        :param scope_label: 云产品显示名称，根据locale返回中文或英文名称
        :type scope_label: str (optional)

        :param resources: 云产品下的资源类型列表
        :type resources: List[ResourceCatalogItem] (optional)

        :param regions: 云产品适用的地域列表。仅配置了固定地域信息时返回；例如全局产品返回global
        :type regions: List[str] (optional)
        """
        super().__init__()
        self.scope = scope
        self.scope_label = scope_label
        self.resources = resources
        self.regions = regions

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
        if self.scope is not None:
            result['scope'] = self.scope
        if self.scope_label is not None:
            result['scopeLabel'] = self.scope_label
        if self.resources is not None:
            result['resources'] = [i.to_dict() for i in self.resources]
        if self.regions is not None:
            result['regions'] = self.regions
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResourceCatalog

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scopeLabel') is not None:
            self.scope_label = m.get('scopeLabel')
        if m.get('resources') is not None:
            self.resources = [ResourceCatalogItem().from_dict(i) for i in m.get('resources')]
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        return self
