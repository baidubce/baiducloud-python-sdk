"""
VdbAutoRenewRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VdbAutoRenewRule(AbstractModel):
    """
    VdbAutoRenewRule
    """

    def __init__(self, renew_time=None, renew_time_unit=None):
        """
        Initialize VdbAutoRenewRule instance.

        :param renew_time:
        :type renew_time: int (optional)

        :param renew_time_unit:
        :type renew_time_unit: str (optional)
        """
        super().__init__()
        self.renew_time = renew_time
        self.renew_time_unit = renew_time_unit

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
        if self.renew_time is not None:
            result['renewTime'] = self.renew_time
        if self.renew_time_unit is not None:
            result['renewTimeUnit'] = self.renew_time_unit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VdbAutoRenewRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('renewTime') is not None:
            self.renew_time = m.get('renewTime')
        if m.get('renewTimeUnit') is not None:
            self.renew_time_unit = m.get('renewTimeUnit')
        return self
