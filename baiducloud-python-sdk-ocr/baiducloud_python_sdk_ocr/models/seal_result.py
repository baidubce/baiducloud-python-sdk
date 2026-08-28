"""
SealResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.seal_location import SealLocation

from baiducloud_python_sdk_ocr.models.seal_reg_field import SealRegField

from baiducloud_python_sdk_ocr.models.seal_reg_field import SealRegField


class SealResult(AbstractModel):
    """
    SealResult
    """

    def __init__(
        self, color=None, seal_image=None, location=None, probability=None, type=None, major=None, minor=None
    ):
        """
        Initialize SealResult instance.

        :param color: 印章颜色，如 black
        :type color: str (optional)

        :param seal_image: 印章切图的 base64 编码，return_image=true 时返回
        :type seal_image: str (optional)

        :param location: location attribute
        :type location: SealLocation (optional)

        :param probability: 每一个识别结果的置信度值
        :type probability: float (optional)

        :param type: type attribute
        :type type: str (optional)

        :param major: major attribute
        :type major: SealRegField (optional)

        :param minor: minor attribute
        :type minor: List[SealRegField] (optional)
        """
        super().__init__()
        self.color = color
        self.seal_image = seal_image
        self.location = location
        self.probability = probability
        self.type = type
        self.major = major
        self.minor = minor

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
        if self.color is not None:
            result['color'] = self.color
        if self.seal_image is not None:
            result['seal_image'] = self.seal_image
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.probability is not None:
            result['probability'] = self.probability
        if self.type is not None:
            result['type'] = self.type
        if self.major is not None:
            result['major'] = self.major.to_dict()
        if self.minor is not None:
            result['minor'] = [i.to_dict() for i in self.minor]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SealResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('color') is not None:
            self.color = m.get('color')
        if m.get('seal_image') is not None:
            self.seal_image = m.get('seal_image')
        if m.get('location') is not None:
            self.location = SealLocation().from_dict(m.get('location'))
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('major') is not None:
            self.major = SealRegField().from_dict(m.get('major'))
        if m.get('minor') is not None:
            self.minor = [SealRegField().from_dict(i) for i in m.get('minor')]
        return self
