from pydantic import BaseModel, Field
from bson import ObjectId
import enum
from typing import Optional


class QuestionCategory(str, enum.Enum):
    RELATIONSHIP = "relationship"
    FUTURE = "future"
    PERSONAL = "personal"
    HOBBIES = "hobbies"
    ENTERTAINMENT = "entertainment"
    VALUES = "values"


class Writers(str, enum.Enum):
    OMER = "omer"
    MAYA = "maya"

    def get_password(self):
        if self == Writers.OMER:
            return "$argon2id$v=19$m=65536,t=3,p=4$S4SuBVmtBxnUlXX2Ojjr/A$R+3xrxC1uxh2pIIojztuhh6dg3ckciU6EWhDMoeimOQ"
        elif self == Writers.MAYA:
            return "$argon2id$v=19$m=65536,t=3,p=4$UxIqbCqtAPoIGLEpZ4wYhA$oDReaHmbD4+JBA8eGTQP1eiOAiwknI6eYy+vNiK2JOc"


class Question(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    text: str = Field(...)
    category: QuestionCategory = Field(...)
    writer: Writers = Field(...)
    answerd: bool = Field(False)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

    def dict(self, *args, **kwargs):
        kwargs["by_alias"] = True
        if not self.id:
            kwargs["exclude"] = {"id"}
        return super().dict(*args, **kwargs)
