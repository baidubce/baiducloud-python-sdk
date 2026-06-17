"""
Request entity for BindTagVolumeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class BindTagVolumeRequest(AbstractModel):
    """
    Request entity for BindTagVolumeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id, change_tags):
        """
        Initialize BindTagVolumeRequest request entity.

        :param volume_id: volume_id parameter
        :type volume_id: str (required)

        :param change_tags: 待绑定的标签列表，绑定的标签如果之前不存在，将自动创建该标签
        :type change_tags: List[TagModel] (required)
        """
        super().__init__()
        self.volume_id = volume_id
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
        :rtype: BindTagVolumeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('changeTags') is not None:
            self.change_tags = [TagModel().from_dict(i) for i in m.get('changeTags')]
        return self
