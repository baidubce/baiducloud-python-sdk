"""
AccurateParagraphsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.accurate_vertexes_location import AccurateVertexesLocation

from baiducloud_python_sdk_ocr.models.accurate_vertexes_location import AccurateVertexesLocation


class AccurateParagraphsResult(AbstractModel):
    """
    AccurateParagraphsResult
    """

    def __init__(
        self, words_result_idx=None, finegrained_vertexes_location=None, min_finegrained_vertexes_location=None
    ):
        """
        Initialize AccurateParagraphsResult instance.

        :param words_result_idx: 一个段落包含的行序号，当 paragraph=true 时返回该字段
        :type words_result_idx: List[int] (optional)

        :param finegrained_vertexes_location: finegrained_vertexes_location attribute
        :type finegrained_vertexes_location: List[AccurateVertexesLocation] (optional)

        :param min_finegrained_vertexes_location: min_finegrained_vertexes_location attribute
        :type min_finegrained_vertexes_location: List[AccurateVertexesLocation] (optional)
        """
        super().__init__()
        self.words_result_idx = words_result_idx
        self.finegrained_vertexes_location = finegrained_vertexes_location
        self.min_finegrained_vertexes_location = min_finegrained_vertexes_location

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
        if self.words_result_idx is not None:
            result['words_result_idx'] = self.words_result_idx
        if self.finegrained_vertexes_location is not None:
            result['finegrained_vertexes_location'] = [i.to_dict() for i in self.finegrained_vertexes_location]
        if self.min_finegrained_vertexes_location is not None:
            result['min_finegrained_vertexes_location'] = [i.to_dict() for i in self.min_finegrained_vertexes_location]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccurateParagraphsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words_result_idx') is not None:
            self.words_result_idx = m.get('words_result_idx')
        if m.get('finegrained_vertexes_location') is not None:
            self.finegrained_vertexes_location = [
                AccurateVertexesLocation().from_dict(i) for i in m.get('finegrained_vertexes_location')
            ]
        if m.get('min_finegrained_vertexes_location') is not None:
            self.min_finegrained_vertexes_location = [
                AccurateVertexesLocation().from_dict(i) for i in m.get('min_finegrained_vertexes_location')
            ]
        return self
