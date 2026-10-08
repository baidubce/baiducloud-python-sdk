"""
Engine information
"""


class Engine:
    """
    Enum class for Engine
    Allowed values: REDIS, PEGADB
    """

    REDIS = 'redis'
    PEGADB = 'PegaDB'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['redis', 'PegaDB']
        return value in valid_values
