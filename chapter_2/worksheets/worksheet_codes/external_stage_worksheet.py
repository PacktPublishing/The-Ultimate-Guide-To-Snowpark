from snowflake.snowpark.functions import col

def main(session: snowpark.Session): 
    # Calling external stage file
    session.add_import("@my_stage/last_name_finder_stage.py.gz") 

    from last_name_finder_stage import last_name_finder
    
    # Your code goes here, inside the "main" handler.
    pandas_df = session.table("SAMPLE_EMPLOYEE_DATA").to_pandas()
    names = pandas_df["NAME"].to_list()
    pandas_df["LAST_NAME"] = last_name_finder(names)

    df = session.create_dataframe(pandas_df)

    # Return value will appear in the Results tab.
    return df