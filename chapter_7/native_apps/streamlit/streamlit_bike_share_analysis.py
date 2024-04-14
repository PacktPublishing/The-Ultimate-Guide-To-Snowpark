####### Import Global Packages 
from snowflake.snowpark.context import get_active_session
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
from scipy import stats
import pandas as pd
from snowflake.snowpark.functions import count, col
from snowflake.snowpark.functions import hour, month, to_date, dayofweek, date_part, mean, stddev, abs
from snowflake.ml.modeling.model_selection import GridSearchCV
from snowflake.ml.modeling.linear_model import LinearRegression, Ridge, Lasso
from snowflake.ml.modeling.ensemble import RandomForestRegressor, GradientBoostingRegressor
from snowflake.ml.modeling.metrics import mean_squared_error, explained_variance_score, mean_absolute_error, \
                mean_absolute_percentage_error, d2_absolute_error_score, d2_pinball_score

###### Set page config
st.set_page_config(layout="wide")

###### Get current session
session = get_active_session()

@st.cache_data()
def load_data():
    # Load Bike Share data
    snow_df = session.table("SNOWFLAKE_NATIVE_APPS_PACKAGE.shared_data.BSD_TRAIN")
    return snow_df.to_pandas()

dataframe = load_data()

def dataset():
    st.subheader("About Dataset")
    st.markdown("""
        ### Overview
        Bike sharing systems are a means of renting bicycles where the process of obtaining membership, rental, and bike return is automated via a network of kiosk locations throughout a city. Using these systems, people are able rent a bike from a one location and return it to a different place on an as-needed basis. Currently, there are over 500 bike-sharing programs around the world.
    """)
    st.markdown("""
        ### Data Fields
        - datetime - hourly date + timestamp
        - season - 1 = spring, 2 = summer, 3 = fall, 4 = winter
        - holiday - whether the day is considered a holiday
        - workingday - whether the day is neither a weekend nor holiday
        - weather -
            - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
            - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
            - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
            - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
        - temp - temperature in Celsius
        - atemp - "feels like" temperature in Celsius
        - humidity - relative humidity
        - windspeed - wind speed
        - casual - number of non-registered user rentals initiated
        - registered - number of registered user rentals initiated
        - count - number of total rentals (Dependent Variable)
    """)
    st.subheader("Sample Data")
    st.dataframe(dataframe.head(n=50))


def display_shape(dataframe):
    st.markdown(""" #### Shape of the data""")
    col1, col2 = st.columns(2)
    number_of_rows = dataframe.count()
    number_of_columns = len(dataframe.columns)
    col1.metric("Rows", number_of_rows)
    col2.metric("Columns", number_of_columns)


def display_data_type_with_count(dataframe):
    st.markdown(""" #### Variable Type Count""")
    data_type_df = pd.DataFrame(dataframe.dtypes.value_counts()).reset_index().rename(
        columns={"index": "variableType", 0: "count"})
    st.bar_chart(data_type_df, x="variableType", y="count")


def display_count_of_columns(dataframe):
    st.markdown(""" #### Data Count for each columns""")
    null_df = dataframe.count().reset_index().rename(columns={"index": "columns", 0: "count"})
    st.dataframe(null_df)
    st.bar_chart(null_df, x="columns", y="count")


def display_outlier_analysis(dataframe):
    st.markdown(""" #### Outlier Analysis""")
    fig, axes = plt.subplots(nrows=2, ncols=2)
    fig.set_size_inches(12, 10)
    sn.boxplot(data=dataframe, y="COUNT", orient="v", ax=axes[0][0])
    sn.boxplot(data=dataframe, y="COUNT", x="SEASON", orient="v", ax=axes[0][1])
    sn.boxplot(data=dataframe, y="COUNT", x="HOUR", orient="v", ax=axes[1][0])
    sn.boxplot(data=dataframe, y="COUNT", x="WORKINGDAY", orient="v", ax=axes[1][1])
    axes[0][0].set(ylabel='Count', title="Box Plot On Count")
    axes[0][1].set(xlabel='Season', ylabel='Count', title="Box Plot On Count Across Season")
    axes[1][0].set(xlabel='Hour Of The Day', ylabel='Count', title="Box Plot On Count Across Hour Of The Day")
    axes[1][1].set(xlabel='Working Day', ylabel='Count', title="Box Plot On Count Across Working Day")
    st.pyplot(fig=fig)


