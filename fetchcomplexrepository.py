import requests
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

def assess_repository(repository_url):
    # Fetch the user's repositories from GitHub API
    response = requests.get(repository_url)
    repositories = response.json()

    most_complex_repository = None
    highest_complexity_score = -1

    # Iterate over each repository
    for repository in repositories:
        repository_name = repository['name']
        repository_description = repository['description']

        # Assess repository complexity using GPT and LangChain
        prompt = f"This repository is named {repository_name}. It is described as: {repository_description}. Please assess its technical complexity."
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
        )

        complexity_score = response.choices[0].text.strip()

        # Update the most complex repository if a higher complexity score is found
        if float(complexity_score) > highest_complexity_score:
            most_complex_repository = repository_name
            highest_complexity_score = float(complexity_score)

    return most_complex_repository

# Example usage
github_user_url = 'https://api.github.com/users/vishnu305/repos'
most_complex_repo = assess_repository(github_user_url)
print(f"The most technically complex repository for the user is: {most_complex_repo}")
