"""
Request entity for BindTagSnapchainRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class BindTagSnapchainRequest(AbstractModel):
    """
    Request entity for BindTagSnapchainRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, chain_id, change_tags):
        """
        Initialize BindTagSnapchainRequest request entity.

        :param chain_id: chain_id parameter
        :type chain_id: str (required)

        :param change_tags: 待绑定的标签列表
        :type change_tags: List[TagModel] (required)
        """
        super().__init__()
        self.chain_id = chain_id
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
        :rtype: BindTagSnapchainRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('chainId') is not None:
            self.chain_id = m.get('chainId')
        if m.get('changeTags') is not None:
            self.change_tags = [TagModel().from_dict(i) for i in m.get('changeTags')]
        return self
