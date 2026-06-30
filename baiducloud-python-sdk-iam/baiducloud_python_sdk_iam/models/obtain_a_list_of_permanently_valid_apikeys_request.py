"""
Request entity for ObtainAListOfPermanentlyValidApikeysRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ObtainAListOfPermanentlyValidApikeysRequest(AbstractModel):
    """
    Request entity for ObtainAListOfPermanentlyValidApikeysRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_id=None, service=None, page_no=None, page_size=None):
        """
        Initialize ObtainAListOfPermanentlyValidApikeysRequest request entity.

        :param user_id: 子用户Id；如果apikey归属其他子用户则必填
        :type user_id: str (optional)

        :param service: service parameter
        :type service: List[str] (optional)

        :param page_no: 页码，从1开始；默认 1
        :type page_no: int (optional)

        :param page_size: 每页大小；默认10
        :type page_size: int (optional)
        """
        super().__init__()
        self.user_id = user_id
        self.service = service
        self.page_no = page_no
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
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.service is not None:
            result['service'] = self.service
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ObtainAListOfPermanentlyValidApikeysRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
