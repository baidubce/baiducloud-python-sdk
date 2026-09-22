"""
Request entity for FacePersonVerifyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FacePersonVerifyRequest(AbstractModel):
    """
    Request entity for FacePersonVerifyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image,
        image_type,
        id_card_number,
        name,
        quality_control=None,
        liveness_control=None,
        spoofing_control=None,
    ):
        """
        Initialize FacePersonVerifyRequest request entity.

        :param image: 图片信息，图片上传方式根据image_type来判断
        :type image: str (required)

        :param image_type: image_type parameter
        :type image_type: str (required)

        :param id_card_number: 证件号码
        :type id_card_number: str (required)

        :param name: 姓名（注：需要是UTF-8编码的中文）
        :type name: str (required)

        :param quality_control: quality_control parameter
        :type quality_control: str (optional)

        :param liveness_control: liveness_control parameter
        :type liveness_control: str (optional)

        :param spoofing_control: spoofing_control parameter
        :type spoofing_control: str (optional)
        """
        super().__init__()
        self.image = image
        self.image_type = image_type
        self.id_card_number = id_card_number
        self.name = name
        self.quality_control = quality_control
        self.liveness_control = liveness_control
        self.spoofing_control = spoofing_control

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
        if self.image_type is not None:
            result['image_type'] = self.image_type
        if self.id_card_number is not None:
            result['id_card_number'] = self.id_card_number
        if self.name is not None:
            result['name'] = self.name
        if self.quality_control is not None:
            result['quality_control'] = self.quality_control
        if self.liveness_control is not None:
            result['liveness_control'] = self.liveness_control
        if self.spoofing_control is not None:
            result['spoofing_control'] = self.spoofing_control
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FacePersonVerifyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('id_card_number') is not None:
            self.id_card_number = m.get('id_card_number')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quality_control') is not None:
            self.quality_control = m.get('quality_control')
        if m.get('liveness_control') is not None:
            self.liveness_control = m.get('liveness_control')
        if m.get('spoofing_control') is not None:
            self.spoofing_control = m.get('spoofing_control')
        return self
