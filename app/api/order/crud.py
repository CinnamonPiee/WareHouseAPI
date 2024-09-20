from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import OrderStatusUpdate, OrderItemCreate
from app.core.models.order import Order, OrderItem


async def create_order_item(session: AsyncSession, order_item_in: OrderItemCreate):
    order = OrderItem(**order_item_in.model_dump())
    session.add(order)
    await session.commit()
    return order


async def get_orders_items(session: AsyncSession) -> list[OrderItem]:
    stmt = select(OrderItem).order_by(OrderItem.id)
    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)


async def get_order_item(session: AsyncSession, order_item_in: int) -> OrderItem | None:
    return await session.get(OrderItem, order_item_in)


async def update_order_status(
        session: AsyncSession,
        order: Order,
        order_update: OrderStatusUpdate,
) -> Order:
    for name, value in order_update.model_dump().items():
        setattr(order, name, value)
    await session.commit()
    return order


async def delete_order_item(session: AsyncSession, order_item: OrderItem) -> None:
    await session.delete(order_item)
    await session.commit()
