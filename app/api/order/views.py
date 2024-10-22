from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import db_helper
from .crud import delete_order_item, get_orders_items, update_order_status, create_order_item
from .schemas import Order, OrderItemCreate, OrderStatusUpdate
from .depencies import order_by_id


router = APIRouter(
    tags=["Orders"],
)


@router.post("/order_create/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(
        order_in: OrderItemCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return create_order(session=session, order_in=order_in)


@router.get("/get_orders/", response_model=list[Order])
async def get_order(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return get_orders_items(session=session)


@router.get("/get_order/{order_id}", response_model=Order)
async def get_order(order: Order = Depends(order_by_id)):
    return order


@router.patch("/update_order_status/{order_id}/status")
async def update_order_status(
        order_update: OrderStatusUpdate,
        order: Order = Depends(order_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_order_status(
        session=session,
        order=order,
        order_update=order_update,
    )


@router.delete("/delete_order/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
        order: Order = Depends(order_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    return await delete_order(session=session, order=order)
