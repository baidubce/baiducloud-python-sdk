"""
FaceDetectLiveness information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceDetectLiveness(AbstractModel):
    """
    FaceDetectLiveness
    """

    def __init__(self, livemapscore=None):
        """
        Initialize FaceDetectLiveness instance.

        :param livemapscore: 单张图片的活体得分，范围[0~1]
        :type livemapscore: float (optional)
        """
        super().__init__()
        self.livemapscore = livemapscore

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.livemapscore is not None:
            result['livemapscore'] = self.livemapscore
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceDetectLiveness

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('livemapscore') is not None:
            self.livemapscore = m.get('livemapscore')
        return self
