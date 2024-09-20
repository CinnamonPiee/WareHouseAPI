import pytest


@pytest.mark.asyncio
async def test_create_order(async_client):
    response = await async_client.post("/orders/", json={"status": "in_progress"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "in_progress"

@pytest.mark.asyncio
async def test_get_orders(async_client):
    response = await async_client.get("/orders/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

@pytest.mark.asyncio
async def test_get_order_by_id(async_client):
    response = await async_client.get("/orders/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

@pytest.mark.asyncio
async def test_update_order_status(async_client):
    response = await async_client.patch("/orders/1/status", json={"status": "sent"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "sent"

@pytest.mark.asyncio
async def test_delete_order(async_client):
    response = await async_client.delete("/orders/1")
    assert response.status_code == 200
