"""
AutoSnapshotPolicyModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AutoSnapshotPolicyModel(AbstractModel):
    """
    AutoSnapshotPolicyModel
    """

    def __init__(
        self,
        id=None,
        name=None,
        time_points=None,
        repeat_weekdays=None,
        status=None,
        retention_days=None,
        created_time=None,
        updated_time=None,
        deleted_time=None,
        last_execute_time=None,
        volume_count=None,
    ):
        """
        Initialize AutoSnapshotPolicyModel instance.

        :param id: 自动快照策略ID（查询磁盘详情返回）
        :type id: str (optional)

        :param name: name attribute
        :type name: str (optional)

        :param time_points: time_points attribute
        :type time_points: List[int] (optional)

        :param repeat_weekdays: repeat_weekdays attribute
        :type repeat_weekdays: List[int] (optional)

        :param status: 快照状态, 有active(运行)、deleted(删除)、paused(暂停)三种状态（查询磁盘详情返回）
        :type status: str (optional)

        :param retention_days: 指定自动快照的保留时间, 单位为天。-1: 永久保存 1~65536: 指定保存天数。（查询磁盘详情返回）
        :type retention_days: int (optional)

        :param created_time: 自动快照策略的创建时间, 符合BCE规范的日期格式 (自该字段起, 及之后字段, 在volume的接口中没有返回)
        :type created_time: str (optional)

        :param updated_time: 自动快照策略的最近更新时间, 符合BCE规范的日期格式
        :type updated_time: str (optional)

        :param deleted_time: 自动快照策略的删除时间, 符合BCE规范的日期格式
        :type deleted_time: str (optional)

        :param last_execute_time: 自动快照策略的最后执行时间, 符合BCE规范的日期格式
        :type last_execute_time: str (optional)

        :param volume_count: 关联磁盘数量
        :type volume_count: int (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.time_points = time_points
        self.repeat_weekdays = repeat_weekdays
        self.status = status
        self.retention_days = retention_days
        self.created_time = created_time
        self.updated_time = updated_time
        self.deleted_time = deleted_time
        self.last_execute_time = last_execute_time
        self.volume_count = volume_count

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.time_points is not None:
            result['timePoints'] = self.time_points
        if self.repeat_weekdays is not None:
            result['repeatWeekdays'] = self.repeat_weekdays
        if self.status is not None:
            result['status'] = self.status
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        if self.deleted_time is not None:
            result['deletedTime'] = self.deleted_time
        if self.last_execute_time is not None:
            result['lastExecuteTime'] = self.last_execute_time
        if self.volume_count is not None:
            result['volumeCount'] = self.volume_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AutoSnapshotPolicyModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('timePoints') is not None:
            self.time_points = m.get('timePoints')
        if m.get('repeatWeekdays') is not None:
            self.repeat_weekdays = m.get('repeatWeekdays')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        if m.get('deletedTime') is not None:
            self.deleted_time = m.get('deletedTime')
        if m.get('lastExecuteTime') is not None:
            self.last_execute_time = m.get('lastExecuteTime')
        if m.get('volumeCount') is not None:
            self.volume_count = m.get('volumeCount')
        return self
