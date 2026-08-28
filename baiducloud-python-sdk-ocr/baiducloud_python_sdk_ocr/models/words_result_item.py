"""
WordsResultItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.mixed_multi_vehicle_location import MixedMultiVehicleLocation

from baiducloud_python_sdk_ocr.models.license_info_item import LicenseInfoItem


class WordsResultItem(AbstractModel):
    """
    WordsResultItem
    """

    def __init__(self, card_type=None, direction=None, probability=None, location=None, license_info=None):
        """
        Initialize WordsResultItem instance.

        :param card_type: card_type attribute
        :type card_type: str (optional)

        :param direction: 图像方向，当图像旋转时，返回该参数。-1：未定义，0：正向，1：逆时针90度，2：逆时针180度，3：逆时针270度
        :type direction: int (optional)

        :param probability: 检测到证件的置信度
        :type probability: float (optional)

        :param location: location attribute
        :type location: MixedMultiVehicleLocation (optional)

        :param license_info: 识别结果信息，key为字段名，value为识别内容
        :type license_info: List[LicenseInfoItem] (optional)
        """
        super().__init__()
        self.card_type = card_type
        self.direction = direction
        self.probability = probability
        self.location = location
        self.license_info = license_info

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
        if self.card_type is not None:
            result['card_type'] = self.card_type
        if self.direction is not None:
            result['direction'] = self.direction
        if self.probability is not None:
            result['probability'] = self.probability
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.license_info is not None:
            result['license_info'] = [i.to_dict() for i in self.license_info]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: WordsResultItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('card_type') is not None:
            self.card_type = m.get('card_type')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('location') is not None:
            self.location = MixedMultiVehicleLocation().from_dict(m.get('location'))
        if m.get('license_info') is not None:
            self.license_info = [LicenseInfoItem().from_dict(i) for i in m.get('license_info')]
        return self
