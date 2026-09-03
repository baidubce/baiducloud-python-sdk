"""
Request entity for SegmentRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SegmentRequest(AbstractModel):
    """
    Request entity for SegmentRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, method, image=None, url=None, return_form=None, refine_mask=None, position=None):
        """
        Initialize SegmentRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param method: method parameter
        :type method: str (required)

        :param return_form: return_form parameter
        :type return_form: str (optional)

        :param refine_mask: 是否对边缘进行平滑处理。<br/>false：不对边缘平滑处理；<br/>true：对边缘平滑处理。默认值为true
        :type refine_mask: bool (optional)

        :param position: position parameter
        :type position: str (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.method = method
        self.return_form = return_form
        self.refine_mask = refine_mask
        self.position = position

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
        if self.method is not None:
            result['method'] = self.method
        if self.return_form is not None:
            result['return_form'] = self.return_form
        if self.refine_mask is not None:
            result['refine_mask'] = self.refine_mask
        if self.position is not None:
            result['position'] = self.position
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SegmentRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('return_form') is not None:
            self.return_form = m.get('return_form')
        if m.get('refine_mask') is not None:
            self.refine_mask = m.get('refine_mask')
        if m.get('position') is not None:
            self.position = m.get('position')
        return self
