Flight Dashboard Project <br>
Welcome to the Flight Dashboard Project! This repository contains the code for a Streamlit-based web application that allows users to explore and analyze flight data. The project includes a backend for connecting to a MySQL database, and a frontend for displaying interactive visualizations.

Project Overview
This Flight Dashboard provides the following features:

Check Flights: Users can select departing and arriving cities to view a table of flights between these cities, including flight name, departing time, arriving time, duration, and price.<br>
Flights Analytics: Users can explore various aspects of flight data between selected cities with the following analyses:
Price Distribution: A bar chart showing the average price of flights from different airlines.
Flight Frequency per Airline: A pie chart illustrating the number of flights each airline operates.
Average Flight Duration per Airline: A bar chart displaying the average flight duration for each airline.
Peak Departure Times: A bar chart showing the frequency of flights at different times of the day.
Price Trend by Time of the Day: A line chart showing how flight prices vary throughout the day.

Getting Started<br>
Prerequisites<br>
Python 3.7 or higher<br>
MySQL

Project Structure<br>
app.py: Main application file containing the Streamlit code.<br>
dbconnector.py: Contains the DB class for connecting to the MySQL database and retrieving data.<br>
requirements.txt: Lists the Python packages required for the project.<br>
Using the Dashboard<br>
Check Flights:<br>

Select the departing and arriving cities from the dropdown menus.<br>
Click the "Search" button to view a table of flights between the selected cities.<br>
Flights Analytics:<br>

Navigate to the "Flights Analytics" section.<br>
Select the source and destination cities from the dropdown menus.<br>
Explore the visualizations to gain insights into flight patterns, prices, and durations.<br>
About the Dashboard<br>
The "About The Dashboard" section provides a brief overview of the tool and its features. This section is styled using HTML to make it visually appealing and informative.

Screenshots<br>
![image](https://github.com/user-attachments/assets/1a8b4ddd-ec74-4ce1-b34a-332db5d7ce13)
![image](https://github.com/user-attachments/assets/5d6d291f-ce06-4fd6-bb89-d51a3d8ee927)


You can also chat with flight database. Flight database is integrated with Large language Model using langchain. Below is the screenshot of the same.
![image](https://github.com/user-attachments/assets/b4a322cc-acc9-48ad-bf95-953b709c3869)


Contributing<br>
Contributions are welcome! If you have any suggestions or improvements, please open an issue or create a pull request.

License<br>
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements<br>
Streamlit<br>
MySQL<br>
Plotly<br>
Contact<br>
If you have any questions, feel free to contact me at adi.763192@gmail.com
