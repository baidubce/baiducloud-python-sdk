"""
ActionRun information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cloudassistant.models.action import Action

from baiducloud_python_sdk_cloudassistant.models.statistics import Statistics

from baiducloud_python_sdk_cloudassistant.models.child_run import ChildRun


class ActionRun(AbstractModel):
    """
    ActionRun
    """

    def __init__(
        self,
        id=None,
        state=None,
        action=None,
        created_timestamp=None,
        finished_timestamp=None,
        statistics=None,
        children=None,
        total_count=None,
    ):
        """
        Initialize ActionRun instance.

        :param id: 执行ID
        :type id: str (optional)

        :param state: state attribute
        :type state: str (optional)

        :param action: action attribute
        :type action: Action (optional)

        :param created_timestamp: 执行开始时间。unix时间戳，单位：毫秒
        :type created_timestamp: int (optional)

        :param finished_timestamp: 执行结束时间，仅执行结束时返回
        :type finished_timestamp: int (optional)

        :param statistics: statistics attribute
        :type statistics: Statistics (optional)

        :param children: 子执行列表，读取详情时，响应此字段
        :type children: List[ChildRun] (optional)

        :param total_count: 子执行总数，读取详情时，响应此字段
        :type total_count: int (optional)
        """
        super().__init__()
        self.id = id
        self.state = state
        self.action = action
        self.created_timestamp = created_timestamp
        self.finished_timestamp = finished_timestamp
        self.statistics = statistics
        self.children = children
        self.total_count = total_count

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
        if self.state is not None:
            result['state'] = self.state
        if self.action is not None:
            result['action'] = self.action.to_dict()
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.finished_timestamp is not None:
            result['finishedTimestamp'] = self.finished_timestamp
        if self.statistics is not None:
            result['statistics'] = self.statistics.to_dict()
        if self.children is not None:
            result['children'] = [i.to_dict() for i in self.children]
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ActionRun

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('action') is not None:
            self.action = Action().from_dict(m.get('action'))
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('finishedTimestamp') is not None:
            self.finished_timestamp = m.get('finishedTimestamp')
        if m.get('statistics') is not None:
            self.statistics = Statistics().from_dict(m.get('statistics'))
        if m.get('children') is not None:
            self.children = [ChildRun().from_dict(i) for i in m.get('children')]
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self
