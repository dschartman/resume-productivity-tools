from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import Optional


class CoreInfo(BaseModel):
    """
    Core information for a resume, including personal and contact details.

    Attributes:
        name (str): Full name of the individual.
        address (str): Postal address, could include street, city, state, and zip code.
        email (EmailStr): Contact email address, must be a valid email format.
        phone (str): Contact phone number as a string.
        linkedin (Optional[HttpUrl]): LinkedIn profile URL, must be a valid URL if provided.
        github (Optional[HttpUrl]): GitHub profile URL, must be a valid URL if provided.
    """

    name: str = Field(
        ..., example="John Doe", description="Full name of the individual."
    )
    address: str = Field(
        ...,
        example="123 Main St, Anytown, Anystate, 12345",
        description="Postal address, including street, city, state, and zip code.",
    )
    email: EmailStr = Field(
        ..., example="john.doe@example.com", description="Contact email address."
    )
    phone: str = Field(..., example="555-123-4567", description="Contact phone number.")
    linkedin: Optional[HttpUrl] = Field(
        None,
        example="https://linkedin.com/in/johndoe",
        description="LinkedIn profile URL.",
    )
    github: Optional[HttpUrl] = Field(
        None, example="https://github.com/johndoe", description="GitHub profile URL."
    )
