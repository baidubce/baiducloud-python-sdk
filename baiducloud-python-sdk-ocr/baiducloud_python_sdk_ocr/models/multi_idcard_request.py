"""
Request entity for MultiIdcardRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MultiIdcardRequest(AbstractModel):
    """
    Request entity for MultiIdcardRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image=None,
        url=None,
        detect_risk=None,
        detect_quality=None,
        detect_photo=None,
        detect_card=None,
        detect_screenshot=None,
    ):
        """
        Initialize MultiIdcardRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param detect_risk: detect_risk parameter
        :type detect_risk: bool (optional)

        :param detect_quality: detect_quality parameter
        :type detect_quality: bool (optional)

        :param detect_photo: detect_photo parameter
        :type detect_photo: bool (optional)

        :param detect_card: detect_card parameter
        :type detect_card: bool (optional)

        :param detect_screenshot: detect_screenshot parameter
        :type detect_screenshot: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.detect_risk = detect_risk
        self.detect_quality = detect_quality
        self.detect_photo = detect_photo
        self.detect_card = detect_card
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
        if self.image is not None:
            result['image'] = self.image
        if self.url is not None:
            result['url'] = self.url
        if self.detect_risk is not None:
            result['detect_risk'] = self.detect_risk
        if self.detect_quality is not None:
            result['detect_quality'] = self.detect_quality
        if self.detect_photo is not None:
            result['detect_photo'] = self.detect_photo
        if self.detect_card is not None:
            result['detect_card'] = self.detect_card
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
        :rtype: MultiIdcardRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('detect_risk') is not None:
            self.detect_risk = m.get('detect_risk')
        if m.get('detect_quality') is not None:
            self.detect_quality = m.get('detect_quality')
        if m.get('detect_photo') is not None:
            self.detect_photo = m.get('detect_photo')
        if m.get('detect_card') is not None:
            self.detect_card = m.get('detect_card')
        if m.get('detect_screenshot') is not None:
            self.detect_screenshot = m.get('detect_screenshot')
        return self
