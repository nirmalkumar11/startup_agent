from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class StartupProfile(BaseModel):
    idea: str
    target_users: Optional[str] = None
    business_model: Optional[str] = None
    market: Optional[str] = None
    budget: Optional[float] = None
    timeline: Optional[str] = None
    team_size: Optional[int] = None
    country: Optional[str] = None
    problem_statement: Optional[str] = None
    technical_requirements: List[str] = Field(default_factory=list)
    missing_fields: List[str] = Field(default_factory=list)


class ResearchContext(BaseModel):
    market_size: Optional[str] = None
    competitors: List[str] = Field(default_factory=list)
    pricing_models: List[str] = Field(default_factory=list)
    tech_stack: List[str] = Field(default_factory=list)
    industry_trends: List[str] = Field(default_factory=list)
    sources: List[str] = Field(default_factory=list)


class SpecialistOutput(BaseModel):
    score: int
    confidence: int
    strengths: List[str]
    weaknesses: List[str]
    risks: List[str]
    assumptions: List[str]
    reasoning: str


class FinalVerdict(BaseModel):
    viability_score: int
    verdict: str
    confidence: int
    strengths: List[str]
    weaknesses: List[str]
    major_risks: List[str]
    recommendation: str