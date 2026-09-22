"""
VideoLivenessVerifyResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.video_liveness_verify_thresholds import VideoLivenessVerifyThresholds

from baiducloud_python_sdk_face.models.video_liveness_verify_code_info import VideoLivenessVerifyCodeInfo

from baiducloud_python_sdk_face.models.best_image import BestImage

from baiducloud_python_sdk_face.models.pic_item import PicItem


class VideoLivenessVerifyResult(AbstractModel):
    """
    VideoLivenessVerifyResult
    """

    def __init__(
        self,
        score=None,
        maxspoofing=None,
        spoofing_score=None,
        thresholds=None,
        code=None,
        lip_language=None,
        action_verify=None,
        best_image=None,
        pic_list=None,
    ):
        """
        Initialize VideoLivenessVerifyResult instance.

        :param score: 活体检测的总体打分，范围[0,1]，分数越高则活体的概率越大
        :type score: float (optional)

        :param maxspoofing: 返回的1-8张图片中合成图检测得分的最大值，范围[0,1]，分数越高则概率越大
        :type maxspoofing: float (optional)

        :param spoofing_score: 返回的1-8张图片中合成图检测得分的中位数，范围[0,1]，分数越高则概率越大
        :type spoofing_score: float (optional)

        :param thresholds: thresholds attribute
        :type thresholds: VideoLivenessVerifyThresholds (optional)

        :param code: code attribute
        :type code: VideoLivenessVerifyCodeInfo (optional)

        :param lip_language: lip_language attribute
        :type lip_language: str (optional)

        :param action_verify: action_verify attribute
        :type action_verify: str (optional)

        :param best_image: best_image attribute
        :type best_image: BestImage (optional)

        :param pic_list: 返回1-8张抽取出来的图片信息
        :type pic_list: List[PicItem] (optional)
        """
        super().__init__()
        self.score = score
        self.maxspoofing = maxspoofing
        self.spoofing_score = spoofing_score
        self.thresholds = thresholds
        self.code = code
        self.lip_language = lip_language
        self.action_verify = action_verify
        self.best_image = best_image
        self.pic_list = pic_list

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
        if self.score is not None:
            result['score'] = self.score
        if self.maxspoofing is not None:
            result['maxspoofing'] = self.maxspoofing
        if self.spoofing_score is not None:
            result['spoofing_score'] = self.spoofing_score
        if self.thresholds is not None:
            result['thresholds'] = self.thresholds.to_dict()
        if self.code is not None:
            result['code'] = self.code.to_dict()
        if self.lip_language is not None:
            result['lip_language'] = self.lip_language
        if self.action_verify is not None:
            result['action_verify'] = self.action_verify
        if self.best_image is not None:
            result['best_image'] = self.best_image.to_dict()
        if self.pic_list is not None:
            result['pic_list'] = [i.to_dict() for i in self.pic_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VideoLivenessVerifyResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('maxspoofing') is not None:
            self.maxspoofing = m.get('maxspoofing')
        if m.get('spoofing_score') is not None:
            self.spoofing_score = m.get('spoofing_score')
        if m.get('thresholds') is not None:
            self.thresholds = VideoLivenessVerifyThresholds().from_dict(m.get('thresholds'))
        if m.get('code') is not None:
            self.code = VideoLivenessVerifyCodeInfo().from_dict(m.get('code'))
        if m.get('lip_language') is not None:
            self.lip_language = m.get('lip_language')
        if m.get('action_verify') is not None:
            self.action_verify = m.get('action_verify')
        if m.get('best_image') is not None:
            self.best_image = BestImage().from_dict(m.get('best_image'))
        if m.get('pic_list') is not None:
            self.pic_list = [PicItem().from_dict(i) for i in m.get('pic_list')]
        return self
