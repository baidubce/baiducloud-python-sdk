"""
Request entity for InpaintingRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InpaintingRequest(AbstractModel):
    """
    Request entity for InpaintingRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, rectangle, image=None, url=None):
        """
        Initialize InpaintingRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param rectangle: rectangle parameter
        :type rectangle: str (required)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.rectangle = rectangle

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
        if self.rectangle is not None:
            result['rectangle'] = self.rectangle
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InpaintingRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('rectangle') is not None:
            self.rectangle = m.get('rectangle')
        return self
