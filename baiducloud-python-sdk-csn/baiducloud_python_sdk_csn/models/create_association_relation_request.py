"""
Request entity for CreateAssociationRelationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateAssociationRelationRequest(AbstractModel):
    """
    Request entity for CreateAssociationRelationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, csn_rt_id, attach_id, client_token=None, description=None):
        """
        Initialize CreateAssociationRelationRequest request entity.

        :param csn_rt_id: csn_rt_id parameter
        :type csn_rt_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param attach_id: 网络实例在云智能网中的身份ID
        :type attach_id: str (required)

        :param description: 描述
        :type description: str (optional)
        """
        super().__init__()
        self.csn_rt_id = csn_rt_id
        self.client_token = client_token
        self.attach_id = attach_id
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
        if self.attach_id is not None:
            result['attachId'] = self.attach_id
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
        :rtype: CreateAssociationRelationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnRtId') is not None:
            self.csn_rt_id = m.get('csnRtId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('attachId') is not None:
            self.attach_id = m.get('attachId')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
