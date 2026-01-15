from pydantic import BaseModel, Field


class Top_terrorists(BaseModel):
    name: str
    location: str
    rate_danger : int = Field(ge= 0, le=10)
