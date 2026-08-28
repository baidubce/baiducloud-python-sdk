"""
LisenceWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.vertex_location import VertexLocation


class LisenceWordsResult(AbstractModel):
    """
    LisenceWordsResult
    """

    def __init__(
        self, color=None, number=None, probability=None, vertexes_location=None, cover_info=None, edit_tool=None
    ):
        """
        Initialize LisenceWordsResult instance.

        :param color: 车牌颜色
        :type color: str (optional)

        :param number: 车牌号码
        :type number: str (optional)

        :param probability: 7个数字分别为车牌中每个字符的置信度（从左往右），区间为0-1
        :type probability: List[float] (optional)

        :param vertexes_location: 返回文字外接多边形顶点位置
        :type vertexes_location: List[VertexLocation] (optional)

        :param cover_info: 判断车牌有没有被遮挡，当detect_complete=true时生效
        :type cover_info: str (optional)

        :param edit_tool: 判断车牌有没有被遮挡，当detect_risk=true时生效；如果检测车牌被编辑过，该字段指定编辑软件名称
        :type edit_tool: str (optional)
        """
        super().__init__()
        self.color = color
        self.number = number
        self.probability = probability
        self.vertexes_location = vertexes_location
        self.cover_info = cover_info
        self.edit_tool = edit_tool

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
        if self.color is not None:
            result['color'] = self.color
        if self.number is not None:
            result['number'] = self.number
        if self.probability is not None:
            result['probability'] = self.probability
        if self.vertexes_location is not None:
            result['vertexes_location'] = [i.to_dict() for i in self.vertexes_location]
        if self.cover_info is not None:
            result['cover_info'] = self.cover_info
        if self.edit_tool is not None:
            result['edit_tool'] = self.edit_tool
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LisenceWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('color') is not None:
            self.color = m.get('color')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('vertexes_location') is not None:
            self.vertexes_location = [VertexLocation().from_dict(i) for i in m.get('vertexes_location')]
        if m.get('cover_info') is not None:
            self.cover_info = m.get('cover_info')
        if m.get('edit_tool') is not None:
            self.edit_tool = m.get('edit_tool')
        return self
