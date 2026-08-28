"""
Request entity for WaybillRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class WaybillRequest(AbstractModel):
    """
    Request entity for WaybillRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, is_identify_virtual_waybill=None):
        """
        Initialize WaybillRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param is_identify_virtual_waybill: is_identify_virtual_waybill parameter
        :type is_identify_virtual_waybill: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.is_identify_virtual_waybill = is_identify_virtual_waybill

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
        if self.image is not None:
            result['image'] = self.image
        if self.url is not None:
            result['url'] = self.url
        if self.is_identify_virtual_waybill is not None:
            result['is_identify_virtual_waybill'] = self.is_identify_virtual_waybill
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: WaybillRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('is_identify_virtual_waybill') is not None:
            self.is_identify_virtual_waybill = m.get('is_identify_virtual_waybill')
        return self
