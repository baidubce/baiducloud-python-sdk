"""
MultiIdcardCardInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.multi_idcard_location import MultiIdcardLocation

from baiducloud_python_sdk_ocr.models.multi_idcard_card_quality import MultiIdcardCardQuality

from baiducloud_python_sdk_ocr.models.multi_idcard_location import MultiIdcardLocation


class MultiIdcardCardInfo(AbstractModel):
    """
    MultiIdcardCardInfo
    """

    def __init__(
        self,
        card_location=None,
        card_type=None,
        direction=None,
        image_status=None,
        risk_type=None,
        edit_tool=None,
        card_quality=None,
        photo=None,
        photo_location=None,
        card_image=None,
        idcard_number_type=None,
    ):
        """
        Initialize MultiIdcardCardInfo instance.

        :param card_location: card_location attribute
        :type card_location: MultiIdcardLocation (optional)

        :param card_type: 身份证正反面类型
        :type card_type: str (optional)

        :param direction: 图像方向
        :type direction: int (optional)

        :param image_status: 识别状态
        :type image_status: str (optional)

        :param risk_type: 输入参数 detect_risk = true 时，则返回该字段识别身份证类型
        :type risk_type: str (optional)

        :param edit_tool: edit_tool attribute
        :type edit_tool: str (optional)

        :param card_quality: card_quality attribute
        :type card_quality: MultiIdcardCardQuality (optional)

        :param photo: 当请求参数 detect_photo = true时返回，头像切图的 base64 编码（无编码头，需自行处理）
        :type photo: str (optional)

        :param photo_location: photo_location attribute
        :type photo_location: MultiIdcardLocation (optional)

        :param card_image: 当请求参数 detect_card = true时返回，身份证裁剪切图的 base64 编码（无编码头，需自行处理）
        :type card_image: str (optional)

        :param idcard_number_type: 用于校验身份证号码、性别、出生是否一致
        :type idcard_number_type: int (optional)
        """
        super().__init__()
        self.card_location = card_location
        self.card_type = card_type
        self.direction = direction
        self.image_status = image_status
        self.risk_type = risk_type
        self.edit_tool = edit_tool
        self.card_quality = card_quality
        self.photo = photo
        self.photo_location = photo_location
        self.card_image = card_image
        self.idcard_number_type = idcard_number_type

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
        if self.card_location is not None:
            result['card_location'] = self.card_location.to_dict()
        if self.card_type is not None:
            result['card_type'] = self.card_type
        if self.direction is not None:
            result['direction'] = self.direction
        if self.image_status is not None:
            result['image_status'] = self.image_status
        if self.risk_type is not None:
            result['risk_type'] = self.risk_type
        if self.edit_tool is not None:
            result['edit_tool'] = self.edit_tool
        if self.card_quality is not None:
            result['card_quality'] = self.card_quality.to_dict()
        if self.photo is not None:
            result['photo'] = self.photo
        if self.photo_location is not None:
            result['photo_location'] = self.photo_location.to_dict()
        if self.card_image is not None:
            result['card_image'] = self.card_image
        if self.idcard_number_type is not None:
            result['idcard_number_type'] = self.idcard_number_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MultiIdcardCardInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('card_location') is not None:
            self.card_location = MultiIdcardLocation().from_dict(m.get('card_location'))
        if m.get('card_type') is not None:
            self.card_type = m.get('card_type')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('image_status') is not None:
            self.image_status = m.get('image_status')
        if m.get('risk_type') is not None:
            self.risk_type = m.get('risk_type')
        if m.get('edit_tool') is not None:
            self.edit_tool = m.get('edit_tool')
        if m.get('card_quality') is not None:
            self.card_quality = MultiIdcardCardQuality().from_dict(m.get('card_quality'))
        if m.get('photo') is not None:
            self.photo = m.get('photo')
        if m.get('photo_location') is not None:
            self.photo_location = MultiIdcardLocation().from_dict(m.get('photo_location'))
        if m.get('card_image') is not None:
            self.card_image = m.get('card_image')
        if m.get('idcard_number_type') is not None:
            self.idcard_number_type = m.get('idcard_number_type')
        return self
