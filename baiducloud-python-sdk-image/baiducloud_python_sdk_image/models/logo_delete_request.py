"""
Request entity for LogoDeleteRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LogoDeleteRequest(AbstractModel):
    """
    Request entity for LogoDeleteRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, cont_sign=None):
        """
        Initialize LogoDeleteRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param cont_sign: 图片签名（和image二选一，image优先级更高）
        :type cont_sign: str (optional)
        """
        super().__init__()
        self.image = image
        self.cont_sign = cont_sign

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
        if self.image is not None:
            result['image'] = self.image
        if self.cont_sign is not None:
            result['cont_sign'] = self.cont_sign
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogoDeleteRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('cont_sign') is not None:
            self.cont_sign = m.get('cont_sign')
        return self
