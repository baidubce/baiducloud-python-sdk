"""
Request entity for BindTagVolumeClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class BindTagVolumeClusterRequest(AbstractModel):
    """
    Request entity for BindTagVolumeClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, change_tags):
        """
        Initialize BindTagVolumeClusterRequest request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param change_tags: 待绑定的标签列表
        :type change_tags: List[TagModel] (required)
        """
        super().__init__()
        self.cluster_id = cluster_id
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
        :rtype: BindTagVolumeClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('changeTags') is not None:
            self.change_tags = [TagModel().from_dict(i) for i in m.get('changeTags')]
        return self
