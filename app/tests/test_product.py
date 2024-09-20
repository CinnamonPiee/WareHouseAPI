import pytest

@pytest.mark.asyncio
async def test_create_product(async_client):
    response = await async_client.post("/products/", json={"name": "Product 1", "description": "A test product", "price": 10.5, "stock": 100})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Product 1"
    assert data["description"] == "A test product"
    assert data["price"] == 10.5
    assert data["stock"] == 100

@pytest.mark.asyncio
async def test_get_products(async_client):
    response = await async_client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

@pytest.mark.asyncio
async def test_get_product_by_id(async_client):
    response = await async_client.get("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

@pytest.mark.asyncio
async def test_update_product(async_client):
    response = await async_client.put("/products/1", json={"name": "Updated Product", "description": "Updated description", "price": 12.5, "stock": 150})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Product"
    assert data["description"] == "Updated description"
    assert data["price"] == 12.5
    assert data["stock"] == 150

@pytest.mark.asyncio
async def test_delete_product(async_client):
    response = await async_client.delete("/products/1")
    assert response.status_code == 200
