"""
Request entity for ModifyCdsAttributeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyCdsAttributeRequest(AbstractModel):
    """
    Request entity for ModifyCdsAttributeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id, cds_name=None, desc=None, delete_with_instance=None, delete_auto_snapshot=None):
        """
        Initialize ModifyCdsAttributeRequest request entity.

        :param volume_id: volume_id parameter
        :type volume_id: str (required)

        :param cds_name: 磁盘新的名称，支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65
        :type cds_name: str (optional)

        :param desc: desc parameter
        :type desc: str (optional)

        :param delete_with_instance: delete_with_instance parameter
        :type delete_with_instance: bool (optional)

        :param delete_auto_snapshot: delete_auto_snapshot parameter
        :type delete_auto_snapshot: bool (optional)
        """
        super().__init__()
        self.volume_id = volume_id
        self.cds_name = cds_name
        self.desc = desc
        self.delete_with_instance = delete_with_instance
        self.delete_auto_snapshot = delete_auto_snapshot

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
        if self.cds_name is not None:
            result['cdsName'] = self.cds_name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.delete_with_instance is not None:
            result['deleteWithInstance'] = self.delete_with_instance
        if self.delete_auto_snapshot is not None:
            result['deleteAutoSnapshot'] = self.delete_auto_snapshot
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyCdsAttributeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('cdsName') is not None:
            self.cds_name = m.get('cdsName')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('deleteWithInstance') is not None:
            self.delete_with_instance = m.get('deleteWithInstance')
        if m.get('deleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('deleteAutoSnapshot')
        return self