def display_correlation_analysis(dataframe):
    st.markdown(""" #### Correlation Analysis""")
    dataframe = dataframe.drop(columns=["DATETIME"])
    corr_matt = dataframe[["TEMP", "ATEMP", "CASUAL", "REGISTERED", "HUMIDITY", "WINDSPEED", "COUNT"]].corr()
    mask = np.array(corr_matt)
    mask[np.tril_indices_from(mask)] = False
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 10)
    sn.heatmap(corr_matt, mask=mask, vmax=.8, square=True, annot=True)
    st.pyplot(fig=fig)
    fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)
    fig.set_size_inches(12, 5)
    sn.regplot(x="TEMP", y="COUNT", data=dataframe, ax=ax1)
    sn.regplot(x="WINDSPEED", y="COUNT", data=dataframe, ax=ax2)
    sn.regplot(x="HUMIDITY", y="COUNT", data=dataframe, ax=ax3)
    st.pyplot(fig=fig)


def display_data_distribution(dataframe):
    st.markdown(""" #### Data Distribution""")
    fig, axes = plt.subplots(ncols=2, nrows=2)
    fig.set_size_inches(12, 10)
    sn.distplot(dataframe["COUNT"], ax=axes[0][0])
    stats.probplot(dataframe["COUNT"], dist='norm', fit=True, plot=axes[0][1])
    sn.distplot(np.log(dataframe["COUNT"]), ax=axes[1][0])
    stats.probplot(np.log1p(dataframe["COUNT"]), dist='norm', fit=True, plot=axes[1][1])
    st.pyplot(fig=fig)


def display_time_period_analysis(dataframe):
    st.markdown(""" #### Data over a period of time""")
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4)
    fig.set_size_inches(12, 20)
    month_aggregated = pd.DataFrame(dataframe.groupby("MONTH")["COUNT"].mean()).reset_index()
    month_sorted = month_aggregated.sort_values(by="COUNT", ascending=False)
    sn.barplot(data=month_sorted, x="MONTH", y="COUNT", ax=ax1)
    ax1.set(xlabel='Month', ylabel='Avearage Count', title="Average Count By Month")
    hour_aggregated = pd.DataFrame(dataframe.groupby(["HOUR", "SEASON"], sort=True)["COUNT"].mean()).reset_index()
    sn.pointplot(x=hour_aggregated["HOUR"], y=hour_aggregated["COUNT"], hue=hour_aggregated["SEASON"], data=hour_aggregated,
                 join=True, ax=ax2)
    ax2.set(xlabel='Hour Of The Day', ylabel='Users Count',
            title="Average Users Count By Hour Of The Day Across Season", label='big')
    hour_aggregated = pd.DataFrame(dataframe.groupby(["HOUR", "WEEKDAY"], sort=True)["COUNT"].mean()).reset_index()
    sn.pointplot(x=hour_aggregated["HOUR"], y=hour_aggregated["COUNT"], hue=hour_aggregated["WEEKDAY"],
                 data=hour_aggregated, join=True, ax=ax3)
    ax3.set(xlabel='Hour Of The Day', ylabel='Users Count',
            title="Average Users Count By Hour Of The Day Across Weekdays", label='big')
    hour_transformed = pd.melt(dataframe[["HOUR", "CASUAL", "REGISTERED"]], id_vars=['HOUR'],
                              value_vars=['CASUAL', 'REGISTERED'])
    hour_aggregated = pd.DataFrame(
        hour_transformed.groupby(["HOUR", "variable"], sort=True)["value"].mean()).reset_index()
    sn.pointplot(x=hour_aggregated["HOUR"], y=hour_aggregated["value"], hue=hour_aggregated["variable"],
                 hue_order=["CASUAL", "REGISTERED"], data=hour_aggregated, join=True, ax=ax4)
    ax4.set(xlabel='Hour Of The Day', ylabel='Users Count',
            title="Average Users Count By Hour Of The Day Across User Type", label='big')
    st.pyplot(fig=fig)


