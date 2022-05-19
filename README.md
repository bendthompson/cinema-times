# Cinema Times🍿
Using web scraping and calling API's to source data for all my nearby cinemas and display it in one place.

[See the app here](https://cinema-times-scraper.herokuapp.com/)

# Skills I used/learned

🎞️ Called API's using the requests package, handling response errors and sending dynamic queries

📽️ Scraped html code using the BeautifulSoup package. Had to use various BSoup methods to work around messily structured websites

🎬 Used RegEx with English and Japanese text

📹 Gained valuable experience about the importance of data architecture and creating a data pipeline 

🎦 Used a wide range of Streamlit features to create a clear and robust frontend that was hosted on Heroku

🎥 Streamlined code to minimize number of http requests and improve runtime

📸 Maintained a structured repo, refactoring code into importable packages to keep app file tidy

# Motivation

I've been a keen cinema-goer for a long time, but since I came to Japan my options for foreign movies at the cinema have been more limited. But sometimes there are some non-blockbuster movies that make it through to Japan, either at mainstream cinemas or independent cinemas. 

My previous tactic was going to the website of each nearby cinema I knew about and checking their showtimes, which took some time. So I decided a good way to practice my data sourcing skills would be to write code that would collect all this information in one place for me! 

I implemented 3 cinemas into the app so far. Plus a feature where you can add your own cinema if Google can find showtimes for it. 

**Data Sources:**

- Images and details are collected from [imdb-api](https://imdb-api.com/)
- Google showtimes info is collected from [serp-api](https://serpapi.com/)
- Meguro Cinema info is scraped from [okura-movie.co.jp](http://www.okura-movie.co.jp/meguro_cinema/now_showing.html)

# Screenshots


![ss1](https://user-images.githubusercontent.com/97390056/168751961-e762f467-7946-4001-9e6d-02a2349224c9.PNG)
![ss2](https://user-images.githubusercontent.com/97390056/168751956-ab1f3e70-ef99-4a7c-8b54-068385ec857d.PNG)
![ss3](https://user-images.githubusercontent.com/97390056/168751954-b4607184-e053-46a5-8ce8-448f2daf2939.PNG)
