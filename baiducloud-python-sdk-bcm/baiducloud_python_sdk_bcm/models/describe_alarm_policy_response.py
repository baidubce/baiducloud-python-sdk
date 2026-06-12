"""
Request entity for DescribeAlarmPolicyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcm.models.alarm_target import AlarmTarget
from baiducloud_python_sdk_bcm.models.alarm_rule import AlarmRule
from baiducloud_python_sdk_bcm.models.policy_action import PolicyAction


class DescribeAlarmPolicyResponse(BceResponse):
    """
    DescribeAlarmPolicyResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        id=None,
        name=None,
        scope=None,
        resource_type=None,
        sub_resource_type=None,
        target=None,
        rules=None,
        actions=None,
        created_time=None,
        updated_time=None,
    ):
        """
        Initialize DescribeAlarmPolicyResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 响应码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param id: 策略ID
        :type id: str (optional)

        :param name: 策略名称
        :type name: str (optional)

        :param scope: 云产品类型
        :type scope: str (optional)

        :param resource_type: 资源类型
        :type resource_type: str (optional)

        :param sub_resource_type: 子资源类型（当requireSubResourceType=true时返回）
        :type sub_resource_type: str (optional)

        :param target: target field
        :type target: AlarmTarget (optional)

        :param rules: 报警规则列表
        :type rules: List[AlarmRule] (optional)

        :param actions: 报警通知项列表
        :type actions: List[PolicyAction] (optional)

        :param created_time: 创建时间，UTC格式
        :type created_time: str (optional)

        :param updated_time: 更新时间，UTC格式
        :type updated_time: str (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.id = id
        self.name = name
        self.scope = scope
        self.resource_type = resource_type
        self.sub_resource_type = sub_resource_type
        self.target = target
        self.rules = rules
        self.actions = actions
        self.created_time = created_time
        self.updated_time = updated_time

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sub_resource_type is not None:
            result['subResourceType'] = self.sub_resource_type
        if self.target is not None:
            result['target'] = self.target.to_dict()
        if self.rules is not None:
            result['rules'] = [i.to_dict() for i in self.rules]
        if self.actions is not None:
            result['actions'] = [i.to_dict() for i in self.actions]
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAlarmPolicyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('subResourceType') is not None:
            self.sub_resource_type = m.get('subResourceType')
        if m.get('target') is not None:
            self.target = AlarmTarget().from_dict(m.get('target'))
        if m.get('rules') is not None:
            self.rules = [AlarmRule().from_dict(i) for i in m.get('rules')]
        if m.get('actions') is not None:
            self.actions = [PolicyAction().from_dict(i) for i in m.get('actions')]
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self
