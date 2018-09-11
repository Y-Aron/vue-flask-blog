
from utils import MySQL
from config import STATUS

class Model(MySQL):

    @staticmethod
    def respData(code: int = STATUS.OK, error: str = None, data=None):
        return dict(
            code=code,
            error=error,
            data=data
        )





