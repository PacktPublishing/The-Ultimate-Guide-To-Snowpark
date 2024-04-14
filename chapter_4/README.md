# Chapter 4 - Building Data Engineering Pipelines with Snowpark

This Chapter focuses on building data engineering pipelines. Data engineering pipelines are build using joins and unions methods served by Snowpark API. We have also introduced how same pipeline can be converted task graph and deployed. The chapter also covers how loggings and exception handling can be utilized to build robust data engineering pipelines and delineates the importance of trace events through telemetry package.

## Contents

The first section of chapter_4.ipynb notebook contains code snippets that covers following data engineering pipelines and exceution through stored procedures.

| File or Folder Name         |  Topics Covered                   |
| ----------------------------|  -------------------------------- |
| Chapter_4.ipynb (Data Engineering)   |<p>Data Preparation </p><p>Data Transformation</p><p> Data Cleanup </p> 
| Chapter_4.ipynb (Task & DAG)   |<p> Setting Up DAG </p><p> Converting pipeline logic as DAG task</p><p> Scheduling & Deploying </p> 
| Chapter_4.ipynb (Logging & Tracing )|  <p> Creating and Setting Up Event Table </p> <p> Setting Log Level </p>  <p> Logging and Exception Handling </p>  <p> Setting Up Event Traces </p> <p> Event Traces - Telemetry Packaage </p>
|
## Datasets

The dataset folder in the repository contains all required dataset files for this chapter

* [purchase_history.csv](../datasets/purchase_history.csv)
* [marketing_additional.csv](../datasets/marketing_additional.csv)
* [campaign_info.json](../datasets/campaign_info.json)
* [complain_info.parquet](../datasets/complain_info.parquet)



