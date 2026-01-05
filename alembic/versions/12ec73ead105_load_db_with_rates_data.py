"""Load DB with rates data

Revision ID: 12ec73ead105
Revises: d4ca94b2c2b6
Create Date: 2025-11-10 16:19:38.951978

"""

import json

import sqlalchemy as sa
from sqlalchemy.sql import column, table

from alembic import op

# revision identifiers, used by Alembic.
revision = "12ec73ead105"
down_revision = "d4ca94b2c2b6"
branch_labels = None
depends_on = None


def upgrade():
    # Load rates from rates.json
    with open("src/utils/rates.json", "r") as file:
        rates = json.load(file).get("rates", {})

    # Insert rates into currencies table
    currencies_table = table(
        "currencies",
        column("code", sa.String),
        column("name", sa.String),
        column("rate", sa.Float),
    )

    op.bulk_insert(
        currencies_table,
        [{"code": code, "name": "TBD", "rate": rate} for code, rate in rates.items()],
    )


def downgrade():
    op.execute("DELETE FROM currencies")
