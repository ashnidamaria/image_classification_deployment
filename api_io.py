from pydantic import BaseModel
from typing import Optional


class PredictApiRequest(BaseModel):
    image_url: str


class PredictApiResponse(BaseModel):
    return_string: Optional[str]
    errors: Optional[str]
