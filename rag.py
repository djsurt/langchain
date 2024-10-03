#Langchain implementation to pull .md files from github repos

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import GithubFileLoader

load_dotenv()
github_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")

loader = GithubFileLoader(
    repo="ModelEarth/langchain", # Mention the repo we need 
    branch="main",  # the branch name
    access_token=github_token,
    github_api_url="https://api.github.com",
    file_filter=lambda file_path: file_path.endswith(
        ".md"
    ),  # load all markdowns files.
)
documents = loader.load()

for doc in documents:
    print(doc.metadata)
    print(doc.page_content)