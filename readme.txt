Movie Recommendation System using Streamlit

Hey there! Welcome to my Movie Recommender System, powered by Streamlit!

Introduction:
So, you know those times when you're in the mood for a movie but can't decide what to watch? Well, fear not! This nifty little app is here to save the day. With just a few clicks, you'll discover a treasure trove of movie recommendations tailored just for you.

Features:
- Easy peasy movie selection from a dropdown menu.
- Hit the "Show Recommendation" button and voila! Similar movies galore.
- Check out movie posters and titles displayed side by side for that cinematic flair.
- Oh, and did I mention? The background is as clean as a freshly wiped whiteboard.

Installation:
1. Clone this repo to your cozy little corner of the internet.
2. Make sure Python is chillin' on your system.
3. Whip up a virtual environment with the command: `python -m venv my_venv`.
4. Activate that virtual vibe: `source my_venv/bin/activate` (for Unix/Linux) or `my_venv\Scripts\activate` (for Windows).
5. Install the must-have goodies with a swift `pip install -r requirements.txt`.
6. Fire up the app and let the movie magic begin: `streamlit run app.py`.

Files:
- **app.py**: Where the movie magic happens.
- **model/movie_list.pkl**: This is where the movie data hangs out.
- **model/similarity.pkl**: Friendship scores between movies live here.
- **requirements.txt**: All the cool kids (a.k.a. Python packages) you need to party.

Usage:
1. Pick your poison from the dropdown menu.
2. Hit that "Show Recommendation" button like it owes you money.
3. Take a leisurely scroll through the recommended movies and let the journey begin.
4. Sit back, relax, and enjoy the show!

Note:
- Keep the internet pipes flowing because we need to fetch movie data and posters from the TMDB API.
- Oh, and don't forget to replace the placeholder in the `fetch_poster` function with your TMDB API key for poster perfection.

Author:
Manish Paneru
Email: mpaneru115@gmail.com

Happy movie-hopping, fellow  cinephiles! ???
