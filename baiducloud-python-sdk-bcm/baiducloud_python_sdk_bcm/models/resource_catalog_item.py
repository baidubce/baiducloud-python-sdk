"""
ResourceCatalogItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResourceCatalogItem(AbstractModel):
    """
    ResourceCatalogItem
    """

    def __init__(self, resource_type=None, resource_type_label=None):
        """
        Initialize ResourceCatalogItem instance.

        :param resource_type: 资源类型标识，可作为指标查询接口的resourceType参数
        :type resource_type: str (optional)

        :param resource_type_label: 资源类型显示名称，根据locale返回中文或英文名称
        :type resource_type_label: str (optional)
        """
        super().__init__()
        self.resource_type = resource_type
        self.resource_type_label = resource_type_label

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
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.resource_type_label is not None:
            result['resourceTypeLabel'] = self.resource_type_label
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResourceCatalogItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('resourceTypeLabel') is not None:
            self.resource_type_label = m.get('resourceTypeLabel')
        return self
