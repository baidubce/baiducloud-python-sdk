"""
Request entity for HandwritingRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HandwritingRequest(AbstractModel):
    """
    Request entity for HandwritingRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image=None,
        url=None,
        pdf_file=None,
        pdf_file_num=None,
        ofd_file=None,
        ofd_file_num=None,
        recognize_granularity=None,
        eng_granularity=None,
        probability=None,
        detect_direction=None,
        detect_alteration=None,
        language_type=None,
    ):
        """
        Initialize HandwritingRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param pdf_file: pdf_file parameter
        :type pdf_file: str (optional)

        :param pdf_file_num: pdf_file_num parameter
        :type pdf_file_num: int (optional)

        :param ofd_file: ofd_file parameter
        :type ofd_file: str (optional)

        :param ofd_file_num: ofd_file_num parameter
        :type ofd_file_num: int (optional)

        :param recognize_granularity: recognize_granularity parameter
        :type recognize_granularity: str (optional)

        :param eng_granularity: eng_granularity parameter
        :type eng_granularity: str (optional)

        :param probability: 是否返回识别结果中每一行的置信度，默认为false，不返回置信度
        :type probability: bool (optional)

        :param detect_direction: detect_direction parameter
        :type detect_direction: bool (optional)

        :param detect_alteration: detect_alteration parameter
        :type detect_alteration: bool (optional)

        :param language_type: language_type parameter
        :type language_type: str (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.pdf_file_num = pdf_file_num
        self.ofd_file = ofd_file
        self.ofd_file_num = ofd_file_num
        self.recognize_granularity = recognize_granularity
        self.eng_granularity = eng_granularity
        self.probability = probability
        self.detect_direction = detect_direction
        self.detect_alteration = detect_alteration
        self.language_type = language_type

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
        if self.pdf_file is not None:
            result['pdf_file'] = self.pdf_file
        if self.pdf_file_num is not None:
            result['pdf_file_num'] = self.pdf_file_num
        if self.ofd_file is not None:
            result['ofd_file'] = self.ofd_file
        if self.ofd_file_num is not None:
            result['ofd_file_num'] = self.ofd_file_num
        if self.recognize_granularity is not None:
            result['recognize_granularity'] = self.recognize_granularity
        if self.eng_granularity is not None:
            result['eng_granularity'] = self.eng_granularity
        if self.probability is not None:
            result['probability'] = self.probability
        if self.detect_direction is not None:
            result['detect_direction'] = self.detect_direction
        if self.detect_alteration is not None:
            result['detect_alteration'] = self.detect_alteration
        if self.language_type is not None:
            result['language_type'] = self.language_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HandwritingRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('pdf_file') is not None:
            self.pdf_file = m.get('pdf_file')
        if m.get('pdf_file_num') is not None:
            self.pdf_file_num = m.get('pdf_file_num')
        if m.get('ofd_file') is not None:
            self.ofd_file = m.get('ofd_file')
        if m.get('ofd_file_num') is not None:
            self.ofd_file_num = m.get('ofd_file_num')
        if m.get('recognize_granularity') is not None:
            self.recognize_granularity = m.get('recognize_granularity')
        if m.get('eng_granularity') is not None:
            self.eng_granularity = m.get('eng_granularity')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        if m.get('detect_direction') is not None:
            self.detect_direction = m.get('detect_direction')
        if m.get('detect_alteration') is not None:
            self.detect_alteration = m.get('detect_alteration')
        if m.get('language_type') is not None:
            self.language_type = m.get('language_type')
        return self
