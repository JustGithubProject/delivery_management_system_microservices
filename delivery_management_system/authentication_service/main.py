from fastapi import FastAPI


authentication_app = FastAPI()


@authentication_app.get("/auth/")
async def auth_test():
    return {"status_code": 200}


