-- Setup script for the Bike Share Streamlit application.

CREATE APPLICATION ROLE app_public;

CREATE OR ALTER VERSIONED SCHEMA code_schema;
GRANT USAGE ON SCHEMA code_schema TO APPLICATION ROLE app_public;

CREATE STREAMLIT code_schema.bike_share_streamlit
  FROM '/streamlit'
  MAIN_FILE = '/streamlit_bike_share_analysis.py';

GRANT USAGE ON STREAMLIT code_schema.bike_share_streamlit TO APPLICATION ROLE app_public;