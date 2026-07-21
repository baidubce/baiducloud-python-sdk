"""
ACL information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_iam.models.acl_entry import ACLEntry


class ACL(AbstractModel):
    """
    ACL
    """

    def __init__(self, id=None, version=None, access_control_list=None):
        """
        Initialize ACL instance.

        :param id: id
        :type id: str (optional)

        :param version: \"v2\"
        :type version: str (optional)

        :param access_control_list: ACL entry
        :type access_control_list: List[ACLEntry] (optional)
        """
        super().__init__()
        self.id = id
        self.version = version
        self.access_control_list = access_control_list

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
        if self.id is not None:
            result['id'] = self.id
        if self.version is not None:
            result['version'] = self.version
        if self.access_control_list is not None:
            result['accessControlList'] = [i.to_dict() for i in self.access_control_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ACL

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('accessControlList') is not None:
            self.access_control_list = [ACLEntry().from_dict(i) for i in m.get('accessControlList')]
        return self
