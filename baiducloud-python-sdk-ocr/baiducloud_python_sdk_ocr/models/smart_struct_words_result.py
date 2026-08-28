"""
SmartStructWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.smart_struct_struct_info import SmartStructStructInfo

from baiducloud_python_sdk_ocr.models.smart_struct_relations import SmartStructRelations

from baiducloud_python_sdk_ocr.models.smart_struct_line_info import SmartStructLineInfo


class SmartStructWordsResult(AbstractModel):
    """
    SmartStructWordsResult
    """

    def __init__(self, struct_info=None, relations=None, line_info=None):
        """
        Initialize SmartStructWordsResult instance.

        :param struct_info: struct_info attribute
        :type struct_info: SmartStructStructInfo (optional)

        :param relations: relations attribute
        :type relations: SmartStructRelations (optional)

        :param line_info: 文字行的识别结果、类别、置信度、位置信息等，当 return_relation=true 时返回
        :type line_info: List[SmartStructLineInfo] (optional)
        """
        super().__init__()
        self.struct_info = struct_info
        self.relations = relations
        self.line_info = line_info

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
        if self.struct_info is not None:
            result['struct_info'] = self.struct_info.to_dict()
        if self.relations is not None:
            result['relations'] = self.relations.to_dict()
        if self.line_info is not None:
            result['line_info'] = [i.to_dict() for i in self.line_info]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SmartStructWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('struct_info') is not None:
            self.struct_info = SmartStructStructInfo().from_dict(m.get('struct_info'))
        if m.get('relations') is not None:
            self.relations = SmartStructRelations().from_dict(m.get('relations'))
        if m.get('line_info') is not None:
            self.line_info = [SmartStructLineInfo().from_dict(i) for i in m.get('line_info')]
        return self
