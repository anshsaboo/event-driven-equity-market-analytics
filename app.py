import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------
st.set_page_config(
    page_title="Earnings Surprise Analytics",
    page_icon="📈",
    layout="wide"
)

# -----------------------------------------
# LOAD DATA
# -----------------------------------------
df = pd.read_csv("powerbi_earnings_dashboard.csv")

# Convert Earnings Date safely
df["Earnings Date"] = pd.to_datetime(
    df["Earnings Date"],
    errors="coerce",
    format="mixed"
)

# Remove rows with invalid dates
df = df.dropna(subset=["Earnings Date"])
# -----------------------------------------
# SIDEBAR FILTERS
# -----------------------------------------

st.sidebar.header("Filters")

selected_category = st.sidebar.multiselect(
    "Surprise Category",
    options=df["Surprise_Category"].unique(),
    default=df["Surprise_Category"].unique()
)

selected_symbol = st.sidebar.multiselect(
    "Symbol",
    options=sorted(df["Symbol"].unique()),
    default=sorted(df["Symbol"].unique())
)

# Apply filters
df = df[
    (df["Surprise_Category"].isin(selected_category)) &
    (df["Symbol"].isin(selected_symbol))
]

search_symbol = st.sidebar.text_input(
    "Search Symbol"
)

if search_symbol:

    df = df[
        df["Symbol"].str.contains(
            search_symbol.upper(),
            case=False
        )
    ]

# -----------------------------------------
# TITLE
# -----------------------------------------
st.title("📈 Earnings Surprise Trading Analytics Dashboard")

st.markdown(
"""
Analyze the relationship between earnings surprises and stock returns,
along with trading performance and risk metrics.
"""
)

# -----------------------------------------
# TABS
# -----------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(
[
"Executive Summary",
"Earnings Analysis",
"Trading Strategy",
"Risk Analytics"
]
)

# =====================================================
# TAB 1
# =====================================================
with tab1:

    st.header("📈 Executive Summary")

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.metric(
            "Total Events",
            len(df)
        )

    with col2:
        st.metric(
            "Avg Surprise %",
            round(df["Surprise(%)"].mean(),2)
        )

    with col3:
        st.metric(
            "Avg 5D Return %",
            round(df["Return_5D_%"].mean(),2)
        )

    with col4:
        st.metric(
            "Best Trade %",
            round(df["Return_5D_%"].max(),2)
        )

    with col5:
        st.metric(
            "Worst Trade %",
            round(df["Return_5D_%"].min(),2)
        )

    avg_returns = pd.DataFrame(
    {
        "Holding Period":
        ["1 Day","5 Day","30 Day"],

        "Average Return":
        [
            df["Return_1D_%"].mean(),
            df["Return_5D_%"].mean(),
            df["Return_30D_%"].mean()
        ]
    })

    fig = px.bar(
        avg_returns,
        x="Holding Period",
        y="Average Return",
        text_auto=".2f",
        title="Average Returns Across Holding Periods"
    )

    st.plotly_chart(fig,use_container_width=True)

    # =====================================================
# TAB 2
# =====================================================
with tab2:

    st.header("📊 Earnings Analysis")

    col1,col2 = st.columns(2)

    with col1:

        fig = px.pie(
            df,
            names="Surprise_Category",
            hole=0.5,
            title="Distribution of Earnings Categories"
        )

        st.plotly_chart(fig,use_container_width=True)

    with col2:

        category_returns = df.groupby(
            "Surprise_Category"
        )["Return_5D_%"].mean().reset_index()

        fig = px.bar(
            category_returns,
            x="Surprise_Category",
            y="Return_5D_%",
            color="Surprise_Category",
            title="Average 5-Day Return by Category"
        )

        st.plotly_chart(fig,use_container_width=True)


    fig = px.scatter(
        df,
        x="Surprise(%)",
        y="Return_5D_%",
        color="Surprise_Category",
        hover_data=["Symbol"],
        title="Earnings Surprise vs 5-Day Return"
    )

    st.plotly_chart(fig,use_container_width=True)

    # =====================================================
# TAB 3
# =====================================================
with tab3:

    st.header("💹 Trading Strategy")

    col1,col2 = st.columns(2)

    with col1:

        top_surprises = df.nlargest(
            10,
            "Surprise(%)"
        )

        fig = px.bar(
            top_surprises,
            y="Symbol",
            x="Surprise(%)",
            orientation="h",
            title="Top 10 Earnings Surprises"
        )

        st.plotly_chart(fig,use_container_width=True)


    with col2:

        top_returns = df.nlargest(
            10,
            "Return_5D_%"
        )

        fig = px.bar(
            top_returns,
            y="Symbol",
            x="Return_5D_%",
            orientation="h",
            title="Top 10 Five-Day Returns"
        )

        st.plotly_chart(fig,use_container_width=True)


    fig = px.box(
        df,
        x="Surprise_Category",
        y="Return_5D_%",
        color="Surprise_Category",
        title="5-Day Return Distribution by Category"
    )

    st.plotly_chart(fig,use_container_width=True)

    # =====================================================
