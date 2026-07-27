"""
Request entity for GetExecutionDetailV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetExecutionDetailV2Request(AbstractModel):
    """
    Request entity for GetExecutionDetailV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, with_log=None, locale=None):
        """
        Initialize GetExecutionDetailV2Request request entity.

        :param id: id parameter
        :type id: str (required)

        :param with_log: with_log parameter
        :type with_log: str (optional)

        :param locale: locale parameter
        :type locale: str (optional)
        """
        super().__init__()
        self.id = id
        self.with_log = with_log
        self.locale = locale

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
        if self.id is not None:
            result['id'] = self.id
        if self.with_log is not None:
            result['withLog'] = self.with_log
        if self.locale is not None:
            result['locale'] = self.locale
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetExecutionDetailV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('withLog') is not None:
            self.with_log = m.get('withLog')
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        return self
