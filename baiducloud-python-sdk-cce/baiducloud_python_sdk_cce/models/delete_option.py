"""
DeleteOption information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteOption(AbstractModel):
    """
    DeleteOption
    """

    def __init__(self, delete_resource=None, delete_cds_snapshot=None, move_out=None):
        """
        Initialize DeleteOption instance.

        :param delete_resource:
        :type delete_resource: bool (optional)

        :param delete_cds_snapshot:
        :type delete_cds_snapshot: bool (optional)

        :param move_out:
        :type move_out: bool (optional)
        """
        super().__init__()
        self.delete_resource = delete_resource
        self.delete_cds_snapshot = delete_cds_snapshot
        self.move_out = move_out

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
        if self.delete_resource is not None:
            result['deleteResource'] = self.delete_resource
        if self.delete_cds_snapshot is not None:
            result['deleteCDSSnapshot'] = self.delete_cds_snapshot
        if self.move_out is not None:
            result['moveOut'] = self.move_out
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteOption

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('deleteResource') is not None:
            self.delete_resource = m.get('deleteResource')
        if m.get('deleteCDSSnapshot') is not None:
            self.delete_cds_snapshot = m.get('deleteCDSSnapshot')
        if m.get('moveOut') is not None:
            self.move_out = m.get('moveOut')
        return self
