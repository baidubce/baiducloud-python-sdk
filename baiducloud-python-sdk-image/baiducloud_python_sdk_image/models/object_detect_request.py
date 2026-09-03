"""
Request entity for ObjectDetectRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ObjectDetectRequest(AbstractModel):
    """
    Request entity for ObjectDetectRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image, with_face=None):
        """
        Initialize ObjectDetectRequest request entity.

        :param image: image parameter
        :type image: str (required)

        :param with_face: with_face parameter
        :type with_face: int (optional)
        """
        super().__init__()
        self.image = image
        self.with_face = with_face

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
        if self.with_face is not None:
            result['with_face'] = self.with_face
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ObjectDetectRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('with_face') is not None:
            self.with_face = m.get('with_face')
        return self
