from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk

# Initialize Flask app
app = Flask(__name__)

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function to scrape BBC News
def scrape_bbc():
    base_url = 'https://www.bbc.com/news'
    response = requests.get(base_url)
    articles = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        for article in soup.find_all('div', attrs={'data-testid': 'edinburgh-card'}):
            title_element = article.find('h2', attrs={'data-testid': 'card-headline'})
            summary_element = article.find('p', attrs={'data-testid': 'card-description'})
            date_element = article.find('span', attrs={'data-testid': 'card-metadata-lastupdated'})
            link_element = article.find('a', attrs={'data-testid': 'internal-link'})

            title = title_element.get_text(strip=True) if title_element else None
            summary = summary_element.get_text(strip=True) if summary_element else title  # Use title as summary if no summary
            publication_date = date_element.get_text(strip=True) if date_element else 'No publication date available'
            url = f"https://www.bbc.com{link_element['href']}" if link_element else None

            # Append to articles list only if title and summary are present
            if title and summary:
                articles.append({
                    'Title': title,
                    'Summary': summary,
                    'Publication Date': publication_date,
                    'Source': 'BBC',
                    'URL': url
                })

    return articles

# Function to update articles data
def update_articles_data():
    bbc_articles = scrape_bbc()

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(bbc_articles)
    df.to_csv('news_articles.csv', index=False)

# Load articles data from CSV (initial load)
update_articles_data()  # Call to scrape and save articles
df = pd.read_csv('news_articles.csv')

# Route to render the homepage with a list of articles
@app.route('/')
def home():
    articles = df.to_dict(orient='records')  # Convert the DataFrame to a list of dictionaries
    return render_template('home.html', articles=articles)

# API Endpoint to retrieve all articles, with optional filtering by category
@app.route('/articles', methods=['GET'])
def get_articles():
    category = request.args.get('category')
    if category:
        filtered_df = df[df['Category'].str.contains(category, case=False)]
        return jsonify(filtered_df.to_dict(orient='records'))
    return jsonify(df.to_dict(orient='records'))

# API Endpoint to retrieve a specific article by its index (id)
@app.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    if id < len(df):
        article = df.iloc[id].to_dict()
        return jsonify(article)
    else:
        return jsonify({"error": "Article not found"}), 404

# API Endpoint to search articles by keyword in title or summary
@app.route('/search', methods=['GET'])
def search_articles():
    keyword = request.args.get('keyword')
    if keyword:
        filtered_df = df[df['Title'].str.contains(keyword, case=False) | df['Summary'].str.contains(keyword, case=False)]
        return jsonify(filtered_df.to_dict(orient='records'))
    else:
        return jsonify({"error": "Keyword is required"}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
