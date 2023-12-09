from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    """base class"""

    name: str
    email: EmailStr
    account_id: int

    # custom validation
    @field_validator("account_id")
    def validate_account_id(cls, value):
        """validate account_id"""
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value


# creating an instance of the class
# HelloWorld - 1
user_1 = User(name="Hello World 1", email="helloworld_1@email.com", account_id=1234)

print(user_1.name)
print(user_1.email)
print(user_1.account_id)

print("\n")

# HelloWorld - 2
user_data = {
    "name": "Hello World 2",
    "email": "helloworld_2@email.com",
    "account_id": 1235,
}
user_2 = User(**user_data)

print(user_2.name)
print(user_2.email)
print(user_2.account_id)

print("\n")

# HelloWorld - 3
# invalid email validation - inbuild validation
# user_3 = User(name="Hello World 3", email="test", account_id=1245)

print("\n")

# HelloWorld - 4
# invalid account_id validation - custom validation
# user_4 = User(name="Hello World 4", email="helloworld_4@email.com", account_id=-1234)

print("\n")

# HelloWorld - 5
# working with json
user_1_json_str = user_1.model_dump_json()
print(user_1_json_str)

print("\n")

# HelloWorld - 6
# working with python dictionary
user_1_json_obj = user_1.model_dump()
print(user_1_json_obj)

print("\n")

# HelloWorld - 7
# convert a json str to object
json_str = '{"name":"Hello World 1","email":"helloworld_1@email.com","account_id":1234}'
user = User.model_validate_json(json_str)
print(user)

print("\n")
