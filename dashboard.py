import plotly.express as px

def generate_charts(df):
    charts = []

    numeric_cols = df.select_dtypes(include='number').columns
    categorical_cols = df.select_dtypes(include='object').columns
    date_cols = df.select_dtypes(include='datetime').columns

    # Histogram
    if len(numeric_cols) > 0:
        charts.append(px.histogram(df, x=numeric_cols[0], title=f"Distribution of {numeric_cols[0]}"))

    # Bar chart
    if len(categorical_cols) > 0 and len(numeric_cols) > 0:
        charts.append(px.bar(df, x=categorical_cols[0], y=numeric_cols[0],
                              title=f"{numeric_cols[0]} by {categorical_cols[0]}"))

    # Line chart
    if len(date_cols) > 0 and len(numeric_cols) > 0:
        charts.append(px.line(df, x=date_cols[0], y=numeric_cols[0],
                               title=f"{numeric_cols[0]} over time"))

    # Scatter plot
    if len(numeric_cols) >= 2:
        charts.append(px.scatter(df, x=numeric_cols[0], y=numeric_cols[1],
                                  title=f"{numeric_cols[0]} vs {numeric_cols[1]}"))

    return charts
