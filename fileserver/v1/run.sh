# cd app
python -m alembic revision --autogenerate -m "init"
python -m alembic upgrade head
# python -m uvicorn main:app --reload --port 9000 --host 0.0.0.0
python userve.py
