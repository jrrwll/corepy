from abc import ABC

from pydantic import BaseModel
from sqlmodel import SQLModel, Session, func, select

from .api import PageResult


class DaoService(ABC):

    def get_required_entity[E: SQLModel](self, session: Session,
            entity_type: type[E], entity_id: int | str) -> E:
        entity: E = session.get(entity_type, entity_id)
        if not entity or entity.deleted:
            raise Exception(f"{entity_type} {entity_id} not found")
        return entity

    def delete_entity[E: SQLModel](self, session: Session,
            entity_type: type[E], entity_id: int | str) -> None:
        entity = self.get_required_entity(session, entity_type, entity_id)
        update_dict = {
            'deleted': True,
        }
        entity.sqlmodel_update(update_dict)
        session.add(entity)
        session.commit()

    # #### #### #### ####    #### #### #### ####    #### #### #### ####

    def page_entities_as_model[E: SQLModel, M: BaseModel](
            self, session: Session, entity_type: type[E],
            page_no: int, page_size: int, model_type: type[M]
    ) -> PageResult[M]:
        entities, count = self.page_entities(session, entity_type, page_no,
                                             page_size)
        return PageResult(
            page_no=page_no,
            page_size=page_size,
            total=count,
            items=[model_type(**i.model_dump()) for i in entities],
        )

    def page_entities[E: SQLModel](
            self, session: Session, entity_type: type[E],
            page_no: int, page_size: int
    ) -> tuple[list[E], int]:
        conditions = [
            entity_type.deleted == False,
        ]
        count_statement = (
            select(func.count()).select_from(entity_type).where(*conditions)
        )
        count = session.exec(count_statement).one()

        offset = (page_no - 1) * page_size
        limit = page_size
        page_statement = (
            select(entity_type)
            .where(*conditions)
            .order_by(entity_type.updated_at.desc())
            .offset(offset)
            .limit(limit)
        )
        entities = session.exec(page_statement).all()
        return entities, count

    def create_entity[E: SQLModel](
            self, session: Session,
            entity_type: type[E], params: BaseModel) -> E:
        entity = entity_type(**params.model_dump())
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def update_entity(self, session: Session,
            entity: SQLModel, params: BaseModel) -> None:
        update_dict = params.model_dump(exclude=set('id'))
        entity.sqlmodel_update(update_dict)
        session.add(entity)
        session.commit()
        session.refresh(entity)
