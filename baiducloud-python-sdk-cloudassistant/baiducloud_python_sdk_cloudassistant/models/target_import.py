"""
TargetImport information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TargetImport(AbstractModel):
    """
    TargetImport
    """

    def __init__(self, keyword_type=None, instances=None):
        """
        Initialize TargetImport instance.

        :param keyword_type: 实例列表导入类型。枚举值：instanceId（通过实例ID导入），internalIp表示（通过实例内网导入）
        :type keyword_type: str (optional)

        :param instances: 实例清单列表
        :type instances: List[str] (optional)
        """
        super().__init__()
        self.keyword_type = keyword_type
        self.instances = instances

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
        if self.keyword_type is not None:
            result['keywordType'] = self.keyword_type
        if self.instances is not None:
            result['instances'] = self.instances
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TargetImport

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keywordType') is not None:
            self.keyword_type = m.get('keywordType')
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        return self
