"""
This is a python web scraping project which saves the billboard Hot 100 as a file.
It also prints the chart history of artists
"""
# import the necessary libraries
from bs4 import BeautifulSoup
import requests
import sys

# creating the function which collects info from the charts
def hot_100():
    url = "https://www.billboard.com/charts/hot-100"
    bill = requests.get(url).text
    soup = BeautifulSoup(bill, "lxml")
    f = open("Hot 100.txt", "w")
    f.write("The Hot 100 list is: \n\n")
    entries = soup.find_all("li", class_="chart-list__element display--flex")

    for index, entry in enumerate(entries):
        entry_rank = entry.find("span", class_="chart-element__rank__number").text
        entry_title = entry.find("span", class_="chart-element__information__song text--truncate color--primary").text
        entry_artist = entry.find("span", class_="chart-element__information__artist text--truncate color--secondary").text

        f.write(f"{entry_rank}. ")
        f.write(f"{entry_title} by ")
        f.write(entry_artist.replace("&", "and"))
        f.write("\n\n")

    f.close()
    print(f"File Hot 100.txt saved...")


def hot_200():
    url = "https://www.billboard.com/charts/billboard-200"
    bill = requests.get(url).text
    soup = BeautifulSoup(bill, "lxml")
    f = open("Hot 200.txt", "w")
    f.write("The Hot 200 list is: \n\n")
    entries = soup.find_all("li", class_="chart-list__element display--flex")

    for index, entry in enumerate(entries):
        entry_rank = entry.find("span", class_="chart-element__rank__number").text
        entry_title = entry.find("span", class_="chart-element__information__song text--truncate color--primary").text
        entry_artist = entry.find("span", class_="chart-element__information__artist text--truncate color--secondary").text

        f.write(f"{entry_rank}. ")
        f.write(f"{entry_title} by ")
        f.write(entry_artist.replace("&", "and"))
        f.write("\n\n")

    f.close()
    print(f"File Hot 200.txt saved...")


def chart_history():
    print("Please enter the name of the artist: \n")
    art = input("> ")
    artist = art.lower().replace(" ", "-")
    url = "https://www.billboard.com/music/"+artist+"/chart-history/HSI"
    f = open(f"{art}.txt", "w")
    f.write(f"The Chart History for {art} is: ")
    print("Gathering information...")

    bill = requests.get(url).text
    soup = BeautifulSoup(bill, "lxml")

    history = soup.find("ul", class_="chart-history__titles__hits").text
    f.write(history)

    entries = soup.find_all("div", class_="chart-history__item")

    for index, entry in enumerate(entries):
        f.write(entry.text)

    f.write(f"and more at {url}")
    f.close()
    print(f"Chart History for {art} is saved...")


if __name__ == "__main__":
    print("Welcome to the Billboard Hot 100 and Chart History programme. \n")
    print("What service do you want? 1. Hot 100 \t 2. Chart History \n 3.Billboard 200 \n")
    user = input("> ")

    if user == "1":
        print("You have selected Hot 100. Please wait while we gather the Hot 100 information.\n")
        print("Gathering the Hot 100 information...")
        hot_100()
        sys.exit()

    if user == "2":
        print("You have selected Chart History information.\n")
        chart_history()
        print("Do you want to try again? 'y' for yes and 'n' for no. ")

        use = input("> ")
        if use == "y":
            chart_history()
        else:
            sys.exit("Goodbye")
    if user == "3":
        print("You have selected Hot 200. Please wait while we gather the Hot 200 information.\n")
        print("Gathering the Hot 200 information...")
        hot_200()
        sys.exit()
    else:
        print("You have chosen a wrong option. Programme will now exit\n")
        sys.exit("Wrong input")
