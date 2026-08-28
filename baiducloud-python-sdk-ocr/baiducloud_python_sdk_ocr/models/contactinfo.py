"""
Contactinfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.website import Website


class Contactinfo(AbstractModel):
    """
    Contactinfo
    """

    def __init__(self, website=None, phonenumber=None, email=None):
        """
        Initialize Contactinfo instance.

        :param website: 网站信息，每个数组可能包含多个object
        :type website: List[Website] (optional)

        :param phonenumber: 联系电话
        :type phonenumber: str (optional)

        :param email: 联系邮箱
        :type email: str (optional)
        """
        super().__init__()
        self.website = website
        self.phonenumber = phonenumber
        self.email = email

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
        if self.website is not None:
            result['website'] = [i.to_dict() for i in self.website]
        if self.phonenumber is not None:
            result['phonenumber'] = self.phonenumber
        if self.email is not None:
            result['email'] = self.email
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Contactinfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('website') is not None:
            self.website = [Website().from_dict(i) for i in m.get('website')]
        if m.get('phonenumber') is not None:
            self.phonenumber = m.get('phonenumber')
        if m.get('email') is not None:
            self.email = m.get('email')
        return self
