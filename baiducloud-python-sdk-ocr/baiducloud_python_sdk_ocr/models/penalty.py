"""
Penalty information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Penalty(AbstractModel):
    """
    Penalty
    """

    def __init__(
        self,
        docno=None,
        penaltytype=None,
        officename=None,
        content=None,
        penaltydate=None,
        publicdate=None,
        remark=None,
    ):
        """
        Initialize Penalty instance.

        :param docno: 行政处罚决定书文号
        :type docno: str (optional)

        :param penaltytype: 违法行为类型
        :type penaltytype: str (optional)

        :param officename: 行政处罚决定机关名称
        :type officename: str (optional)

        :param content: 行政处罚内容
        :type content: str (optional)

        :param penaltydate: 作出行政处罚决定日期
        :type penaltydate: str (optional)

        :param publicdate: 作出行政公示日期
        :type publicdate: str (optional)

        :param remark: 备注
        :type remark: str (optional)
        """
        super().__init__()
        self.docno = docno
        self.penaltytype = penaltytype
        self.officename = officename
        self.content = content
        self.penaltydate = penaltydate
        self.publicdate = publicdate
        self.remark = remark

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
        if self.docno is not None:
            result['docno'] = self.docno
        if self.penaltytype is not None:
            result['penaltytype'] = self.penaltytype
        if self.officename is not None:
            result['officename'] = self.officename
        if self.content is not None:
            result['content'] = self.content
        if self.penaltydate is not None:
            result['penaltydate'] = self.penaltydate
        if self.publicdate is not None:
            result['publicdate'] = self.publicdate
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Penalty

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('docno') is not None:
            self.docno = m.get('docno')
        if m.get('penaltytype') is not None:
            self.penaltytype = m.get('penaltytype')
        if m.get('officename') is not None:
            self.officename = m.get('officename')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('penaltydate') is not None:
            self.penaltydate = m.get('penaltydate')
        if m.get('publicdate') is not None:
            self.publicdate = m.get('publicdate')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self
