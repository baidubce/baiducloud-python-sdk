"""
DishResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_image.models.baike_info import BaikeInfo


class DishResult(AbstractModel):
    """
    DishResult
    """

    def __init__(self, name=None, calorie=None, probability=None, has_calorie=None, baike_info=None):
        """
        Initialize DishResult instance.

        :param name: 菜品名称
        :type name: str (optional)

        :param calorie: 卡路里，每100g的卡路里含量
        :type calorie: str (optional)

        :param probability: 识别概率
        :type probability: str (optional)

        :param has_calorie: 是否有卡路里信息
        :type has_calorie: bool (optional)

        :param baike_info: baike_info attribute
        :type baike_info: BaikeInfo (optional)
        """
        super().__init__()
        self.name = name
        self.calorie = calorie
        self.probability = probability
        self.has_calorie = has_calorie
        self.baike_info = baike_info

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
        if self.name is not None:
            result['name'] = self.name
        if self.calorie is not None:
            result['calorie'] = self.calorie
        if self.probability is not None:
            result['probability'] = self.probability
        if self.has_calorie is not None:
            result['has_calorie'] = self.has_calorie
        if self.baike_info is not None:
            result['baike_info'] = self.baike_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DishResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('calorie') is not None:
            self.calorie = m.get('calorie')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('has_calorie') is not None:
            self.has_calorie = m.get('has_calorie')
        if m.get('baike_info') is not None:
            self.baike_info = BaikeInfo().from_dict(m.get('baike_info'))
        return self
