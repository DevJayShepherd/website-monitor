from datetime import datetime

from core.hashing import Hasher
from db.models.users import Users
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    user = Users(username=user.username,
                email=user.email,
                hashed_password=Hasher.get_password_hashed(user.password),
                alerts_active=False,
                date_joined=datetime.now())

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
