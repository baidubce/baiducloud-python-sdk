"""
Request entity for ModifyEhcClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyEhcClusterRequest(AbstractModel):
    """
    Request entity for ModifyEhcClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ehc_cluster_id, name=None, description=None):
        """
        Initialize ModifyEhcClusterRequest request entity.

        :param ehc_cluster_id: 需要修改的EHC集群ID
        :type ehc_cluster_id: str (required)

        :param name: EHC集群名，不能与description同为空
        :type name: str (optional)

        :param description: EHC集群描述，不能与name同为空
        :type description: str (optional)
        """
        super().__init__()
        self.ehc_cluster_id = ehc_cluster_id
        self.name = name
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
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        if self.name is not None:
            result['name'] = self.name
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
        :rtype: ModifyEhcClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
