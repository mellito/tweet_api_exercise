from typing import Optional,List
from uuid import UUID
from datetime import date,datetime

#pydantic
from pydantic import BaseModel,EmailStr,Field

#fastapi
from fastapi import FastAPI,status

app= FastAPI()

class UserBase(BaseModel):

    user_id: UUID=Field(...)
    email:EmailStr=Field(...) 


class UserLogin(UserBase):

    password: str= Field(
    ...,
    min_length=8,
    max_length=64
    )

class User(UserBase):
    
    first_name:str=Field(
        ...,
        min_length=1,
        max_length=50
        ),
    last_name:str=Field(
        ...,
        min_length=1,
        max_length=50
        ),
    birth_date:Optional[date]=Field(default=None)    
        
class Tweet(BaseModel):
    Tweet_id: UUID= Field(...)
    content: str =Field(
    ...,
    min_length=1,
    max_length=256
    )
    created_at:datetime = Field(default=datetime.now())
    updated_at:Optional[datetime]= Field(default=None)
    by: User = Field(...)


class tweet(BaseModel):
    pass

# path operation

@app.get(
    path="/"
    )
def home():
    return {"Twitter API":"working!"}

## users
@app.post(
    path="/signup", 
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["User"]
)
def singup():
    pass

@app.post(
    path="/Login", 
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["User"]
)
def login():
    pass

@app.get(
    path="/users", 
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all user",
    tags=["User"]
)
def show_all_user():
    pass

@app.get(
    path="/users/{user_id}", 
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="show a user",
    tags=["User"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete", 
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["User"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update", 
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="update a user",
    tags=["User"]
)
def update_a_user():
    pass


## tweets

