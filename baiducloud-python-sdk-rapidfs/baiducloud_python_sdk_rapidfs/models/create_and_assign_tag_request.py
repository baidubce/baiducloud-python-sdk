"""
Request entity for CreateAndAssignTagRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rapidfs.models.tag_resource import TagResource


class CreateAndAssignTagRequest(AbstractModel):
    """
    Request entity for CreateAndAssignTagRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, tag_resources, client_token=None):
        """
        Initialize CreateAndAssignTagRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param tag_resources: 需要修改的实例及标签信息，支持批量修改，见附录 TagResource，仅支持 RapidFS 实例绑定标签
        :type tag_resources: List[TagResource] (required)
        """
        super().__init__()
        self.client_token = client_token
        self.tag_resources = tag_resources

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
        if self.tag_resources is not None:
            result['tagResources'] = [i.to_dict() for i in self.tag_resources]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAndAssignTagRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('tagResources') is not None:
            self.tag_resources = [TagResource().from_dict(i) for i in m.get('tagResources')]
        return self
