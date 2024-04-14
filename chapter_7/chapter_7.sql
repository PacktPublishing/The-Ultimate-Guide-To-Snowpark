-- Create & Use Application Package
GRANT CREATE APPLICATION PACKAGE ON ACCOUNT TO ROLE accountadmin; 

CREATE APPLICATION PACKAGE snowflake_native_apps_package;

SHOW APPLICATION PACKAGES;

USE APPLICATION PACKAGE snowflake_native_apps_package;


-- Create Schema & Stage
CREATE SCHEMA MY_SCHEMA; 

CREATE OR REPLACE STAGE snowflake_native_apps_package.my_schema.my_stage FILE_FORMAT = (TYPE = 'csv' FIELD_DELIMITER = '|' SKIP_HEADER = 1); 

CREATE APPLICATION ROLE app_public;

LIST @snowflake_native_apps_package.MY_SCHEMA.my_stage;


-- Create Application Package
CREATE APPLICATION bike_share_native_app FROM APPLICATION PACKAGE snowflake_native_apps_package USING '@snowflake_native_apps_package.my_schema.my_stage'; 


-- CREATE VIEW ON BIKE SHARE DEMAND TABLE

CREATE SCHEMA IF NOT EXISTS shared_data;

GRANT REFERENCE_USAGE ON DATABASE snowpark_definitive_guide
  TO SHARE IN APPLICATION PACKAGE snowflake_native_apps_package;


CREATE VIEW snowflake_native_apps_package.shared_data.BSD_TRAIN
  AS SELECT *
  FROM snowpark_definitive_guide.my_schema.BSD_TRAIN;

GRANT USAGE ON SCHEMA snowflake_native_apps_package.shared_data
  TO SHARE IN APPLICATION PACKAGE snowflake_native_apps_package;

GRANT SELECT ON VIEW snowflake_native_apps_package.shared_data.BSD_TRAIN
  TO SHARE IN APPLICATION PACKAGE snowflake_native_apps_package;










