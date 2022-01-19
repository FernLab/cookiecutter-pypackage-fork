"""
{{ cookiecutter.project_slug }}.

{{ cookiecutter.project_short_description }}.
"""

from typing import Optional
from pydantic import BaseModel, Field


class GETItemsResponse(BaseModel):
    """Template for [GET] /item response."""
    data: Optional[list] = Field(title="data", description="A list of Items.")

    class Config:
        """Config GETItemsResponse class with an example."""

        schema_extra = {
            "title": "GET Items Response",
            "example": {
                "data": [
                    {"id": "1000", "price": 102.19},
                    {"id": "1002", "price": 151.89}
                ]
            }
        }


class GETItemResponse(BaseModel):
    """Template for [GET] /item/{id} response."""
    
    data: Optional[dict] = Field(
        title="data", description="An item data dictionary.")

    class Config:
        """Config GETItemResponse class with an example."""

        schema_extra = {
            "title": "GET Item Response",
            "example": {
                "data": {"id": "1000", "price": 102.19}
            }
        }
