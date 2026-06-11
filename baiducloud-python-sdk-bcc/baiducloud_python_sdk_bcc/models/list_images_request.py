"""
Request entity for ListImagesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListImagesRequest(AbstractModel):
    """
    Request entity for ListImagesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, marker=None, max_keys=None, image_type=None, image_name=None):
        """
        Initialize ListImagesRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param image_type: image_type parameter
        :type image_type: str (optional)

        :param image_name: image_name parameter
        :type image_name: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.image_type = image_type
        self.image_name = image_name

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListImagesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('imageType') is not None:
            self.image_type = m.get('imageType')
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        return self
