"""
BlbInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BlbInfo(AbstractModel):
    """
    BlbInfo
    """

    def __init__(self, blb_id=None, blb_name=None, blb_type=None, sg_ids=None):
        """
        Initialize BlbInfo instance.

        :param blb_id: BLB实例ID
        :type blb_id: str (optional)

        :param blb_name: BLB实例名称
        :type blb_name: str (optional)

        :param blb_type: blbType类型：Blb-普通型BLB，AppBLb-应用型BLB，Ipv6Blb-ipv6型BLB
        :type blb_type: str (optional)

        :param sg_ids: 当blb类型为应用型BLB时，服务器组必填，可选多个。其他类型BLB不需要填写该值。
        :type sg_ids: List[str] (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.blb_name = blb_name
        self.blb_type = blb_type
        self.sg_ids = sg_ids

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
        if self.blb_id is not None:
            result['blbId'] = self.blb_id
        if self.blb_name is not None:
            result['blbName'] = self.blb_name
        if self.blb_type is not None:
            result['blbType'] = self.blb_type
        if self.sg_ids is not None:
            result['sgIds'] = self.sg_ids
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BlbInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('blbName') is not None:
            self.blb_name = m.get('blbName')
        if m.get('blbType') is not None:
            self.blb_type = m.get('blbType')
        if m.get('sgIds') is not None:
            self.sg_ids = m.get('sgIds')
        return self
