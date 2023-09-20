![One Click Wonders Banner](https://user-images.githubusercontent.com/108072497/268628903-8cccdf2d-5b04-412a-97a7-4d497c6e1294.png)

# One Click Wonders

One Click Wonders is a route planner app made to ease transportation experience in UberLand. It provides seamless integration between public transport and ridesharing.

## Features (planned)

- Easy journey planning
- Real-Time Updates: Stay informed about transit schedules, delays, and ride status.
- Affordable Fares
- Safety First

## Usage

### Self Host

You can self-host this web app by following these instructions:

1. Clone this repository using your preferred method (`git clone https://github.com/yeetyboi56/OneClickWonders.git`).
2. Create a virtual environment (`python -m venv .venv`)
3. [Activate the virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work) (`source .venv/bin/activate` on bash/zsh)
4. Run `npm install` and `pip install -r requirements.txt` to install all packages required to run this program.
5. Run `npm run build` to build the CSS file
6. Set environment variable `MONGODB_URI` and `SECRET_KEY` the `SECRET_KEY` can be anything that's secure.
7. Start the server by running `gunicorn app:create_app()`. Your app should be available at [127.0.0.1:8000](http://127.0.0.1:8000/) by default.

## Troubleshooting

#### There's an error associated with `app.db_client.get_default_database()`
Your MongoDB URI must contain the database name. For example, `mongodb://localhost:27017/database_name`
