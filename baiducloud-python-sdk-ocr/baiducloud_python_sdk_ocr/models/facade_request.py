"""
Request entity for FacadeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FacadeRequest(AbstractModel):
    """
    Request entity for FacadeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image):
        """
        Initialize FacadeRequest request entity.

        :param image: image parameter
        :type image: str (required)
        """
        super().__init__()
        self.image = image

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FacadeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        return self
