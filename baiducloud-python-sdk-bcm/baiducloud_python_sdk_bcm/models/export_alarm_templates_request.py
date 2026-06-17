"""
Request entity for ExportAlarmTemplatesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ExportAlarmTemplatesRequest(AbstractModel):
    """
    Request entity for ExportAlarmTemplatesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, names):
        """
        Initialize ExportAlarmTemplatesRequest request entity.

        :param names: 报警模板名称列表
        :type names: List[str] (required)
        """
        super().__init__()
        self.names = names

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
        if self.names is not None:
            result['names'] = self.names
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ExportAlarmTemplatesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('names') is not None:
            self.names = m.get('names')
        return self
