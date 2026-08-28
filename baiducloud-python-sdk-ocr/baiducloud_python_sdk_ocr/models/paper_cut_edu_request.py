"""
Request entity for PaperCutEduRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PaperCutEduRequest(AbstractModel):
    """
    Request entity for PaperCutEduRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image=None,
        url=None,
        pdf_file=None,
        pdf_file_num=None,
        language_type=None,
        detect_direction=None,
        words_type=None,
        splice_text=None,
        enhance=None,
        only_split=None,
    ):
        """
        Initialize PaperCutEduRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param pdf_file: pdf_file parameter
        :type pdf_file: str (optional)

        :param pdf_file_num: 需要识别的PDF文件的对应页码，当pdf_file参数有效时，识别传入页码的对应页面内容，若不传入，则默认识别第1页
        :type pdf_file_num: int (optional)

        :param language_type: language_type parameter
        :type language_type: str (optional)

        :param detect_direction: detect_direction parameter
        :type detect_direction: bool (optional)

        :param words_type: words_type parameter
        :type words_type: str (optional)

        :param splice_text: splice_text parameter
        :type splice_text: bool (optional)

        :param enhance: 是否打开图像矫正与增强，默认不打开，即：false。可选值包括：<br/>- true：开启；- false：不开启
        :type enhance: bool (optional)

        :param only_split: 是否仅进行题目切分，默认不打开，即：false。可选值包括：<br/>- true：开启；- false：不开启
        :type only_split: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.pdf_file_num = pdf_file_num
        self.language_type = language_type
        self.detect_direction = detect_direction
        self.words_type = words_type
        self.splice_text = splice_text
        self.enhance = enhance
        self.only_split = only_split

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
        if self.language_type is not None:
            result['language_type'] = self.language_type
        if self.detect_direction is not None:
            result['detect_direction'] = self.detect_direction
        if self.words_type is not None:
            result['words_type'] = self.words_type
        if self.splice_text is not None:
            result['splice_text'] = self.splice_text
        if self.enhance is not None:
            result['enhance'] = self.enhance
        if self.only_split is not None:
            result['only_split'] = self.only_split
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PaperCutEduRequest

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
        if m.get('language_type') is not None:
            self.language_type = m.get('language_type')
        if m.get('detect_direction') is not None:
            self.detect_direction = m.get('detect_direction')
        if m.get('words_type') is not None:
            self.words_type = m.get('words_type')
        if m.get('splice_text') is not None:
            self.splice_text = m.get('splice_text')
        if m.get('enhance') is not None:
            self.enhance = m.get('enhance')
        if m.get('only_split') is not None:
            self.only_split = m.get('only_split')
        return self
