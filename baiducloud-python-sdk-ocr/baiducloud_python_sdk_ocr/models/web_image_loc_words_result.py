"""
WebImageLocWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.web_image_loc_location import WebImageLocLocation

from baiducloud_python_sdk_ocr.models.web_image_loc_probability import WebImageLocProbability

from baiducloud_python_sdk_ocr.models.web_image_loc_poly_location import WebImageLocPolyLocation

from baiducloud_python_sdk_ocr.models.web_image_loc_char import WebImageLocChar


class WebImageLocWordsResult(AbstractModel):
    """
    WebImageLocWordsResult
    """

    def __init__(self, words=None, location=None, probability=None, poly_location=None, chars=None):
        """
        Initialize WebImageLocWordsResult instance.

        :param words: 整行的识别结果
        :type words: str (optional)

        :param location: location attribute
        :type location: WebImageLocLocation (optional)

        :param probability: probability attribute
        :type probability: WebImageLocProbability (optional)

        :param poly_location: 当 probability=true 时返回该字段。文字所在区域的外接矩形的4个点坐标信息
        :type poly_location: List[WebImageLocPolyLocation] (optional)

        :param chars: 单字符结果，当 recognize_granularity=small 时返回该字段
        :type chars: List[WebImageLocChar] (optional)
        """
        super().__init__()
        self.words = words
        self.location = location
        self.probability = probability
        self.poly_location = poly_location
        self.chars = chars

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
        if self.chars is not None:
            result['chars'] = [i.to_dict() for i in self.chars]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: WebImageLocWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('location') is not None:
            self.location = WebImageLocLocation().from_dict(m.get('location'))
        if m.get('probability') is not None:
            self.probability = WebImageLocProbability().from_dict(m.get('probability'))
        if m.get('poly_location') is not None:
            self.poly_location = [WebImageLocPolyLocation().from_dict(i) for i in m.get('poly_location')]
        if m.get('chars') is not None:
            self.chars = [WebImageLocChar().from_dict(i) for i in m.get('chars')]
        return self
