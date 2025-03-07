# mypy: disable-error-code="attr-defined"
from datetime import datetime
from typing import Sequence, Type, Generic, TypeVar
from fastapi import HTTPException
from sqlmodel import Session, select

M = TypeVar("M") # Model
P = TypeVar("P") # Schema
E = TypeVar("E") # Entity

# TODO: falta implementar manejo de errores
class BaseRepository( Generic[M, P, E] ):
    
    def __init__(self, 
                 db: Session, 
                 model: Type[M],
                 schema_pd: Type[P],
                 entity_class: Type[E]
        ):
        self.db = db
        self.model = model
        self.schema_pd = schema_pd
        self.entity_class = entity_class
    
    # Retorna lista de objetos
    def list(self) -> Sequence[E]:
        
        list_obj_models = self.db.exec(select(self.model)).all()
        return [self.entity_class(**self.schema_pd.model_validate(obj_model).model_dump()) for obj_model in list_obj_models] # type: ignore
        
    def get_by_id(self,
                  id: str,
        ) -> E:
        obj_model = self.db.get(self.model, id)
        obj_schema = self.schema_pd.model_validate(obj_model) 
        return self.entity_class(**obj_schema.model_dump())
    
    # obj_data es un modelo, validado con su schema en el caso de uso
    def create(self, 
               obj_data: M,
        ) -> E :
        self.db.add(obj_data)
        self.db.commit()
        self.db.refresh(obj_data)
        return self.entity_class(**obj_data.model_dump())
    
    def update(self, 
               id: str, 
               updated_data: M,
               
        ) -> E:
        
        obj_model:M|None = self.db.get(self.model, id)
        if not obj_model:
            raise HTTPException(status_code=404, detail="Hero not found")
        
        obj_data:dict = updated_data.model_dump(exclude_unset=True) # type: ignore
        obj_model.sqlmodel_update(obj_data) # type: ignore
        
        self.db.add(obj_model)
        self.db.commit()
        self.db.refresh(obj_model)        
        return self.entity_class(**obj_model.model_dump()) # type: ignore
    
    # *Importante: updated_date se actualiza en: db y backend  
    def unsubscribe(self,
                    id: str
        ) -> None:  
        obj_model:M|None = self.db.get(self.model, id)
        try:

            obj_model.updated_date = datetime.now() # type: ignore
            obj_model.state = False # type: ignore
            self.db.add(obj_model)
            self.db.commit()
            self.db.refresh(obj_model)
        
        except Exception as err:    
            self.db.rollback()
            print(f'Error-backend: {err}')
        
    def delete(self, 
               id: str) -> dict[str, bool]:
        
        obj_model:M|None = self.db.get(self.model, id)
        self.db.delete(obj_model)
        self.db.commit()
        
        return {"ok": True}
        
        
        