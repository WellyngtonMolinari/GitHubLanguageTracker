# GitHub Language Tracker

This Flask application tracks the most used programming languages across your GitHub repositories and visualizes the data in a bar chart using Chart.js.

## Features

- Fetches data from GitHub API using a personal access token.
- Processes repository language data to count usage frequency.
- Displays the language usage statistics in a dynamic bar chart on a web page.
- Supports customization and expansion for additional features.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- requests library
- Chart.js (included via CDN in `index.html`)

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-github-username/github-language-tracker.git
   cd github-language-tracker
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your GitHub credentials**:

   - Replace `'your-github-username'` with your GitHub username in `app.py`.
   - Replace `'your-github-token'` with your GitHub personal access token in `app.py`.

4. **Run the application**:

   ```bash
   python app.py
   ```

5. **View the application**:

   Open your web browser and go to `http://127.0.0.1:5000/` to see your GitHub language usage displayed in a bar chart.

## Files and Directories

- `app.py`: Flask application script that fetches GitHub data and serves web pages.
- `templates/`: Directory containing `index.html`, the template file for displaying the bar chart.
- `requirements.txt`: Lists Python libraries required for the application (`Flask`, `requests`).

## Usage

- The bar chart on the homepage (`index.html`) updates dynamically based on the languages detected in your GitHub repositories.
- Customize the visualization or add additional features by modifying `index.html` and extending `app.py`.

## Troubleshooting

- **TemplateNotFound**: Ensure `index.html` is located in the `templates/` directory and is correctly referenced in `render_template('index.html')` in `app.py`.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
