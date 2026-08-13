"""
FallbackConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FallbackConfig(AbstractModel):
    """
    FallbackConfig
    """

    def __init__(self, enabled=None, service_name=None, model_name_mode=None, specified_model_name=None):
        """
        Initialize FallbackConfig instance.

        :param enabled: 是否启用 AI Fallback
        :type enabled: bool (optional)

        :param service_name: Fallback 服务名称
        :type service_name: str (optional)

        :param model_name_mode: 模型名称模式：passthrough、specify
        :type model_name_mode: str (optional)

        :param specified_model_name: modelNameMode 为 specify 时使用的固定模型名称
        :type specified_model_name: str (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.service_name = service_name
        self.model_name_mode = model_name_mode
        self.specified_model_name = specified_model_name

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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.model_name_mode is not None:
            result['modelNameMode'] = self.model_name_mode
        if self.specified_model_name is not None:
            result['specifiedModelName'] = self.specified_model_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FallbackConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('modelNameMode') is not None:
            self.model_name_mode = m.get('modelNameMode')
        if m.get('specifiedModelName') is not None:
            self.specified_model_name = m.get('specifiedModelName')
        return self
