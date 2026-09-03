"""
Request entity for ProductImageAddRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ProductImageAddRequest(AbstractModel):
    """
    Request entity for ProductImageAddRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, brief, image=None, url=None, class_id1=None, class_id2=None):
        """
        Initialize ProductImageAddRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param brief: brief parameter
        :type brief: str (required)

        :param class_id1: class_id1 parameter
        :type class_id1: int (optional)

        :param class_id2: class_id2 parameter
        :type class_id2: int (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.brief = brief
        self.class_id1 = class_id1
        self.class_id2 = class_id2

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
        if self.brief is not None:
            result['brief'] = self.brief
        if self.class_id1 is not None:
            result['class_id1'] = self.class_id1
        if self.class_id2 is not None:
            result['class_id2'] = self.class_id2
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ProductImageAddRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('brief') is not None:
            self.brief = m.get('brief')
        if m.get('class_id1') is not None:
            self.class_id1 = m.get('class_id1')
        if m.get('class_id2') is not None:
            self.class_id2 = m.get('class_id2')
        return self
