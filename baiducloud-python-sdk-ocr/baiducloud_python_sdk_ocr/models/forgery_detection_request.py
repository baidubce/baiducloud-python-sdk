"""
Request entity for ForgeryDetectionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ForgeryDetectionRequest(AbstractModel):
    """
    Request entity for ForgeryDetectionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image=None,
        url=None,
        detect_proportion=None,
        detect_threshold=None,
        return_heatmap=None,
        restrict_probability=None,
    ):
        """
        Initialize ForgeryDetectionRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param detect_proportion: 是否返回图片篡改置信度，默认不返回，即：false。<br/>- true：返回图片篡改置信度；- false：不返回
        :type detect_proportion: bool (optional)

        :param detect_threshold: detect_threshold parameter
        :type detect_threshold: float (optional)

        :param return_heatmap: return_heatmap parameter
        :type return_heatmap: bool (optional)

        :param restrict_probability: restrict_probability parameter
        :type restrict_probability: float (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.detect_proportion = detect_proportion
        self.detect_threshold = detect_threshold
        self.return_heatmap = return_heatmap
        self.restrict_probability = restrict_probability

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
        if self.detect_proportion is not None:
            result['detect_proportion'] = self.detect_proportion
        if self.detect_threshold is not None:
            result['detect_threshold'] = self.detect_threshold
        if self.return_heatmap is not None:
            result['return_heatmap'] = self.return_heatmap
        if self.restrict_probability is not None:
            result['restrict_probability'] = self.restrict_probability
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ForgeryDetectionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('detect_proportion') is not None:
            self.detect_proportion = m.get('detect_proportion')
        if m.get('detect_threshold') is not None:
            self.detect_threshold = m.get('detect_threshold')
        if m.get('return_heatmap') is not None:
            self.return_heatmap = m.get('return_heatmap')
        if m.get('restrict_probability') is not None:
            self.restrict_probability = m.get('restrict_probability')
        return self
