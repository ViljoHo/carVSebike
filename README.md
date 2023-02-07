# ebikeVScar

This project is still under progress!

Idea of this project is to make website which shows how much money I have saved riding an electric bike instead of a car.
I use Polar's smart watch to measure cycled distances and this program utilizes this data to make calculations.
Backend is made with django and frontend with react.

At this point, there is only one button "update calculations" on green. When it is clicked, program makes request to Polars api where all users data is stored and summarizeds all new kilometers to combined kilometers.

As I mentioned, backend is based on django project structure. The most relevant thing what I have done totally myself are in files api/authorization, api/logic.py and frontend/src

Below is short example gif how this web application works and seems.
![](https://github.com/ViljoHo/ebikeVScar/blob/main/example.gif)