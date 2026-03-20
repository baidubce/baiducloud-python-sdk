"""
Request entity for StartEipAutoRenewRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class StartEipAutoRenewRequest(AbstractModel):
    """
    Request entity for StartEipAutoRenewRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eip, client_token=None, auto_renew_time_unit=None, auto_renew_time=None):
        """
        Initialize StartEipAutoRenewRequest request entity.

        :param eip: eip parameter
        :type eip: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param auto_renew_time_unit: 取值为 month 获 year （默认 month）
        :type auto_renew_time_unit: str (optional)

        :param auto_renew_time: 根据autoRenewTimeUnit的取值有不同的范围，month 为1到9，year 为1到3
        :type auto_renew_time: int (optional)
        """
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time

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
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: StartEipAutoRenewRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        return self
