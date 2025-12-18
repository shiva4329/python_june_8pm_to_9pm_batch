from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
async def root():
    return{'Message':"Welcome to first app"}
@app.get("/hello")
async def main():
    return{'Message':"Welcome hello"}



if __name__ == "__main__":
   uvicorn.run("APIs:app", host="127.0.0.1", port=8000, reload=True)