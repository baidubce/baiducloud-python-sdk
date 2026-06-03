"""
ExecuteInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ExecuteInfo(AbstractModel):
    """
    ExecuteInfo
    """

    def __init__(self, job_id=None, trigger_time=None, status=None, errmsg=None, report=None):
        """
        Initialize ExecuteInfo instance.

        :param job_id: 任务子ID
        :type job_id: str (optional)

        :param trigger_time: 任务触发时间
        :type trigger_time: str (optional)

        :param status: 任务执行状态<br>• 0: 任务成功<br>• 1: 任务失败(有报告)<br>• 2: 任务失败(没报告)
        :type status: int (optional)

        :param errmsg: 错误提示信息
        :type errmsg: str (optional)

        :param report: 任务报告所在的bos路径
        :type report: str (optional)
        """
        super().__init__()
        self.job_id = job_id
        self.trigger_time = trigger_time
        self.status = status
        self.errmsg = errmsg
        self.report = report

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
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.trigger_time is not None:
            result['triggerTime'] = self.trigger_time
        if self.status is not None:
            result['status'] = self.status
        if self.errmsg is not None:
            result['errmsg'] = self.errmsg
        if self.report is not None:
            result['report'] = self.report
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ExecuteInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('triggerTime') is not None:
            self.trigger_time = m.get('triggerTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('errmsg') is not None:
            self.errmsg = m.get('errmsg')
        if m.get('report') is not None:
            self.report = m.get('report')
        return self
