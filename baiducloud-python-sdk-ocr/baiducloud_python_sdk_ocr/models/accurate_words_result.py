"""
AccurateWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.accurate_location import AccurateLocation

from baiducloud_python_sdk_ocr.models.accurate_char import AccurateChar

from baiducloud_python_sdk_ocr.models.accurate_probability import AccurateProbability

from baiducloud_python_sdk_ocr.models.accurate_vertexes_location import AccurateVertexesLocation

from baiducloud_python_sdk_ocr.models.accurate_vertexes_location import AccurateVertexesLocation

from baiducloud_python_sdk_ocr.models.accurate_vertexes_location import AccurateVertexesLocation


class AccurateWordsResult(AbstractModel):
    """
    AccurateWordsResult
    """

    def __init__(
        self,
        words=None,
        location=None,
        chars=None,
        probability=None,
        vertexes_location=None,
        finegrained_vertexes_location=None,
        min_finegrained_vertexes_location=None,
    ):
        """
        Initialize AccurateWordsResult instance.

        :param words: 识别结果字符串
        :type words: str (optional)

        :param location: location attribute
        :type location: AccurateLocation (optional)

        :param chars: 单字符结果，当 recognize_granularity=small 时返回该字段
        :type chars: List[AccurateChar] (optional)

        :param probability: probability attribute
        :type probability: AccurateProbability (optional)

        :param vertexes_location: 识别结果中每一行的外包四边形点坐标，当 vertexes_location=true 时返回该字段
        :type vertexes_location: List[AccurateVertexesLocation] (optional)

        :param finegrained_vertexes_location: 识别结果中每一行的多边形轮廓点坐标，当 vertexes_location=true 时返回该字段
        :type finegrained_vertexes_location: List[AccurateVertexesLocation] (optional)

        :param min_finegrained_vertexes_location: min_finegrained_vertexes_location attribute
        :type min_finegrained_vertexes_location: List[AccurateVertexesLocation] (optional)
        """
        super().__init__()
        self.words = words
        self.location = location
        self.chars = chars
        self.probability = probability
        self.vertexes_location = vertexes_location
        self.finegrained_vertexes_location = finegrained_vertexes_location
        self.min_finegrained_vertexes_location = min_finegrained_vertexes_location

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
        if self.words is not None:
            result['words'] = self.words
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.chars is not None:
            result['chars'] = [i.to_dict() for i in self.chars]
        if self.probability is not None:
            result['probability'] = self.probability.to_dict()
        if self.vertexes_location is not None:
            result['vertexes_location'] = [i.to_dict() for i in self.vertexes_location]
        if self.finegrained_vertexes_location is not None:
            result['finegrained_vertexes_location'] = [i.to_dict() for i in self.finegrained_vertexes_location]
        if self.min_finegrained_vertexes_location is not None:
            result['min_finegrained_vertexes_location'] = [i.to_dict() for i in self.min_finegrained_vertexes_location]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccurateWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('location') is not None:
            self.location = AccurateLocation().from_dict(m.get('location'))
        if m.get('chars') is not None:
            self.chars = [AccurateChar().from_dict(i) for i in m.get('chars')]
        if m.get('probability') is not None:
            self.probability = AccurateProbability().from_dict(m.get('probability'))
        if m.get('vertexes_location') is not None:
            self.vertexes_location = [AccurateVertexesLocation().from_dict(i) for i in m.get('vertexes_location')]
        if m.get('finegrained_vertexes_location') is not None:
            self.finegrained_vertexes_location = [
                AccurateVertexesLocation().from_dict(i) for i in m.get('finegrained_vertexes_location')
            ]
        if m.get('min_finegrained_vertexes_location') is not None:
            self.min_finegrained_vertexes_location = [
                AccurateVertexesLocation().from_dict(i) for i in m.get('min_finegrained_vertexes_location')
            ]
        return self
