import snowflake.connector
from utils.logging import logger
from config.settings import snowflake_settings


def get_snowflake_connection():
    try:
        conn = snowflake.connector.connect(
            user=snowflake_settings["user"],
            password=snowflake_settings["password"],
            account=snowflake_settings["account"],
            warehouse=snowflake_settings["warehouse"],
            database=snowflake_settings["database"],
            schema=snowflake_settings["schema"],
            role=snowflake_settings["role"],
        )
        logger.info("Successfully connected to Snowflake")
        return conn
    except Exception as e:
        logger.error(f"Failed to connect to Snowflake: {str(e)}")
        return None


def execute_query(conn, query):
    cursor = None
    try:
        cursor = conn.cursor()
        logger.info("Executing Snowflake query")
        cursor.execute(query)
        df = cursor.fetch_pandas_all()
        logger.info(f"Query executed successfully, retrieved {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Error executing query: {str(e)}")
        return None
    finally:
        if cursor is not None:
            cursor.close()
