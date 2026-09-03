"""
AdvancedGeneralResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_image.models.baike_info import BaikeInfo


class AdvancedGeneralResult(AbstractModel):
    """
    AdvancedGeneralResult
    """

    def __init__(self, keyword=None, score=None, root=None, baike_info=None):
        """
        Initialize AdvancedGeneralResult instance.

        :param keyword: 图片中的物体或场景名称
        :type keyword: str (optional)

        :param score: 置信度，0-1
        :type score: float (optional)

        :param root: 识别结果的上层类目
        :type root: str (optional)

        :param baike_info: baike_info attribute
        :type baike_info: BaikeInfo (optional)
        """
        super().__init__()
        self.keyword = keyword
        self.score = score
        self.root = root
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
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.score is not None:
            result['score'] = self.score
        if self.root is not None:
            result['root'] = self.root
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
        :rtype: AdvancedGeneralResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('root') is not None:
            self.root = m.get('root')
        if m.get('baike_info') is not None:
            self.baike_info = BaikeInfo().from_dict(m.get('baike_info'))
        return self
