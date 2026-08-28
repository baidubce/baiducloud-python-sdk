"""
Request entity for PaperCutEduVlmCreateTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PaperCutEduVlmCreateTaskRequest(AbstractModel):
    """
    Request entity for PaperCutEduVlmCreateTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, scene_type, image=None, url=None, pdf_file=None, pdf_file_num=None, only_split=None, enhance=None
    ):
        """
        Initialize PaperCutEduVlmCreateTaskRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param pdf_file: pdf_file parameter
        :type pdf_file: str (optional)

        :param pdf_file_num: 需要识别的PDF文件的对应页码，当pdf_file参数有效时，识别传入页码的对应页面内容，若不传入，则默认识别第 1 页
        :type pdf_file_num: int (optional)

        :param only_split: only_split parameter
        :type only_split: bool (optional)

        :param scene_type: 指定传入文件的场景类型，paper：试卷题目识别场景；answer_sheet：答题卡识别场景
        :type scene_type: str (required)

        :param enhance: 是否开启矫正增强，默认关闭
        :type enhance: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.pdf_file_num = pdf_file_num
        self.only_split = only_split
        self.scene_type = scene_type
        self.enhance = enhance

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
        if self.only_split is not None:
            result['only_split'] = self.only_split
        if self.scene_type is not None:
            result['scene_type'] = self.scene_type
        if self.enhance is not None:
            result['enhance'] = self.enhance
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PaperCutEduVlmCreateTaskRequest

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
        if m.get('only_split') is not None:
            self.only_split = m.get('only_split')
        if m.get('scene_type') is not None:
            self.scene_type = m.get('scene_type')
        if m.get('enhance') is not None:
            self.enhance = m.get('enhance')
        return self
