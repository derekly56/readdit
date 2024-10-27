from app.db.database import Database
from fastapi import APIRouter, Depends, Query, Request


def create_router(db: Database) -> APIRouter:
    pass
