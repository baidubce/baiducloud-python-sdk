"""
Request entity for ApplicationParameterTemplateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.cache_cluster_show_id_item import CacheClusterShowIdItem
from baiducloud_python_sdk_scs.models.parameters import Parameters


class ApplicationParameterTemplateRequest(AbstractModel):
    """
    Request entity for ApplicationParameterTemplateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, template_show_id, extra, cache_cluster_list=None, reboot_type=None, parameters=None):
        """
        Initialize ApplicationParameterTemplateRequest request entity.

        :param template_show_id: template_show_id parameter
        :type template_show_id: str (required)

        :param extra: 是否有额外的修改（0：无；1：有），没有修改的参数不需要传parameters
        :type extra: str (required)

        :param cache_cluster_list: 实例ID集合
        :type cache_cluster_list: List[CacheClusterShowIdItem] (optional)

        :param reboot_type: 是否需要重启（0 不重启 1 维护时间重启 2 立即重启 如果是热活的主集群的话不可以重启）
        :type reboot_type: int (optional)

        :param parameters: 参数模版中需要修改的参数，extra=1时有效
        :type parameters: List[Parameters] (optional)
        """
        super().__init__()
        self.template_show_id = template_show_id
        self.extra = extra
        self.cache_cluster_list = cache_cluster_list
        self.reboot_type = reboot_type
        self.parameters = parameters

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
        if self.extra is not None:
            result['extra'] = self.extra
        if self.cache_cluster_list is not None:
            result['cacheClusterList'] = [i.to_dict() for i in self.cache_cluster_list]
        if self.reboot_type is not None:
            result['rebootType'] = self.reboot_type
        if self.parameters is not None:
            result['parameters'] = [i.to_dict() for i in self.parameters]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ApplicationParameterTemplateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateShowId') is not None:
            self.template_show_id = m.get('templateShowId')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('cacheClusterList') is not None:
            self.cache_cluster_list = [CacheClusterShowIdItem().from_dict(i) for i in m.get('cacheClusterList')]
        if m.get('rebootType') is not None:
            self.reboot_type = m.get('rebootType')
        if m.get('parameters') is not None:
            self.parameters = [Parameters().from_dict(i) for i in m.get('parameters')]
        return self
