"""
Request entity for DescribeDatasetsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeDatasetsRequest(AbstractModel):
    """
    Request entity for DescribeDatasetsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        keyword=None,
        storage_type=None,
        storage_instances=None,
        import_format=None,
        page_number=None,
        page_size=None,
    ):
        """
        Initialize DescribeDatasetsRequest request entity.

        :param keyword: keyword parameter
        :type keyword: str (optional)

        :param storage_type: storage_type parameter
        :type storage_type: str (optional)

        :param storage_instances: storage_instances parameter
        :type storage_instances: str (optional)

        :param import_format: import_format parameter
        :type import_format: str (optional)

        :param page_number: page_number parameter
        :type page_number: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.keyword = keyword
        self.storage_type = storage_type
        self.storage_instances = storage_instances
        self.import_format = import_format
        self.page_number = page_number
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
        :rtype: DescribeDatasetsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('storageInstances') is not None:
            self.storage_instances = m.get('storageInstances')
        if m.get('importFormat') is not None:
            self.import_format = m.get('importFormat')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
