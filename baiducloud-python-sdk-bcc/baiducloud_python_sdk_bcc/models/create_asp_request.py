"""
Request entity for CreateAspRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateAspRequest(AbstractModel):
    """
    Request entity for CreateAspRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, time_points, repeat_weekdays, retention_days):
        """
        Initialize CreateAspRequest request entity.

        :param name: 自动快照策略名称，支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65
        :type name: str (required)

        :param time_points: 一天中做快照时间点，取值为0~23
        :type time_points: List[int] (required)

        :param repeat_weekdays: 一周中做快照的时间，取值为0~6
        :type repeat_weekdays: List[int] (required)

        :param retention_days: 自动快照保留天数，取-1则永久保留
        :type retention_days: str (required)
        """
        super().__init__()
        self.name = name
        self.time_points = time_points
        self.repeat_weekdays = repeat_weekdays
        self.retention_days = retention_days

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
        if self.name is not None:
            result['name'] = self.name
        if self.time_points is not None:
            result['timePoints'] = self.time_points
        if self.repeat_weekdays is not None:
            result['repeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAspRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('timePoints') is not None:
            self.time_points = m.get('timePoints')
        if m.get('repeatWeekdays') is not None:
            self.repeat_weekdays = m.get('repeatWeekdays')
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        return self
