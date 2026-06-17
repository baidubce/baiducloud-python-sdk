"""
Request entity for GetZoneBySpecRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetZoneBySpecRequest(AbstractModel):
    """
    Request entity for GetZoneBySpecRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_type=None, product_type=None, spec=None, spec_id=None):
        """
        Initialize GetZoneBySpecRequest request entity.

        :param instance_type: instance_type parameter
        :type instance_type: str (optional)

        :param product_type: product_type parameter
        :type product_type: str (optional)

        :param spec: spec parameter
        :type spec: str (optional)

        :param spec_id: spec_id parameter
        :type spec_id: str (optional)
        """
        super().__init__()
        self.instance_type = instance_type
        self.product_type = product_type
        self.spec = spec
        self.spec_id = spec_id

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
        :rtype: GetZoneBySpecRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('specId') is not None:
            self.spec_id = m.get('specId')
        return self
