"""
FaceVerifyOcclusion information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceVerifyOcclusion(AbstractModel):
    """
    FaceVerifyOcclusion
    """

    def __init__(
        self, left_eye=None, right_eye=None, nose=None, mouth=None, left_cheek=None, right_cheek=None, chin=None
    ):
        """
        Initialize FaceVerifyOcclusion instance.

        :param left_eye: 左眼遮挡比例，[0-1]，1表示完全遮挡
        :type left_eye: float (optional)

        :param right_eye: 右眼遮挡比例，[0-1]，1表示完全遮挡
        :type right_eye: float (optional)

        :param nose: 鼻子遮挡比例，[0-1]，1表示完全遮挡
        :type nose: float (optional)

        :param mouth: 嘴巴遮挡比例，[0-1]，1表示完全遮挡
        :type mouth: float (optional)

        :param left_cheek: 左脸颊遮挡比例，[0-1]，1表示完全遮挡
        :type left_cheek: float (optional)

        :param right_cheek: 右脸颊遮挡比例，[0-1]，1表示完全遮挡
        :type right_cheek: float (optional)

        :param chin: 下巴遮挡比例，[0-1]，1表示完全遮挡
        :type chin: float (optional)
        """
        super().__init__()
        self.left_eye = left_eye
        self.right_eye = right_eye
        self.nose = nose
        self.mouth = mouth
        self.left_cheek = left_cheek
        self.right_cheek = right_cheek
        self.chin = chin

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
        if self.left_eye is not None:
            result['left_eye'] = self.left_eye
        if self.right_eye is not None:
            result['right_eye'] = self.right_eye
        if self.nose is not None:
            result['nose'] = self.nose
        if self.mouth is not None:
            result['mouth'] = self.mouth
        if self.left_cheek is not None:
            result['left_cheek'] = self.left_cheek
        if self.right_cheek is not None:
            result['right_cheek'] = self.right_cheek
        if self.chin is not None:
            result['chin'] = self.chin
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceVerifyOcclusion

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('left_eye') is not None:
            self.left_eye = m.get('left_eye')
        if m.get('right_eye') is not None:
            self.right_eye = m.get('right_eye')
        if m.get('nose') is not None:
            self.nose = m.get('nose')
        if m.get('mouth') is not None:
            self.mouth = m.get('mouth')
        if m.get('left_cheek') is not None:
            self.left_cheek = m.get('left_cheek')
        if m.get('right_cheek') is not None:
            self.right_cheek = m.get('right_cheek')
        if m.get('chin') is not None:
            self.chin = m.get('chin')
        return self
