# TFT_Analysis

The purpose of this project is to help players understand trends in the current meta of Team Fight Tactics. Information provided will include an easy to ingest dashboard with key trends in players habits of selecting certain champions, traits, items, and compositions along with their correlation to getting a top 4 placement. The end user will be able to apply date filters to get the appropriate data set they want information for. This information will be very useful for players as they will get a sense of what is currently strong to play, what items people are building with success, and what champions are too contested and to avoid. This will help players use Riot's team builder tool to begin building the right composition for them.

Data is obtained from Riot's API and includes ranked games from players in North America and stored in a Postgres database. Once match data is extracted from the API, it undergoes a transformation using Pandas/Pyspark to deliver a clean dataset which is then saved as a csv to be used by Tableau - Public Edition for the dashboard.

## Visual Analysis of Trends

### November 4 - November 16
![Total_Champion_plays](/images/total_champ_usage.png)
![Average_Champion_plays](/images/average_champ_usage.png)
![Correlation_Champions](/images/correlation_placement_champion.png)