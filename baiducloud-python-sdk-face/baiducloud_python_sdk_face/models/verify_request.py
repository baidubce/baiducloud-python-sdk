"""
Request entity for VerifyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VerifyRequest(AbstractModel):
    """
    Request entity for VerifyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, video_base64, type_identify=None, session_id=None, lip_identify=None, face_field=None):
        """
        Initialize VerifyRequest request entity.

        :param video_base64: video_base64 parameter
        :type video_base64: str (required)

        :param type_identify: voice为语音验证，action为视频动作活体验证，默认为voice （若您需要静默视频活体验证，此参数无需传入）
        :type type_identify: str (optional)

        :param session_id: session_id parameter
        :type session_id: str (optional)

        :param lip_identify: lip_identify parameter
        :type lip_identify: str (optional)

        :param face_field: 需要使用合成图功能时，此项传入spoofing；需要使用图片质量信息时，则传入quality；字段之间使用,号分隔
        :type face_field: str (optional)
        """
        super().__init__()
        self.video_base64 = video_base64
        self.type_identify = type_identify
        self.session_id = session_id
        self.lip_identify = lip_identify
        self.face_field = face_field

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
        if self.video_base64 is not None:
            result['video_base64'] = self.video_base64
        if self.type_identify is not None:
            result['type_identify'] = self.type_identify
        if self.session_id is not None:
            result['session_id'] = self.session_id
        if self.lip_identify is not None:
            result['lip_identify'] = self.lip_identify
        if self.face_field is not None:
            result['face_field'] = self.face_field
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VerifyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('video_base64') is not None:
            self.video_base64 = m.get('video_base64')
        if m.get('type_identify') is not None:
            self.type_identify = m.get('type_identify')
        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')
        if m.get('lip_identify') is not None:
            self.lip_identify = m.get('lip_identify')
        if m.get('face_field') is not None:
            self.face_field = m.get('face_field')
        return self
