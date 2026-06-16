"""
Request entity for UpdateDeploySetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateDeploySetRequest(AbstractModel):
    """
    Request entity for UpdateDeploySetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, deploy_id, name=None, desc=None):
        """
        Initialize UpdateDeploySetRequest request entity.

        :param deploy_id: deploy_id parameter
        :type deploy_id: str (required)

        :param name: 部署集名字（name与desc至少传一个）
        :type name: str (optional)

        :param desc: desc parameter
        :type desc: str (optional)
        """
        super().__init__()
        self.deploy_id = deploy_id
        self.name = name
        self.desc = desc

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
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateDeploySetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('deployId') is not None:
            self.deploy_id = m.get('deployId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self
