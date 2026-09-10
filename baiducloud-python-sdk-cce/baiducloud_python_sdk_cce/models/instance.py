"""
Instance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Instance(AbstractModel):
    """
    Instance
    """

    def __init__(self, spec=None, status=None, created_at=None, updated_at=None):
        """
        Initialize Instance instance.

        :param spec:
        :type spec: object (optional)

        :param status:
        :type status: object (optional)

        :param created_at:
        :type created_at: str (optional)

        :param updated_at:
        :type updated_at: str (optional)
        """
        super().__init__()
        self.spec = spec
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Instance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self
