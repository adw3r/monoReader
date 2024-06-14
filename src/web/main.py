import logging

import uvicorn

from fastapi import FastAPI, BackgroundTasks
from src import main


app = FastAPI(name='api')


@app.get('/api/get_table_data')
async def get_table_data(days: int = 5, tasks: BackgroundTasks = BackgroundTasks()):
    tasks.add_task(main.main, days, logging.DEBUG)
    return 'Success {}'.format(days)


if __name__ == '__main__':
    uvicorn.run('src.web.main:app', host='0.0.0.0', port=8080, reload=True, reload_delay=0)
