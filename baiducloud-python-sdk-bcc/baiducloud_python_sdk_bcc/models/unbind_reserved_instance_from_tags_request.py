"""
Request entity for UnbindReservedInstanceFromTagsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class UnbindReservedInstanceFromTagsRequest(AbstractModel):
    """
    Request entity for UnbindReservedInstanceFromTagsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, reserved_instance_ids, change_tags):
        """
        Initialize UnbindReservedInstanceFromTagsRequest request entity.

        :param reserved_instance_ids: 预留实例券ID列表，单次最多100个。
        :type reserved_instance_ids: List[str] (required)

        :param change_tags: 待解绑的标签列表。
        :type change_tags: List[TagModel] (required)
        """
        super().__init__()
        self.reserved_instance_ids = reserved_instance_ids
        self.change_tags = change_tags

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
        if self.reserved_instance_ids is not None:
            result['reservedInstanceIds'] = self.reserved_instance_ids
        if self.change_tags is not None:
            result['changeTags'] = [i.to_dict() for i in self.change_tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UnbindReservedInstanceFromTagsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstanceIds') is not None:
            self.reserved_instance_ids = m.get('reservedInstanceIds')
        if m.get('changeTags') is not None:
            self.change_tags = [TagModel().from_dict(i) for i in m.get('changeTags')]
        return self
