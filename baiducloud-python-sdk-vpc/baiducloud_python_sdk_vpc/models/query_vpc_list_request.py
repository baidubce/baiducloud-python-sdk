"""
Request entity for QueryVpcListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryVpcListRequest(AbstractModel):
    """
    Request entity for QueryVpcListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, marker=None, max_keys=None, is_default=None, vpc_ids=None):
        """
        Initialize QueryVpcListRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param is_default: is_default parameter
        :type is_default: bool (optional)

        :param vpc_ids: vpc_ids parameter
        :type vpc_ids: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.is_default = is_default
        self.vpc_ids = vpc_ids

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
        :rtype: QueryVpcListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('vpcIds') is not None:
            self.vpc_ids = m.get('vpcIds')
        return self
