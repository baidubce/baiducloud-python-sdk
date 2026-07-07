"""
Request entity for BatchAcquisitionOfUsersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchAcquisitionOfUsersRequest(AbstractModel):
    """
    Request entity for BatchAcquisitionOfUsersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_pool_id, ids):
        """
        Initialize BatchAcquisitionOfUsersRequest request entity.

        :param user_pool_id: 用户池 ID
        :type user_pool_id: str (required)

        :param ids: 用户 ID 列表，最多 100 个
        :type ids: List[str] (required)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
        self.ids = ids

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
        if self.user_pool_id is not None:
            result['userPoolId'] = self.user_pool_id
        if self.ids is not None:
            result['ids'] = self.ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchAcquisitionOfUsersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        return self
