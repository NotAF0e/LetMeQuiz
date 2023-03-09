import os

try:
    import bs4
    from rich.console import Console
    import requests
except ModuleNotFoundError:
    if input("To continue the needed modules have to be installed. "
             "Would you like to automatically install them?(y, n): ").strip().lower() == "y":
        os.system("pip install -r requirements.txt")
    else:
        exit("Packages not installed")

    import bs4
    from rich.console import Console
    import requests


# Http request and formatting
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"}

url = "https://quizlet.com/gb/781941445/role-play-questions-and-useful-expressions-flash-cards/"

soup = bs4.BeautifulSoup(requests.get(
    url, headers=headers).content, "html.parser")


# Q&A scrapper
# Thanks: https://www.appsloveworld.com/coding/python3x/51/how-to-scrape-answer-from-quizlet-flashcard-bs4-and-requests
finder = zip(soup.select("a.SetPageTerm-wordText"),
             soup.select("a.SetPageTerm-definitionText"))

questions = []
answers = []

for (question, answer) in finder:
    questions.append(question.get_text(strip=True))
    answers.append(answer.get_text(strip=True, separator="\n"))

print(questions, answers)