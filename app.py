import requests
import streamlit as st

def assess_repository(github_user_url):
    # Extracting the username from the GitHub URL
    username = github_user_url.split("/")[-1]

    # Fetching the user's repositories using the GitHub REST API
    repositories_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(repositories_url)
    repositories = response.json()

    # Assessing each repository individually based on complexity
    most_complex_repo = None
    highest_complexity_score = float('-inf')

    for repo in repositories:
        # Fetching the repository details
        repo_url = repo['url']
        response = requests.get(repo_url)
        repo_details = response.json()

        # Calculating the complexity score based on your desired criteria
        complexity_score = calculate_complexity_score(repo_details)

        # Updating the most complex repository if necessary
        if complexity_score > highest_complexity_score:
            highest_complexity_score = complexity_score
            most_complex_repo = repo['name']

    return most_complex_repo

def calculate_complexity_score(repo_details):
    # Calculate the complexity score for the given repository details
    # You can define your own logic here based on your criteria

    # Example: Calculating the complexity score based on the number of stars
    return repo_details.get('stargazers_count', 0)

# Streamlit app
def main():
    # App title and description
    st.title("GitHub Repository Complexity Assessment")
    st.write("Enter a GitHub username to find the most technically complex repository.")

    # User input field
    github_username = st.text_input("GitHub Username")

    # Button to trigger repository assessment
    if st.button("Assess Repository"):
        if github_username:
            # Call the assess_repository function to get the most complex repository
            most_complex_repo = assess_repository(f"https://github.com/{github_username}")

            # Display the result
            if most_complex_repo:
                st.success(f"The most technically challenging repository of {github_username} is: {most_complex_repo}")
            else:
                st.warning(f"No repositories found for {github_username}")
        else:
            st.warning("Please enter a GitHub username.")

# Run the Streamlit app
if __name__ == '__main__':
    main()
