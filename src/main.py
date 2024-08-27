import uvicorn
from src.api.router import all_routers
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.db import Base, engine



@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.drop_all(engine)
    print('База очищена!')

    Base.metadata.create_all(engine)
    print('База готовa к работе!')

    yield
    print('Завершение...')



app = FastAPI(
    title='Упрощенный аналог Jira',
    lifespan=lifespan
)


for router in all_routers:
    app.include_router(router)



if __name__ == '__main__':
    uvicorn.run('src.main:app', reload=True)
