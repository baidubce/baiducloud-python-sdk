"""
MedicalReportDetectionCommonDataItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.medical_report_detection_location import MedicalReportDetectionLocation

from baiducloud_python_sdk_ocr.models.medical_report_detection_probability import MedicalReportDetectionProbability


class MedicalReportDetectionCommonDataItem(AbstractModel):
    """
    MedicalReportDetectionCommonDataItem
    """

    def __init__(self, word_name=None, word=None, location=None, probability=None):
        """
        Initialize MedicalReportDetectionCommonDataItem instance.

        :param word_name: word_name attribute
        :type word_name: str (optional)

        :param word: 字段识别结果
        :type word: str (optional)

        :param location: location attribute
        :type location: MedicalReportDetectionLocation (optional)

        :param probability: probability attribute
        :type probability: MedicalReportDetectionProbability (optional)
        """
        super().__init__()
        self.word_name = word_name
        self.word = word
        self.location = location
        self.probability = probability

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
        if self.word_name is not None:
            result['word_name'] = self.word_name
        if self.word is not None:
            result['word'] = self.word
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.probability is not None:
            result['probability'] = self.probability.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalReportDetectionCommonDataItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('word_name') is not None:
            self.word_name = m.get('word_name')
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('location') is not None:
            self.location = MedicalReportDetectionLocation().from_dict(m.get('location'))
        if m.get('probability') is not None:
            self.probability = MedicalReportDetectionProbability().from_dict(m.get('probability'))
        return self
