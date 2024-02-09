# Тестирование проекта Canadian Vineyard Site Selection

Репозиторий создан в рамках проверочного задания на позицию тестировщика.
В качестве кода для тестов выступил проект Canadian Vineyard Site Selection, взятый из репозитория: https://github.com/SpencerMartel/VineyardComparison.git

На основе анализа кода принято решение тестировать модули: app, cloud, data_analysis и функции: get_data(), queried_df(), calculate_soil_mean(), get_elevation(), make_profile_card(), make_card_chart(), comparison(), make_queried_json(), make_profile_comparative_json(),get_location_temp(),get_location_diurnal_range()
Особое внимание стоит уделить функциям, которые запрашивают данныe с помощью библиотеки ee и используются для анализа данных, полученных с сервера. Функции, возвращающие словари с данными, будут проверены на соответствие правильному формату результата. 
Далее были проведены интеграционные тесты, проверяющие взаимодействия модулей и функций между собой.

Анализируя код, было обнаружено, что модуль make_profile и все входящие в него функции используются исключительно для демонстрации их работы на странице в качестве примера функциональности программы, поэтому их функциональность не проверялась. Функция piechart() модуля data_analysis не была вызвана извне, что также показывает отсутствие необходимости для её проверки.

В процессе разворачивания среды приложения, были вявлено множество конфликтов библиотек, а также необходимость изменять исходный код для инициализации библиотеки EarthEngine. Более подробно это будет описано в баг-репортах

Также, для более быстрого осваивания в проекте, была создана схема зависимостей модулей и функций. 

README первоначального источника:
This app is live at https://canadianvineyards.streamlit.app/

This is the final project for my fall 2022 class GEOG466 - Geomedia and the Geoweb. The project was to create a web app that had an interactive map.
My idea was to compare canadian terroir to that of famous wine regions to tell the user which grapes they should try growing at their selected location.

This project was an excellent opportunity to learn raster processing using Google Earth Engine as well as some basic web dev.
I used Streamlit for the frontend of the project as it allowed me to write in pure python with some small HTML and CSS injections here and there, and focus more on the technical geographic aspects of the project.
