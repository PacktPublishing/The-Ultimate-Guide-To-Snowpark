#!/opt/conda/bin/python3

import argparse
import logging
import os
import sys

from snowflake.snowpark import Session
from snowflake.snowpark.functions import month, to_date, date_part
from snowflake.snowpark.exceptions import *
import json

# Environment variables below will be automatically populated by Snowflake.
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_HOST = os.getenv("SNOWFLAKE_HOST")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")

# Custom environment variables
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ROLE = os.getenv("SNOWFLAKE_ROLE")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")


def get_arg_parser():
    """
    Input argument list.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--table", required=True, help="Table to Operate")
    parser.add_argument("--date_column", required=True, help="Date Column")
    return parser


def get_logger():
    """
    Get a logger for local logging.
    """
    logger = logging.getLogger("job-tutorial")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_login_token():
    """
    Read the login token supplied automatically by Snowflake. These tokens
    are short lived and should always be read right before creating any new connection.
    """
    with open("/snowflake/session/token", "r") as f:
        return f.read()


def get_connection_params():
    """
    Construct Snowflake connection params from environment variables.
    """
    if os.path.exists("/snowflake/session/token"):
        return {
            "account": SNOWFLAKE_ACCOUNT,
            "host": SNOWFLAKE_HOST,
            "authenticator": "oauth",
            "token": get_login_token(),
            "warehouse": "COMPUTE_WH",
            "database": SNOWFLAKE_DATABASE,
            "schema": SNOWFLAKE_SCHEMA
        }
    else:
        return {
            "account": SNOWFLAKE_ACCOUNT,
            "host": SNOWFLAKE_HOST,
            "user": SNOWFLAKE_USER,
            "password": SNOWFLAKE_PASSWORD,
            "role": SNOWFLAKE_ROLE,
            "warehouse": "COMPUTE_WH",
            "database": SNOWFLAKE_DATABASE,
            "schema": SNOWFLAKE_SCHEMA
        }


def run_job():
    """
    Main body of this job.
    """
    logger = get_logger()
    logger.info("Job started")

    # Parse input arguments
    args = get_arg_parser().parse_args()
    table = args.table
    column = args.date_column


    # Start a Snowflake session, run the query and write results to specified table
    with Session.builder.configs(get_connection_params()).create() as session:
        # Print out current session context information.
        database = session.get_current_database()
        schema = session.get_current_schema()
        warehouse = session.get_current_warehouse()
        role = session.get_current_role()
        logger.info(
            f"Connection succeeded. Current session context: database={database}, schema={schema}, warehouse={warehouse}, role={role}"
        )

        # Execute query and persist results in a table.
        df_table = session.table(table)
        df_table = df_table.with_column("month", month(column))
        df_table = df_table.with_column("date", to_date(column))
        df_table = df_table.with_column("year", date_part("year", df_table[column]))
        # If the table already exists, the query result must match the table scheme.
        # If the table does not exist, this will create a new table.
        df_table.write.mode("overwrite").save_as_table(table)

    logger.info("Job finished")




if __name__ == "__main__":
    run_job()

