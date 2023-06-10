from pydantic import BaseModel, Field
from bson import ObjectId
import enum


class QuestionCategory(enum.Enum):
    RELATIONSHIP = "relationship"
    FUTURE = "future"
    PERSONAL = "personal"
    HOBBIES = "hobbies"
    ENTERTAINMENT = "entertainment"
    VALUES = "values"


class Writers(enum.Enum):
    OMER = "omer"
    MAYA = "maya"


class Question(BaseModel):

    id: ObjectId = Field(alias="_id")
    text: str = Field(...)
    category: QuestionCategory = Field(...)
    writer: Writers = Field(...)
    answerd: bool = Field(False)

    class Config:
        allow_population_by_field_name = True
        orm_mode = True

    def dict(self, *args, **kwargs):
        kwargs["by_alias"] = True
        return super().dict(*args, **kwargs)
