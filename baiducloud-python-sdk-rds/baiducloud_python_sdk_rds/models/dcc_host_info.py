"""
DccHostInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.dcc_host_id import DccHostId

from baiducloud_python_sdk_rds.models.dcc_host_id import DccHostId


class DccHostInfo(AbstractModel):
    """
    DccHostInfo
    """

    def __init__(self, master=None, backup=None):
        """
        Initialize DccHostInfo instance.

        :param master: master attribute
        :type master: DccHostId (optional)

        :param backup: backup attribute
        :type backup: DccHostId (optional)
        """
        super().__init__()
        self.master = master
        self.backup = backup

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
        if self.master is not None:
            result['master'] = self.master.to_dict()
        if self.backup is not None:
            result['backup'] = self.backup.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DccHostInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('master') is not None:
            self.master = DccHostId().from_dict(m.get('master'))
        if m.get('backup') is not None:
            self.backup = DccHostId().from_dict(m.get('backup'))
        return self
