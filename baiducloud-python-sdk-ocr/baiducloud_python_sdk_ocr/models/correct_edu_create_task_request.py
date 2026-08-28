"""
Request entity for CorrectEduCreateTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CorrectEduCreateTaskRequest(AbstractModel):
    """
    Request entity for CorrectEduCreateTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, only_split=None, disable_preprocess=None):
        """
        Initialize CorrectEduCreateTaskRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param only_split: 是否仅进行题目切分，默认false。true：开启（同步返回，扣切题额度）；false：不开启（端到端批改）
        :type only_split: bool (optional)

        :param disable_preprocess: 是否关闭图片矫正，默认false。true：关闭矫正；false：开启矫正
        :type disable_preprocess: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.only_split = only_split
        self.disable_preprocess = disable_preprocess

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
        if self.only_split is not None:
            result['only_split'] = self.only_split
        if self.disable_preprocess is not None:
            result['disable_preprocess'] = self.disable_preprocess
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CorrectEduCreateTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('only_split') is not None:
            self.only_split = m.get('only_split')
        if m.get('disable_preprocess') is not None:
            self.disable_preprocess = m.get('disable_preprocess')
        return self
