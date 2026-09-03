"""
Request entity for SameImageDeleteRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SameImageDeleteRequest(AbstractModel):
    """
    Request entity for SameImageDeleteRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, cont_sign=None):
        """
        Initialize SameImageDeleteRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param cont_sign: cont_sign parameter
        :type cont_sign: str (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
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
        if self.url is not None:
            result['url'] = self.url
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
        :rtype: SameImageDeleteRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('cont_sign') is not None:
            self.cont_sign = m.get('cont_sign')
        return self
