"""
TopicItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.topic_tag_item import TopicTagItem

from baiducloud_python_sdk_nlp.models.topic_tag_item import TopicTagItem


class TopicItem(AbstractModel):
    """
    TopicItem
    """

    def __init__(self, lv1_tag_list=None, lv2_tag_list=None):
        """
        Initialize TopicItem instance.

        :param lv1_tag_list: 一级分类结果（唯一）
        :type lv1_tag_list: List[TopicTagItem] (optional)

        :param lv2_tag_list: 二级分类结果
        :type lv2_tag_list: List[TopicTagItem] (optional)
        """
        super().__init__()
        self.lv1_tag_list = lv1_tag_list
        self.lv2_tag_list = lv2_tag_list

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
        if self.lv1_tag_list is not None:
            result['lv1_tag_list'] = [i.to_dict() for i in self.lv1_tag_list]
        if self.lv2_tag_list is not None:
            result['lv2_tag_list'] = [i.to_dict() for i in self.lv2_tag_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TopicItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('lv1_tag_list') is not None:
            self.lv1_tag_list = [TopicTagItem().from_dict(i) for i in m.get('lv1_tag_list')]
        if m.get('lv2_tag_list') is not None:
            self.lv2_tag_list = [TopicTagItem().from_dict(i) for i in m.get('lv2_tag_list')]
        return self
