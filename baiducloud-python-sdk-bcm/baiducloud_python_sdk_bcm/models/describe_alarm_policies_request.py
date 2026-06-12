"""
Request entity for DescribeAlarmPoliciesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAlarmPoliciesRequest(AbstractModel):
    """
    Request entity for DescribeAlarmPoliciesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        page_no,
        page_size,
        policy_name=None,
        policy_id=None,
        scope=None,
        resource_type=None,
        recursive=None,
        sub_resource_type=None,
        notify_enabled=None,
        type=None,
        order=None,
        order_by=None,
    ):
        """
        Initialize DescribeAlarmPoliciesRequest request entity.

        :param policy_name: 按策略名称筛选，支持部分匹配
        :type policy_name: str (optional)

        :param policy_id: 按策略ID筛选，精确匹配
        :type policy_id: str (optional)

        :param scope: 云产品类型筛选
        :type scope: str (optional)

        :param resource_type: 资源类型筛选（scope不能为空）
        :type resource_type: str (optional)

        :param recursive: 是否包含子类型，默认为false
        :type recursive: bool (optional)

        :param sub_resource_type: 子资源类型筛选
        :type sub_resource_type: str (optional)

        :param notify_enabled: 通知状态筛选
        :type notify_enabled: bool (optional)

        :param type: 策略类型筛选，可选值：APP / SITE / CLOUD / CUSTOM
        :type type: str (optional)

        :param order: 排序顺序，默认值：desc，可选值：desc / asc
        :type order: str (optional)

        :param order_by: 排序字段，默认值：updatedTime，可选值：updatedTime / createdTime
        :type order_by: str (optional)

        :param page_no: 页号，从1开始
        :type page_no: int (required)

        :param page_size: 页大小，取值范围：[1, 100]
        :type page_size: int (required)
        """
        super().__init__()
        self.policy_name = policy_name
        self.policy_id = policy_id
        self.scope = scope
        self.resource_type = resource_type
        self.recursive = recursive
        self.sub_resource_type = sub_resource_type
        self.notify_enabled = notify_enabled
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
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.recursive is not None:
            result['recursive'] = self.recursive
        if self.sub_resource_type is not None:
            result['subResourceType'] = self.sub_resource_type
        if self.notify_enabled is not None:
            result['notifyEnabled'] = self.notify_enabled
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
        :rtype: DescribeAlarmPoliciesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('recursive') is not None:
            self.recursive = m.get('recursive')
        if m.get('subResourceType') is not None:
            self.sub_resource_type = m.get('subResourceType')
        if m.get('notifyEnabled') is not None:
            self.notify_enabled = m.get('notifyEnabled')
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
