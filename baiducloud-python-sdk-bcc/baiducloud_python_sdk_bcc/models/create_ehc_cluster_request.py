"""
Request entity for CreateEhcClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateEhcClusterRequest(AbstractModel):
    """
    Request entity for CreateEhcClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, zone_name, description):
        """
        Initialize CreateEhcClusterRequest request entity.

        :param name: EHC集群名
        :type name: str (required)

        :param zone_name: 指定zone信息，命名规范是国家-region-可用区序列，例如cn-bj-a
        :type zone_name: str (required)

        :param description: EHC集群描述
        :type description: str (required)
        """
        super().__init__()
        self.name = name
        self.zone_name = zone_name
        self.description = description

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
        if self.name is not None:
            result['name'] = self.name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateEhcClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
