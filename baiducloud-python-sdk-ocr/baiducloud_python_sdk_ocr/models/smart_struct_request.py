"""
Request entity for SmartStructRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SmartStructRequest(AbstractModel):
    """
    Request entity for SmartStructRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, pdf_file=None, pdf_file_num=None, return_relation=None):
        """
        Initialize SmartStructRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param pdf_file: pdf_file parameter
        :type pdf_file: str (optional)

        :param pdf_file_num: pdf_file_num parameter
        :type pdf_file_num: int (optional)

        :param return_relation: 是否返回结构化对应关系及单文本行结果，默认为 false，即不返回，为 true 时返回
        :type return_relation: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.pdf_file_num = pdf_file_num
        self.return_relation = return_relation

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
        if self.return_relation is not None:
            result['return_relation'] = self.return_relation
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SmartStructRequest

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
        if m.get('return_relation') is not None:
            self.return_relation = m.get('return_relation')
        return self
