"""
Request entity for ActionRunListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cloudassistant.models.action_filter import ActionFilter


class ActionRunListRequest(AbstractModel):
    """
    Request entity for ActionRunListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        page_no,
        page_size,
        locale=None,
        sort=None,
        ascending=None,
        action=None,
        state=None,
        run_id=None,
        start_time=None,
        end_time=None,
    ):
        """
        Initialize ActionRunListRequest request entity.

        :param locale: locale parameter
        :type locale: str (optional)

        :param page_no: 页码
        :type page_no: int (required)

        :param page_size: 页大小
        :type page_size: int (required)

        :param sort: 排序字段
        :type sort: str (optional)

        :param ascending: 是否升序，默认false
        :type ascending: bool (optional)

        :param action: action parameter
        :type action: ActionFilter (optional)

        :param state: 根据执行状态过滤。枚举值：FAILED（执行失败），RUNNING（执行中），SUCCESS（执行完成）
        :type state: str (optional)

        :param run_id: 根据执行ID过滤
        :type run_id: str (optional)

        :param start_time: 时间筛选，Unix时间戳（毫秒）。执行开始时间 >= endTime,Unix时间戳（毫秒）
        :type start_time: int (optional)

        :param end_time: 时间筛选，Unix时间戳（毫秒）。执行开始时间 <= endTime，Unix时间戳（毫秒）
        :type end_time: int (optional)
        """
        super().__init__()
        self.locale = locale
        self.page_no = page_no
        self.page_size = page_size
        self.sort = sort
        self.ascending = ascending
        self.action = action
        self.state = state
        self.run_id = run_id
        self.start_time = start_time
        self.end_time = end_time

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
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sort is not None:
            result['sort'] = self.sort
        if self.ascending is not None:
            result['ascending'] = self.ascending
        if self.action is not None:
            result['action'] = self.action.to_dict()
        if self.state is not None:
            result['state'] = self.state
        if self.run_id is not None:
            result['runId'] = self.run_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ActionRunListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('ascending') is not None:
            self.ascending = m.get('ascending')
        if m.get('action') is not None:
            self.action = ActionFilter().from_dict(m.get('action'))
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('runId') is not None:
            self.run_id = m.get('runId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
