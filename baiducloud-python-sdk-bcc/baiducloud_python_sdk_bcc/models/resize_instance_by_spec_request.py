"""
Request entity for ResizeInstanceBySpecRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResizeInstanceBySpecRequest(AbstractModel):
    """
    Request entity for ResizeInstanceBySpecRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, action, spec=None, enable_jumbo_frame=None):
        """
        Initialize ResizeInstanceBySpecRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param action: action parameter
        :type action: str (required)

        :param spec: 目标实例规格
        :type spec: str (optional)

        :param enable_jumbo_frame: enable_jumbo_frame parameter
        :type enable_jumbo_frame: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.action = action
        self.spec = spec
        self.enable_jumbo_frame = enable_jumbo_frame

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
        if self.spec is not None:
            result['spec'] = self.spec
        if self.enable_jumbo_frame is not None:
            result['enableJumboFrame'] = self.enable_jumbo_frame
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResizeInstanceBySpecRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('enableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('enableJumboFrame')
        return self
