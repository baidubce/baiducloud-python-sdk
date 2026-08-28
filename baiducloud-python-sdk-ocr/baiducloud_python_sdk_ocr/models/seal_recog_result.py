"""
SealRecogResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_anaysis_office_location import DocAnaysisOfficeLocation

from baiducloud_python_sdk_ocr.models.seal_field import SealField

from baiducloud_python_sdk_ocr.models.seal_field import SealField


class SealRecogResult(AbstractModel):
    """
    SealRecogResult
    """

    def __init__(self, location=None, probability=None, type=None, major=None, minor=None):
        """
        Initialize SealRecogResult instance.

        :param location: location attribute
        :type location: DocAnaysisOfficeLocation (optional)

        :param probability: 每一个印章的置信度值
        :type probability: float (optional)

        :param type: 印章的类别，circle（圆章），ellipse（椭圆章），rectangle（方章）
        :type type: str (optional)

        :param major: major attribute
        :type major: SealField (optional)

        :param minor: 印章内其他字段信息
        :type minor: List[SealField] (optional)
        """
        super().__init__()
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
        :rtype: SealRecogResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = DocAnaysisOfficeLocation().from_dict(m.get('location'))
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('major') is not None:
            self.major = SealField().from_dict(m.get('major'))
        if m.get('minor') is not None:
            self.minor = [SealField().from_dict(i) for i in m.get('minor')]
        return self
