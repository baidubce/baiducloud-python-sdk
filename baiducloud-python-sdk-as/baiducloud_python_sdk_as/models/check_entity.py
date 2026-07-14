"""
CheckEntity information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.check_detail import CheckDetail


class CheckEntity(AbstractModel):
    """
    CheckEntity
    """

    def __init__(self, label=None, status=None, result=None):
        """
        Initialize CheckEntity instance.

        :param label: 标签
        :type label: str (optional)

        :param status: 检查状态
        :type status: object (optional)

        :param result: result attribute
        :type result: CheckDetail (optional)
        """
        super().__init__()
        self.label = label
        self.status = status
        self.result = result

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
        if self.label is not None:
            result['label'] = self.label
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckEntity

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = CheckDetail().from_dict(m.get('result'))
        return self
