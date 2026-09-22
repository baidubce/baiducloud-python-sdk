"""
Request entity for ModifyDeploymentSetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyDeploymentSetRequest(AbstractModel):
    """
    Request entity for ModifyDeploymentSetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, deploy_set_id, name, concurrency, desc=None):
        """
        Initialize ModifyDeploymentSetRequest request entity.

        :param deploy_set_id: deploy_set_id parameter
        :type deploy_set_id: str (required)

        :param desc: 备注。
        :type desc: str (optional)

        :param name: 部署集名称。
        :type name: str (required)

        :param concurrency: 并发度。取值范围：1-127。默认值：20。
        :type concurrency: int (required)
        """
        super().__init__()
        self.deploy_set_id = deploy_set_id
        self.desc = desc
        self.name = name
        self.concurrency = concurrency

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
        if self.desc is not None:
            result['desc'] = self.desc
        if self.name is not None:
            result['name'] = self.name
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyDeploymentSetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('deploySetId') is not None:
            self.deploy_set_id = m.get('deploySetId')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        return self
