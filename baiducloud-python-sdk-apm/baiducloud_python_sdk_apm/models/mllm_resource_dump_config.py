"""
MllmResourceDumpConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


from baiducloud_python_sdk_core.annotation import host


class MllmResourceDumpConfig(AbstractModel):
    """
    MllmResourceDumpConfig
    """

    def __init__(self, retention_days=None, bucket=None):
        """
        Initialize MllmResourceDumpConfig instance.

        :param retention_days: 转储时长，单位：天
        :type retention_days: int (optional)

        :param bucket: BOS Bucket名称
        :type bucket: str (optional)
        """
        super().__init__()
        self.retention_days = retention_days
        self._bucket = bucket

    @property
    @host
    def bucket(self):
        """BOS Bucket名称"""
        return self._bucket

    @bucket.setter
    def bucket(self, value):
        """Set bucket value"""
        self._bucket = value

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
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.bucket is not None:
            result['bucket'] = self.bucket
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MllmResourceDumpConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        return self
