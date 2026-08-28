"""
Request entity for DocCropEnhanceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.doc_crop_enhance_point import DocCropEnhancePoint


class DocCropEnhanceResponse(BceResponse):
    """
    DocCropEnhanceResponse
    """

    def __init__(self, log_id=None, image_processed=None, points=None, pdf_file_size=None):
        """
        Initialize DocCropEnhanceResponse response.

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param image_processed: 返回处理后的图片，base64编码，如请求参数 scan_type = 1&enhance_type =0，则返回原图
        :type image_processed: str (optional)

        :param points: 检测到的图片内主体在原图中的四角点坐标，scan_type = 2 时不返回此参数
        :type points: List[DocCropEnhancePoint] (optional)

        :param pdf_file_size: 传入PDF文件的总页数，当 pdf_file 参数有效时返回该字段
        :type pdf_file_size: int (optional)
        """
        super().__init__()
        self.log_id = log_id
        self.image_processed = image_processed
        self.points = points
        self.pdf_file_size = pdf_file_size

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.log_id is not None:
            result['log_id'] = self.log_id
        if self.image_processed is not None:
            result['image_processed'] = self.image_processed
        if self.points is not None:
            result['points'] = [i.to_dict() for i in self.points]
        if self.pdf_file_size is not None:
            result['pdf_file_size'] = self.pdf_file_size
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocCropEnhanceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('log_id') is not None:
            self.log_id = m.get('log_id')
        if m.get('image_processed') is not None:
            self.image_processed = m.get('image_processed')
        if m.get('points') is not None:
            self.points = [DocCropEnhancePoint().from_dict(i) for i in m.get('points')]
        if m.get('pdf_file_size') is not None:
            self.pdf_file_size = m.get('pdf_file_size')
        return self
