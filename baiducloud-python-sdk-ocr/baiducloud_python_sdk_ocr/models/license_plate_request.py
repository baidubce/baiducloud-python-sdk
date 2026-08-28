"""
Request entity for LicensePlateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LicensePlateRequest(AbstractModel):
    """
    Request entity for LicensePlateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, image=None, url=None, multi_detect=None, multi_scale=None, detect_complete=None, detect_risk=None
    ):
        """
        Initialize LicensePlateRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param multi_detect: 是否检测多张车牌 <div/>- false：默认值，仅检测最清晰的车牌 <br/>- true：检测多张车牌
        :type multi_detect: bool (optional)

        :param multi_scale: multi_scale parameter
        :type multi_scale: bool (optional)

        :param detect_complete: 是否开启车牌遮挡检测功能 <div/> - false：默认值,不开启 <br/>- true：开启遮挡检测
        :type detect_complete: bool (optional)

        :param detect_risk: 是否开启车牌PS检测功能 <div/>- false：默认值，不开启 <br/>- true：开启PS检测
        :type detect_risk: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.multi_detect = multi_detect
        self.multi_scale = multi_scale
        self.detect_complete = detect_complete
        self.detect_risk = detect_risk

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
        if self.multi_detect is not None:
            result['multi_detect'] = self.multi_detect
        if self.multi_scale is not None:
            result['multi_scale'] = self.multi_scale
        if self.detect_complete is not None:
            result['detect_complete'] = self.detect_complete
        if self.detect_risk is not None:
            result['detect_risk'] = self.detect_risk
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LicensePlateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('multi_detect') is not None:
            self.multi_detect = m.get('multi_detect')
        if m.get('multi_scale') is not None:
            self.multi_scale = m.get('multi_scale')
        if m.get('detect_complete') is not None:
            self.detect_complete = m.get('detect_complete')
        if m.get('detect_risk') is not None:
            self.detect_risk = m.get('detect_risk')
        return self
