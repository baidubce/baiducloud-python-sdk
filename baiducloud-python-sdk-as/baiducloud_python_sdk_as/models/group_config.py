"""
GroupConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GroupConfig(AbstractModel):
    """
    GroupConfig
    """

    def __init__(self, min_node_num=None, max_node_num=None, cooldown_in_sec=None, expect_num=None, init_num=None):
        """
        Initialize GroupConfig instance.

        :param min_node_num: 最小节点数量
        :type min_node_num: int (optional)

        :param max_node_num: 最大节点数量
        :type max_node_num: int (optional)

        :param cooldown_in_sec: 冷却时间
        :type cooldown_in_sec: int (optional)

        :param expect_num: 期望节点数，默认为-1，开启期望节点数后，健康检查任务会自动巡检，如果当前节点数和期望不一致会自动扩缩容保持一致
        :type expect_num: int (optional)

        :param init_num: 初始节点数，默认为-1
        :type init_num: int (optional)
        """
        super().__init__()
        self.min_node_num = min_node_num
        self.max_node_num = max_node_num
        self.cooldown_in_sec = cooldown_in_sec
        self.expect_num = expect_num
        self.init_num = init_num

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
        if self.min_node_num is not None:
            result['minNodeNum'] = self.min_node_num
        if self.max_node_num is not None:
            result['maxNodeNum'] = self.max_node_num
        if self.cooldown_in_sec is not None:
            result['cooldownInSec'] = self.cooldown_in_sec
        if self.expect_num is not None:
            result['expectNum'] = self.expect_num
        if self.init_num is not None:
            result['initNum'] = self.init_num
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GroupConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('minNodeNum') is not None:
            self.min_node_num = m.get('minNodeNum')
        if m.get('maxNodeNum') is not None:
            self.max_node_num = m.get('maxNodeNum')
        if m.get('cooldownInSec') is not None:
            self.cooldown_in_sec = m.get('cooldownInSec')
        if m.get('expectNum') is not None:
            self.expect_num = m.get('expectNum')
        if m.get('initNum') is not None:
            self.init_num = m.get('initNum')
        return self
