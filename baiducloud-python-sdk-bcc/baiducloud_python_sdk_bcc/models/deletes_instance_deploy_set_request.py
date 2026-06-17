"""
Request entity for DeletesInstanceDeploySetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeletesInstanceDeploySetRequest(AbstractModel):
    """
    Request entity for DeletesInstanceDeploySetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, deploy_id, instance_id_list):
        """
        Initialize DeletesInstanceDeploySetRequest request entity.

        :param deploy_id: 部署集ID
        :type deploy_id: str (required)

        :param instance_id_list: 实例ID列表
        :type instance_id_list: List[str] (required)
        """
        super().__init__()
        self.deploy_id = deploy_id
        self.instance_id_list = instance_id_list

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
        if self.deploy_id is not None:
            result['deployId'] = self.deploy_id
        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeletesInstanceDeploySetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('deployId') is not None:
            self.deploy_id = m.get('deployId')
        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')
        return self
