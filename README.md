# Movie Recommendation System
The project can be accessed by clicking [HERE](https://movierecommendation-ml.herokuapp.com/)
## About the project
Movie recommendation is a popular technique where movies similar to a particular movie are shown so that any user looking for movies similar to his/her favourite movies can easily search for them. Movie recommendation is used by tech giants like Netflix, Amazon Prime, HBO, Hulu etc. This project is a first attempt to learn about the world of recommendation systems and learning about techniques to recommend things based on different criteria.\
Movie Recommendation System is of **three** types :-
* **Content Based:** The recommendation system recommends other movies which are like that selected movie. It uses only the item data maintaining a profile for each item. Each user is assumed to operate independently. No need for data on other users. Considering the attributes or	feature of the item, it	finds the similarity between items, and recommends the most similar item for an item.
* **Collaborative:** The recommendation system recommends movies which are rated highly by the similar users. It maintains a database of many users’ ratings of a variety of items.
* **Hybrid Approach:** In this, we attempt to hybridize collaborative filtering and content-based recommendation. Item similarity measure used in content-based recommendation is learned from a collaborative social network of users.

## Methodology
* I have downloaded the movie dataset from Kaggle. This dataset has information like director’s name, actor’s name, number of likes and dislikes by the users, genre of the movie, IMDB rating, year of release and duration of movie.
* I have another dataset that has information of 2017 movies but in json format. I have used ast (Abstract Syntax Trees) library to evaluate a string containing a python dictionary.
* After pre-processing of all datasets, I finally append them to make the single dataset i.e., main_data.csv.
* I have done sentiment analysis on review dataset of movies where reviews are classified as good or bad.
* In main.py file, I have used Similarity Score to find out most similar movie user likes. It is a numerical value ranges between zero to one which helps to determine how much two items are like each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
* Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
<p align="center">
<img alt="EcoJourney" src="./templates/CosineSimilarity.png" width="250px" height="250px"/>
</p>
<ul>
<li>I have designed the front-end and back-end using HTML, CSS and have made webapp of my project using flask .</li>
<li>The webapp works in the following way: As the user opens it, the first page shows an input field and a submit button. The user has to type the name of the movie and click the submit button.</li>
<li>As the user clicks the submit button, a list of 5 movies is presented on the next screen which are the top 5 similar movies to the movie searched by the user. </li>
<li>In case the user types a movie name not present in the dataset or a movie which does not exists then a message is shown “The movie does not exist”
  The user can then press the back button to search more movies and get recommendations.</li>
</ul>

## Input/Output Screenshots
<p>
  The homepage that is visible to the user on visiting the website is as follows:
</p>
<img alt="EcoJourney" src="./templates/FrontPage.png" width="100%"  />
<p>
  The user can search any movie by typing it in the single input field. The view can be seen below:
</p>
<p align="center">
<img alt="EcoJourney" src="./templates/Search.png" width="500px" height="500px" />
</p>
<p> 
  If the movie is present in the database, it applies the model and generates movie similar to the entered movie. The view can be seen below:
</p>
<img alt="EcoJourney" src="./templates/FinalPage.png" width="100%" />
<p> 
  If the movie is NOT present in the database, the output is as follows:
</p>
<img alt="EcoJourney" src="./templates/Wrong.png" width="100%" />   


