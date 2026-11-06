"""
Request entity for ModifyDescriptionInformationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyDescriptionInformationRequest(AbstractModel):
    """
    Request entity for ModifyDescriptionInformationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, db_name, remark):
        """
        Initialize ModifyDescriptionInformationRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param db_name: db_name parameter
        :type db_name: str (required)

        :param remark: 描述信息
        :type remark: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.db_name = db_name
        self.remark = remark

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
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyDescriptionInformationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self
