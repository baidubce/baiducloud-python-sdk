"""
DatasetScanInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.statistics import Statistics


class DatasetScanInfo(AbstractModel):
    """
    DatasetScanInfo
    """

    def __init__(self, statistics=None, is_truncated=None):
        """
        Initialize DatasetScanInfo instance.

        :param statistics: statistics attribute
        :type statistics: Statistics (optional)

        :param is_truncated: 是否截断
        :type is_truncated: bool (optional)
        """
        super().__init__()
        self.statistics = statistics
        self.is_truncated = is_truncated

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
        if self.statistics is not None:
            result['statistics'] = self.statistics.to_dict()
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DatasetScanInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('statistics') is not None:
            self.statistics = Statistics().from_dict(m.get('statistics'))
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        return self
