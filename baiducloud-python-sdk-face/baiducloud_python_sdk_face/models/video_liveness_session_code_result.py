"""
VideoLivenessSessionCodeResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VideoLivenessSessionCodeResult(AbstractModel):
    """
    VideoLivenessSessionCodeResult
    """

    def __init__(self, session_id=None, code=None):
        """
        Initialize VideoLivenessSessionCodeResult instance.

        :param session_id: session_id attribute
        :type session_id: str (optional)

        :param code: code attribute
        :type code: str (optional)
        """
        super().__init__()
        self.session_id = session_id
        self.code = code

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
        if self.session_id is not None:
            result['session_id'] = self.session_id
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VideoLivenessSessionCodeResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self
