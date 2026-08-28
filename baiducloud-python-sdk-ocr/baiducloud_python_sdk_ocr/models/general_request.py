"""
Request entity for GeneralRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GeneralRequest(AbstractModel):
    """
    Request entity for GeneralRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image=None,
        url=None,
        pdf_file=None,
        pdf_file_num=None,
        ofd_file=None,
        ofd_file_num=None,
        recognize_granularity=None,
        language_type=None,
        detect_direction=None,
        detect_language=None,
        paragraph=None,
        vertexes_location=None,
        probability=None,
    ):
        """
        Initialize GeneralRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param pdf_file: pdf_file parameter
        :type pdf_file: str (optional)

        :param pdf_file_num: pdf_file_num parameter
        :type pdf_file_num: int (optional)

        :param ofd_file: ofd_file parameter
        :type ofd_file: str (optional)

        :param ofd_file_num: ofd_file_num parameter
        :type ofd_file_num: int (optional)

        :param recognize_granularity: 是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
        :type recognize_granularity: str (optional)

        :param language_type: language_type parameter
        :type language_type: str (optional)

        :param detect_direction: detect_direction parameter
        :type detect_direction: bool (optional)

        :param detect_language: 是否检测语言，默认不检测，即：false。当前支持中文、英语、日语、韩语
        :type detect_language: bool (optional)

        :param paragraph: 是否输出段落信息
        :type paragraph: bool (optional)

        :param vertexes_location: 是否返回文字外接多边形顶点位置，不支持单字位置。默认为false
        :type vertexes_location: bool (optional)

        :param probability: 是否返回识别结果中每一行的置信度
        :type probability: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.pdf_file_num = pdf_file_num
        self.ofd_file = ofd_file
        self.ofd_file_num = ofd_file_num
        self.recognize_granularity = recognize_granularity
        self.language_type = language_type
        self.detect_direction = detect_direction
        self.detect_language = detect_language
        self.paragraph = paragraph
        self.vertexes_location = vertexes_location
        self.probability = probability

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
        if self.pdf_file is not None:
            result['pdf_file'] = self.pdf_file
        if self.pdf_file_num is not None:
            result['pdf_file_num'] = self.pdf_file_num
        if self.ofd_file is not None:
            result['ofd_file'] = self.ofd_file
        if self.ofd_file_num is not None:
            result['ofd_file_num'] = self.ofd_file_num
        if self.recognize_granularity is not None:
            result['recognize_granularity'] = self.recognize_granularity
        if self.language_type is not None:
            result['language_type'] = self.language_type
        if self.detect_direction is not None:
            result['detect_direction'] = self.detect_direction
        if self.detect_language is not None:
            result['detect_language'] = self.detect_language
        if self.paragraph is not None:
            result['paragraph'] = self.paragraph
        if self.vertexes_location is not None:
            result['vertexes_location'] = self.vertexes_location
        if self.probability is not None:
            result['probability'] = self.probability
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GeneralRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('pdf_file') is not None:
            self.pdf_file = m.get('pdf_file')
        if m.get('pdf_file_num') is not None:
            self.pdf_file_num = m.get('pdf_file_num')
        if m.get('ofd_file') is not None:
            self.ofd_file = m.get('ofd_file')
        if m.get('ofd_file_num') is not None:
            self.ofd_file_num = m.get('ofd_file_num')
        if m.get('recognize_granularity') is not None:
            self.recognize_granularity = m.get('recognize_granularity')
        if m.get('language_type') is not None:
            self.language_type = m.get('language_type')
        if m.get('detect_direction') is not None:
            self.detect_direction = m.get('detect_direction')
        if m.get('detect_language') is not None:
            self.detect_language = m.get('detect_language')
        if m.get('paragraph') is not None:
            self.paragraph = m.get('paragraph')
        if m.get('vertexes_location') is not None:
            self.vertexes_location = m.get('vertexes_location')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        return self
