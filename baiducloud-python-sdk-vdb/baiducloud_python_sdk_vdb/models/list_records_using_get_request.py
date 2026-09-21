"""
Request entity for ListRecordsUsingGetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListRecordsUsingGetRequest(AbstractModel):
    """
    Request entity for ListRecordsUsingGetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, engine_type=None, list_order=None, page=None, page_size=None):
        """
        Initialize ListRecordsUsingGetRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)

        :param list_order: list_order parameter
        :type list_order: str (optional)

        :param page: page parameter
        :type page: str (optional)

        :param page_size: page_size parameter
        :type page_size: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.engine_type = engine_type
        self.list_order = list_order
        self.page = page
        self.page_size = page_size

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
        :rtype: ListRecordsUsingGetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('listOrder') is not None:
            self.list_order = m.get('listOrder')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
