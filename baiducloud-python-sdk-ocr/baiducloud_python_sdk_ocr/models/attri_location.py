"""
AttriLocation information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_analysis_office_point import DocAnalysisOfficePoint


class AttriLocation(AbstractModel):
    """
    AttriLocation
    """

    def __init__(self, points=None):
        """
        Initialize AttriLocation instance.

        :param points: 四角点坐标数组，依次为左上、右上、右下、左下
        :type points: List[DocAnalysisOfficePoint] (optional)
        """
        super().__init__()
        self.points = points

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
        if self.points is not None:
            result['points'] = [i.to_dict() for i in self.points]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AttriLocation

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('points') is not None:
            self.points = [DocAnalysisOfficePoint().from_dict(i) for i in m.get('points')]
        return self
