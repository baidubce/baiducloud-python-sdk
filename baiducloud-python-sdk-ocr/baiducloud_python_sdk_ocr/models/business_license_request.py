"""
Request entity for BusinessLicenseRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BusinessLicenseRequest(AbstractModel):
    """
    Request entity for BusinessLicenseRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, accuracy=None, risk_warn=None, detect_quality=None, fullwidth_shift=None):
        """
        Initialize BusinessLicenseRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param accuracy: 识别精度
        :type accuracy: str (optional)

        :param risk_warn: 是否开启风险类型功能，默认不开启。 - false：不开启 - true：开启
        :type risk_warn: bool (optional)

        :param detect_quality: detect_quality parameter
        :type detect_quality: bool (optional)

        :param fullwidth_shift: fullwidth_shift parameter
        :type fullwidth_shift: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.accuracy = accuracy
        self.risk_warn = risk_warn
        self.detect_quality = detect_quality
        self.fullwidth_shift = fullwidth_shift

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
        if self.accuracy is not None:
            result['accuracy'] = self.accuracy
        if self.risk_warn is not None:
            result['risk_warn'] = self.risk_warn
        if self.detect_quality is not None:
            result['detect_quality'] = self.detect_quality
        if self.fullwidth_shift is not None:
            result['fullwidth_shift'] = self.fullwidth_shift
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BusinessLicenseRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('accuracy') is not None:
            self.accuracy = m.get('accuracy')
        if m.get('risk_warn') is not None:
            self.risk_warn = m.get('risk_warn')
        if m.get('detect_quality') is not None:
            self.detect_quality = m.get('detect_quality')
        if m.get('fullwidth_shift') is not None:
            self.fullwidth_shift = m.get('fullwidth_shift')
        return self
