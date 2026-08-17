"""
Request entity for MedicalInvoiceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MedicalInvoiceRequest(AbstractModel):
    """
    Request entity for MedicalInvoiceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, location=None, probability=None, medi_query=None):
        """
        Initialize MedicalInvoiceRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param location: location parameter
        :type location: bool (optional)

        :param probability: probability parameter
        :type probability: bool (optional)

        :param medi_query: medi_query parameter
        :type medi_query: str (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.location = location
        self.probability = probability
        self.medi_query = medi_query

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
        if self.location is not None:
            result['location'] = self.location
        if self.probability is not None:
            result['probability'] = self.probability
        if self.medi_query is not None:
            result['medi_query'] = self.medi_query
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalInvoiceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('medi_query') is not None:
            self.medi_query = m.get('medi_query')
        return self
