from fastapi import FastAPI

app = FastAPI(title='FastAPI Task Automation')

@app.get('/')
def read_root():
    return {'message': 'FastAPI Task Automation is running!'}

