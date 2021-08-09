from passlib.context import CryptoContext
from starlette import schemas

pwd_context = CryptoContext(schemas=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hashed(plain_password):
        return pwd_context.hash(plain_password)

