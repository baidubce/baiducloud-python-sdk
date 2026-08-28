"""
Request entity for IdcardResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.id_card_quality import IdCardQuality
from baiducloud_python_sdk_ocr.models.idcard_location import IdcardLocation
from baiducloud_python_sdk_ocr.models.idcard_location import IdcardLocation


class IdcardResponse(BceResponse):
    """
    IdcardResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        words_result_num=None,
        words_result=None,
        direction=None,
        image_status=None,
        risk_type=None,
        card_quality=None,
        photo=None,
        photo_location=None,
        card_image=None,
        card_location=None,
        idcard_number_type=None,
        card_ps=None,
        edit_tool=None,
    ):
        """
        Initialize IdcardResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param words_result_num: 识别结果数
        :type words_result_num: int (optional)

        :param words_result: 识别结果，key为字段名称（如：姓名、性别、民族、出生、住址、公民身份号码、签发机关、失效日期等）
        :type words_result: object (optional)

        :param direction: 图像方向（当detect_direction=true时返回）
        :type direction: int (optional)

        :param image_status: 识别状态
        :type image_status: str (optional)

        :param risk_type: 风险类型（可选）
        :type risk_type: str (optional)

        :param card_quality: card_quality field
        :type card_quality: IdCardQuality (optional)

        :param photo: 头像切图的base64编码（当detect_photo=true时返回）
        :type photo: str (optional)

        :param photo_location: photo_location field
        :type photo_location: IdcardLocation (optional)

        :param card_image: 身份证裁剪切图的base64编码（当detect_card=true时返回）
        :type card_image: str (optional)

        :param card_location: card_location field
        :type card_location: IdcardLocation (optional)

        :param idcard_number_type: 用于校验身份证号码、性别、出生是否一致
        :type idcard_number_type: int (optional)

        :param card_ps: 判断身份证是否被PS（当detect_ps=true时返回）
        :type card_ps: int (optional)

        :param edit_tool: edit_tool field
        :type edit_tool: str (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.words_result_num = words_result_num
        self.words_result = words_result
        self.direction = direction
        self.image_status = image_status
        self.risk_type = risk_type
        self.card_quality = card_quality
        self.photo = photo
        self.photo_location = photo_location
        self.card_image = card_image
        self.card_location = card_location
        self.idcard_number_type = idcard_number_type
        self.card_ps = card_ps
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
        if self.words_result_num is not None:
            result['words_result_num'] = self.words_result_num
        if self.words_result is not None:
            result['words_result'] = self.words_result
        if self.direction is not None:
            result['direction'] = self.direction
        if self.image_status is not None:
            result['image_status'] = self.image_status
        if self.risk_type is not None:
            result['risk_type'] = self.risk_type
        if self.card_quality is not None:
            result['card_quality'] = self.card_quality.to_dict()
        if self.photo is not None:
            result['photo'] = self.photo
        if self.photo_location is not None:
            result['photo_location'] = self.photo_location.to_dict()
        if self.card_image is not None:
            result['card_image'] = self.card_image
        if self.card_location is not None:
            result['card_location'] = self.card_location.to_dict()
        if self.idcard_number_type is not None:
            result['idcard_number_type'] = self.idcard_number_type
        if self.card_ps is not None:
            result['card_ps'] = self.card_ps
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
        :rtype: IdcardResponse

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
        if m.get('words_result_num') is not None:
            self.words_result_num = m.get('words_result_num')
        if m.get('words_result') is not None:
            self.words_result = m.get('words_result')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('image_status') is not None:
            self.image_status = m.get('image_status')
        if m.get('risk_type') is not None:
            self.risk_type = m.get('risk_type')
        if m.get('card_quality') is not None:
            self.card_quality = IdCardQuality().from_dict(m.get('card_quality'))
        if m.get('photo') is not None:
            self.photo = m.get('photo')
        if m.get('photo_location') is not None:
            self.photo_location = IdcardLocation().from_dict(m.get('photo_location'))
        if m.get('card_image') is not None:
            self.card_image = m.get('card_image')
        if m.get('card_location') is not None:
            self.card_location = IdcardLocation().from_dict(m.get('card_location'))
        if m.get('idcard_number_type') is not None:
            self.idcard_number_type = m.get('idcard_number_type')
        if m.get('card_ps') is not None:
            self.card_ps = m.get('card_ps')
        if m.get('edit_tool') is not None:
            self.edit_tool = m.get('edit_tool')
        return self
