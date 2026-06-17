"""
DisableTime information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DisableTime(AbstractModel):
    """
    DisableTime
    """

    def __init__(self, bls_from=None, to=None):
        """
        Initialize DisableTime instance.

        :param bls_from: 报警屏蔽开始时间
        :type bls_from: datetime (optional)

        :param to: 报警屏蔽结束时间
        :type to: datetime (optional)
        """
        super().__init__()
        self.bls_from = bls_from
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
        if self.bls_from is not None:
            result['from'] = self.bls_from
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
        :rtype: DisableTime

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('from') is not None:
            self.bls_from = m.get('from')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self
