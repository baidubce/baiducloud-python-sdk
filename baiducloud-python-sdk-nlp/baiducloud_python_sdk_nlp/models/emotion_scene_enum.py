"""
EmotionSceneEnum information
"""


class EmotionSceneEnum:
    """
    Enum class for EmotionSceneEnum
    Allowed values: DEFAULT, TALK, TASK, CUSTOMER_SERVICE
    """

    DEFAULT = 'default'
    TALK = 'talk'
    TASK = 'task'
    CUSTOMER_SERVICE = 'customer_service'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['default', 'talk', 'task', 'customer_service']
        return value in valid_values
