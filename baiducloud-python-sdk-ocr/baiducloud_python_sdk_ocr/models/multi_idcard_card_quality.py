"""
MultiIdcardCardQuality information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MultiIdcardCardQuality(AbstractModel):
    """
    MultiIdcardCardQuality
    """

    def __init__(
        self,
        is_clear=None,
        is_complete=None,
        is_no_cover=None,
        is_clear_propobility=None,
        is_complete_propobility=None,
        is_no_cover_propobility=None,
    ):
        """
        Initialize MultiIdcardCardQuality instance.

        :param is_clear: 是否清晰
        :type is_clear: int (optional)

        :param is_complete: 是否边框/四角完整
        :type is_complete: int (optional)

        :param is_no_cover: 是否头像、关键字段无遮挡/马赛克
        :type is_no_cover: int (optional)

        :param is_clear_propobility: 是否清晰的概率，值在0-1之间，值越大表示图像质量越好
        :type is_clear_propobility: float (optional)

        :param is_complete_propobility: 是否边框/四角完整的概率，值在0-1之间，值越大表示图像质量越好
        :type is_complete_propobility: float (optional)

        :param is_no_cover_propobility: 是否头像、关键字段无遮挡/马赛克的概率，值在0-1之间，值越大表示图像质量越好
        :type is_no_cover_propobility: float (optional)
        """
        super().__init__()
        self.is_clear = is_clear
        self.is_complete = is_complete
        self.is_no_cover = is_no_cover
        self.is_clear_propobility = is_clear_propobility
        self.is_complete_propobility = is_complete_propobility
        self.is_no_cover_propobility = is_no_cover_propobility

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
        if self.is_clear is not None:
            result['IsClear'] = self.is_clear
        if self.is_complete is not None:
            result['IsComplete'] = self.is_complete
        if self.is_no_cover is not None:
            result['IsNoCover'] = self.is_no_cover
        if self.is_clear_propobility is not None:
            result['IsClear_propobility'] = self.is_clear_propobility
        if self.is_complete_propobility is not None:
            result['IsComplete_propobility'] = self.is_complete_propobility
        if self.is_no_cover_propobility is not None:
            result['IsNoCover_propobility'] = self.is_no_cover_propobility
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MultiIdcardCardQuality

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('IsClear') is not None:
            self.is_clear = m.get('IsClear')
        if m.get('IsComplete') is not None:
            self.is_complete = m.get('IsComplete')
        if m.get('IsNoCover') is not None:
            self.is_no_cover = m.get('IsNoCover')
        if m.get('IsClear_propobility') is not None:
            self.is_clear_propobility = m.get('IsClear_propobility')
        if m.get('IsComplete_propobility') is not None:
            self.is_complete_propobility = m.get('IsComplete_propobility')
        if m.get('IsNoCover_propobility') is not None:
            self.is_no_cover_propobility = m.get('IsNoCover_propobility')
        return self
