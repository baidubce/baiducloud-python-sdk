"""
BigKeyTask information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BigKeyTask(AbstractModel):
    """
    BigKeyTask
    """

    def __init__(
        self,
        node_id=None,
        task_id=None,
        create_time=None,
        end_time=None,
        start_time=None,
        status=None,
        status_desc=None,
    ):
        """
        Initialize BigKeyTask instance.

        :param node_id: 节点ID
        :type node_id: str (optional)

        :param task_id: 任务ID
        :type task_id: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param end_time: 结束时间
        :type end_time: str (optional)

        :param start_time: 开始时间
        :type start_time: str (optional)

        :param status: 任务状态：1：等待调度2：等待分析3：分析中4：分析成功5：分析失败6：已删除
        :type status: int (optional)

        :param status_desc: 状态的描述：等待调度等待分析分析中分析成功分析失败已删除
        :type status_desc: str (optional)
        """
        super().__init__()
        self.node_id = node_id
        self.task_id = task_id
        self.create_time = create_time
        self.end_time = end_time
        self.start_time = start_time
        self.status = status
        self.status_desc = status_desc

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
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BigKeyTask

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        return self
