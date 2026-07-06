"""
JobResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class JobResult(AbstractModel):
    """
    JobResult
    """

    def __init__(self, job_id=None, success=None, error_msg=None):
        """
        Initialize JobResult instance.

        :param job_id: 训练任务唯一标识id
        :type job_id: str (optional)

        :param success: 任务是否处理成功（成功列表固定为 true，失败列表固定为 false）
        :type success: bool (optional)

        :param error_msg: 失败原因描述，失败时返回，成功返回空
        :type error_msg: str (optional)
        """
        super().__init__()
        self.job_id = job_id
        self.success = success
        self.error_msg = error_msg

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
        if self.success is not None:
            result['success'] = self.success
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: JobResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        return self
