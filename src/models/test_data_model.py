from datetime import time
from pydantic import BaseModel


class TestDataModel(BaseModel):
    __test__ = False

    photo_name: str
    amount_of_required_interests: int
    expected_timer_value: time