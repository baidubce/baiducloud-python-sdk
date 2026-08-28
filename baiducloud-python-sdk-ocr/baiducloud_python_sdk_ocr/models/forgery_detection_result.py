"""
ForgeryDetectionResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.tampered_location import TamperedLocation


class ForgeryDetectionResult(AbstractModel):
    """
    ForgeryDetectionResult
    """

    def __init__(self, detection_result=None, tampered_proportion=None, tampered_location=None, heatmap=None):
        """
        Initialize ForgeryDetectionResult instance.

        :param detection_result: 篡改检测结果
        :type detection_result: str (optional)

        :param tampered_proportion: 图片篡改置信度（当请求参数 detect_proportion = true 时返回）
        :type tampered_proportion: float (optional)

        :param tampered_location: 伪造区域的坐标信息（当 probability ≥ restrict_probability 阈值时返回坐标信息）
        :type tampered_location: List[TamperedLocation] (optional)

        :param heatmap: 篡改区域热力图（当请求参数 return_heatmap = true 时返回）
        :type heatmap: str (optional)
        """
        super().__init__()
        self.detection_result = detection_result
        self.tampered_proportion = tampered_proportion
        self.tampered_location = tampered_location
        self.heatmap = heatmap

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
        if self.detection_result is not None:
            result['detection_result'] = self.detection_result
        if self.tampered_proportion is not None:
            result['tampered_proportion'] = self.tampered_proportion
        if self.tampered_location is not None:
            result['tampered_location'] = [i.to_dict() for i in self.tampered_location]
        if self.heatmap is not None:
            result['heatmap'] = self.heatmap
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ForgeryDetectionResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('detection_result') is not None:
            self.detection_result = m.get('detection_result')
        if m.get('tampered_proportion') is not None:
            self.tampered_proportion = m.get('tampered_proportion')
        if m.get('tampered_location') is not None:
            self.tampered_location = [TamperedLocation().from_dict(i) for i in m.get('tampered_location')]
        if m.get('heatmap') is not None:
            self.heatmap = m.get('heatmap')
        return self
