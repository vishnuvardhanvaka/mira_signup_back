from asyncio import run
from fastapi import Depends, FastAPI, HTTPException, status,Form,Response,Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passlib.context import CryptContext
# from database import Database
# from security import *
# from sendMail import Mail

import uvicorn
from fastapi import FastAPI

connection_url='mongodb+srv://vishnu:vishnu1$@babycare.7pgjopj.mongodb.net/?retryWrites=true&w=majority' #os.environ.get('MONGO_CONNECTION_URL')
# print(connection_url)
client=MongoClient(connection_url)
#print('Client connection successful !')
database=client.babycare
login_collection=database.logins
user_collection=database.userdata
print('Successfully connected to the database !')

# db=Database()
# # mail=Mail()

# ACCESS_TOKEN_EXPIRE_MINUTES=40
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost:3000",
#     "http://localhost:3000/",
#     "http://192.168.0.128:3000/",
#     "https://miraparentpal.com",
#     "https://www.miraparentpal.com",
#     'https://miraparentpal.vercel.app'
# ]

# app=FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # db={
# #     'vishnu@gmail.com':{
# #         'username':'vishnu',
# #         'full_name':'vishnu vardhan gowd',
# #         'email':'vishnu@gmail.com',
# #         'password':'$2b$12$1wWBGtrpd.I97eZYVyjG4ukcQTaszhV3Azmz4S5MGXo2ZJfqSxClm',
# #         'disabled':False,
# #         'invalid_entries':0
# #     }
# # }
# class FormData(BaseModel):
#     username:str = Form(...)
#     email:str = Form(...)
#     password:str = Form(...)

# class Token(BaseModel):
#     access_token:str
#     email:str
#     username:str
# class TokenData(BaseModel):
#     email:str or None = None

# class User(BaseModel):
#     username:str
#     email:str or None=None
#     full_name:str or None=None
#     disabled:bool or None=None
#     invalid_entries:int or None=None
# class UserInDB(User):
#     password:str


# @app.post('/auth/signup/')
# async def signup(request : Request):
    
#     payload = await request.form()
#     payload=dict(payload)
#     payload['password']=get_password_hash(payload['password'])
#     user_details=payload
#     # user_details={
#     #     'username':username,
#     #     'email':email,
#     #     'password':get_password_hash(password)
#     # }
#     state=db.insert_user(user_details)
#     return state
# @app.post('/sendOTP/')
# async def getOTP(request:Request,username:str = Form(...),email:str = Form(...)):
#     user=db.get_user(email)
#     if user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail='User already exists. ',
#             headers={'WWW-Authenticate':'Bearer'}
#         )
#     mail=Mail()
#     otp,msg=mail.sendOTP(username,email)
#     print(otp,msg)
#     if otp==None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail=f'{msg}',
#             headers={'WWW-Authenticate':'Bearer'}
#         )
#     return otp
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


