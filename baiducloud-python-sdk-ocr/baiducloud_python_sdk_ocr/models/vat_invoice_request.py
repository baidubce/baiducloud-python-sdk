"""
Request entity for VatInvoiceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VatInvoiceRequest(AbstractModel):
    """
    Request entity for VatInvoiceRequest operation.

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
        type=None,
        seal_tag=None,
    ):
        """
        Initialize VatInvoiceRequest request entity.

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

        :param type: type parameter
        :type type: str (optional)

        :param seal_tag: 是否开启印章判断功能，并返回印章内容的识别结果。true：开启；false：不开启
        :type seal_tag: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.pdf_file_num = pdf_file_num
        self.ofd_file = ofd_file
        self.ofd_file_num = ofd_file_num
        self.type = type
        self.seal_tag = seal_tag

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
        if self.type is not None:
            result['type'] = self.type
        if self.seal_tag is not None:
            result['seal_tag'] = self.seal_tag
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VatInvoiceRequest

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
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('seal_tag') is not None:
            self.seal_tag = m.get('seal_tag')
        return self
