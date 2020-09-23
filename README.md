# Steam_Game_Recommender

## Background
Steam is a one stop shop for PC users to buy games. As of 2019, steam offers a total of over 30,000 games, and as of 2020, there are approximately 20 million concurrent users on the platform. With so many games to choose from, how does anyone know what games are out there? Well, that's where recommenders comes in to play. Recommenders take many forms from content, collaborative, to hybrid systems. For this project, I will building an item-item colaborative recommender to recommend games for users. 

## Data
The dataset consisted of Australian Steam users and the games they have played, which will be used as the ratings for the recommender. The dataset had 88310 rows, each of which are users, and five columns: user_id, items_count, steam_id, user_url, and items. The two columns of interest are user_id and items. The items column contained the games that users have played in dictionaries. The column was exploded using pandas ```json_normalize()``` function. 

Once exploded, item_id, item_name, playtime_forever, and playtime_2weeks were created.Playtime_2weeks was dropped from the dataframe, and playtiem_forever was used as the ratings. 


## EDA
After inputing the data into, a pandas dataframe, I found that there were some duplicate users, and after dropping them, the total users came down to 87626 unique users and 10,978 games played between all users. 

Below are plots and a table depicting how many games a user has played(Ratings Per User) and how many users have played a game(Ratings Per Game).

![img](https://github.com/HienHa34/Steam_Game_Recommender/blob/master/img/RatingsPerGame.png)
![img](https://github.com/HienHa34/Steam_Game_Recommender/blob/master/img/RatingsPerUser.png)

|                 | Min | Max| Mean|
|-----------------|-----|----|-----|
|Ratings Per User | 1   |7762|71.84|
|Ratings Per Game | 1   |49136|464.03|


From the right skewness, of both plots, one can expect the utility matrix of ratings to be sparse. The density of the utility matrix is 0.0065. Due to the sparsity, I wanted to filter out users and games to better extract signal and reduce computational costs.  

I decided to keep users who have played at least 30 games and games that have been played by at least 5000 users.This reduced the users to 20540 and to 210 games. The density of the new utility matrix increased to 0.3074. 


## Item-Item Recommender

Once the utility matrix has been set, a 210 x 210 item-item simlarity matrix was made using cosine similarity, and this simlarity matrix in conjunction with the utility matrix can be used to predict ratings. From those ratings, I want to recommend the top 10 games to users according to their play history.
 
#### Testing and Evaluation

To test the recommender, I sampled 10 random ratings from each user and replaced those ratings with NaNs for the recommender to predict. In the perfect world, the recommender would pick up all the signal and rate the 10 sampled games the highest, which would be the 10 I recommend. 

The metric I decided to use to evaluate the recommender is precision@k. A recommendation is successful if precision@k is 0.10 meaning that 1 of the 10 recommendations was actually in the test set. 

My first item-item recommender used the raw time that users have played each game, which are in minutes. The minutes played range from 0 to 642773. My second item- item recommender had binary ratings. If a user has played a game, it would be a 1 for the rating, and if a user has not, then it would be a 0. 

| Recommender| Average precision@k|
|------------|--------------------|
|Non-binary  | .04                |
|Binary       | .038              |

My two recommenders use a neighborhood of 20 similar games to predict the ratings. I also tested a Non-binary recommender that had a neighborhood of 30 but it yielded slighlty worse results with .038. 

The results are underperforming of what I consider a successful recommendation, so I took a look at the recommendations a user was given and compared it to some of the games the users actually did play. 


![img](https://github.com/HienHa34/Steam_Game_Recommender/blob/master/img/recommended.png)

![img](https://github.com/HienHa34/Steam_Game_Recommender/blob/master/img/actuallyplayed.png)



The snippet on top are the games recommended to the user, and the snippet on the bootom are some games the user actually played.The recommender is recommending similar games in same genre(action in this case) that the user plays. The precision@k score is low because there are over 200 games to recommend. The precision@k can be higher if we increase the amount of recommendations to give to a user. 

Alternatively to my two item-item recommenders, I also used an SVD and CoCluster based recommenders from surprise that achieved significantly better results. 

| Recommender| Average precision@k|
|------------|--------------------|
|SVD | .65|
|CoCluster|.71|

## Next Steps
- Explore optimization of the recommenders.
 - specifically neighnborhood size for my first recommenders.
- Build other types of recommenders.
- I would like build a web app with flask down the line after developing a robust recommender. :thumbsup:
