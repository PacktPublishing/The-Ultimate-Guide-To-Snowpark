1. docker build --rm --platform linux/amd64 -t tzplfmd-ww72981.registry.snowflakecomputing.com/snowpark/tutorial/snowpark_ml/test_service:latest .
2. docker login tzplfmd-ww72981.registry.snowflakecomputing.com -u admin
3. docker push tzplfmd-ww72981.registry.snowflakecomputing.com/snowpark/tutorial/snowpark_ml/test_service:latest


4. USE ROLE ACCOUNTADMIN;

CREATE ROLE container_service_role;


GRANT OWNERSHIP ON DATABASE SNOWPARK TO ROLE container_service_role COPY CURRENT GRANTS;


GRANT USAGE ON WAREHOUSE compute_wh TO ROLE container_service_role;

CREATE SECURITY INTEGRATION IF NOT EXISTS snowservices_ingress_oauth
  TYPE=oauth
  OAUTH_CLIENT=snowservices_ingress
  ENABLED=true;

GRANT BIND SERVICE ENDPOINT ON ACCOUNT TO ROLE container_service_role;

CREATE COMPUTE POOL tutorial_compute_pool
  MIN_NODES = 1
  MAX_NODES = 1
  INSTANCE_FAMILY = CPU_X64_XS;
GRANT USAGE, MONITOR ON COMPUTE POOL tutorial_compute_pool TO ROLE container_service_role;

GRANT ROLE container_service_role TO USER admin;

