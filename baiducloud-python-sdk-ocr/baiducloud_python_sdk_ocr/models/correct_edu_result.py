"""
CorrectEduResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.stat_result import StatResult

from baiducloud_python_sdk_ocr.models.image_result import ImageResult


class CorrectEduResult(AbstractModel):
    """
    CorrectEduResult
    """

    def __init__(self, task_id=None, is_all_finished=None, status=None, stat_result=None, image_results=None):
        """
        Initialize CorrectEduResult instance.

        :param task_id: 任务ID
        :type task_id: str (optional)

        :param is_all_finished: 是否完成批改。true：批改完成；false：批改未完成
        :type is_all_finished: bool (optional)

        :param status: status attribute
        :type status: str (optional)

        :param stat_result: stat_result attribute
        :type stat_result: StatResult (optional)

        :param image_results: 单张图片的批改结果数组，每张图片对应一个元素
        :type image_results: List[ImageResult] (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.is_all_finished = is_all_finished
        self.status = status
        self.stat_result = stat_result
        self.image_results = image_results

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
        if self.is_all_finished is not None:
            result['isAllFinished'] = self.is_all_finished
        if self.status is not None:
            result['status'] = self.status
        if self.stat_result is not None:
            result['stat_result'] = self.stat_result.to_dict()
        if self.image_results is not None:
            result['imageResults'] = [i.to_dict() for i in self.image_results]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CorrectEduResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        if m.get('isAllFinished') is not None:
            self.is_all_finished = m.get('isAllFinished')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('stat_result') is not None:
            self.stat_result = StatResult().from_dict(m.get('stat_result'))
        if m.get('imageResults') is not None:
            self.image_results = [ImageResult().from_dict(i) for i in m.get('imageResults')]
        return self
