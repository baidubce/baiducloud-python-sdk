"""
CdsCustomPeriod information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CdsCustomPeriod(AbstractModel):
    """
    CdsCustomPeriod
    """

    def __init__(self, period=None, volume_id=None):
        """
        Initialize CdsCustomPeriod instance.

        :param period: 续费时长，单位为月，范围为【1，60】。需保证续费后磁盘的到期时间等于或晚于BCC到期时间，否则续费失败。（实例续费）
        :type period: int (optional)

        :param volume_id: 磁盘ID（磁盘详情、磁盘列表接口返回、实例续费）
        :type volume_id: str (optional)
        """
        super().__init__()
        self.period = period
        self.volume_id = volume_id

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
        if self.period is not None:
            result['period'] = self.period
        if self.volume_id is not None:
            result['volumeId'] = self.volume_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CdsCustomPeriod

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        return self
