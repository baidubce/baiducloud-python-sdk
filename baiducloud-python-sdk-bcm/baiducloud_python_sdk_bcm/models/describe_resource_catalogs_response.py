"""
Request entity for DescribeResourceCatalogsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcm.models.resource_catalog import ResourceCatalog
from baiducloud_python_sdk_bcm.models.resource_catalog_item import ResourceCatalogItem


class DescribeResourceCatalogsResponse(BceResponse):
    """
    DescribeResourceCatalogsResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        catalogs=None,
        catalogs_scope=None,
        catalogs_scope_label=None,
        catalogs_resources=None,
        catalogs_resources_resource_type=None,
        catalogs_resources_resource_type_label=None,
        catalogs_regions=None,
    ):
        """
        Initialize DescribeResourceCatalogsResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 响应码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param catalogs: 云产品资源目录列表
        :type catalogs: List[ResourceCatalog] (optional)

        :param catalogs_scope: 云产品标识，可作为指标查询接口的scope参数
        :type catalogs_scope: str (optional)

        :param catalogs_scope_label: 云产品显示名称，根据locale返回中文或英文名称
        :type catalogs_scope_label: str (optional)

        :param catalogs_resources: 云产品下的资源类型列表
        :type catalogs_resources: List[ResourceCatalogItem] (optional)

        :param catalogs_resources_resource_type: 资源类型标识，可作为指标查询接口的resourceType参数
        :type catalogs_resources_resource_type: str (optional)

        :param catalogs_resources_resource_type_label: 资源类型显示名称，根据locale返回中文或英文名称
        :type catalogs_resources_resource_type_label: str (optional)

        :param catalogs_regions: 云产品适用的地域列表。仅配置了固定地域信息时返回；例如全局产品返回global
        :type catalogs_regions: List[str] (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.catalogs = catalogs
        self.catalogs_scope = catalogs_scope
        self.catalogs_scope_label = catalogs_scope_label
        self.catalogs_resources = catalogs_resources
        self.catalogs_resources_resource_type = catalogs_resources_resource_type
        self.catalogs_resources_resource_type_label = catalogs_resources_resource_type_label
        self.catalogs_regions = catalogs_regions

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.catalogs is not None:
            result['catalogs'] = [i.to_dict() for i in self.catalogs]
        if self.catalogs_scope is not None:
            result['catalogs[].scope'] = self.catalogs_scope
        if self.catalogs_scope_label is not None:
            result['catalogs[].scopeLabel'] = self.catalogs_scope_label
        if self.catalogs_resources is not None:
            result['catalogs[].resources'] = [i.to_dict() for i in self.catalogs_resources]
        if self.catalogs_resources_resource_type is not None:
            result['catalogs[].resources[].resourceType'] = self.catalogs_resources_resource_type
        if self.catalogs_resources_resource_type_label is not None:
            result['catalogs[].resources[].resourceTypeLabel'] = self.catalogs_resources_resource_type_label
        if self.catalogs_regions is not None:
            result['catalogs[].regions'] = self.catalogs_regions
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeResourceCatalogsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('catalogs') is not None:
            self.catalogs = [ResourceCatalog().from_dict(i) for i in m.get('catalogs')]
        if m.get('catalogs[].scope') is not None:
            self.catalogs_scope = m.get('catalogs[].scope')
        if m.get('catalogs[].scopeLabel') is not None:
            self.catalogs_scope_label = m.get('catalogs[].scopeLabel')
        if m.get('catalogs[].resources') is not None:
            self.catalogs_resources = [ResourceCatalogItem().from_dict(i) for i in m.get('catalogs[].resources')]
        if m.get('catalogs[].resources[].resourceType') is not None:
            self.catalogs_resources_resource_type = m.get('catalogs[].resources[].resourceType')
        if m.get('catalogs[].resources[].resourceTypeLabel') is not None:
            self.catalogs_resources_resource_type_label = m.get('catalogs[].resources[].resourceTypeLabel')
        if m.get('catalogs[].regions') is not None:
            self.catalogs_regions = m.get('catalogs[].regions')
        return self
