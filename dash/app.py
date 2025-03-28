import dash
from dash import html, dcc
from dash import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests

# Функция получения данных из NocoDB
def get_nocodb_data():
    url = "http://backend:8000/nocodb-data/"  # Замените на ваш URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            records = data.get('records', [])
            print("Полученные данные:", records)
            cleaned_records = [
                {k: v for k, v in record.items() if not k.startswith('_nc_m2m_')}
                for record in records
            ]
            return pd.DataFrame(cleaned_records)
        else:
            print("Ошибка при получении данных:", response.status_code)
            return pd.DataFrame()
    except Exception as e:
        print(f"Ошибка соединения: {e}")
        return pd.DataFrame()

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Базовый макет приложения
app.layout = html.Div([
    html.H1('User Dashboard'),
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,  # Обновление каждые 1 секунду (при первой загрузке)
        n_intervals=0,
        max_intervals=1  # Выполняется только один раз при загрузке
    ),
    html.Div(id='dashboard-content')
])

# Callback для обновления содержимого при загрузке
@app.callback(
    Output('dashboard-content', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_dashboard(n):
    # Получение данных
    df = get_nocodb_data()

    # Проверка наличия данных
    if df.empty:
        return html.P('Нет данных для отображения. Проверьте соединение с NocoDB.')

    # Создание таблиц и графиков
    return html.Div([
        html.H3('Таблица пользователей'),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {'name': 'ID', 'id': 'Id'},
                {'name': 'Имя', 'id': 'Name'},
                {'name': 'Пол', 'id': 'Gender'},
                {'name': 'Возраст', 'id': 'Age'},
                {'name': 'Город', 'id': 'City'},
                {'name': 'Академическое давление', 'id': 'Academic_pressure'},
                {'name': 'Удовлетворенность учебой', 'id': 'Study_satisfaction'}
            ],
            style_cell={
                'textAlign': 'left'
            },
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            }
        ),
        html.Hr(),
        html.H3('Графики'),
        dcc.Graph(
            figure=px.histogram(df, x="City", color="Gender",
                               title="Распределение пользователей по городам и полу")
        ),
        dcc.Graph(
            figure=px.bar(df, x="Age", y=["Academic_pressure", "Study_satisfaction"],
                          barmode='group', title="Сравнение академического давления и удовлетворенности учебой по возрасту")
        )
    ])

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)