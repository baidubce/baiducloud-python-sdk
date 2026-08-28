"""
Request entity for HandwritingCompositionCreateTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HandwritingCompositionCreateTaskRequest(AbstractModel):
    """
    Request entity for HandwritingCompositionCreateTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, pdf_file=None, recognize_granularity=None, pdf_file_num=None):
        """
        Initialize HandwritingCompositionCreateTaskRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param pdf_file: pdf_file parameter
        :type pdf_file: str (optional)

        :param recognize_granularity: 识别粒度，控制坐标返回。line：行级坐标返回；word：行级坐标+字级别坐标返回；none：不返回坐标
        :type recognize_granularity: str (optional)

        :param pdf_file_num: 需要识别的PDF文件的对应页码，默认识别第1页
        :type pdf_file_num: int (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.recognize_granularity = recognize_granularity
        self.pdf_file_num = pdf_file_num

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
        if self.recognize_granularity is not None:
            result['recognize_granularity'] = self.recognize_granularity
        if self.pdf_file_num is not None:
            result['pdf_file_num'] = self.pdf_file_num
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HandwritingCompositionCreateTaskRequest

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
        if m.get('recognize_granularity') is not None:
            self.recognize_granularity = m.get('recognize_granularity')
        if m.get('pdf_file_num') is not None:
            self.pdf_file_num = m.get('pdf_file_num')
        return self
