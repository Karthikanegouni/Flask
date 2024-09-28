# News Aggregator

A simple web application built with Flask that aggregates news articles from BBC News. Users can view, search, and filter articles by category.


## Features

- Scrapes news articles from BBC News.
- Displays articles in a user-friendly interface.
- Search functionality to find articles by title or summary.
- Filter articles by category.
- Responsive design for a better mobile experience.

## Technologies Used

- **Python**: Backend development.
- **Flask**: Web framework for building the web application.
- **Beautiful Soup**: For web scraping.
- **Pandas**: For data manipulation and CSV handling.
- **NLTK**: For natural language processing tasks (not extensively used in this version).
- **HTML/CSS/JavaScript**: Frontend development.
- **jQuery**: For handling search functionality in the frontend.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Karthikanegouni/Flask-projects.git

2. Navigate to the project directory:
   ```bash
   cd Flask-projects

3. Create a virtual environment:
   ```bash
   python -m venv .venv

4. Activate the virtual environment:

      - On Windows:
         ```bash
         .venv\Scripts\activate
         ```
      - On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

5. Install the required packages:
    ```bash
     pip install -r requirements.txt

## Usage

1. Run the Flask application:
  ```bash
  python app.py
```
2. Open your web browser and navigate to:
```bash
http://127.0.0.1:5000/
```

3. You can view the aggregated news articles, search for specific articles, and filter by category.

## Folder Structure
```bash
/news_aggregator
│
├── app.py                 # Main application file
├── news_articles.csv      # CSV file to store scraped articles
└── templates
    └── home.html         # HTML template for the homepage
└── static
    ├── styles.css        # CSS styles for the application
    └── script.js         # JavaScript for search functionality
```

## API Endpoints
- GET /: Renders the homepage with a list of articles.
- GET /articles: Retrieves all articles, with optional filtering by category.
- GET /articles/<id>: Retrieves a specific article by its index.
- GET /search: Searches articles by keyword in title or summary.
