from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


DEMO_USER = {
    "email": "zakriyawahid@gmail.com",
    "password": "123456"
}


def authenticate_user(email: str, password: str):

    if (
        email == DEMO_USER["email"]
        and password == DEMO_USER["password"]
    ):
        return True

    return False