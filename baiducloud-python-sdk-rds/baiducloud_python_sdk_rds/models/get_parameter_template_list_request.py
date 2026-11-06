"""
Request entity for GetParameterTemplateListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetParameterTemplateListRequest(AbstractModel):
    """
    Request entity for GetParameterTemplateListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_no, page_size, db_type=None, db_version=None):
        """
        Initialize GetParameterTemplateListRequest request entity.

        :param page_no: page_no parameter
        :type page_no: int (required)

        :param page_size: page_size parameter
        :type page_size: int (required)

        :param db_type: db_type parameter
        :type db_type: str (optional)

        :param db_version: db_version parameter
        :type db_version: str (optional)
        """
        super().__init__()
        self.page_no = page_no
        self.page_size = page_size
        self.db_type = db_type
        self.db_version = db_version

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
        :rtype: GetParameterTemplateListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('dbType') is not None:
            self.db_type = m.get('dbType')
        if m.get('dbVersion') is not None:
            self.db_version = m.get('dbVersion')
        return self
