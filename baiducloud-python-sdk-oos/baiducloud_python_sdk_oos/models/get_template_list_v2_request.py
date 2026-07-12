"""
Request entity for GetTemplateListV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetTemplateListV2Request(AbstractModel):
    """
    Request entity for GetTemplateListV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        page_no,
        page_size,
        locale=None,
        namespace=None,
        name=None,
        id=None,
        type=None,
        sort=None,
        ascending=None,
        supported_instance_type=None,
    ):
        """
        Initialize GetTemplateListV2Request request entity.

        :param locale: locale parameter
        :type locale: str (optional)

        :param namespace: 名称空间，默认 default
        :type namespace: str (optional)

        :param name: 模板名称
        :type name: str (optional)

        :param id: 模板 ID
        :type id: str (optional)

        :param type: 模板类型 INDIVIDUAL/GLOBAL
        :type type: str (optional)

        :param sort: 排序字段，默认为创建时间
        :type sort: str (optional)

        :param ascending: 是否升序，默认 false
        :type ascending: bool (optional)

        :param page_no: 页数，从 1 开始计数
        :type page_no: int (required)

        :param page_size: 每页展示数量，最大值：100
        :type page_size: int (required)

        :param supported_instance_type: 支持的实例类型筛选
        :type supported_instance_type: str (optional)
        """
        super().__init__()
        self.locale = locale
        self.namespace = namespace
        self.name = name
        self.id = id
        self.type = type
        self.sort = sort
        self.ascending = ascending
        self.page_no = page_no
        self.page_size = page_size
        self.supported_instance_type = supported_instance_type

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
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.type is not None:
            result['type'] = self.type
        if self.sort is not None:
            result['sort'] = self.sort
        if self.ascending is not None:
            result['ascending'] = self.ascending
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.supported_instance_type is not None:
            result['supportedInstanceType'] = self.supported_instance_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetTemplateListV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('ascending') is not None:
            self.ascending = m.get('ascending')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('supportedInstanceType') is not None:
            self.supported_instance_type = m.get('supportedInstanceType')
        return self
