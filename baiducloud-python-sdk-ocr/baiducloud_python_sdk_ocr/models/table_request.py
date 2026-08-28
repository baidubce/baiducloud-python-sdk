"""
Request entity for TableRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TableRequest(AbstractModel):
    """
    Request entity for TableRequest operation.

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
        return_excel=None,
        cell_contents=None,
    ):
        """
        Initialize TableRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param pdf_file: pdf_file parameter
        :type pdf_file: str (optional)

        :param pdf_file_num: 需要识别的PDF文件的对应页码，当 pdf_file 参数有效时，识别传入页码的对应页面内容，若不传入，则默认识别第1页
        :type pdf_file_num: int (optional)

        :param ofd_file: ofd_file parameter
        :type ofd_file: str (optional)

        :param ofd_file_num: 需要识别的OFD文件的对应页码，当 ofd_file 参数有效时，识别传入页码的对应页面内容，若不传入，则默认识别第1页
        :type ofd_file_num: int (optional)

        :param return_excel: return_excel parameter
        :type return_excel: bool (optional)

        :param cell_contents: cell_contents parameter
        :type cell_contents: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.pdf_file_num = pdf_file_num
        self.ofd_file = ofd_file
        self.ofd_file_num = ofd_file_num
        self.return_excel = return_excel
        self.cell_contents = cell_contents

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
        if self.return_excel is not None:
            result['return_excel'] = self.return_excel
        if self.cell_contents is not None:
            result['cell_contents'] = self.cell_contents
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableRequest

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
        if m.get('return_excel') is not None:
            self.return_excel = m.get('return_excel')
        if m.get('cell_contents') is not None:
            self.cell_contents = m.get('cell_contents')
        return self