def eda():
    st.subheader('Exploratory Data Analysis')
    dataframe = session.table("SNOWFLAKE_NATIVE_APPS_PACKAGE.shared_data.BSD_TRAIN")
    pandas_df = dataframe.to_pandas()
    display_shape(dataframe)
    display_data_type_with_count(pandas_df)
    display_count_of_columns(pandas_df)
    display_correlation_analysis(pandas_df)
    display_data_distribution(pandas_df)


def remove_outliers(dataframe):
    mean_value = dataframe.select(mean("count")).collect()[0][0]
    std_value = dataframe.select(stddev("count")).collect()[0][0]
    dataframe = dataframe.filter((abs(dataframe["count"] - mean_value)) < (3 * std_value))
    return dataframe


def fill_windspeed(dataframe):
    wind_speed_mean = dataframe.select(mean("windspeed")).collect()[0][0]
    dataframe = dataframe.replace({0: wind_speed_mean}, subset=["windspeed"])
    return dataframe


def perform_feature_engineering(operation_list):
    dataframe = session.table("SNOWFLAKE_NATIVE_APPS_PACKAGE.shared_data.BSD_TRAIN")
    for operation in operation_list:
        if operation == "Extract Hour":
            dataframe = dataframe.with_column("hour", hour("DATETIME"))
        elif operation == "Extract Month":
            dataframe = dataframe.with_column("month", month("DATETIME"))
        elif operation == "Extract Date":
            dataframe = dataframe.with_column("date", to_date("DATETIME"))
        elif operation == "Extract Week Day":
            dataframe = dataframe.with_column("weekday", dayofweek("DATETIME"))
        elif operation == "Extract Year":
            dataframe = dataframe.with_column("year", date_part("year", dataframe["DATETIME"]))
        elif operation == "Remove Outliers":
            dataframe = remove_outliers(dataframe)
        elif operation == "Fill Zero Wind Speed":
            dataframe = fill_windspeed(dataframe)
    return dataframe
    #dataframe.write.mode("overwrite").save_as_table("SNOWFLAKE_NATIVE_APPS_PACKAGE.shared_data.BSD_TRAIN_OUTPUT")


def feature_engineering():
    st.subheader("Feature Engineering")
    st.markdown(""" All Feature Engineering Steps Should Be Carried Out- To Run Model""")
    st.markdown(""" #### Date Operations""")
    col1, col2, col3 = st.columns(3)
    with col1:
        hour = st.checkbox('Extract Hour')
    with col2:
        month = st.checkbox('Extract Month')
    with col3:
        date = st.checkbox('Extract Date')
    col4, col5, col6 = st.columns(3)
    with col4:
        week_day = st.checkbox('Extract Week Day')
    with col5:
        year = st.checkbox('Extract Year')
    st.markdown(""" #### Outliers""")
    outliers = st.checkbox('Remove Outliers')
    st.markdown(""" #### Wind Speed""")
    windspeed = st.checkbox('Fill Zero Wind Speed')

    def click_button():
        operation_list = []
        if hour:
            operation_list.append("Extract Hour")
        if month:
            operation_list.append("Extract Month")
        if date:
            operation_list.append("Extract Date")
        if week_day:
            operation_list.append("Extract Week Day")
        if year:
            operation_list.append("Extract Year")
        if outliers:
            operation_list.append("Remove Outliers")
        if windspeed:
            operation_list.append("Fill Zero Wind Speed")
        df_feature = perform_feature_engineering(operation_list)
        st.success("Feature Engineering completed and data is ready")
        st.subheader("Data After Feature Engineering")
        st.dataframe(df_feature.to_pandas().head(n=50))

    st.button("Apply", type="primary", on_click=click_button)


# Display header
st.header("Bike Ride Share")

# Create sidebar and load the first page
page_names_to_funcs = {
    "About Dataset": dataset,
    "Feature Engineering": feature_engineering,
    "EDA": eda
}
selected_page = st.sidebar.selectbox("Select", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()