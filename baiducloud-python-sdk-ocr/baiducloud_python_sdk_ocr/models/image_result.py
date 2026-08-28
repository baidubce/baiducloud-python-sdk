"""
ImageResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.question_result import QuestionResult


class ImageResult(AbstractModel):
    """
    ImageResult
    """

    def __init__(self, image_id=None, image_url=None, paper_subject=None, resize_ratio=None, result=None):
        """
        Initialize ImageResult instance.

        :param image_id: 图片id
        :type image_id: str (optional)

        :param image_url: 实际请求的图片可能会经过压缩与矫正，此为处理后的图片url
        :type image_url: str (optional)

        :param paper_subject: paper_subject attribute
        :type paper_subject: str (optional)

        :param resize_ratio: 原图预处理缩放比例，用于前端坐标还原
        :type resize_ratio: float (optional)

        :param result: 单题批改结果
        :type result: List[QuestionResult] (optional)
        """
        super().__init__()
        self.image_id = image_id
        self.image_url = image_url
        self.paper_subject = paper_subject
        self.resize_ratio = resize_ratio
        self.result = result

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
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.paper_subject is not None:
            result['paperSubject'] = self.paper_subject
        if self.resize_ratio is not None:
            result['resize_ratio'] = self.resize_ratio
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImageResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('paperSubject') is not None:
            self.paper_subject = m.get('paperSubject')
        if m.get('resize_ratio') is not None:
            self.resize_ratio = m.get('resize_ratio')
        if m.get('result') is not None:
            self.result = [QuestionResult().from_dict(i) for i in m.get('result')]
        return self
