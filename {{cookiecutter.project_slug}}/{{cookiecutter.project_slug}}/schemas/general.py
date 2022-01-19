"""A test FastAPI application to reach a stable version for cookiecutter."""

from pydantic import BaseModel, Field
from typing import Optional


class Message(BaseModel):
    """A general template for those responses contain a message."""
    msg: Optional[str] = Field(
        title="Message", description="Message from the API")

    class Config:
        """Config Message class with an example."""

        schema_extra = {
            "title": "Message",
            "example": {
                "msg": "This is a test message coming from the API.",
            }
        }
