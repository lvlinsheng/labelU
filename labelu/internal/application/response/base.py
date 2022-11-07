from typing import Union

from pydantic import BaseModel
from typing import Generic, TypeVar
from typing import Generic, TypeVar
from pydantic.generics import GenericModel

DataT = TypeVar("DataT", bound=BaseModel)


class MetaData(BaseModel):
    total: int
    page: int
    size: int


class OkResp(GenericModel, Generic[DataT]):
    data: DataT


class OkRespWithMeta(GenericModel, Generic[DataT]):
    meta_data: Union[MetaData, None] = None
    data: DataT