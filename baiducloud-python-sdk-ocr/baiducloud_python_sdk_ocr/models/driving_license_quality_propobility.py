"""
DrivingLicenseQualityPropobility information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DrivingLicenseQualityPropobility(AbstractModel):
    """
    DrivingLicenseQualityPropobility
    """

    def __init__(self, is_clear_propobility=None, is_complete_propobility=None, is_noshield_propobility=None):
        """
        Initialize DrivingLicenseQualityPropobility instance.

        :param is_clear_propobility: is_clear_propobility attribute
        :type is_clear_propobility: float (optional)

        :param is_complete_propobility: is_complete_propobility attribute
        :type is_complete_propobility: float (optional)

        :param is_noshield_propobility: 是否被遮挡质量类型对应的概率，0代表图像被遮挡，1代表图像没有被遮挡
        :type is_noshield_propobility: str (optional)
        """
        super().__init__()
        self.is_clear_propobility = is_clear_propobility
        self.is_complete_propobility = is_complete_propobility
        self.is_noshield_propobility = is_noshield_propobility

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
        if self.is_clear_propobility is not None:
            result['is_clear_propobility'] = self.is_clear_propobility
        if self.is_complete_propobility is not None:
            result['is_complete_propobility'] = self.is_complete_propobility
        if self.is_noshield_propobility is not None:
            result['is_noshield_propobility'] = self.is_noshield_propobility
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DrivingLicenseQualityPropobility

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('is_clear_propobility') is not None:
            self.is_clear_propobility = m.get('is_clear_propobility')
        if m.get('is_complete_propobility') is not None:
            self.is_complete_propobility = m.get('is_complete_propobility')
        if m.get('is_noshield_propobility') is not None:
            self.is_noshield_propobility = m.get('is_noshield_propobility')
        return self
