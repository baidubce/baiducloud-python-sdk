"""
Task information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.progress import Progress


class Task(AbstractModel):
    """
    Task
    """

    def __init__(
        self,
        task_id=None,
        task_type=None,
        task_name=None,
        instance_id=None,
        instance_name=None,
        user_id=None,
        region=None,
        task_status=None,
        create_time=None,
        update_time=None,
        finish_time=None,
        cancel_flag=None,
        progress=None,
    ):
        """
        Initialize Task instance.

        :param task_id: 任务ID
        :type task_id: int (optional)

        :param task_type: task_type attribute
        :type task_type: str (optional)

        :param task_name: 任务名称，如：配置变更/主备切换/原地重启实例/迁移可用区/切换重启实例
        :type task_name: str (optional)

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param instance_name: 实例名称
        :type instance_name: str (optional)

        :param user_id: 用户ID
        :type user_id: str (optional)

        :param region: 实例所在地域
        :type region: str (optional)

        :param task_status: 任务状态，可取值：created/running/success/failed/cancelled
        :type task_status: str (optional)

        :param create_time: 任务创建时间
        :type create_time: str (optional)

        :param update_time: 任务更新时间
        :type update_time: str (optional)

        :param finish_time: 任务完成时间，未完成时为 `0000-00-00 00:00:00`
        :type finish_time: str (optional)

        :param cancel_flag: 是否可取消标志，0：不可取消，1：可取消
        :type cancel_flag: int (optional)

        :param progress: 任务进度步骤列表，元素结构见下方 Progress
        :type progress: List[Progress] (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.task_type = task_type
        self.task_name = task_name
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.user_id = user_id
        self.region = region
        self.task_status = task_status
        self.create_time = create_time
        self.update_time = update_time
        self.finish_time = finish_time
        self.cancel_flag = cancel_flag
        self.progress = progress

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
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.task_name is not None:
            result['taskName'] = self.task_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.region is not None:
            result['region'] = self.region
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.cancel_flag is not None:
            result['cancelFlag'] = self.cancel_flag
        if self.progress is not None:
            result['progress'] = [i.to_dict() for i in self.progress]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Task

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('cancelFlag') is not None:
            self.cancel_flag = m.get('cancelFlag')
        if m.get('progress') is not None:
            self.progress = [Progress().from_dict(i) for i in m.get('progress')]
        return self
