"""
BusinessLicenseQuality information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BusinessLicenseQuality(AbstractModel):
    """
    BusinessLicenseQuality
    """

    def __init__(self, is_clear=None, is_clear_propobility=None, is_complete=None, is_complete_propobility=None):
        """
        Initialize BusinessLicenseQuality instance.

        :param is_clear: 是否清晰：0-不清晰，1-清晰
        :type is_clear: int (optional)

        :param is_clear_propobility: 清晰概率，值在0-1之间，值越大表示图像质量越好
        :type is_clear_propobility: float (optional)

        :param is_complete: 是否边框/四角完整：0-不完整，1-完整
        :type is_complete: int (optional)

        :param is_complete_propobility: 边框/四角完整概率，值在0-1之间，值越大表示图像质量越好
        :type is_complete_propobility: float (optional)
        """
        super().__init__()
        self.is_clear = is_clear
        self.is_clear_propobility = is_clear_propobility
        self.is_complete = is_complete
        self.is_complete_propobility = is_complete_propobility

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
        if self.is_clear is not None:
            result['is_clear'] = self.is_clear
        if self.is_clear_propobility is not None:
            result['is_clear_propobility'] = self.is_clear_propobility
        if self.is_complete is not None:
            result['is_complete'] = self.is_complete
        if self.is_complete_propobility is not None:
            result['is_complete_propobility'] = self.is_complete_propobility
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BusinessLicenseQuality

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('is_clear') is not None:
            self.is_clear = m.get('is_clear')
        if m.get('is_clear_propobility') is not None:
            self.is_clear_propobility = m.get('is_clear_propobility')
        if m.get('is_complete') is not None:
            self.is_complete = m.get('is_complete')
        if m.get('is_complete_propobility') is not None:
            self.is_complete_propobility = m.get('is_complete_propobility')
        return self
