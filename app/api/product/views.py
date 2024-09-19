from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from .crud import delete_product, get_products, update_product, create_products
from app.core.models import db_helper
from .schemas import Product, ProductCreate, ProductUpdate, PartialUpdateProduct
from .depencies import product_by_id


router = APIRouter(
    tags=["Products"],
)


@router.post("/create/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
        product_in: ProductCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await create_products(session=session, product_in=product_in)


@router.get("/get_products/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return get_products(session=session)


@router.get("/get_product/{product_id}", response_model=Product)
async def get_product(product: Product = Depends(product_by_id)):
    return product


@router.put("/update_product/{product_id}")
async def update_product(
        product_update: ProductUpdate,
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.patch("/update_product/{product_id}")
async def update_product_partial(
    product_update: PartialUpdateProduct,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )


@router.delete("/delete_product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    return await delete_product(session=session, product=product)

