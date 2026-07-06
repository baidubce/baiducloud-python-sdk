"""
AdvancedSettings information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AdvancedSettings(AbstractModel):
    """
    AdvancedSettings
    """

    def __init__(self, runtime_env=None, submitter_backoff_limit=None):
        """
        Initialize AdvancedSettings instance.

        :param runtime_env: 否
        :type runtime_env: str (optional)

        :param submitter_backoff_limit: 否
        :type submitter_backoff_limit: int (optional)
        """
        super().__init__()
        self.runtime_env = runtime_env
        self.submitter_backoff_limit = submitter_backoff_limit

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
        if self.runtime_env is not None:
            result['runtimeEnv'] = self.runtime_env
        if self.submitter_backoff_limit is not None:
            result['SubmitterBackoffLimit'] = self.submitter_backoff_limit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AdvancedSettings

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('runtimeEnv') is not None:
            self.runtime_env = m.get('runtimeEnv')
        if m.get('SubmitterBackoffLimit') is not None:
            self.submitter_backoff_limit = m.get('SubmitterBackoffLimit')
        return self
