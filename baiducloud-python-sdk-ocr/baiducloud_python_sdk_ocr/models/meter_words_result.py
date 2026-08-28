"""
MeterWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.meter_location import MeterLocation

from baiducloud_python_sdk_ocr.models.meter_probability import MeterProbability

from baiducloud_python_sdk_ocr.models.meter_poly_point import MeterPolyPoint


class MeterWordsResult(AbstractModel):
    """
    MeterWordsResult
    """

    def __init__(self, words=None, location=None, probability=None, poly_location=None):
        """
        Initialize MeterWordsResult instance.

        :param words: 识别结果字符串
        :type words: str (optional)

        :param location: location attribute
        :type location: MeterLocation (optional)

        :param probability: probability attribute
        :type probability: MeterProbability (optional)

        :param poly_location: 外接四边形的4个点坐标，当请求 poly_location=true 时存在
        :type poly_location: List[MeterPolyPoint] (optional)
        """
        super().__init__()
        self.words = words
        self.location = location
        self.probability = probability
        self.poly_location = poly_location

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
        if self.probability is not None:
            result['probability'] = self.probability.to_dict()
        if self.poly_location is not None:
            result['poly_location'] = [i.to_dict() for i in self.poly_location]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MeterWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('location') is not None:
            self.location = MeterLocation().from_dict(m.get('location'))
        if m.get('probability') is not None:
            self.probability = MeterProbability().from_dict(m.get('probability'))
        if m.get('poly_location') is not None:
            self.poly_location = [MeterPolyPoint().from_dict(i) for i in m.get('poly_location')]
        return self
