# DBMS Project
In this project, our objective is to simulate unnormalized vs normalized form of Database. On the other hand, we also created an 'app' which is a web-based data management and dashboard written in Python.

I am responsible for creating the app and the practical comparison between the unnormalized vs normalized database.

# App Screenshots
In this section, I will be showcasing the result of the app that was created during the project.
## Home/Index
![Main menu](/DOCS/index.png)
## Dashboard
![Dashboard page](/DOCS/dashboard.png)
## Management page
![Management page](/DOCS/management1.png)
## Data management page
![Data management page](/DOCS/add_try.png)

# Unnormalized vs Normalized
In this section, I will be showing the practical comparison. I will explain each image.
## Broken data
![Broken data](/DOCS/normalization/broken.png)

It can be vividly seen that the unnormalized (right) appears to be broken as it is filled with *NULL* values compared to the normalized (left) data.
## Ineffecient query
![Ineffecient query](/DOCS/normalization/query.png)

Normalized (left) data is easier to query as the information we would like to gather are already at their respective tables. Therefore, we don't need to experience in too much of hassle.
## Redundant size
![Redundant size](/DOCS/normalization/size.png)

This is the most important one, it can be seen that unnormalized (right) data requires bigger space compared to the normalized (left) data. In my case it is pretty small, but what if we were to have billions of data? It would require A LOT of space, especially when the data is unnormalized.

# Technologies
The libraries that I use in this project are as follow:
*Note that not everything is probably used here, perhaps some are installed just to test and is not removed in the finalization of the project*

| Library | Version |
| --- | --- |
| blinker |   1.9.0 |
| click   |   8.1.7 |
| colorama|   0.4.6 |
| dash    |   2.9.3 |
| dash-core-components | 2.0.0 |
| dash-html-components | 2.0.0 |
| dash-table      |     5.0.0 |
| Flask            |    3.1.0 |
| greenlet          |   3.1.1 |
| itsdangerous  |       2.2.0 |
| Jinja2         |      3.1.4 |
| MarkupSafe      |     3.0.2 |
| mysql            |    0.0.3 |
| mysql-connector   |   2.2.9 |
| mysqlclient       |   2.2.6 |
| numpy      |          2.1.3 |
| packaging   |         24.2  |
| pandas       |        2.2.3 |
| pip           |       24.3.1 |
| plotly     |          5.24.1 |
| PyMySQL     |         1.1.1 |
| python-dateutil |     2.9.0.post0 |
| pytz       |          2024.2 |
| setuptools  |         75.6.0 |
| six          |        1.16.0 |
| SQLAlchemy    |       2.0.36 |
| tenacity       |      9.0.0  |
| typing_extensions |   4.12.2 |
| tzdata     |          2024.2 |
| Werkzeug    |         3.1.3  |
