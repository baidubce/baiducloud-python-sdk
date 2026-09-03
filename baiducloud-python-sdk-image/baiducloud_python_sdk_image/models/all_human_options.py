"""
AllHumanOptions information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AllHumanOptions(AbstractModel):
    """
    AllHumanOptions
    """

    def __init__(
        self,
        body_heighten=None,
        remove_bg_flaw=None,
        leg_long=None,
        all_skin_color_same=None,
        remove_pure_bg_flaw=None,
    ):
        """
        Initialize AllHumanOptions instance.

        :param body_heighten: 增高
        :type body_heighten: float (optional)

        :param remove_bg_flaw: 非纯色背景去瑕疵
        :type remove_bg_flaw: float (optional)

        :param leg_long: 长腿
        :type leg_long: float (optional)

        :param all_skin_color_same: 多人肤色统一
        :type all_skin_color_same: float (optional)

        :param remove_pure_bg_flaw: 纯色背景去瑕疵
        :type remove_pure_bg_flaw: float (optional)
        """
        super().__init__()
        self.body_heighten = body_heighten
        self.remove_bg_flaw = remove_bg_flaw
        self.leg_long = leg_long
        self.all_skin_color_same = all_skin_color_same
        self.remove_pure_bg_flaw = remove_pure_bg_flaw

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
        if self.body_heighten is not None:
            result['body_heighten'] = self.body_heighten
        if self.remove_bg_flaw is not None:
            result['remove_bg_flaw'] = self.remove_bg_flaw
        if self.leg_long is not None:
            result['leg_long'] = self.leg_long
        if self.all_skin_color_same is not None:
            result['all_skin_color_same'] = self.all_skin_color_same
        if self.remove_pure_bg_flaw is not None:
            result['remove_pure_bg_flaw'] = self.remove_pure_bg_flaw
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AllHumanOptions

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('body_heighten') is not None:
            self.body_heighten = m.get('body_heighten')
        if m.get('remove_bg_flaw') is not None:
            self.remove_bg_flaw = m.get('remove_bg_flaw')
        if m.get('leg_long') is not None:
            self.leg_long = m.get('leg_long')
        if m.get('all_skin_color_same') is not None:
            self.all_skin_color_same = m.get('all_skin_color_same')
        if m.get('remove_pure_bg_flaw') is not None:
            self.remove_pure_bg_flaw = m.get('remove_pure_bg_flaw')
        return self
