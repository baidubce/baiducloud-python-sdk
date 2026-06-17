"""
Request entity for UpdateDeploySetRelationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateDeploySetRelationRequest(AbstractModel):
    """
    Request entity for UpdateDeploySetRelationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, deployset_id_list=None):
        """
        Initialize UpdateDeploySetRelationRequest request entity.

        :param instance_id: 实例id
        :type instance_id: str (required)

        :param deployset_id_list: 要加入的部署集id列表
        :type deployset_id_list: List[str] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.deployset_id_list = deployset_id_list

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.deployset_id_list is not None:
            result['deploysetIdList'] = self.deployset_id_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateDeploySetRelationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('deploysetIdList') is not None:
            self.deployset_id_list = m.get('deploysetIdList')
        return self
