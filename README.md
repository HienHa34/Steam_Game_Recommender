# Steam_Game_Recommender

## Background
Steam is a one stop shop for PC users to buy games. As of 2019, steam offers a total of over 30,000 games, and as of 2020, there are approximately 20 million concurrent users on the platform. With so many games to choose from, how does anyone know what games are out there? Well, that's where recommenders comes in to play. Recommenders take many forms from content, collaborative, to hybrid systems. For this project, I will building an item-item colaborative recommender to recommend games for users. 

## Data
The dataset consisted of Australian Steam users and the games they have played, which will be used as the ratings for the recommender. The dataset had 88310 rows, each of which are users, and five columns: user_id, items_count, steam_id, user_url, and items. The two columns of interest are user_id and items. The items column contained the games that users have played in dictionaries. The column was exploded using pandas ```json_normalize()``` function. 

Once exploded, item_id, item_name, playtime_forever, and playtime_2weeks were created.Playtime_2weeks was dropped from the dataframe, and playtiem_forever was used as the ratings. 


## EDA
After inputing the data into, a pandas dataframe, I found that there were some duplicate users, and after dropping them, the total users came down to 87626 unique users and 10,978 games played between all users. 

Below is a table with a description of how many games a user has played(Ratings Per User) and how many users have played a game(Ratings Per Game). 

![alt text](https://github.com/HienHa34/Steam_Game_Recommender/blob/master/img/RatingsPerGame.png)
|                 | Min | Max| Mean|
|-----------------|-----|----|-----|
|Ratings Per User | 1   |7762|71.84|
|Ratings Per Game | 1   |49136|464.03|
