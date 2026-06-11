"""
Request entity for UnShareImageRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UnShareImageRequest(AbstractModel):
    """
    Request entity for UnShareImageRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image_id, account=None, account_id=None, uc_account=None):
        """
        Initialize UnShareImageRequest request entity.

        :param image_id: image_id parameter
        :type image_id: str (required)

        :param account: 待取消共享的用户名
        :type account: str (optional)

        :param account_id: 待取消共享的用户ID
        :type account_id: str (optional)

        :param uc_account: uc账号
        :type uc_account: str (optional)
        """
        super().__init__()
        self.image_id = image_id
        self.account = account
        self.account_id = account_id
        self.uc_account = uc_account

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
        if self.account is not None:
            result['account'] = self.account
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.uc_account is not None:
            result['ucAccount'] = self.uc_account
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UnShareImageRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('ucAccount') is not None:
            self.uc_account = m.get('ucAccount')
        return self
