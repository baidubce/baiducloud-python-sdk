"""
Request entity for PaperCutEduResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.qus_figure import QusFigure
from baiducloud_python_sdk_ocr.models.qus_result import QusResult


class PaperCutEduResponse(BceResponse):
    """
    PaperCutEduResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        direction=None,
        qus_result_num=None,
        qus_figure=None,
        qus_result=None,
        pdf_file_size=None,
        processed_status=None,
    ):
        """
        Initialize PaperCutEduResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误描述信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param direction: 检测到的图像朝向，当detect_direction=true时返回
        :type direction: int (optional)

        :param qus_result_num: 识别题目结果数，表示qus_result的元素个数
        :type qus_result_num: int (optional)

        :param qus_figure: 试卷内题目图片信息
        :type qus_figure: List[QusFigure] (optional)

        :param qus_result: 试卷切题信息
        :type qus_result: List[QusResult] (optional)

        :param pdf_file_size: 传入PDF文件的总页数，当pdf_file参数有效时返回该字段
        :type pdf_file_size: int (optional)

        :param processed_status: 处理状态，如 success
        :type processed_status: str (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.direction = direction
        self.qus_result_num = qus_result_num
        self.qus_figure = qus_figure
        self.qus_result = qus_result
        self.pdf_file_size = pdf_file_size
        self.processed_status = processed_status

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
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.log_id is not None:
            result['log_id'] = self.log_id
        if self.direction is not None:
            result['direction'] = self.direction
        if self.qus_result_num is not None:
            result['qus_result_num'] = self.qus_result_num
        if self.qus_figure is not None:
            result['qus_figure'] = [i.to_dict() for i in self.qus_figure]
        if self.qus_result is not None:
            result['qus_result'] = [i.to_dict() for i in self.qus_result]
        if self.pdf_file_size is not None:
            result['pdf_file_size'] = self.pdf_file_size
        if self.processed_status is not None:
            result['processed_status'] = self.processed_status
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PaperCutEduResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('log_id') is not None:
            self.log_id = m.get('log_id')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('qus_result_num') is not None:
            self.qus_result_num = m.get('qus_result_num')
        if m.get('qus_figure') is not None:
            self.qus_figure = [QusFigure().from_dict(i) for i in m.get('qus_figure')]
        if m.get('qus_result') is not None:
            self.qus_result = [QusResult().from_dict(i) for i in m.get('qus_result')]
        if m.get('pdf_file_size') is not None:
            self.pdf_file_size = m.get('pdf_file_size')
        if m.get('processed_status') is not None:
            self.processed_status = m.get('processed_status')
        return self
