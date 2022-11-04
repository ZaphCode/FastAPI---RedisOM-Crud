from redis_om import JsonModel, EmbeddedJsonModel, Field
from pydantic import EmailStr, PositiveInt
from typing import Optional, List
from .connections import redis_db
from datetime import datetime

class Bio(EmbeddedJsonModel):
    hobies: Optional[List[str]] = None
    job: Optional[str] = Field(None, index=True)
    city: Optional[str] = Field(None, index=True)
    single: bool = Field(False, index=True)

class User(JsonModel):
    email: EmailStr = Field(index=True, full_text_search=True)
    username: str = Field(index=True, full_text_search=True)
    password: str 
    age: PositiveInt = Field(sortable=True, index=True)
    created_at: datetime = Field(default=datetime.utcnow())
    bio: Optional[Bio]

    class Meta:
        database = redis_db




