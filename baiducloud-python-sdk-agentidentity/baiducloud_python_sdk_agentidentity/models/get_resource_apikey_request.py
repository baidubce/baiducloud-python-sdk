"""
Request entity for GetResourceApikeyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_core.annotation import host


class GetResourceApikeyRequest(AbstractModel):
    """
    Request entity for GetResourceApikeyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, x_bce_workload_access_token, name, workload_access_token=None):
        """
        Initialize GetResourceApikeyRequest request entity.

        :param x_bce_workload_access_token: x_bce_workload_access_token parameter
        :type x_bce_workload_access_token: str (required)

        :param name: 凭证提供方名称
        :type name: str (required)

        :param workload_access_token: WAT 令牌，也可通过 Header 传递
        :type workload_access_token: str (optional)
        """
        super().__init__()
        self._x_bce_workload_access_token = x_bce_workload_access_token
        self.name = name
        self.workload_access_token = workload_access_token

    @property
    @host
    def x_bce_workload_access_token(self):
        """x_bce_workload_access_token property"""
        return self._x_bce_workload_access_token

    @x_bce_workload_access_token.setter
    def x_bce_workload_access_token(self, value):
        """Set x_bce_workload_access_token value"""
        self._x_bce_workload_access_token = value

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
        if self.name is not None:
            result['name'] = self.name
        if self.workload_access_token is not None:
            result['workloadAccessToken'] = self.workload_access_token
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetResourceApikeyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('xBceWorkloadAccessToken') is not None:
            self.x_bce_workload_access_token = m.get('xBceWorkloadAccessToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('workloadAccessToken') is not None:
            self.workload_access_token = m.get('workloadAccessToken')
        return self
