"""
Request entity for GetSystemParameterListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetSystemParameterListRequest(AbstractModel):
    """
    Request entity for GetSystemParameterListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, engine=None, engine_version=None, cluster_type=None):
        """
        Initialize GetSystemParameterListRequest request entity.

        :param engine: engine parameter
        :type engine: str (optional)

        :param engine_version: engine_version parameter
        :type engine_version: str (optional)

        :param cluster_type: cluster_type parameter
        :type cluster_type: str (optional)
        """
        super().__init__()
        self.engine = engine
        self.engine_version = engine_version
        self.cluster_type = cluster_type

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
        :rtype: GetSystemParameterListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        return self
