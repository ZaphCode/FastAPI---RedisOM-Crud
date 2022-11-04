from pydantic import BaseModel, Field
from typing import List

class BioSch(BaseModel):
    hobies: List[str] = Field(None, example=['Play Videogames', 'Crossfit'])
    job: str = Field(None, example='developer')
    city: str = Field(None, example='Mexico')
    single: bool = False