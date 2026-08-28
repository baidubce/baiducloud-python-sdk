"""
PaperCutEduVlmGetResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.paper_cut_edu_vlm_get_qus_result import PaperCutEduVlmGetQusResult


class PaperCutEduVlmGetResult(AbstractModel):
    """
    PaperCutEduVlmGetResult
    """

    def __init__(self, task_id=None, status=None, qus_results=None):
        """
        Initialize PaperCutEduVlmGetResult instance.

        :param task_id: 任务ID
        :type task_id: str (optional)

        :param status: 任务状态：pending-排队中；running-运行中；Success-成功；failed-失败
        :type status: str (optional)

        :param qus_results: 题目元素信息
        :type qus_results: List[PaperCutEduVlmGetQusResult] (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.status = status
        self.qus_results = qus_results

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
        if self.qus_results is not None:
            result['qus_results'] = [i.to_dict() for i in self.qus_results]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PaperCutEduVlmGetResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('qus_results') is not None:
            self.qus_results = [PaperCutEduVlmGetQusResult().from_dict(i) for i in m.get('qus_results')]
        return self
