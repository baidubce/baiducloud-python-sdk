"""
Request entity for DescribeAlarmsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAlarmsRequest(AbstractModel):
    """
    Request entity for DescribeAlarmsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        start_time,
        end_time,
        page_no,
        page_size,
        policy_name=None,
        scope=None,
        resource_type=None,
        state=None,
        type=None,
        order=None,
        order_by=None,
    ):
        """
        Initialize DescribeAlarmsRequest request entity.

        :param start_time: 查询起始时间
        :type start_time: str (required)

        :param end_time: 查询结束时间
        :type end_time: str (required)

        :param policy_name: 报警策略名称，模糊查询
        :type policy_name: str (optional)

        :param scope: 云产品命名空间
        :type scope: str (optional)

        :param resource_type: 资源类型
        :type resource_type: str (optional)

        :param state: 报警状态，可选OK/ALERT/NO_DATA/CLOSED
        :type state: str (optional)

        :param type: 报警类型
        :type type: str (optional)

        :param order: 排序方式，asc/desc
        :type order: str (optional)

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param page_no: 页码
        :type page_no: int (required)

        :param page_size: 每页条数
        :type page_size: int (required)
        """
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.policy_name = policy_name
        self.scope = scope
        self.resource_type = resource_type
        self.state = state
        self.type = type
        self.order = order
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size

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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.state is not None:
            result['state'] = self.state
        if self.type is not None:
            result['type'] = self.type
        if self.order is not None:
            result['order'] = self.order
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAlarmsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
