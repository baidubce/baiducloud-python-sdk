"""
SilencePeriod information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SilencePeriod(AbstractModel):
    """
    SilencePeriod
    """

    def __init__(self, bcm_from=None, to=None):
        """
        Initialize SilencePeriod instance.

        :param bcm_from: 静默开始时间，24小时制，格式：HH:mm:ss
        :type bcm_from: str (optional)

        :param to: 静默结束时间，24小时制，格式：HH:mm:ss
        :type to: str (optional)
        """
        super().__init__()
        self.bcm_from = bcm_from
        self.to = to

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
        if self.bcm_from is not None:
            result['from'] = self.bcm_from
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SilencePeriod

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('from') is not None:
            self.bcm_from = m.get('from')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self
