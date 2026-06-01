"""
ServiceTopoConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ServiceTopoConfig(AbstractModel):
    """
    ServiceTopoConfig
    """

    def __init__(self, var_global=None, request_seconds_threshold=None, error_rate_threshold=None):
        """
        Initialize ServiceTopoConfig instance.

        :param var_global:
        :type var_global: bool (optional)

        :param request_seconds_threshold:
        :type request_seconds_threshold: float (optional)

        :param error_rate_threshold:
        :type error_rate_threshold: float (optional)
        """
        super().__init__()
        self.var_global = var_global
        self.request_seconds_threshold = request_seconds_threshold
        self.error_rate_threshold = error_rate_threshold

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
        if self.var_global is not None:
            result['global'] = self.var_global
        if self.request_seconds_threshold is not None:
            result['requestSecondsThreshold'] = self.request_seconds_threshold
        if self.error_rate_threshold is not None:
            result['errorRateThreshold'] = self.error_rate_threshold
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ServiceTopoConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('global') is not None:
            self.var_global = m.get('global')
        if m.get('requestSecondsThreshold') is not None:
            self.request_seconds_threshold = m.get('requestSecondsThreshold')
        if m.get('errorRateThreshold') is not None:
            self.error_rate_threshold = m.get('errorRateThreshold')
        return self
