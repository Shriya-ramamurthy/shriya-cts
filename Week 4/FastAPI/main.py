from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="Week 4 API",
    description="FastAPI CRUD API with Pydantic and Auto-Generated OpenAPI Docs",
    version="1.0.0"
)

# In-memory database simulation
items_db = {}

# --- Pydantic Models ---
class ItemBase(BaseModel):
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, Eggs, Bread")

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True


# --- Endpoints ---
@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(item: ItemCreate):
    item_id = len(items_db) + 1
    new_item = ItemResponse(id=item_id, **item.dict())
    items_db[item_id] = new_item
    return new_item

@app.get("/items/", response_model=List[ItemResponse], tags=["Items"])
def read_items():
    return list(items_db.values())

@app.get("/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]
