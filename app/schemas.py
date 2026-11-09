from pydantic import BaseModel, Field, field_validator
from typing import Literal
class InterviewRequest(BaseModel):
    area: str = Field(min_length=2, max_length=80)
    nivel: Literal['primeiro_emprego','estagio','transicao'] = 'primeiro_emprego'
    projeto: str | None = Field(default=None, max_length=800)
    @field_validator('area')
    @classmethod
    def strip_area(cls,v): return v.strip()
class FeedbackRequest(InterviewRequest):
    pergunta: str = Field(min_length=8, max_length=500)
    resposta: str = Field(min_length=10, max_length=2500)
class Source(BaseModel):
    id: str
    titulo: str
    score: float
class AIResponse(BaseModel):
    texto: str
    fontes: list[Source]
    aviso: str = 'Orientação educacional, não decisão de recrutamento.'
