"""
TriggerJob information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TriggerJob(AbstractModel):
    """
    TriggerJob
    """

    def __init__(
        self,
        creation_time=None,
        event_type=None,
        id=None,
        images=None,
        notify_type=None,
        operator=None,
        policy_id=None,
        status=None,
        update_time=None,
    ):
        """
        Initialize TriggerJob instance.

        :param creation_time: 触发器任务创建时间
        :type creation_time: str (optional)

        :param event_type: 触发事件类型
        :type event_type: str (optional)

        :param id: 触发器任务 ID
        :type id: int (optional)

        :param images: 触发对象列表
        :type images: List[str] (optional)

        :param notify_type: 通知类型
        :type notify_type: str (optional)

        :param operator: 操作人员
        :type operator: str (optional)

        :param policy_id: 触发器策略 ID
        :type policy_id: int (optional)

        :param status: 触发器任务状态
        :type status: str (optional)

        :param update_time: 触发器任务更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.creation_time = creation_time
        self.event_type = event_type
        self.id = id
        self.images = images
        self.notify_type = notify_type
        self.operator = operator
        self.policy_id = policy_id
        self.status = status
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
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.event_type is not None:
            result['eventType'] = self.event_type
        if self.id is not None:
            result['id'] = self.id
        if self.images is not None:
            result['images'] = self.images
        if self.notify_type is not None:
            result['notifyType'] = self.notify_type
        if self.operator is not None:
            result['operator'] = self.operator
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.status is not None:
            result['status'] = self.status
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
        :rtype: TriggerJob

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('images') is not None:
            self.images = m.get('images')
        if m.get('notifyType') is not None:
            self.notify_type = m.get('notifyType')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
