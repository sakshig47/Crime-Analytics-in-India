import pandas as pd
from database.database import engine


# KPI QUERIES


def total_crimes():
    query = "SELECT COUNT(*) AS total_crimes FROM crime_data;"
    return pd.read_sql(query, engine).iloc[0, 0]


def total_cities():
    query = "SELECT COUNT(DISTINCT city) AS total_cities FROM crime_data;"
    return pd.read_sql(query, engine).iloc[0, 0]


def total_crime_types():
    query = """
    SELECT COUNT(DISTINCT crime_description) AS total_crime_types
    FROM crime_data;
    """
    return pd.read_sql(query, engine).iloc[0, 0]


def average_victim_age():
    query = """
    SELECT ROUND(AVG(victim_age),2) AS average_age
    FROM crime_data;
    """
    return pd.read_sql(query, engine).iloc[0, 0]


def average_police_deployed():
    query = """
    SELECT ROUND(AVG(police_deployed),2) AS avg_police
    FROM crime_data;
    """
    return pd.read_sql(query, engine).iloc[0, 0]


def closure_rate():
    query = """
    SELECT
    ROUND(
    SUM(CASE WHEN case_closed='Yes' THEN 1 ELSE 0 END)
    *100.0/COUNT(*),2) AS closure_rate
    FROM crime_data;
    """
    return pd.read_sql(query, engine).iloc[0, 0]


def average_days_to_close():
    query = """
    SELECT
    ROUND(
    AVG(DATEDIFF(date_case_closed,date_reported)),2
    ) AS avg_days_to_close
    FROM crime_data
    WHERE case_closed='Yes';
    """
    return pd.read_sql(query, engine).iloc[0, 0]



# CHART DATA


def cases_closed_open():
    query = """
    SELECT
        case_closed,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY case_closed;
    """
    return pd.read_sql(query, engine)


def crimes_by_city():
    query = """
    SELECT
        city,
        COUNT(*) AS total_crimes
    FROM crime_data
    GROUP BY city
    ORDER BY total_crimes DESC;
    """
    return pd.read_sql(query, engine)


def top_crime_types():
    query = """
    SELECT
        crime_description,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY crime_description
    ORDER BY total_cases DESC
    LIMIT 10;
    """
    return pd.read_sql(query, engine)


def crime_domain_distribution():
    query = """
    SELECT
        crime_domain,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY crime_domain
    ORDER BY total_cases DESC;
    """
    return pd.read_sql(query, engine)


def victims_by_gender():
    query = """
    SELECT
        victim_gender,
        COUNT(*) AS total_victims
    FROM crime_data
    GROUP BY victim_gender;
    """
    return pd.read_sql(query, engine)


def victims_by_age_group():
    query = """
    SELECT
        age_group,
        COUNT(*) AS total_victims
    FROM crime_data
    GROUP BY age_group
    ORDER BY total_victims DESC;
    """
    return pd.read_sql(query, engine)


def weapon_usage():
    query = """
    SELECT
        weapon_used,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY weapon_used
    ORDER BY total_cases DESC;
    """
    return pd.read_sql(query, engine)


def crimes_by_month():
    query = """
    SELECT
        MONTH(date_of_occurrence) AS month,
        MONTHNAME(date_of_occurrence) AS month_name,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY MONTH(date_of_occurrence),MONTHNAME(date_of_occurrence)
    ORDER BY MONTH(date_of_occurrence);
    """
    return pd.read_sql(query, engine)


def crimes_by_year():
    query = """
    SELECT
        YEAR(date_of_occurrence) AS year,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY year
    ORDER BY year;
    """
    return pd.read_sql(query, engine)


def crimes_by_day():
    query = """
    SELECT
        DAYNAME(date_of_occurrence) AS day_name,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY day_name;
    """
    return pd.read_sql(query, engine)


def crimes_by_hour():
    query = """
    SELECT
        HOUR(time_of_occurrence) AS hour,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY hour
    ORDER BY hour;
    """
    return pd.read_sql(query, engine)


def police_deployment():
    query = """
    SELECT
        police_deployed,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY police_deployed
    ORDER BY police_deployed;
    """
    return pd.read_sql(query, engine)


def closed_cases_city():
    query = """
    SELECT
        city,
        COUNT(*) AS closed_cases
    FROM crime_data
    WHERE case_closed='Yes'
    GROUP BY city
    ORDER BY closed_cases DESC;
    """
    return pd.read_sql(query, engine)


def open_cases_city():
    query = """
    SELECT
        city,
        COUNT(*) AS open_cases
    FROM crime_data
    WHERE case_closed='No'
    GROUP BY city
    ORDER BY open_cases DESC;
    """
    return pd.read_sql(query, engine)


def monthly_crime_trend():
    query = """
    SELECT
        DATE_FORMAT(date_of_occurrence,'%%Y-%%m') AS month,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY DATE_FORMAT(date_of_occurrence,'%%Y-%%m')
    ORDER BY DATE_FORMAT(date_of_occurrence,'%%Y-%%m');
    """
    return pd.read_sql(query, engine)


def crime_domain_city():
    query = """
    SELECT
        city,
        crime_domain,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY city,crime_domain
    ORDER BY city,total_cases DESC;
    """
    return pd.read_sql(query, engine)


def crime_gender():
    query = """
    SELECT
        victim_gender,
        crime_description,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY victim_gender,crime_description
    ORDER BY victim_gender,total_cases DESC;
    """
    return pd.read_sql(query, engine)


def crime_age_group():
    query = """
    SELECT
        age_group,
        crime_description,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY age_group,crime_description
    ORDER BY age_group,total_cases DESC;
    """
    return pd.read_sql(query, engine)


def dangerous_hour():
    query = """
    SELECT
        HOUR(time_of_occurrence) AS hour,
        COUNT(*) AS crimes
    FROM crime_data
    GROUP BY hour
    ORDER BY crimes DESC
    LIMIT 1;
    """
    return pd.read_sql(query, engine)


def dangerous_day():
    query = """
    SELECT
        DAYNAME(date_of_occurrence) AS day,
        COUNT(*) AS crimes
    FROM crime_data
    GROUP BY day
    ORDER BY crimes DESC
    LIMIT 1;
    """
    return pd.read_sql(query, engine)


def dangerous_city():
    query = """
    SELECT
        city,
        COUNT(*) AS total_crimes
    FROM crime_data
    GROUP BY city
    ORDER BY total_crimes DESC
    LIMIT 10;
    """
    return pd.read_sql(query, engine)


def crime_heatmap():
    query = """
    SELECT
        city,
        HOUR(time_of_occurrence) AS hour,
        COUNT(*) AS total_cases
    FROM crime_data
    GROUP BY city,hour
    ORDER BY city,hour;
    """
    return pd.read_sql(query, engine)