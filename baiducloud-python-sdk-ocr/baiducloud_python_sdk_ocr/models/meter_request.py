"""
Request entity for MeterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MeterRequest(AbstractModel):
    """
    Request entity for MeterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, probability=None, poly_location=None):
        """
        Initialize MeterRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param probability: 是否返回每行识别结果的置信度，默认为false
        :type probability: bool (optional)

        :param poly_location: poly_location parameter
        :type poly_location: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.probability = probability
        self.poly_location = poly_location

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
        if self.probability is not None:
            result['probability'] = self.probability
        if self.poly_location is not None:
            result['poly_location'] = self.poly_location
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MeterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('poly_location') is not None:
            self.poly_location = m.get('poly_location')
        return self
