"""
Request entity for SessionCodeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SessionCodeRequest(AbstractModel):
    """
    Request entity for SessionCodeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, type=None, min_code_length=None, max_code_length=None):
        """
        Initialize SessionCodeRequest request entity.

        :param type: 0：下发语音验证码和唇语验证码，默认类型；1：下发视频动作活体验证码
        :type type: str (optional)

        :param min_code_length: min_code_length parameter
        :type min_code_length: str (optional)

        :param max_code_length: max_code_length parameter
        :type max_code_length: str (optional)
        """
        super().__init__()
        self.type = type
        self.min_code_length = min_code_length
        self.max_code_length = max_code_length

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
        if self.type is not None:
            result['type'] = self.type
        if self.min_code_length is not None:
            result['min_code_length'] = self.min_code_length
        if self.max_code_length is not None:
            result['max_code_length'] = self.max_code_length
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SessionCodeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('min_code_length') is not None:
            self.min_code_length = m.get('min_code_length')
        if m.get('max_code_length') is not None:
            self.max_code_length = m.get('max_code_length')
        return self
