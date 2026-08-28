"""
PaperCutEduVlmGetQusResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.paper_cut_edu_vlm_location import PaperCutEduVlmLocation

from baiducloud_python_sdk_ocr.models.qus_elements import QusElements


class PaperCutEduVlmGetQusResult(AbstractModel):
    """
    PaperCutEduVlmGetQusResult
    """

    def __init__(self, qus_id=None, location=None, qus_elements=None):
        """
        Initialize PaperCutEduVlmGetQusResult instance.

        :param qus_id: 题号
        :type qus_id: int (optional)

        :param location: location attribute
        :type location: PaperCutEduVlmLocation (optional)

        :param qus_elements: qus_elements attribute
        :type qus_elements: QusElements (optional)
        """
        super().__init__()
        self.qus_id = qus_id
        self.location = location
        self.qus_elements = qus_elements

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
        if self.qus_id is not None:
            result['qus_id'] = self.qus_id
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.qus_elements is not None:
            result['qus_elements'] = self.qus_elements.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PaperCutEduVlmGetQusResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('qus_id') is not None:
            self.qus_id = m.get('qus_id')
        if m.get('location') is not None:
            self.location = PaperCutEduVlmLocation().from_dict(m.get('location'))
        if m.get('qus_elements') is not None:
            self.qus_elements = QusElements().from_dict(m.get('qus_elements'))
        return self
