"""
Request entity for FaceVerifyDateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceVerifyDateRequest(AbstractModel):
    """
    Request entity for FaceVerifyDateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        id_card_number,
        start_date,
        end_date,
        image,
        image_type,
        liveness_control=None,
        spoofing_control=None,
        quality_control=None,
    ):
        """
        Initialize FaceVerifyDateRequest request entity.

        :param name: 姓名(需要是 utf8 编码)
        :type name: str (required)

        :param id_card_number: 身份证件号
        :type id_card_number: str (required)

        :param start_date: start_date parameter
        :type start_date: str (required)

        :param end_date: end_date parameter
        :type end_date: str (required)

        :param image: 图片信息(数据大小应小于10M 分辨率应小于1920*1080)
        :type image: str (required)

        :param image_type: 图片类型 **BASE64** : 图片的base64值
        :type image_type: str (required)

        :param liveness_control: liveness_control parameter
        :type liveness_control: str (optional)

        :param spoofing_control: spoofing_control parameter
        :type spoofing_control: str (optional)

        :param quality_control: quality_control parameter
        :type quality_control: str (optional)
        """
        super().__init__()
        self.name = name
        self.id_card_number = id_card_number
        self.start_date = start_date
        self.end_date = end_date
        self.image = image
        self.image_type = image_type
        self.liveness_control = liveness_control
        self.spoofing_control = spoofing_control
        self.quality_control = quality_control

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
        if self.name is not None:
            result['name'] = self.name
        if self.id_card_number is not None:
            result['id_card_number'] = self.id_card_number
        if self.start_date is not None:
            result['start_date'] = self.start_date
        if self.end_date is not None:
            result['end_date'] = self.end_date
        if self.image is not None:
            result['image'] = self.image
        if self.image_type is not None:
            result['image_type'] = self.image_type
        if self.liveness_control is not None:
            result['liveness_control'] = self.liveness_control
        if self.spoofing_control is not None:
            result['spoofing_control'] = self.spoofing_control
        if self.quality_control is not None:
            result['quality_control'] = self.quality_control
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceVerifyDateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id_card_number') is not None:
            self.id_card_number = m.get('id_card_number')
        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')
        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('liveness_control') is not None:
            self.liveness_control = m.get('liveness_control')
        if m.get('spoofing_control') is not None:
            self.spoofing_control = m.get('spoofing_control')
        if m.get('quality_control') is not None:
            self.quality_control = m.get('quality_control')
        return self
