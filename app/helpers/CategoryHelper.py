from app.schemas.CategorySchemas import CategoryPost
from app.config.dbConfig import db
from app.models.Category import Category
from fastapi import HTTPException, status


@db.atomic()
def create_category_helper(category: CategoryPost):
    """
    creates category and insert it into the database .
    ARGS:
        category(CategoryPost): input category data (pydantic model object) .
    """
    category_exists: bool = Category.select().where(Category.name == category.name).exists()

    if category_exists:
        raise HTTPException(detail="category name already exist, failed to create category object",
                            status_code=status.HTTP_409_CONFLICT)

    category: dict = category.model_dump()
    new_category: Category = Category(**category)
    new_category.save()
