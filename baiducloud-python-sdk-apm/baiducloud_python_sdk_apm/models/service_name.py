"""
ServiceName information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ServiceName(AbstractModel):
    """
    ServiceName
    """

    def __init__(self, service_name=None, service_id=None, service_display_name=None, language=None, include_llm=None):
        """
        Initialize ServiceName instance.

        :param service_name: 应用名称
        :type service_name: str (optional)

        :param service_id: 应用ID
        :type service_id: str (optional)

        :param service_display_name: 部署名称
        :type service_display_name: str (optional)

        :param language: 语言
        :type language: str (optional)

        :param include_llm: 是否为大模型应用
        :type include_llm: bool (optional)
        """
        super().__init__()
        self.service_name = service_name
        self.service_id = service_id
        self.service_display_name = service_display_name
        self.language = language
        self.include_llm = include_llm

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
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_display_name is not None:
            result['serviceDisplayName'] = self.service_display_name
        if self.language is not None:
            result['language'] = self.language
        if self.include_llm is not None:
            result['includeLLM'] = self.include_llm
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ServiceName

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceDisplayName') is not None:
            self.service_display_name = m.get('serviceDisplayName')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('includeLLM') is not None:
            self.include_llm = m.get('includeLLM')
        return self
