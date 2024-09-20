from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models import db_helper
from . import crud


async def order_by_id(
    order_item_in: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    order = await crud.get_order_item(session=session, order_item_in=order_item_in)
    if order is not None:
        return order

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Order {order_item_in} not found!",
    )
