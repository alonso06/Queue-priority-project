from typing import Sequence, Type, Generic, TypeVar
from sqlmodel import Session, select


T = TypeVar("T") # Model
P = TypeVar("P") # Schema
E = TypeVar("E") # Entity

# TODO: falta implementar manejo de errores
class BaseRepository( Generic[T, P, E] ):
    
    def __init__(self, 
                 db: Session, 
                 model: Type[T],
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
        query = select(self.model).where(self.model.id == id) # type: ignore
        obj_model = self.db.exec(query).one()
        obj_schema = self.schema_pd.model_validate(obj_model) # type: ignore
        return self.entity_class(**obj_schema.model_dump())
    
    # obj_data es un entidad validad con su schema en el caso de uso
    def create(self, 
               obj_data: E,
        ) -> E :
        self.db.add(obj_data)
        self.db.commit()
        self.db.refresh(obj_data)
        return obj_data
        
    
    def update(self, 
               id: str, 
               updated_data: E,
               
        ) -> E:
        
        obj_data = self.get_by_id(id)
        
        for key, value in updated_data.dict(exclude_unset=True).items(): # type: ignore
            if hasattr(obj_data, key):
                setattr(obj_data,key, value)
        
        self.db.add(obj_data)
        self.db.commit()
        self.db.refresh(obj_data)        
        return obj_data
        
    def unsubscribe(self,
                    id: str
        ) -> None:  
        obj_data = self.get_by_id(id)
        try:
            obj_data.state = False # type: ignore
            self.db.add(obj_data)
            self.db.commit()
            self.db.refresh(obj_data)
        
        except Exception as err:    
            self.db.rollback()
            print(f'Error-backend: {err}')
        
    def delete(self, 
               id: str) -> dict[str, bool]:
        obj_data = self.get_by_id(id)
        self.db.delete(obj_data)
        self.db.commit()
        
        return {"ok": True}
        
        
        