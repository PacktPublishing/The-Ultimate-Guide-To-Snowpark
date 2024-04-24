-- The command may change as we are in private preview
-- Command 1
EXECUTE SERVICE IN COMPUTE POOL snowpark_cs_compute_pool FROM @snowpark_cs_stage SPEC='my_job_spec.yaml'; 


-- Alternate Command
EXECUTE JOB SERVICE
  IN COMPUTE POOL snowpark_cs_compute_pool
  NAME = test_job
  FROM @SNOWPARK_CS_STAGE
  SPECIFICATION_FILE='my_job_spec.yaml';
