"""
Request entity for CheckBeforeCreateInstanceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.err_info import ErrInfo


class CheckBeforeCreateInstanceResponse(BceResponse):
    """
    CheckBeforeCreateInstanceResponse
    """

    def __init__(self, rapidfs_pass=None, err_info=None):
        """
        Initialize CheckBeforeCreateInstanceResponse response.

        :param rapidfs_pass: 是否通过校验
        :type rapidfs_pass: bool (optional)

        :param err_info: err_info field
        :type err_info: ErrInfo (optional)
        """
        super().__init__()
        self.rapidfs_pass = rapidfs_pass
        self.err_info = err_info

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.rapidfs_pass is not None:
            result['pass'] = self.rapidfs_pass
        if self.err_info is not None:
            result['errInfo'] = self.err_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckBeforeCreateInstanceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pass') is not None:
            self.rapidfs_pass = m.get('pass')
        if m.get('errInfo') is not None:
            self.err_info = ErrInfo().from_dict(m.get('errInfo'))
        return self
