"""
RetryPolicy information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RetryPolicy(AbstractModel):
    """
    RetryPolicy
    """

    def __init__(self, enabled=None, retry_conditions=None, num_retries=None):
        """
        Initialize RetryPolicy instance.

        :param enabled: 是否启用
        :type enabled: bool (optional)

        :param retry_conditions: 重试条件
        :type retry_conditions: str (optional)

        :param num_retries: 重试次数
        :type num_retries: int (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.retry_conditions = retry_conditions
        self.num_retries = num_retries

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
        if self.retry_conditions is not None:
            result['retryConditions'] = self.retry_conditions
        if self.num_retries is not None:
            result['numRetries'] = self.num_retries
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RetryPolicy

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('retryConditions') is not None:
            self.retry_conditions = m.get('retryConditions')
        if m.get('numRetries') is not None:
            self.num_retries = m.get('numRetries')
        return self
