"""
Request entity for MaterielImageSearchRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MaterielImageSearchRequest(AbstractModel):
    """
    Request entity for MaterielImageSearchRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, tags=None, tag_logic=None, pn=None, rn=None):
        """
        Initialize MaterielImageSearchRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param tags: tags parameter
        :type tags: str (optional)

        :param tag_logic: 检索时tag之间的逻辑关系
        :type tag_logic: int (optional)

        :param pn: pn parameter
        :type pn: int (optional)

        :param rn: 分页功能，截取条数，例：10。可选值范围：1 - 300范围内的整数
        :type rn: int (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.tags = tags
        self.tag_logic = tag_logic
        self.pn = pn
        self.rn = rn

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
        if self.image is not None:
            result['image'] = self.image
        if self.url is not None:
            result['url'] = self.url
        if self.tags is not None:
            result['tags'] = self.tags
        if self.tag_logic is not None:
            result['tag_logic'] = self.tag_logic
        if self.pn is not None:
            result['pn'] = self.pn
        if self.rn is not None:
            result['rn'] = self.rn
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MaterielImageSearchRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('tag_logic') is not None:
            self.tag_logic = m.get('tag_logic')
        if m.get('pn') is not None:
            self.pn = m.get('pn')
        if m.get('rn') is not None:
            self.rn = m.get('rn')
        return self
