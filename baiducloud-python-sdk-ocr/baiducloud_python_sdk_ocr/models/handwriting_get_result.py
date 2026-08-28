"""
HandwritingGetResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.handwriting_get_essay_result import HandwritingGetEssayResult


class HandwritingGetResult(AbstractModel):
    """
    HandwritingGetResult
    """

    def __init__(
        self,
        task_id=None,
        status=None,
        created_time=None,
        started_time=None,
        finished_time=None,
        duration=None,
        result=None,
    ):
        """
        Initialize HandwritingGetResult instance.

        :param task_id: 任务ID
        :type task_id: str (optional)

        :param status: 任务状态，pending：排队中；processing：运行中；success：成功；failed：失败
        :type status: str (optional)

        :param created_time: 任务创建时间
        :type created_time: int (optional)

        :param started_time: 任务开始时间
        :type started_time: int (optional)

        :param finished_time: 任务结束时间
        :type finished_time: int (optional)

        :param duration: 任务执行时长
        :type duration: int (optional)

        :param result: result attribute
        :type result: HandwritingGetEssayResult (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.status = status
        self.created_time = created_time
        self.started_time = started_time
        self.finished_time = finished_time
        self.duration = duration
        self.result = result

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
        if self.created_time is not None:
            result['created_time'] = self.created_time
        if self.started_time is not None:
            result['started_time'] = self.started_time
        if self.finished_time is not None:
            result['finished_time'] = self.finished_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.result is not None:
            result['result'] = self.result.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HandwritingGetResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('created_time') is not None:
            self.created_time = m.get('created_time')
        if m.get('started_time') is not None:
            self.started_time = m.get('started_time')
        if m.get('finished_time') is not None:
            self.finished_time = m.get('finished_time')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('result') is not None:
            self.result = HandwritingGetEssayResult().from_dict(m.get('result'))
        return self
