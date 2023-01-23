import requests
from tkinter import *
from webbrowser import open as open_browser


def search_github(search_criteria):
    # Set the number of stars
    min_stars = 100

    # Send a GET request to the GitHub Search API
    url = f'https://api.github.com/search/repositories?q={search_criteria}+stars:%3E{min_stars}'
    response = requests.get(url)
    data = response.json()

    if 'items' in data:
        # Extract the name, number of stars and html_url of each repository
        repos = []
        for item in data['items']:
            name = item['name']
            stars = item['stargazers_count']
            html_url = item['html_url']
            repos.append((name, stars, html_url))
        return repos
    else:
        return 'No repositories found'


# GUI
root = Tk()
root.title("GitHub Search")
root.geometry("400x300")

# Search criteria label and input
search_label = Label(root, text="Enter your search criteria: ")
search_label.pack()
search_criteria_input = Entry(root)
search_criteria_input.pack()

# Search button
search_button = Button(root, text="Search",
                       command=lambda: search_and_display())
search_button.pack()

# Results label
results_label = Label(root, justify=LEFT)
results_label.pack()


def search_and_display():
    # Get search criteria from the user
    search_criteria = search_criteria_input.get()
    # Clear previous results
    for widget in results_label.winfo_children():
        widget.destroy()
    # Search GitHub
    repos = search_github(search_criteria)
    # Display results
    for repo in repos:
        link = Label(
            results_label, text=f'Repository: {repo[0]}, Stars: {repo[1]}', fg="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e, url=repo[2]: open_browser(url))


# start the event loop
root.mainloop()
