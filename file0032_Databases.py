# The Alembic Config object.
config = context.config

# Configure Alembic to use our DATABASE_URL and our table definitions...
import app
config.set_main_option('sqlalchemy.url', str(app.DATABASE_URL))
target_metadata = app.metadata

...

def upgrade():
    op.create_table(
      'notes',
      sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
      sqlalchemy.Column("text", sqlalchemy.String),
      sqlalchemy.Column("completed", sqlalchemy.Boolean),
    )

def downgrade():
    op.drop_table('notes')


from alembic import command
from alembic.config import Config
import app

...

@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    url = str(app.DATABASE_URL)
    engine = create_engine(url)
    assert not database_exists(url), 'Test database already exists. Aborting tests.'
    create_database(url)             # Create the test database.
    config = Config("alembic.ini")   # Run the migrations.
    command.upgrade(config, "head")
    yield                            # Run the tests.
    drop_database(url)               # Drop the test database.
