"""
FaceVerifyDateResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceVerifyDateResult(AbstractModel):
    """
    FaceVerifyDateResult
    """

    def __init__(self, verify_status=None, verify_score=None):
        """
        Initialize FaceVerifyDateResult instance.

        :param verify_status: verify_status attribute
        :type verify_status: int (optional)

        :param verify_score: verify_score attribute
        :type verify_score: float (optional)
        """
        super().__init__()
        self.verify_status = verify_status
        self.verify_score = verify_score

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
        if self.verify_status is not None:
            result['verify_status'] = self.verify_status
        if self.verify_score is not None:
            result['verify_score'] = self.verify_score
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceVerifyDateResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('verify_status') is not None:
            self.verify_status = m.get('verify_status')
        if m.get('verify_score') is not None:
            self.verify_score = m.get('verify_score')
        return self
