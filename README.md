# ebikeVScar

This project is still under progress!

Idea of this project is to make website which shows how much money I have saved riding an electric bike instead of a car.
I use Polar's smart watch to measure cycled distances and this program utilizes this data to make calculations.
Backend is made with django and frontend with react.

At this point, there is only one button "update calculations" on green. When it is clicked, program makes request to Polars api where all users data is stored.

As I mentioned, backend is based on djangos project structure. The most relevant thing what I have done are in file api/authorization, api/logic.py and frontend/src

Below is short example gift how this web application works and seems like.
![](https://github.com/ViljoHo/ebikeVScar/blob/main/example.gif)