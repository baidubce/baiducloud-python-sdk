"""
Request entity for BindServiceTagRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.tag import Tag


class BindServiceTagRequest(AbstractModel):
    """
    Request entity for BindServiceTagRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, service_name, service_id, tags):
        """
        Initialize BindServiceTagRequest request entity.

        :param service_name: 应用名
        :type service_name: str (required)

        :param service_id: 应用ID
        :type service_id: str (required)

        :param tags: 绑定标签列表，只支持更新全量标签，不支持更新部分标签
        :type tags: List[Tag] (required)
        """
        super().__init__()
        self.service_name = service_name
        self.service_id = service_id
        self.tags = tags

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
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindServiceTagRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
