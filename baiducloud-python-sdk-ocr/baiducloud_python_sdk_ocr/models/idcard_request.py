"""
Request entity for IdcardRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IdcardRequest(AbstractModel):
    """
    Request entity for IdcardRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        id_card_side,
        image=None,
        url=None,
        detect_ps=None,
        detect_risk=None,
        detect_quality=None,
        detect_photo=None,
        detect_card=None,
        detect_direction=None,
        detect_screenshot=None,
    ):
        """
        Initialize IdcardRequest request entity.

        :param id_card_side: id_card_side parameter
        :type id_card_side: str (required)

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param detect_ps: 是否检测PS，默认不检测，即：false <div/>- true：检测 <br/>- false：不检测
        :type detect_ps: bool (optional)

        :param detect_risk: detect_risk parameter
        :type detect_risk: bool (optional)

        :param detect_quality: detect_quality parameter
        :type detect_quality: bool (optional)

        :param detect_photo: detect_photo parameter
        :type detect_photo: bool (optional)

        :param detect_card: detect_card parameter
        :type detect_card: bool (optional)

        :param detect_direction: 是否检测身份证图片方向，默认不检测，即：false。<div/>- true：检测 <br/>- false：不检测
        :type detect_direction: bool (optional)

        :param detect_screenshot: detect_screenshot parameter
        :type detect_screenshot: bool (optional)
        """
        super().__init__()
        self.id_card_side = id_card_side
        self.image = image
        self.url = url
        self.detect_ps = detect_ps
        self.detect_risk = detect_risk
        self.detect_quality = detect_quality
        self.detect_photo = detect_photo
        self.detect_card = detect_card
        self.detect_direction = detect_direction
        self.detect_screenshot = detect_screenshot

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
        if self.id_card_side is not None:
            result['id_card_side'] = self.id_card_side
        if self.image is not None:
            result['image'] = self.image
        if self.url is not None:
            result['url'] = self.url
        if self.detect_ps is not None:
            result['detect_ps'] = self.detect_ps
        if self.detect_risk is not None:
            result['detect_risk'] = self.detect_risk
        if self.detect_quality is not None:
            result['detect_quality'] = self.detect_quality
        if self.detect_photo is not None:
            result['detect_photo'] = self.detect_photo
        if self.detect_card is not None:
            result['detect_card'] = self.detect_card
        if self.detect_direction is not None:
            result['detect_direction'] = self.detect_direction
        if self.detect_screenshot is not None:
            result['detect_screenshot'] = self.detect_screenshot
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IdcardRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id_card_side') is not None:
            self.id_card_side = m.get('id_card_side')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('detect_ps') is not None:
            self.detect_ps = m.get('detect_ps')
        if m.get('detect_risk') is not None:
            self.detect_risk = m.get('detect_risk')
        if m.get('detect_quality') is not None:
            self.detect_quality = m.get('detect_quality')
        if m.get('detect_photo') is not None:
            self.detect_photo = m.get('detect_photo')
        if m.get('detect_card') is not None:
            self.detect_card = m.get('detect_card')
        if m.get('detect_direction') is not None:
            self.detect_direction = m.get('detect_direction')
        if m.get('detect_screenshot') is not None:
            self.detect_screenshot = m.get('detect_screenshot')
        return self
