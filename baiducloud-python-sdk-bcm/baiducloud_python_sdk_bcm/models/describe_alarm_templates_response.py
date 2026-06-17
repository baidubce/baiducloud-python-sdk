"""
Request entity for DescribeAlarmTemplatesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcm.models.alarm_template import AlarmTemplate
from baiducloud_python_sdk_bcm.models.alarm_rule import AlarmRule


class DescribeAlarmTemplatesResponse(BceResponse):
    """
    DescribeAlarmTemplatesResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        page_no=None,
        page_size=None,
        total_count=None,
        alarm_templates=None,
        alarm_templates_id=None,
        alarm_templates_scope=None,
        alarm_templates_resource_type=None,
        alarm_templates_sub_resource_type=None,
        alarm_templates_name=None,
        alarm_templates_comment=None,
        alarm_templates_rules=None,
    ):
        """
        Initialize DescribeAlarmTemplatesResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 响应码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param page_no: 当前页码
        :type page_no: int (optional)

        :param page_size: 每页条数
        :type page_size: int (optional)

        :param total_count: 总记录数
        :type total_count: int (optional)

        :param alarm_templates: 报警模板列表
        :type alarm_templates: List[AlarmTemplate] (optional)

        :param alarm_templates_id: 报警模板ID
        :type alarm_templates_id: str (optional)

        :param alarm_templates_scope: 云产品类型
        :type alarm_templates_scope: str (optional)

        :param alarm_templates_resource_type: 资源类型
        :type alarm_templates_resource_type: str (optional)

        :param alarm_templates_sub_resource_type: 子资源类型
        :type alarm_templates_sub_resource_type: str (optional)

        :param alarm_templates_name: 模板名称
        :type alarm_templates_name: str (optional)

        :param alarm_templates_comment: 备注信息
        :type alarm_templates_comment: str (optional)

        :param alarm_templates_rules: 报警规则列表
        :type alarm_templates_rules: List[AlarmRule] (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.alarm_templates = alarm_templates
        self.alarm_templates_id = alarm_templates_id
        self.alarm_templates_scope = alarm_templates_scope
        self.alarm_templates_resource_type = alarm_templates_resource_type
        self.alarm_templates_sub_resource_type = alarm_templates_sub_resource_type
        self.alarm_templates_name = alarm_templates_name
        self.alarm_templates_comment = alarm_templates_comment
        self.alarm_templates_rules = alarm_templates_rules

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
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.alarm_templates is not None:
            result['alarmTemplates'] = [i.to_dict() for i in self.alarm_templates]
        if self.alarm_templates_id is not None:
            result['alarmTemplates.id'] = self.alarm_templates_id
        if self.alarm_templates_scope is not None:
            result['alarmTemplates.scope'] = self.alarm_templates_scope
        if self.alarm_templates_resource_type is not None:
            result['alarmTemplates.resourceType'] = self.alarm_templates_resource_type
        if self.alarm_templates_sub_resource_type is not None:
            result['alarmTemplates.subResourceType'] = self.alarm_templates_sub_resource_type
        if self.alarm_templates_name is not None:
            result['alarmTemplates.name'] = self.alarm_templates_name
        if self.alarm_templates_comment is not None:
            result['alarmTemplates.comment'] = self.alarm_templates_comment
        if self.alarm_templates_rules is not None:
            result['alarmTemplates.rules'] = [i.to_dict() for i in self.alarm_templates_rules]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAlarmTemplatesResponse

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
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('alarmTemplates') is not None:
            self.alarm_templates = [AlarmTemplate().from_dict(i) for i in m.get('alarmTemplates')]
        if m.get('alarmTemplates.id') is not None:
            self.alarm_templates_id = m.get('alarmTemplates.id')
        if m.get('alarmTemplates.scope') is not None:
            self.alarm_templates_scope = m.get('alarmTemplates.scope')
        if m.get('alarmTemplates.resourceType') is not None:
            self.alarm_templates_resource_type = m.get('alarmTemplates.resourceType')
        if m.get('alarmTemplates.subResourceType') is not None:
            self.alarm_templates_sub_resource_type = m.get('alarmTemplates.subResourceType')
        if m.get('alarmTemplates.name') is not None:
            self.alarm_templates_name = m.get('alarmTemplates.name')
        if m.get('alarmTemplates.comment') is not None:
            self.alarm_templates_comment = m.get('alarmTemplates.comment')
        if m.get('alarmTemplates.rules') is not None:
            self.alarm_templates_rules = [AlarmRule().from_dict(i) for i in m.get('alarmTemplates.rules')]
        return self
