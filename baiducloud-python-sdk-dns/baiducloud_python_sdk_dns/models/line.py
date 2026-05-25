"""
Line information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Line(AbstractModel):
    """
    Line
    """

    def __init__(self, id=None, name=None, lines=None, related_zone_count=None, related_record_count=None):
        """
        Initialize Line instance.

        :param id: 线路组id。
        :type id: str (optional)

        :param name: 线路组名称。
        :type name: str (optional)

        :param lines: 线路名称，取值见[LineName](#LineName)。
        :type lines: List[str] (optional)

        :param related_zone_count: 关联的zone数量。
        :type related_zone_count: int (optional)

        :param related_record_count: 关联的解析记录数量。
        :type related_record_count: int (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.lines = lines
        self.related_zone_count = related_zone_count
        self.related_record_count = related_record_count

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.lines is not None:
            result['lines'] = self.lines
        if self.related_zone_count is not None:
            result['relatedZoneCount'] = self.related_zone_count
        if self.related_record_count is not None:
            result['relatedRecordCount'] = self.related_record_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Line

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('lines') is not None:
            self.lines = m.get('lines')
        if m.get('relatedZoneCount') is not None:
            self.related_zone_count = m.get('relatedZoneCount')
        if m.get('relatedRecordCount') is not None:
            self.related_record_count = m.get('relatedRecordCount')
        return self
