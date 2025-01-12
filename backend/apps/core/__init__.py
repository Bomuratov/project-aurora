__all__=(
    "Basemodel",
    "utils"
)

from core import utils

def get_basemodel():
    from core.models import Basemodel
    return Basemodel