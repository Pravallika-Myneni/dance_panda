#download package
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


#CONNECT TO SPOTIFY - make spotify for developers account to get cid and secret id
cid ="type your cliend id here" 
secret = "type your secret id here"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



#GET SONG METRICS FROM PLAYLIST
#connect to playlist
playlist = sp.user_playlist("userid", "put in playlist URI code here") 
songs = playlist["tracks"]["items"] 
ids = [] 

#obtain data
for i in range(len(songs)): 
    ids.append(songs[i]["track"]["id"]) 
features = sp.audio_features(ids) 
dfmet = pd.DataFrame(features)
dfmet.info()

#song metrics data cleanup
columns_to_drop_met = ['analysis_url','track_href','type','uri']
dfmet.drop(columns_to_drop_met, axis=1,inplace=True)
dfmet.rename(columns={'id': 'track_id'}, inplace=True)

dfmet.shape
dfmet.info()
dfmet.head()




#GET SONG NAME FROM PLAYLIST
# create empty lists where the results are going to be stored
artist_name = []
track_name = []
popularity = []
track_id = []

#Get playlist
track_results = sp.user_playlist("userid", "type playlist URI code here")["tracks"]["items"]

for t in track_results:
    artist_name.append(t['track']['artists'][0]['name'])
    track_name.append(t['track']['name'])
    track_id.append(t['track']['id'])
    popularity.append(t['track']['popularity'])
print('number of elements in the track_id list:', len(track_id))

#imports track names
import pandas as pd
dftracks = pd.DataFrame({'artist_name':artist_name,'track_name':track_name,'track_id':track_id,'popularity':popularity})
print(df_tracks.shape)

dftracks.shape
dftracks.info()
dftracks.head()

#song name data cleanup
grouped = dftracks.groupby(['artist_name','track_name'], as_index=True).size()
grouped[grouped > 1].count()
dftracks.drop_duplicates(subset=['artist_name','track_name'], inplace=True)

# doing the same grouping as before to verify the solution
grouped_after_dropping = dftracks.groupby(['artist_name','track_name'], as_index=True).size()
grouped_after_dropping[grouped_after_dropping > 1].count()
dftracks[dftracks.duplicated(subset=['artist_name','track_name'],keep=False)].count()
dftracks.shape




# MERGE BOTH DATAFRAMES - SONG METRICS AND SONG NAME
# the 'inner' method matches the track IDs and combines using that as reference
dftotal = pd.merge(dftracks,dfmet,on='track_id',how='inner')
dftotal.head()
dftotal.info()




#write to csv
dftotal.to_csv('Spotifyscrape.csv')