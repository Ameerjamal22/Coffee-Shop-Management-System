from app.schemas.CategorySchemas import CategoryPost, CategoryGet
from app.config.dbConfig import db
from app.models.Category import Category
from fastapi import HTTPException, status


@db.atomic()
def category_name_exist(category: CategoryPost) -> bool:
    """
    checks if the category name already exist in the database .
    Args:
        category (CategoryPost): category input that name will be checked .
    Returns (bool): true if the name exist already false if not .
    """
    category_exists: bool = Category.select().where(Category.name == category.name).exists()
    return category_exists


@db.atomic()
def create_category_helper(category: CategoryPost) -> CategoryGet:
    """
    creates category and insert it into the database .
    ARGS:
        category(CategoryPost): input category data (pydantic model object) .
    """
    category_exists: bool = category_name_exist(category)

    if category_exists:
        raise HTTPException(detail="category name already exist, failed to create category object",
                            status_code=status.HTTP_409_CONFLICT)

    category: dict = category.model_dump()
    new_category: Category = Category(**category)
    new_category.save()

    return CategoryGet.from_orm(new_category)


@db.atomic()
def get_categories_helper(offset: int, limit: int) -> list[CategoryGet]:
    """
    get categories from database .
    Args:
        offset(int): number of categories to skip .
        limit(int): number of categories to return .
    Returns:
        list[CategoryGet]: list of categories returned as pydantic models .
    """
    categories = list(Category.select().limit(limit).offset(offset))
    categories = [CategoryGet.from_orm(category) for category in categories]
    return categories


@db.atomic()
def category_id_exist(category_id: int) -> bool:
    """
    checks if the category id exist in the database or not .
    ARGS:
        category_id(int): category id to be checked .
    Returns:
        (bool): true if the category id exist in the database . false otherwise .
    """
    exists: bool = Category.select().where(Category.category_id == category_id).exists()

    if exists:
        return True

    return False


@db.atomic()
def get_category_helper(category_id: int) -> CategoryGet:
    """
    get category from database using its id .
    Args:
        category_id: the id of the category to bring from database .
    Returns:
        (CategoryGet): category get pydantic model for the category with the passed id .
    """
    id_exists = category_id_exist(category_id)

    if not id_exists:
        raise HTTPException(detail="there is not category with the passed id check the id",
                            status_code=status.HTTP_404_NOT_FOUND)

    category = CategoryGet.from_orm(Category.select().where(Category.category_id == category_id).get())
    return category


@db.atomic()
def update_category_helper(category_id: int, category: CategoryPost) -> CategoryGet:
    """
    Updates a category in the database.
    Args:
        category_id (int): The ID of the category to update.
        category (CategoryPost): The new data for the category (Pydantic model object).
    Returns:
        CategoryGet: Updated category data as a Pydantic model.
    """
    if not category_id_exist(category_id):
        raise HTTPException(detail="There is no category with the passed ID, check the ID",
                            status_code=status.HTTP_404_NOT_FOUND)

    category_data: dict = category.model_dump()
    query = Category.update(category_data).where(Category.category_id == category_id)
    query.execute()

    updated_category = CategoryGet.from_orm(Category.select().where(Category.category_id == category_id).get())
    return updated_category


@db.atomic()
def delete_category_helper(category_id: int) -> None:
    """
    Deletes a category from the database.
    Args:
        category_id (int): The ID of the category to delete.
    """
    if not category_id_exist(category_id):
        raise HTTPException(detail="There is no category with the passed ID, check the ID",
                            status_code=status.HTTP_404_NOT_FOUND)

    query = Category.delete().where(Category.category_id == category_id)
    query.execute()
