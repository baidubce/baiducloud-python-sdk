"""
Request entity for HouseholdRegisterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HouseholdRegisterRequest(AbstractModel):
    """
    Request entity for HouseholdRegisterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image=None, url=None, household_register_side=None):
        """
        Initialize HouseholdRegisterRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param household_register_side: 户口本类型页面： - subpage：默认值，常住人口登记卡（成员页） - homepage：户主页
        :type household_register_side: str (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.household_register_side = household_register_side

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.url is not None:
            result['url'] = self.url
        if self.household_register_side is not None:
            result['household_register_side'] = self.household_register_side
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HouseholdRegisterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('household_register_side') is not None:
            self.household_register_side = m.get('household_register_side')
        return self
