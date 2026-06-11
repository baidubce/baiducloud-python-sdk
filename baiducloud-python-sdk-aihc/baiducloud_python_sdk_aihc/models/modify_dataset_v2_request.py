"""
Request entity for ModifyDatasetV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aihc.models.permission_entry import PermissionEntry
from baiducloud_python_sdk_aihc.models.permission_entry import PermissionEntry


class ModifyDatasetV2Request(AbstractModel):
    """
    Request entity for ModifyDatasetV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        dataset_id,
        name=None,
        description=None,
        visibility_scope=None,
        visibility_user=None,
        visibility_group=None,
    ):
        """
        Initialize ModifyDatasetV2Request request entity.

        :param dataset_id: dataset_id parameter
        :type dataset_id: str (required)

        :param name: 数据集名称
        :type name: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param visibility_scope: visibility_scope parameter
        :type visibility_scope: str (optional)

        :param visibility_user: visibility_user parameter
        :type visibility_user: List[PermissionEntry] (optional)

        :param visibility_group: visibility_group parameter
        :type visibility_group: List[PermissionEntry] (optional)
        """
        super().__init__()
        self.dataset_id = dataset_id
        self.name = name
        self.description = description
        self.visibility_scope = visibility_scope
        self.visibility_user = visibility_user
        self.visibility_group = visibility_group

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
        if self.description is not None:
            result['description'] = self.description
        if self.visibility_scope is not None:
            result['visibilityScope'] = self.visibility_scope
        if self.visibility_user is not None:
            result['visibilityUser'] = [i.to_dict() for i in self.visibility_user]
        if self.visibility_group is not None:
            result['visibilityGroup'] = [i.to_dict() for i in self.visibility_group]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyDatasetV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('visibilityScope') is not None:
            self.visibility_scope = m.get('visibilityScope')
        if m.get('visibilityUser') is not None:
            self.visibility_user = [PermissionEntry().from_dict(i) for i in m.get('visibilityUser')]
        if m.get('visibilityGroup') is not None:
            self.visibility_group = [PermissionEntry().from_dict(i) for i in m.get('visibilityGroup')]
        return self
