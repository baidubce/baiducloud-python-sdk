"""
Request entity for RenewTbspRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RenewTbspRequest(AbstractModel):
    """
    Request entity for RenewTbspRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, renew_time, renew_time_unit, client_token=None):
        """
        Initialize RenewTbspRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param renew_time: 续费周期（按月:1-9； 按年:1-3）
        :type renew_time: int (required)

        :param renew_time_unit: 续费周期单位（DAY/MONTH/YEAR)
        :type renew_time_unit: str (required)
        """
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.renew_time = renew_time
        self.renew_time_unit = renew_time_unit

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
        if self.renew_time is not None:
            result['renewTime'] = self.renew_time
        if self.renew_time_unit is not None:
            result['renewTimeUnit'] = self.renew_time_unit
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RenewTbspRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('renewTime') is not None:
            self.renew_time = m.get('renewTime')
        if m.get('renewTimeUnit') is not None:
            self.renew_time_unit = m.get('renewTimeUnit')
        return self
