#!/bin/bash

docker build --rm --platform linux/amd64 -t <orgname>-<acctname>.registry.snowflakecomputing.com/snowpark_definitive_guide/my_schema/snowpark_cs_repository/my_filter_service_image:latest . 

docker login <registry_hostname> -u <username> 

docker push <orgname>-<acctname>.registry.snowflakecomputing.com/snowpark_definitive_guide/my_schema/snowpark_cs_repository/my_filter_service_image:latest