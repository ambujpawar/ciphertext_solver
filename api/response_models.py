"""
Response models for the API
"""
from pydantic import BaseModel, validator
from pydantic.schema import Optional


class CipherText(BaseModel):
    """
    The ciphertext to be solved.
    """

    ciphertext: str

    @validator("ciphertext")
    def convert_to_lowercase(cls, v):
        """
        Convert the input ciphertext to lowercase.
        """
        return v.lower()


class Plaintext(BaseModel):
    """
    The plaintext solution.
    """

    plaintext: str

    @validator("plaintext")
    def convert_to_lowercase(cls, v):
        """
        Convert the input plaintext to lowercase.
        """
        return v.lower()


class CipherResponse(BaseModel):
    """
    The response from the API.
    """

    ciphertext: str
    plaintext: Optional[str]
    mapping: Optional[dict]
