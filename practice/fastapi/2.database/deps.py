from services.todo_service import TodoService
from database import async_session


async def get_todo_service():
    async with async_session() as session:
        async with session.begin():
            yield TodoService(session)