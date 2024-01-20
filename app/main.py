# app/main.py

from fastapi import FastAPI, HTTPException
from webdriver.login import MyWebDriver

app = FastAPI()


@app.post("/login")
def user_login(username: str, password: str):
    web_driver = MyWebDriver()

    if not web_driver.login(username, password):
        web_driver.close()
        raise HTTPException(status_code=400, detail="Login failed")

    # Fetch additional data as needed
    # ...

    # web_driver.close()
    return {"message": "Login successful"}
