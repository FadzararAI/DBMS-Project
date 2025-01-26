import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

def create_dash_app(flask_app):
    dash_app = dash.Dash(__name__, server=flask_app, url_base_pathname="/dashboard/")
    # Dummy data for demonstration
    data = {
        "Product": ["Lego Bricks", "Colorbuds", "Magic Sand", "Action Figure", "Rubik's Cube", 
                    "Deck Of Cards", "Splash Balls", "Nerf Gun", "Animal Figures", "Dart Gun"],
        "Sales": [2.39, 1.56, 0.97, 0.93, 0.91, 0.59, 0.54, 0.53, 0.51, 0.51],
        "Profit": [299000, 835000, 120000, 348000, 91000, 252000, 54000, 133000, 125000, 126000],
        "Category": ["Toys", "Art & Crafts", "Toys", "Toys", "Games", "Games", "Toys", "Sports", "Toys", "Sports"],
        "Store": ["Ciudad de Mexico 2", "Guadalajara 3", "Ciudad de Mexico 1", "Toluca 1", 
                "Monterrey 2", "Guadalajara 4", "Hermosillo 3", "Xalapa 2", "Ciudad de Mexico 3", "Saltillo 1"],
        "Store_Sales": [555000, 449000, 434000, 411000, 373000, 348000, 345000, 340000, 337000, 330000],
        "Store_Profit": [170000, 122000, 111000, 107000, 105000, 102000, 99000, 97000, 94000, 94000]
    }
    df = pd.DataFrame(data)

    # Layout
    dash_app.layout = html.Div([
        html.H1("Maven Toys Sales Dashboard", style={'textAlign': 'center'}),

        # KPIs
        html.Div([
        # Total Sales
        html.Div([
            html.H3("Total Sales"),
            dcc.Graph(
        id='total-sales-line',
        figure=px.area(
            x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],  # Example months
            y=[2.0, 2.5, 3.0, 3.5, 4.0, 4.5],  # Example sales data in millions
            title="",
            height=100  # Adjust the height to make it small
        ).update_traces(
            line_color="blue",  # Custom line color
            fill="tozeroy",  # Fill area under the line
            hovertemplate="<b>Month:</b> %{x}<br><b>Revenue:</b> $%{y:.2f}M<extra></extra>"  # Custom hover text
        ).update_layout(
            margin=dict(l=10, r=10, t=10, b=10),  # Minimize margins
            xaxis=dict(visible=False),  # Hide the x-axis
            yaxis=dict(visible=False),  # Hide the y-axis
            showlegend=False,
            plot_bgcolor="rgba(0,0,0,0)",  # Transparent plot background
            paper_bgcolor="rgba(0,0,0,0)"  # Transparent chart background
        )
    ),
    html.P("$14.4M")

        ], className="kpi", style={'width': '18%', 'padding': '10px', 'textAlign': 'center'}),

        # Total Profit
        html.Div([
            html.H3("Total Profit"),
            dcc.Graph(
                id='total-profit-line',
                figure=px.area(
                    x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],  # Example months
                    y=[0.5, 0.8, 1.2, 2.0, 3.0, 4.0],  # Example profit data in millions
                    title="",
                    height=100
                ).update_traces(
            line_color="blue",  # Custom line color
            fill="tozeroy",  # Fill area under the line
            hovertemplate="<b>Month:</b> %{x}<br><b>Gross Profit:</b> $%{y:.2f}M<extra></extra>"  # Custom hover text
        ).update_layout(
            margin=dict(l=10, r=10, t=10, b=10),  # Minimize margins
            xaxis=dict(visible=False),  # Hide the x-axis
            yaxis=dict(visible=False),  # Hide the y-axis
            showlegend=False,
            plot_bgcolor="rgba(0,0,0,0)",  # Transparent plot background
            paper_bgcolor="rgba(0,0,0,0)"  # Transparent chart background
        )
            ),
            html.P("$4.0M")
        ], className="kpi", style={'width': '18%', 'padding': '10px', 'textAlign': 'center'}),

        # Profit Margin
        html.Div([
            html.H3("% Profit Margin"),
            dcc.Graph(
                id='profit-margin-line',
                figure=px.area(
                    x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],  # Example months
                    y=[25, 26, 27, 28, 28, 29],  # Example profit margin percentage
                    title="",
                    height=100
                ).update_traces(
            line_color="blue",  # Custom line color
            fill="tozeroy",  # Fill area under the line
            hovertemplate="<b>Month:</b> %{x}<br><b>Gross Profit Margin:</b> $%{y:.2f}M<extra></extra>"  # Custom hover text
        ).update_layout(
            margin=dict(l=10, r=10, t=10, b=10),  # Minimize margins
            xaxis=dict(visible=False),  # Hide the x-axis
            yaxis=dict(visible=False),  # Hide the y-axis
            showlegend=False,
            plot_bgcolor="rgba(0,0,0,0)",  # Transparent plot background
            paper_bgcolor="rgba(0,0,0,0)"  # Transparent chart background
        )
            ),
            html.P("28%")
        ], className="kpi", style={'width': '18%', 'padding': '10px', 'textAlign': 'center'}),

        # Total Orders
        html.Div([
            html.H3("Total Orders"),
            dcc.Graph(
                id='total-orders-line',
                figure=px.area(
                    x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],  # Example months
                    y=[100, 200, 300, 400, 500, 600],  # Example orders in thousands
                    title="",
                    height=100
                ).update_traces(
            line_color="blue",  # Custom line color
            fill="tozeroy",  # Fill area under the line
            hovertemplate="<b>Month:</b> %{x}<br><b>Count of Sale:</b> $%{y:.2f}M<extra></extra>"  # Custom hover text
        ).update_layout(
            margin=dict(l=10, r=10, t=10, b=10),  # Minimize margins
            xaxis=dict(visible=False),  # Hide the x-axis
            yaxis=dict(visible=False),  # Hide the y-axis
            showlegend=False,
            plot_bgcolor="rgba(0,0,0,0)",  # Transparent plot background
            paper_bgcolor="rgba(0,0,0,0)"  # Transparent chart background
        )
            ),
            html.P("829,262")
        ], className="kpi", style={'width': '18%', 'padding': '10px', 'textAlign': 'center'}),

        # Total Quantity Sold
        html.Div([
            html.H3("Total Quantity Sold"),
            dcc.Graph(
                id='total-quantity-line',
                figure=px.area(
                    x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],  # Example months
                    y=[150, 300, 450, 600, 800, 1000],  # Example quantities in thousands
                    title="",
                    height=100
                ).update_traces(
            line_color="blue",  # Custom line color
            fill="tozeroy",  # Fill area under the line
            hovertemplate="<b>Month:</b> %{x}<br><b>Units:</b> $%{y:.2f}M<extra></extra>"  # Custom hover text
        ).update_layout(
            margin=dict(l=10, r=10, t=10, b=10),  # Minimize margins
            xaxis=dict(visible=False),  # Hide the x-axis
            yaxis=dict(visible=False),  # Hide the y-axis
            showlegend=False,
            plot_bgcolor="rgba(0,0,0,0)",  # Transparent plot background
            paper_bgcolor="rgba(0,0,0,0)"  # Transparent chart background
        )
            ),
            html.P("1,091K")
        ], className="kpi", style={'width': '18%', 'padding': '10px', 'textAlign': 'center'})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'alignItems': 'center'}),

        # Charts
        # First Row: Top 10 Products
    html.Div([
        html.Div([
            dcc.Graph(
                id='sales-by-product',
                figure=px.bar(
                    df,
                    y='Product',
                    x='Sales',
                    color='Category',
                    orientation='h',
                    title="Top 10 Products by Sales"
                ).update_traces(
                    text=[f"${val:.2f}M" for val in df['Sales']],  # Add text labels
                    textposition='outside'  # Position text at the end of bars
                ).update_layout(
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)"
                )
            )
        ], style={'flex': '50%', 'padding': '10px'}),

        html.Div([
            dcc.Graph(
                id='profit-by-product',
                figure=px.bar(
                    df,
                    y='Product',
                    x='Profit',
                    color='Category',
                    orientation='h',
                    title="Top 10 Most Profitable Products"
                ).update_traces(
                    text=[f"${val:,}" for val in df['Profit']],  # Add text labels with commas
                    textposition='outside'  # Position text at the end of bars
                ).update_layout(
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)"
                )
            )
        ], style={'flex': '50%', 'padding': '10px'})
    ], style={'display': 'flex', 'justify-content': 'space-between'}),

    # Second Row: Top 10 Stores
    html.Div([
        html.Div([
            dcc.Graph(
                id='sales-by-store',
                figure=px.bar(
                    df,
                    y='Store',
                    x='Store_Sales',
                    color='Store',
                    orientation='h',
                    title="Top 10 Stores by Sales"
                ).update_traces(
                    text=[f"${val:,}" for val in df['Store_Sales']],  # Add text labels with commas
                    textposition='outside'  # Position text at the end of bars
                ).update_layout(
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)"
                )
            )
        ], style={'flex': '50%', 'padding': '10px'}),

        html.Div([
            dcc.Graph(
                id='profit-by-store',
                figure=px.bar(
                    df,
                    y='Store',
                    x='Store_Profit',
                    color='Store',
                    orientation='h',
                    title="Top 10 Most Profitable Stores"
                ).update_traces(
                    text=[f"${val:,}" for val in df['Store_Profit']],  # Add text labels with commas
                    textposition='outside'  # Position text at the end of bars
                ).update_layout(
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)"
                )
            )
        ], style={'flex': '50%', 'padding': '10px'})
    ], style={'display': 'flex', 'justify-content': 'space-between'})
    ])
    return dash_app
dash_app = create_dash_app(app)

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
