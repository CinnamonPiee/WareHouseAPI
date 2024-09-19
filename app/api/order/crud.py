from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import OrderCreate, OrderStatusUpdate, OrderItemCreate, OrderItemBase
from app.core.models.order import Order, OrderItem


# CRUD для заказов
async def create_order(session: AsyncSession, order_in: OrderCreate):
    order = Order(**order_in.model_dump())
    session.add(order)
    await session.commit()
    return order


async def get_orders(session: AsyncSession) -> list[Order]:
    stmt = select(Order).order_by(Order.id)
    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)


async def get_order(session: AsyncSession, order_id: int) -> Order | None:
    return await session.get(Order, order_id)


async def update_order_status(
        session: AsyncSession,
        order: Order,
        order_update: OrderStatusUpdate,
) -> Order:
    for name, value in order_update.model_dump().items():
        setattr(order, name, value)
    await session.commit()
    return order


async def delete_order(session: AsyncSession, order: Order) -> None:
    await session.delete(order)
    await session.commit()


# CRUD для элементов заказа
async def create_order_item(session: AsyncSession, order_in: OrderItemCreate):
    order_item = OrderItem(**order_in.model_dump())
    session.add(order_item)
    await session.commit()
    return order_item


async def get_order_items(session: AsyncSession) -> list[OrderItem]:
    stmt = select(OrderItem).order_by(OrderItemBase.id)
    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)


async def delete_order_item(session: AsyncSession, order_item: OrderItem) -> None:
    await session.delete(order_item)
    await session.commit()
