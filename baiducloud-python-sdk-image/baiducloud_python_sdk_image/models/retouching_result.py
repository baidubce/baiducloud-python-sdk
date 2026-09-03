"""
RetouchingResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RetouchingResult(AbstractModel):
    """
    RetouchingResult
    """

    def __init__(self, task_id=None, status=None, dlink=None, callback_data=None):
        """
        Initialize RetouchingResult instance.

        :param task_id: 任务ID
        :type task_id: str (optional)

        :param status: 任务状态：pending排队中；processing运行中；success成功；failed失败
        :type status: str (optional)

        :param dlink: 结果图下载链接，有效期8小时
        :type dlink: str (optional)

        :param callback_data: 提交任务时的透传参数
        :type callback_data: str (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.status = status
        self.dlink = dlink
        self.callback_data = callback_data

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
            result['task_id'] = self.task_id
        if self.status is not None:
            result['status'] = self.status
        if self.dlink is not None:
            result['dlink'] = self.dlink
        if self.callback_data is not None:
            result['callback_data'] = self.callback_data
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RetouchingResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('dlink') is not None:
            self.dlink = m.get('dlink')
        if m.get('callback_data') is not None:
            self.callback_data = m.get('callback_data')
        return self
