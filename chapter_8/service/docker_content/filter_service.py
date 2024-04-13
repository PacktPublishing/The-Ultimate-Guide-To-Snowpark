import json

from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from snowflake.snowpark import Session
import logging
import os
import sys

SERVICE_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
SERVICE_PORT = os.getenv('SERVER_PORT', 8080)
CHARACTER_NAME = os.getenv('CHARACTER_NAME', 'I')



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


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(
        logging.Formatter(
            '%(name)s [%(asctime)s] [%(levelname)s] %(message)s'))
    logger.addHandler(handler)
    return logger


logger = get_logger('filter-service')

app = Flask(__name__)


@app.get("/healthcheck")
def readiness_probe():
    return "I'm ready!"


@app.post("/filter")
def udf_calling_function():
    message = request.json
    logger.debug(f'Received request: {message}')

    if message is None or not message['data']:
        logger.info('Received empty message')
        return {}

    unique_id = message['data']
    try:
        with Session.builder.configs(get_connection_params()).create() as session:
            database = session.get_current_database()
            schema = session.get_current_schema()
            warehouse = session.get_current_warehouse()
            logger.info(warehouse)
            role = session.get_current_role()
            logger.info(
                f"Connection succeeded. Current session context: database={database}, schema={schema}, warehouse={warehouse}, role={role}"
            )

            # Execute query and persist results in a table.
            df_table = session.table("NEWS_CATEGORY")

            df_table = df_table.filter(df_table["UNIQUE_ID"] == int(unique_id[0][1]))
            data = df_table.to_pandas()
            data = data.to_json(orient="records")
            data = json.loads(data)
            logger.info(data)
            return make_response({"data": [[0, data]]})
    except Exception as e:
        logger.error(e)
        return json.dumps({"data": []})


@app.route("/ui", methods=["GET", "POST"])
def ui():
    '''
    Main handler for providing a web UI.
    '''
    if request.method == "POST":
        # getting input in HTML form
        input_text = request.form.get("input")
        # display input and output
        return render_template("basic_ui.html",
            echo_input=input_text,
            echo_reponse=get_filter_response(input_text))
    return render_template("basic_ui.html")



def get_filter_response(input_text):
    with Session.builder.configs(get_connection_params()).create() as session:
        database = session.get_current_database()
        schema = session.get_current_schema()
        warehouse = session.get_current_warehouse()
        logger.info(warehouse)
        role = session.get_current_role()
        logger.info(
            f"Connection succeeded. Current session context: database={database}, schema={schema}, warehouse={warehouse}, role={role}"
        )

        # Execute query and persist results in a table.
        df_table = session.table("NEWS_CATEGORY")

        df_table = df_table.filter(df_table["UNIQUE_ID"] == int(input_text))
        data = df_table.to_pandas()
        data = data.to_json(orient="records")

    return data  # Assuming the result is a JSON string


if __name__ == '__main__':
    app.run(host=SERVICE_HOST, port=SERVICE_PORT)
