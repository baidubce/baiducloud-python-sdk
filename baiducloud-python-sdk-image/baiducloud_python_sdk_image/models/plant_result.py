"""
PlantResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_image.models.baike_info import BaikeInfo


class PlantResult(AbstractModel):
    """
    PlantResult
    """

    def __init__(self, name=None, score=None, baike_info=None):
        """
        Initialize PlantResult instance.

        :param name: 植物名称
        :type name: str (optional)

        :param score: 置信度
        :type score: float (optional)

        :param baike_info: baike_info attribute
        :type baike_info: BaikeInfo (optional)
        """
        super().__init__()
        self.name = name
        self.score = score
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
        if self.score is not None:
            result['score'] = self.score
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
        :rtype: PlantResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('baike_info') is not None:
            self.baike_info = BaikeInfo().from_dict(m.get('baike_info'))
        return self
