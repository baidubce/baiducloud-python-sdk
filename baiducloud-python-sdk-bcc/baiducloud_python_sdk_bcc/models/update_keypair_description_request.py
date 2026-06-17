"""
Request entity for UpdateKeypairDescriptionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateKeypairDescriptionRequest(AbstractModel):
    """
    Request entity for UpdateKeypairDescriptionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, keypair_id, description=None):
        """
        Initialize UpdateKeypairDescriptionRequest request entity.

        :param keypair_id: keypair_id parameter
        :type keypair_id: str (required)

        :param description: description parameter
        :type description: str (optional)
        """
        super().__init__()
        self.keypair_id = keypair_id
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
        :rtype: UpdateKeypairDescriptionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keypairId') is not None:
            self.keypair_id = m.get('keypairId')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
