"""
StopBatchResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aihc.models.job_result import JobResult

from baiducloud_python_sdk_aihc.models.job_result import JobResult


class StopBatchResult(AbstractModel):
    """
    StopBatchResult
    """

    def __init__(self, success_num=None, failed_num=None, success=None, success_list=None, failed_list=None):
        """
        Initialize StopBatchResult instance.

        :param success_num: 成功任务数量
        :type success_num: int (optional)

        :param failed_num: 失败任务数量
        :type failed_num: int (optional)

        :param success: 整体是否全部成功
        :type success: bool (optional)

        :param success_list: 成功任务列表
        :type success_list: List[JobResult] (optional)

        :param failed_list: 失败任务列表（无失败则为空）
        :type failed_list: List[JobResult] (optional)
        """
        super().__init__()
        self.success_num = success_num
        self.failed_num = failed_num
        self.success = success
        self.success_list = success_list
        self.failed_list = failed_list

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
        if self.success_num is not None:
            result['successNum'] = self.success_num
        if self.failed_num is not None:
            result['failedNum'] = self.failed_num
        if self.success is not None:
            result['success'] = self.success
        if self.success_list is not None:
            result['successList'] = [i.to_dict() for i in self.success_list]
        if self.failed_list is not None:
            result['failedList'] = [i.to_dict() for i in self.failed_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: StopBatchResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('successNum') is not None:
            self.success_num = m.get('successNum')
        if m.get('failedNum') is not None:
            self.failed_num = m.get('failedNum')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('successList') is not None:
            self.success_list = [JobResult().from_dict(i) for i in m.get('successList')]
        if m.get('failedList') is not None:
            self.failed_list = [JobResult().from_dict(i) for i in m.get('failedList')]
        return self
