"""
Request entity for DrivingLicenseRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DrivingLicenseRequest(AbstractModel):
    """
    Request entity for DrivingLicenseRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image=None,
        url=None,
        detect_direction=None,
        driving_license_side=None,
        unified_valid_period=None,
        quality_warn=None,
        risk_warn=None,
    ):
        """
        Initialize DrivingLicenseRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param detect_direction: detect_direction parameter
        :type detect_direction: bool (optional)

        :param driving_license_side: driving_license_side parameter
        :type driving_license_side: str (optional)

        :param unified_valid_period: unified_valid_period parameter
        :type unified_valid_period: bool (optional)

        :param quality_warn: quality_warn parameter
        :type quality_warn: bool (optional)

        :param risk_warn: risk_warn parameter
        :type risk_warn: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.detect_direction = detect_direction
        self.driving_license_side = driving_license_side
        self.unified_valid_period = unified_valid_period
        self.quality_warn = quality_warn
        self.risk_warn = risk_warn

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
        if self.detect_direction is not None:
            result['detect_direction'] = self.detect_direction
        if self.driving_license_side is not None:
            result['driving_license_side'] = self.driving_license_side
        if self.unified_valid_period is not None:
            result['unified_valid_period'] = self.unified_valid_period
        if self.quality_warn is not None:
            result['quality_warn'] = self.quality_warn
        if self.risk_warn is not None:
            result['risk_warn'] = self.risk_warn
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DrivingLicenseRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('detect_direction') is not None:
            self.detect_direction = m.get('detect_direction')
        if m.get('driving_license_side') is not None:
            self.driving_license_side = m.get('driving_license_side')
        if m.get('unified_valid_period') is not None:
            self.unified_valid_period = m.get('unified_valid_period')
        if m.get('quality_warn') is not None:
            self.quality_warn = m.get('quality_warn')
        if m.get('risk_warn') is not None:
            self.risk_warn = m.get('risk_warn')
        return self
