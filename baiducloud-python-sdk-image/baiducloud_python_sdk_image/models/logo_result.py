"""
LogoResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_image.models.logo_location import LogoLocation


class LogoResult(AbstractModel):
    """
    LogoResult
    """

    def __init__(self, location=None, name=None, probability=None, type=None):
        """
        Initialize LogoResult instance.

        :param location: location attribute
        :type location: LogoLocation (optional)

        :param name: 识别的品牌名称
        :type name: str (optional)

        :param probability: 分类结果置信度（0--1.0）
        :type probability: float (optional)

        :param type: type=0为1千种高优商标识别结果;type=1为2万类logo库的结果；其它type为自定义logo库结果
        :type type: int (optional)
        """
        super().__init__()
        self.location = location
        self.name = name
        self.probability = probability
        self.type = type

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
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.name is not None:
            result['name'] = self.name
        if self.probability is not None:
            result['probability'] = self.probability
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogoResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = LogoLocation().from_dict(m.get('location'))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
