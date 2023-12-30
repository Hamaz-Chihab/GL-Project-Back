from pydantic import BaseModel
from fastapi import UploadFile, File
from typing import Annotated

class LoginSchema(BaseModel):
    email: str
    password: str

class UserRegisterSchema(BaseModel):
    email: str
    password: str | None = None
    nom: str
    prenom: str

class AvocatRegisterSchema(UserRegisterSchema):
    address: str
    phoneNumber: str
    facebookUrl: str
    Wilaya :str
    description: str
    categories: list[str] = []

class CreateAvocatSchema(BaseModel):
    address: str
    phoneNumber: str
    facebookUrl: str
    Wilaya :str
    description: str
    categories: list[str] = []
    userId: int
    imageUrl: str