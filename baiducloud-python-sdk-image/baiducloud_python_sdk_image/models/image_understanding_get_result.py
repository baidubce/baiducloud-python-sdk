"""
ImageUnderstandingGetResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ImageUnderstandingGetResult(AbstractModel):
    """
    ImageUnderstandingGetResult
    """

    def __init__(self, task_id=None, ret_code=None, ret_msg=None, description=None):
        """
        Initialize ImageUnderstandingGetResult instance.

        :param task_id: 该结果对应请求的task_id
        :type task_id: str (optional)

        :param ret_code: 识别状态，0：处理成功；1：处理中
        :type ret_code: int (optional)

        :param ret_msg: 识别状态信息，success：处理成功；processing：处理中
        :type ret_msg: str (optional)

        :param description: 针对输入的question问题，对图片内容进行分析后输出的答案
        :type description: str (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.ret_code = ret_code
        self.ret_msg = ret_msg
        self.description = description

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
        if self.ret_code is not None:
            result['ret_code'] = self.ret_code
        if self.ret_msg is not None:
            result['ret_msg'] = self.ret_msg
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImageUnderstandingGetResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        if m.get('ret_code') is not None:
            self.ret_code = m.get('ret_code')
        if m.get('ret_msg') is not None:
            self.ret_msg = m.get('ret_msg')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
