"""
Request entity for DeleteAlarmTemplatesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteAlarmTemplatesRequest(AbstractModel):
    """
    Request entity for DeleteAlarmTemplatesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ids):
        """
        Initialize DeleteAlarmTemplatesRequest request entity.

        :param ids: 要删除的报警模板ID列表
        :type ids: List[str] (required)
        """
        super().__init__()
        self.ids = ids

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAlarmTemplatesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        return self
