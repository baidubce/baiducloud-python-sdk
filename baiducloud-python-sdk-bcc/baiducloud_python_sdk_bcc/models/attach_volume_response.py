"""
Request entity for AttachVolumeResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.volume_attachment_model import VolumeAttachmentModel


class AttachVolumeResponse(BceResponse):
    """
    AttachVolumeResponse
    """

    def __init__(self, volume_attachment=None, warning_list=None):
        """
        Initialize AttachVolumeResponse response.

        :param volume_attachment: volume_attachment field
        :type volume_attachment: VolumeAttachmentModel (optional)

        :param warning_list: 挂载磁盘产生的warning信息
        :type warning_list: List[str] (optional)
        """
        super().__init__()
        self.volume_attachment = volume_attachment
        self.warning_list = warning_list

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.volume_attachment is not None:
            result['volumeAttachment'] = self.volume_attachment.to_dict()
        if self.warning_list is not None:
            result['warningList'] = self.warning_list
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AttachVolumeResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeAttachment') is not None:
            self.volume_attachment = VolumeAttachmentModel().from_dict(m.get('volumeAttachment'))
        if m.get('warningList') is not None:
            self.warning_list = m.get('warningList')
        return self
