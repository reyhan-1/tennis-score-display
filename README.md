# Current Tennis Score Displayer

This simple Python program displays the current score during a tennis match.  

## Features
- Displays the current tennis score in standard format (e.g., "15-30", "Love-All", "Deuce", "Advantage for Player 1").
- Supports input directly through the command line or from a file using command line arguments.
- Customizable player names for each game session, default Player 1 - Player 2 if names are not provided.
- Handles common input errors like invalid score formats or missing files.

## Set Up
- Clone the repository

```bash
git clone https://github.com/reyhan-1/tennis-score-display.git
cd tennis-score-display
```

- Check the Python version 
Ensure that Python 3.x is installed on your local machine. You can check this by running ```python --version``` or ```python3 --version``` in your terminal or command prompt. 

- The code uses the built-in Python libraries ```argparse``` and ```enum```, included by default in Python. Thus, setting up a virtual environment is optional. 

## Run the Program 
After setting up the environment, you can run the program in two ways using the command line arguments.

### 1. User Input
Score in the format X-Y (e.g., 3-5).
```bash
python main.py 3-5
```
To specify custom player names, use the --names option:
```
python main.py 3-5 --names Serena Naomi
```

### 2. File 
<file_path> is a text file containing scores in the format X-Y, one per line.
```bash
python main.py scores.txt
```
To specify custom player names, use the --names option:
```
python main.py scores.txt --names Nadal Federer
```

## Code Overview / Design Choices
This project uses a single file for simplicity.  **`main.py`** contains the logic and execution for this program to keep things simple and focused on the simple task. As the project grows, splitting it into multiple modules may improve maintainability.
- For fixed values of points ranging from 0-3  **`Enum`**  is used. 
- The **`WINNING_SCORE`** constant is used instead of 4 to improve readability and clarity.
- Deuce, Advantage, and Win conditions are evaluated in separate functions to improve readability and keeping **`current_score()`** simpler and more focused. I choose this approach after the initial hacky implementation: 'if else' statements  for each condition in **`current_score()`**. Another reason for this redesign was to make it easier for full scope of tennis scoring in the future, which includes sets, matches, and multiple players. 
- To ensure code quality, ```pylint main.py``` has 10.00/10 pylint rate.
- scores.txt file covers all the edge cases and tests for the scores.

  
## Future Enhancements 
1. Another form of external input could be based on the input query.

Endpoint
```GET /score?q={score}```

Query Parameter
q: The current score in the format playerA-playerB (e.g., 6-6).

Example:
```GET localhost:3000/score?q=6-6```
Response **`"Deuce"`**

2. **` Web Scraping:`** web scraping could be used to fetch live scores from a website.
This requires third party libraries such as BeautifulSoup to scrape static content.
For dynamic content (JavaScript-loaded), use Selenium to interact with the page.

Example function: 

```
import requests
from bs4 import BeautifulSoup

def get_score_from_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    score = soup.find('span', class_='score').text.strip()
    return score

```
