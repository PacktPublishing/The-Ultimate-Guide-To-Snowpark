# The Ultimate Guide to Snowpark

<a href="https://www.packtpub.com/product/the-ultimate-guide-to-snowpark/9781805123415"><img src="https://content.packt.com/_/image/original/B19923/cover_image_large.jpg" alt="no-image" height="256px" align="right"></a>

This is the code repository for [The Ultimate Guide to Snowpark](https://www.packtpub.com/product/the-ultimate-guide-to-snowpark/9781805123415), published by Packt.

**Design and deploy Snowpark with Python for efficient data workloads**

## What is this book about?
This book will guide you through the fundamental and advanced features of the Snowpark framework in Python. You’ll learn how to use Snowpark for implementing workloads in the fields of data engineering, data science, and data applications.

This book covers the following exciting features:
* Harness Snowpark with Python for diverse workloads
* Develop robust data pipelines with Snowpark using Python
* Deploy mature machine learning models
* Explore the process of developing, deploying, and monetizing native apps using Snowpark
* Deploy and operate containers in Snowpark
* Discover the pathway to adopting Snowpark effectively in production

If you feel this book is for you, get your [copy](https://www.amazon.com/Ultimate-Guide-Snowpark-efficient-workloads/dp/1805123416/ref=sr_1_1?crid=2P5IRN21SZ7E0&dib=eyJ2IjoiMSJ9.R9aZEw_8-XtikjJxrzVrrQ.mxgeyvNls8B-eQjNvCRaFeXtuzrrZ4q3xeIjESmMo_k&dib_tag=se&keywords=The+Ultimate+Guide+to+Snowpark&qid=1716612889&sprefix=the+ultimate+guide+to+snowpark%2Caps%2C548&sr=8-1) today!
<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>
## Instructions and Navigations
All of the code is organized into folders. For example, Chapter04.

The code will look like the following:
```
current_runs = dag_op.get_current_dag_runs(dag)
for r in current_runs:
    print(f"RunId={r.run_id} State={r.state}")

```

**Following is what you need for this book:**
This book is for data engineers, data scientists, developers, and data practitioners seeking an in-depth understanding of Snowpark’s features and best practices for deploying various workloads in Snowpark using the Python programming language. Basic knowledge of SQL, proficiency in Python, an understanding of data engineering and data science basics, and familiarity with the Snowflake Data Cloud platform are required to get the most out of this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-8).
## Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-8 | Snowflake| Windows, macOS, or Linux(Any) |
| 1-8 | Python | Windows, macOS, or Linux(Any) |
| 1-8 | Visual Studio Code | Windows, macOS, or Linux(Any) |
| 1-8 | Chrome or another latest Browser | |

## Contents

This Repository has the codes and datasets used in the book. It is organized chapter-wise, along with the respective notebooks, featuring all the code used in the book. The dataset holds all datasets used in the book for demonstrative purposes.

| Chapter Name                                      | Folder Name  | Notebooks                        |
| --------------------------------------------------| -------------| -------------------------------- |
| Establishing Foundation with Snowpark             | chapter_2    | chapter_2.ipynb                  |
| Simplifying Data Processing Through Snowpark      | chapter_3    | <p> chapter_3_data_load.ipynb </p> <p> chapter_3_explore_transform.ipynb </p>  <p> chapter_3_agg_analysis.ipynb </p>  | 
| Building Data Engineering Pipelines with Snowpark | chapter_4    | chapter_4.ipynb                  |
| Developing Data Science Projects with Snowpark | chapter_5    | chapter_5.ipynb                  |
| Deploying and Managing ML Models with Snowpark | chapter_6    | <p> chapter_6_model_register_deployment.ipynb     </p>    <p> chapter_6_feature_store.ipynb     </p>          |
| Developing Native Application With Snowpark | chapter_7 | <p> chapter_7.sql </p> <p> streamlit_bike_share_analysis.py </p> |
| Introduction To Snowpark Container Services | chapter_8 | chapter_8.ipynb </p> |

## Related products
* Data Modeling with Snowflake [[Packt]](https://www.packtpub.com/product/data-modeling-with-snowflake/9781837634453) [[Amazon]](https://www.amazon.com/Data-Modeling-Snowflake-accelerating-development/dp/1837634459/ref=sr_1_1?crid=3SIPQOY91EQWO&dib=eyJ2IjoiMSJ9.LRe44vcV9Q5OMI02Um0D_rJ6HstFPlhO6XSXiAmhb8BspMQrzh6gBC23kv3kWdx9SFiMT5HfOja4DS8eZMN8ad0wDKPirQ5dzJH49csC3SY7eCpEKn8VbdG1dUOTveC3DjQhLnqSVlQQ0i5riQtl32nlaFEYNJRH2B19XHJDj0td7jUdwf7yyfsBTk5kSbUUM84n6vDKwxNaER-cC18RKt-HS6nqQS_1WNsIClgLPIQ.OQVDD_DY0AdR2vr5uZCJyBa3_17zoXZWdz1MWfkDupE&dib_tag=se&keywords=Data+Modeling+with+Snowflake&qid=1716614007&sprefix=data+modeling+with+snowflake%2Caps%2C563&sr=8-1)

* Data Engineering with dbt [[Packt]](https://www.packtpub.com/product/data-engineering-with-dbt/9781803246284) [[Amazon]](https://www.amazon.com/Data-Engineering-dbt-cloud-based-dependable/dp/1803246286/ref=sr_1_1?crid=1F0LHDFCCBRJL&dib=eyJ2IjoiMSJ9.ymZC7by8vDEUpw0oRZFLQcyStOmg01OBTbtPF9R5ZVWT-ALxqYzswC4EWfERwbmCn8V9K97eUyJMOgB_PhAl_ABqumD-DmiN4SWMbwV_UojbjbBYN0w0iudf1dSKR4DRnqRNButCDHh2kg56xzGhD1poW9v9mUIgpbMfbg4OVvkNhdswDBRF1XIk5NfGyqtl1tDl73gvA4aKL5AoJOmJLPagw2vtd4l_2NGs-LYg5uA.freQ1IXBYj9w1QnYBfimu5lTB9bfytnUsT44pGHhgJg&dib_tag=se&keywords=Data+Engineering+with+dbt&qid=1716614036&sprefix=data+engineering+with+dbt%2Caps%2C424&sr=8-1)

## Get to Know the Author
**Shankar Narayanan SGS**
is a Technical Architect with over a decade of diverse experience leading and delivering large-scale Data and Cloud implementations for Fortune 500 companies across various industries. He has successfully implemented Snowflake Data Cloud for many organizations leading the customers to adopt Snowflake.
He holds a bachelor's and master&rsquo;s degree in Computer science and holds many certifications in multi-cloud platforms and Snowflake. He is an award-winning blogger and actively contributes to various technical publications and open-source projects.
For his technical contribution to the community, He has been selected as SAP Community Topic leader by SAP and is selected as one of the 72 Snowflake Data Heroes by Snowflake.

**Vivekanandan SS**
 spearheads the GenAI enablement team at Verizon, leveraging over a decade of expertise in Data Science and Big Data. His professional journey spans across building analytics solutions and products across diverse domains, and proficient in cloud analytics and data warehouses.
He holds a bachelor's degree in Industrial engineering from Anna University, a long distance program in Big Data analytics from IIM, Bangalore, and a master's in Data Science from Eastern University. As a seasoned trainer, he imparts his knowledge, specializing in Snowflake and GenAI, also a data science guest faculty and advisor for various educational institutes. His solution is ranked in the top 1 percentile in Kaggle Kernels globally.

