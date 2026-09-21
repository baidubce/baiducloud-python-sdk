"""
MySQLFilterItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MySQLFilterItem(AbstractModel):
    """
    MySQLFilterItem
    """

    def __init__(
        self,
        filter_id=None,
        filter_key=None,
        filter_limit=None,
        filter_type=None,
        filter_status=None,
        create_time=None,
        update_time=None,
    ):
        """
        Initialize MySQLFilterItem instance.

        :param filter_id: 限流任务ID
        :type filter_id: str (optional)

        :param filter_key: 限流关键字，多组关键字，逗号分割，支持字符集utf8，除逗号为关键字外只能做分隔符使用，其他不设置限制
        :type filter_key: str (optional)

        :param filter_limit: 限流规则的并发数：取值 0-100w 闭区间
        :type filter_limit: int (optional)

        :param filter_type: SQL限流类型，支持SELECT、UPDATE、INSERT、DELETE、REPLACE
        :type filter_type: str (optional)

        :param filter_status: 任务指定操作类型：ON：开启SQL限流OFF：停止SQL限流
        :type filter_status: str (optional)

        :param create_time: 任务创建时间
        :type create_time: datetime (optional)

        :param update_time: 任务更新时间
        :type update_time: datetime (optional)
        """
        super().__init__()
        self.filter_id = filter_id
        self.filter_key = filter_key
        self.filter_limit = filter_limit
        self.filter_type = filter_type
        self.filter_status = filter_status
        self.create_time = create_time
        self.update_time = update_time

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
        if self.filter_id is not None:
            result['filterId'] = self.filter_id
        if self.filter_key is not None:
            result['filterKey'] = self.filter_key
        if self.filter_limit is not None:
            result['filterLimit'] = self.filter_limit
        if self.filter_type is not None:
            result['filterType'] = self.filter_type
        if self.filter_status is not None:
            result['filterStatus'] = self.filter_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MySQLFilterItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('filterId') is not None:
            self.filter_id = m.get('filterId')
        if m.get('filterKey') is not None:
            self.filter_key = m.get('filterKey')
        if m.get('filterLimit') is not None:
            self.filter_limit = m.get('filterLimit')
        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')
        if m.get('filterStatus') is not None:
            self.filter_status = m.get('filterStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
