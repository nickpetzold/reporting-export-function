from app import app, db
from app.models import Report, Result


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Report': Report, 'Result': Result}
