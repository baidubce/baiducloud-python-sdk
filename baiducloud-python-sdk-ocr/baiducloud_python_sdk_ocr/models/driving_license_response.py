"""
Request entity for DrivingLicenseResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.driving_license_quality_propobility import DrivingLicenseQualityPropobility


class DrivingLicenseResponse(BceResponse):
    """
    DrivingLicenseResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        direction=None,
        words_result_num=None,
        words_result=None,
        warn_infos=None,
        quality_propobility=None,
        risk_type=None,
        edit_tool=None,
    ):
        """
        Initialize DrivingLicenseResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误描述信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param direction: direction field
        :type direction: int (optional)

        :param words_result_num: 识别结果数，表示words_result的元素个数
        :type words_result_num: int (optional)

        :param words_result: 识别结果，key为字段名（如：姓名、出生日期、证号等），value为识别内容
        :type words_result: object (optional)

        :param warn_infos: 质量告警信息，当 driving_license_side=front 且 quality_warn=true 时输出
        :type warn_infos: List[str] (optional)

        :param quality_propobility: quality_propobility field
        :type quality_propobility: DrivingLicenseQualityPropobility (optional)

        :param risk_type: 风险告警信息，当risk_warn=true时输出
        :type risk_type: str (optional)

        :param edit_tool: edit_tool field
        :type edit_tool: str (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.direction = direction
        self.words_result_num = words_result_num
        self.words_result = words_result
        self.warn_infos = warn_infos
        self.quality_propobility = quality_propobility
        self.risk_type = risk_type
        self.edit_tool = edit_tool

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
        if self.words_result_num is not None:
            result['words_result_num'] = self.words_result_num
        if self.words_result is not None:
            result['words_result'] = self.words_result
        if self.warn_infos is not None:
            result['warn_infos'] = self.warn_infos
        if self.quality_propobility is not None:
            result['quality_propobility'] = self.quality_propobility.to_dict()
        if self.risk_type is not None:
            result['risk_type'] = self.risk_type
        if self.edit_tool is not None:
            result['edit_tool'] = self.edit_tool
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DrivingLicenseResponse

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
        if m.get('words_result_num') is not None:
            self.words_result_num = m.get('words_result_num')
        if m.get('words_result') is not None:
            self.words_result = m.get('words_result')
        if m.get('warn_infos') is not None:
            self.warn_infos = m.get('warn_infos')
        if m.get('quality_propobility') is not None:
            self.quality_propobility = DrivingLicenseQualityPropobility().from_dict(m.get('quality_propobility'))
        if m.get('risk_type') is not None:
            self.risk_type = m.get('risk_type')
        if m.get('edit_tool') is not None:
            self.edit_tool = m.get('edit_tool')
        return self
