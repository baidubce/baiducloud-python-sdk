"""
CheckDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CheckDetail(AbstractModel):
    """
    CheckDetail
    """

    def __init__(self, resource_id=None, detail=None, advice=None):
        """
        Initialize CheckDetail instance.

        :param resource_id: 资源id
        :type resource_id: str (optional)

        :param detail: 详细信息
        :type detail: str (optional)

        :param advice: 系统建议
        :type advice: str (optional)
        """
        super().__init__()
        self.resource_id = resource_id
        self.detail = detail
        self.advice = advice

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
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.detail is not None:
            result['detail'] = self.detail
        if self.advice is not None:
            result['advice'] = self.advice
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('advice') is not None:
            self.advice = m.get('advice')
        return self
