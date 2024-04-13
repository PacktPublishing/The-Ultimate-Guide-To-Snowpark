GRANT ROLE test_role TO USER [user_name];
USE ROLE test_role;
CREATE SERVICE filter_service
  IN COMPUTE POOL snowpark_cs_compute_pool
  FROM SPECIFICATION $$
    spec:
      containers:
      - name: filter
        image: /snowpark_definitive_guide/my_schema/snowpark_cs_repository/my_filter_service_image:latest
        env:
          SERVER_PORT: 8000
        readinessProbe:
          port: 8000
          path: /healthcheck
      endpoints:
      - name: filterendpoint
        port: 8000
        public: true
      $$
   MIN_INSTANCES=1
   MAX_INSTANCES=1;

