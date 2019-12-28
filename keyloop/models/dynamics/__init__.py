import pymodm

from dyn_pymodm import DynamicModelHandler
from ..user import User


class DynamicModels:
    def __init__(self):
        self.user_handler = DynamicModelHandler(
            class_name="User", connection_alias="keyloop", parent_classes=User
        )

    @property
    def User(self):
        return self.user_handler.model
