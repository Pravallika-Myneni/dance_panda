# Dance Panda

## How to run it on your system
1. Clone this repository 
2. Install all the python packages: Streamlit using ```pip install```
3. Go to terminal and change the directory to this folder
4. run the application using the command
 ``` streamlit run streamlit_app.py``` 

## Inspiration
Imagine having a cultural fest in your college or sangeet or any occasion demanding you to make some moves to the beats and show the world out there what you got. imagine that one songs with the beats you'd love to dance for. That one song you'd feel zestful to dance for.
you may search for the premade dance videos. but what if you couldn't find the right one?
what if you hiring a choreographer or ask for help isn't really an option for the moment?
Dance-panda is going to help you through it all


## What it does
Enter the title of song or input your audio file. Dance-panda is going to generate a youtube link or you can find our 3D models dancing for your song and manual instructions on how to do it

## How we built it
we used streamlit a python library to build the interface of website. We have three options for you: 
- A youtube dance tutorial: For the youtube video, based on the son entered in the form, we used requests library to search for the  youtube video
- A 3D dancing model that predicts the type of the dance group that the song can potentially belongs to using spotify API, clustering and classification techniques
- A 3D dancing pose model: A pose model to learn step-by-step dance for the song

## Challenges we ran into
-It was a bit challenging to find the right 3D model for different genres, but it was fun 

## Accomplishments that we're proud of
- Building a streamlit application 
- Applying machine learning techniques
- Using our application for learning dance moves for an upcoming fest

## What we learned
- Time management
- Planning and Organization
- Developing streamlit application
- Video editing techniques using natural voices

## What's next for dance-panda
We have so many ideas for extending our project by implementing the following
- To generate a 3D **Panda** dancing pose model
- A Deep learning based dance choreography
- A more detailed step-by-step tutorial and scoring mechanism 
- To deploy the website
