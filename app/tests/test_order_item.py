import pytest


@pytest.mark.asyncio
async def test_create_order_item(async_client):
    response = await async_client.post("/order_items/", json={"order_id": 1, "product_id": 1, "quantity": 10})
    assert response.status_code == 200
    data = response.json()
    assert data["order_id"] == 1
    assert data["product_id"] == 1
    assert data["quantity"] == 10

@pytest.mark.asyncio
async def test_get_order_items(async_client):
    response = await async_client.get("/orders/1/items")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

@pytest.mark.asyncio
async def test_delete_order_item(async_client):
    response = await async_client.delete("/order_items/1")
    assert response.status_code == 200
