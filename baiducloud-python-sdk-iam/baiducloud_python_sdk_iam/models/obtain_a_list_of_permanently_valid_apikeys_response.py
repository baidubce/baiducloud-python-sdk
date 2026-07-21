"""
Request entity for ObtainAListOfPermanentlyValidApikeysResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_iam.models.page import Page


class ObtainAListOfPermanentlyValidApikeysResponse(BceResponse):
    """
    ObtainAListOfPermanentlyValidApikeysResponse
    """

    def __init__(self, success=None, status=None, page=None):
        """
        Initialize ObtainAListOfPermanentlyValidApikeysResponse response.

        :param success: 成功标识
        :type success: bool (optional)

        :param status: 状态码
        :type status: int (optional)

        :param page: page field
        :type page: Page (optional)
        """
        super().__init__()
        self.success = success
        self.status = status
        self.page = page

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.success is not None:
            result['success'] = self.success
        if self.status is not None:
            result['status'] = self.status
        if self.page is not None:
            result['page'] = self.page.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ObtainAListOfPermanentlyValidApikeysResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('page') is not None:
            self.page = Page().from_dict(m.get('page'))
        return self
