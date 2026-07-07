"""
Request entity for CompleteOauth2sessionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_core.annotation import host


class CompleteOauth2sessionRequest(AbstractModel):
    """
    Request entity for CompleteOauth2sessionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, x_bce_workload_access_token, session_uri, user_identifier, user_identifier_user_id, workload_access_token
    ):
        """
        Initialize CompleteOauth2sessionRequest request entity.

        :param x_bce_workload_access_token: x_bce_workload_access_token parameter
        :type x_bce_workload_access_token: str (required)

        :param session_uri: OAuth2 会话标识
        :type session_uri: str (required)

        :param user_identifier: 用户标识
        :type user_identifier: object (required)

        :param user_identifier_user_id: 用户 ID（当前仅支持 userId）
        :type user_identifier_user_id: str (required)

        :param workload_access_token: WAT（Body 传递，也可通过 Header 传递）
        :type workload_access_token: str (required)
        """
        super().__init__()
        self._x_bce_workload_access_token = x_bce_workload_access_token
        self.session_uri = session_uri
        self.user_identifier = user_identifier
        self.user_identifier_user_id = user_identifier_user_id
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
        if self.session_uri is not None:
            result['sessionUri'] = self.session_uri
        if self.user_identifier is not None:
            result['userIdentifier'] = self.user_identifier
        if self.user_identifier_user_id is not None:
            result['userIdentifier.userId'] = self.user_identifier_user_id
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
        :rtype: CompleteOauth2sessionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('xBceWorkloadAccessToken') is not None:
            self.x_bce_workload_access_token = m.get('xBceWorkloadAccessToken')
        if m.get('sessionUri') is not None:
            self.session_uri = m.get('sessionUri')
        if m.get('userIdentifier') is not None:
            self.user_identifier = m.get('userIdentifier')
        if m.get('userIdentifier.userId') is not None:
            self.user_identifier_user_id = m.get('userIdentifier.userId')
        if m.get('workloadAccessToken') is not None:
            self.workload_access_token = m.get('workloadAccessToken')
        return self
