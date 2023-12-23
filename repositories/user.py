from sqlalchemy.orm import Session
from models.models import User
from schemas.auth import UserRegisterSchema
from utils.hashing import Hash
from datetime import datetime


def create(db: Session, userSchema: UserRegisterSchema):
    user = User(name = userSchema.name, fname = userSchema.fname, email = userSchema.email, password = Hash.bcrypt(userSchema.password), role = 'User', createdAt = datetime.now(),is_admi =False)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    return user