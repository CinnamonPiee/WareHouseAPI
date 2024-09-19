from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import OrderCreate
from app.core.models.order import Order


async def create_order(session: AsyncSession, order_in: OrderCreate):
    order = Order(**order_in.model_dump())
    session.add(order)
    await session.commit()
    return order
