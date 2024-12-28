import plotly.graph_objects as go


def create_similarity_visualization(data, categories_col, x_col, y_col1, y_col2):
    """
    Create a dual-axis dynamic visualization for similarity scores and PRI counts.
    
    Args:
        data (pd.DataFrame): Filtered data for visualization.
        categories_col (str): Column name for categories.
        x_col (str): Column name for x-axis (e.g., site names).
        y_col1 (str): Column name for first y-axis data.
        y_col2 (str): Column name for second y-axis data.
    """
    categories = data[categories_col].unique()
    fig = go.Figure()

    for category in categories:
        category_data = data[data[categories_col] == category]
        aggregated_data = category_data.groupby(x_col).agg(
            avg_similarity=(y_col1, 'mean'),
            pri_count=(y_col2, 'max')
        ).reset_index()

        fig.add_trace(go.Scatter(
            x=aggregated_data[x_col],
            y=aggregated_data['avg_similarity'],
            mode='markers',
            name=f'Avg Similarity ({category})',
            marker=dict(size=8, color='blue'),
            visible=False
        ))

        fig.add_trace(go.Scatter(
            x=aggregated_data[x_col],
            y=aggregated_data['pri_count'],
            mode='lines+markers',
            name=f'PRI Count ({category})',
            line=dict(color='orange', width=2),
            visible=False
        ))

    # Set the first category visible
    fig.data[0].visible = True
    fig.data[1].visible = True

    # Add dropdown menu for toggling categories
    buttons = [
        dict(
            label=category,
            method="update",
            args=[
                {"visible": [i == j * 2 or i == j * 2 + 1 for i in range(len(categories) * 2)]},
                {"title": f"Insights for {category}"}
            ]
        ) for j, category in enumerate(categories)
    ]

    fig.update_layout(
        updatemenus=[dict(active=0, buttons=buttons)],
        title="Similarity Scores and PRI Counts by Category",
        xaxis=dict(title=x_col),
        yaxis=dict(title="Avg Similarity"),
        height=600,
        width=1000
    )

    fig.show()
