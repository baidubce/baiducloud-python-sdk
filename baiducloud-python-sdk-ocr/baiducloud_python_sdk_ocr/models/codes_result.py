"""
CodesResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.qr_code_location import QRCodeLocation


class CodesResult(AbstractModel):
    """
    CodesResult
    """

    def __init__(self, type=None, text=None, location=None):
        """
        Initialize CodesResult instance.

        :param type: type attribute
        :type type: str (optional)

        :param text: 条形码/二维码识别内容，目前仅支持输出中英文结果
        :type text: List[str] (optional)

        :param location: location attribute
        :type location: QRCodeLocation (optional)
        """
        super().__init__()
        self.type = type
        self.text = text
        self.location = location

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
        if self.type is not None:
            result['type'] = self.type
        if self.text is not None:
            result['text'] = self.text
        if self.location is not None:
            result['location'] = self.location.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CodesResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('location') is not None:
            self.location = QRCodeLocation().from_dict(m.get('location'))
        return self
