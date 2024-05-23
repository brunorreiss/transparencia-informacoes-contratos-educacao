from enum import Enum
from pydantic import BaseModel
from typing import Optional, List, Union


class Orgao(str, Enum):
    tipo_1 = 'FUNDACAO DE CIENCIA, TECNOLOGIA E INOVACAO DE FORTALEZA'
    tipo_2 = 'FUNDO MUNICIPAL DE CULTURA'
    tipo_3 = 'SECRETARIA MUNICIPAL DA CULTURA DE FORTALEZA'
    tipo_4 = 'FUNDO MUNICIPAL DE EDUCACAO'
    tipo_5 = 'FUNDO MUNICIPAL DE EDUCACAO - INFRAESTRUTURA'
    tipo_6 = 'SECRETARIA MUNICIPAL DA EDUCACAO'


class ResponseSite(BaseModel):
    ID: Optional[Union[int, str]] = ''
    ANOCONTRATO: Optional[Union[int, str]] = ''
    NUMEROCONTRATOSISTEMA: Optional[Union[int, str]] = ''
    NUMEROCONTRATOINSTITUICAO: Optional[Union[int, str]] = ''
    CONTRATADO: Optional[Union[int, str]] = ''
    OBJETOCONTRATO: Optional[Union[int, str]] = ''
    IDUO: Optional[Union[int, str]] = ''
    DESCRICAOUO: Optional[Union[int, str]] = ''
    VALORCONTRATO: Optional[float] = 0.0
    IDCONTRATO: Optional[Union[int, str]] = ''
    ANEXOS: Optional[Union[int, str]] = ''
    QTDADITIVOS: Optional[Union[int, str]] = ''
    CODIGOCOMPLETOUO: Optional[Union[int, str]] = ''
    MODALIDADEPROCESSO: Optional[Union[int, str]] = ''
    MODALIDADEAPLICACAO: Optional[Union[int, str]] = ''
    IDCONTRATOORIGEM: Optional[Union[int, str]] = ''

class ResponseDefault(BaseModel):
    code: int
    message: str
    datetime: str
    results: List[ResponseSite]

class ResponseError(BaseModel):
    code: int
    message: str