"""
LoopModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.tag_selector import TagSelector


class LoopModel(AbstractModel):
    """
    LoopModel
    """

    def __init__(self, init_context=None, worker_selectors=None):
        """
        Initialize LoopModel instance.

        :param init_context: 循环初始上下文
        :type init_context: object (optional)

        :param worker_selectors: 工作机选择器列表
        :type worker_selectors: List[TagSelector] (optional)
        """
        super().__init__()
        self.init_context = init_context
        self.worker_selectors = worker_selectors

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
        if self.init_context is not None:
            result['initContext'] = self.init_context
        if self.worker_selectors is not None:
            result['workerSelectors'] = [i.to_dict() for i in self.worker_selectors]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LoopModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('initContext') is not None:
            self.init_context = m.get('initContext')
        if m.get('workerSelectors') is not None:
            self.worker_selectors = [TagSelector().from_dict(i) for i in m.get('workerSelectors')]
        return self
