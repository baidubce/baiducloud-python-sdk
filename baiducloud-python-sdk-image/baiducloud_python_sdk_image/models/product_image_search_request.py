"""
Request entity for ProductImageSearchRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ProductImageSearchRequest(AbstractModel):
    """
    Request entity for ProductImageSearchRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, class_id1=None, class_id2=None, tag_logic=None, pn=None, rn=None):
        """
        Initialize ProductImageSearchRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param class_id1: 商品分类维度1，支持1-65535范围内的整数
        :type class_id1: int (optional)

        :param class_id2: 商品分类维度2，支持1-65535范围内的整数
        :type class_id2: int (optional)

        :param tag_logic: 检索时tag之间的逻辑，0：逻辑and，1：逻辑or
        :type tag_logic: int (optional)

        :param pn: pn parameter
        :type pn: int (optional)

        :param rn: 分页功能，截取条数，例：250。取值范围1-1000
        :type rn: int (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.class_id1 = class_id1
        self.class_id2 = class_id2
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
        if self.class_id1 is not None:
            result['class_id1'] = self.class_id1
        if self.class_id2 is not None:
            result['class_id2'] = self.class_id2
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
        :rtype: ProductImageSearchRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('class_id1') is not None:
            self.class_id1 = m.get('class_id1')
        if m.get('class_id2') is not None:
            self.class_id2 = m.get('class_id2')
        if m.get('tag_logic') is not None:
            self.tag_logic = m.get('tag_logic')
        if m.get('pn') is not None:
            self.pn = m.get('pn')
        if m.get('rn') is not None:
            self.rn = m.get('rn')
        return self
