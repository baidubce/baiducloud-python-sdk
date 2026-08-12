"""
ListSandboxesResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_ax.models.listed_sandbox import ListedSandbox


class ListSandboxesResponse(BceResponse):
    """
    ListSandboxesResponse
    """

    def __init__(self, sandboxes=None):
        """
        Initialize ListSandboxesResponse instance.

        :param sandboxes: 沙箱实例数组。
        :type sandboxes: List[ListedSandbox] (optional)
        """
        super().__init__()
        self.sandboxes = sandboxes

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.sandboxes is not None:
            result['sandboxes'] = [i.to_dict() for i in self.sandboxes]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListSandboxesResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxes') is not None:
            self.sandboxes = [ListedSandbox().from_dict(i) for i in m.get('sandboxes')]
        return self
