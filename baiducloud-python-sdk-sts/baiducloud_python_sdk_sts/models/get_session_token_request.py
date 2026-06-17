"""
Request entity for GetSessionTokenRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetSessionTokenRequest(AbstractModel):
    """
    Request entity for GetSessionTokenRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, duration_seconds=None, access_control_list=None, attachment=None):
        """
        Initialize GetSessionTokenRequest request entity.

        :param duration_seconds: duration_seconds parameter
        :type duration_seconds: str (optional)

        :param access_control_list: 为临时身份凭证绑定的权限
        :type access_control_list: str (optional)

        :param attachment: 业务方绑定在credential上的一些信息
        :type attachment: str (optional)
        """
        super().__init__()
        self.duration_seconds = duration_seconds
        self.access_control_list = access_control_list
        self.attachment = attachment

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
        if self.access_control_list is not None:
            result['accessControlList'] = self.access_control_list
        if self.attachment is not None:
            result['attachment'] = self.attachment
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetSessionTokenRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('durationSeconds') is not None:
            self.duration_seconds = m.get('durationSeconds')
        if m.get('accessControlList') is not None:
            self.access_control_list = m.get('accessControlList')
        if m.get('attachment') is not None:
            self.attachment = m.get('attachment')
        return self
