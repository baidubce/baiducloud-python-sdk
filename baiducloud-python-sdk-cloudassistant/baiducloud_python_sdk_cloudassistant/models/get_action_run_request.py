"""
Request entity for GetActionRunRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetActionRunRequest(AbstractModel):
    """
    Request entity for GetActionRunRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, with_log=None, page_no=None, page_size=None, child_run_state=None, locale=None):
        """
        Initialize GetActionRunRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param with_log: with_log parameter
        :type with_log: str (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)

        :param child_run_state: child_run_state parameter
        :type child_run_state: str (optional)

        :param locale: locale parameter
        :type locale: str (optional)
        """
        super().__init__()
        self.id = id
        self.with_log = with_log
        self.page_no = page_no
        self.page_size = page_size
        self.child_run_state = child_run_state
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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetActionRunRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('withLog') is not None:
            self.with_log = m.get('withLog')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('childRunState') is not None:
            self.child_run_state = m.get('childRunState')
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        return self
