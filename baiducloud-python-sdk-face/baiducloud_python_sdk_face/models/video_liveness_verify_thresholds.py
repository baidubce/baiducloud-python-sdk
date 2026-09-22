"""
VideoLivenessVerifyThresholds information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VideoLivenessVerifyThresholds(AbstractModel):
    """
    VideoLivenessVerifyThresholds
    """

    def __init__(self, frr_1e_4=None, frr_1e_3=None, frr_1e_2=None):
        """
        Initialize VideoLivenessVerifyThresholds instance.

        :param frr_1e_4: 万分之一误拒率的阈值
        :type frr_1e_4: float (optional)

        :param frr_1e_3: 千分之一误拒率的阈值
        :type frr_1e_3: float (optional)

        :param frr_1e_2: 百分之一误拒率的阈值
        :type frr_1e_2: float (optional)
        """
        super().__init__()
        self.frr_1e_4 = frr_1e_4
        self.frr_1e_3 = frr_1e_3
        self.frr_1e_2 = frr_1e_2

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
        if self.frr_1e_4 is not None:
            result['frr_1e-4'] = self.frr_1e_4
        if self.frr_1e_3 is not None:
            result['frr_1e-3'] = self.frr_1e_3
        if self.frr_1e_2 is not None:
            result['frr_1e-2'] = self.frr_1e_2
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VideoLivenessVerifyThresholds

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('frr_1e-4') is not None:
            self.frr_1e_4 = m.get('frr_1e-4')
        if m.get('frr_1e-3') is not None:
            self.frr_1e_3 = m.get('frr_1e-3')
        if m.get('frr_1e-2') is not None:
            self.frr_1e_2 = m.get('frr_1e-2')
        return self