# TAB 4
# =====================================================
with tab4:

    st.header("⚠ Risk Analytics")

    # -------------------------------------------------
    # Risk Metrics
    # -------------------------------------------------

    returns = df["Return_5D_%"] / 100

    volatility = returns.std() * np.sqrt(252)
    sharpe_ratio = returns.mean()/returns.std()
    equity_curve = (1 + returns).cumprod()
    rolling_max = equity_curve.cummax()
    drawdown = (equity_curve - rolling_max)/rolling_max
    max_drawdown = drawdown.min()

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric(
            "Annualized Volatility",
            f"{volatility:.2%}"
        )

    with col2:
        st.metric(
            "Sharpe Ratio",
            round(sharpe_ratio,2)
        )

    with col3:
        st.metric(
            "Maximum Drawdown",
            f"{max_drawdown:.2%}"
        )

            # -------------------------------------------------
    # Heatmap
    # -------------------------------------------------

    st.subheader("Return Performance by Category")

    heatmap_df = df.groupby(
        "Surprise_Category"
    )[[
        "Return_1D_%",
        "Return_5D_%",
        "Return_30D_%"
    ]].mean()

    fig = px.imshow(
        heatmap_df,
        text_auto=".2f",
        color_continuous_scale="RdYlGn",
        aspect="auto"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

        # -------------------------------------------------
    # Histogram
    # -------------------------------------------------

    st.subheader("Distribution of 5-Day Returns")

    fig = px.histogram(
        df,
        x="Return_5D_%",
        nbins=30,
        color_discrete_sequence=["royalblue"]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

        # -------------------------------------------------
    # Risk vs Reward
    # -------------------------------------------------

    st.subheader("Short-Term vs Long-Term Performance")

    fig = px.scatter(
        df,
        x="Return_5D_%",
        y="Return_30D_%",
        size=abs(df["Surprise(%)"]),
        color="Surprise_Category",
        hover_data=["Symbol"]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

        # -------------------------------------------------
    # Treemap
    # -------------------------------------------------

    st.subheader("Average Returns by Category")

    tree_df = (
        df.groupby("Surprise_Category")
        ["Return_5D_%"]
        .mean()
        .reset_index()
    )

    fig = px.treemap(
        tree_df,
        path=["Surprise_Category"],
        values="Return_5D_%",
        color="Return_5D_%",
        color_continuous_scale="RdYlGn"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

        # -------------------------------------------------
    # Equity Curve
    # -------------------------------------------------

    st.subheader("Strategy Equity Curve")

    equity_df = pd.DataFrame({
        "Trade Number": range(len(equity_curve)),
        "Portfolio Value": equity_curve
    })

    fig = px.line(
        equity_df,
        x="Trade Number",
        y="Portfolio Value"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

        # -------------------------------------------------
    # Drawdown Curve
    # -------------------------------------------------

    st.subheader("Portfolio Drawdown")

    drawdown_df = pd.DataFrame({
        "Trade Number": range(len(drawdown)),
        "Drawdown": drawdown
    })

    fig = px.area(
        drawdown_df,
        x="Trade Number",
        y="Drawdown"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -------------------------------------------------
# Correlation Matrix
# -------------------------------------------------

st.subheader("Correlation Matrix")

corr = df[
[
"Surprise(%)",
"Return_1D_%",
"Return_5D_%",
"Return_30D_%"
]
].corr()

fig, ax = plt.subplots(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="RdYlGn",
    ax=ax
)

st.pyplot(fig)

# -------------------------------------------------
# Key Insights
# -------------------------------------------------

st.subheader("Key Insights")

st.markdown("""
- Strong Beat stocks generated the highest average returns.

- Positive earnings surprises generally produced better short-term performance.

- Strategy experienced moderate volatility and manageable drawdowns.

- Return distributions contained a few high-performing outliers.

- Risk-adjusted performance remained relatively stable across the sample.
""")

st.divider()
with st.expander("View Dataset"):
    st.dataframe(df)
    csv = df.to_csv(index=False)

st.download_button(
    label="Download Dataset",
    data=csv,
    file_name="earnings_data.csv",
    mime="text/csv"
)

st.divider()

st.caption(
"Developed by Ansh Saboo | Python • Streamlit • Plotly • Pandas"
)
