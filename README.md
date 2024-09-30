# README Generator

## Project Description

This project contains a Python script that automatically generates a comprehensive README.md file for a repository. The script scans the repository for specific file types (Terraform, Shell, and Python files) and uses AI-powered text generation to create a detailed README in markdown based on the repository's content.

The main features of this project include:

- Scanning the repository for relevant files
- Using AI (either Anthropic or OpenAI) to generate README content
- Supporting multiple AI providers (Anthropic and OpenAI)
- Customisable AI model selection

## Installation

To install and set up the project, follow these steps:

- Add `workflows` and `scripts` to your repo under `.github/`
- Set the `Actions permissions` to `Read and write permissions`
- Add `AI_MODEL` and `AI_PROVIDER` to repo variables either `anthropic` or `openai` with their respective models e.g `claude-3-5-sonnet-20240620`
- Add relevant AI API as secret variables named `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`.
- Any push to the repo will start the README creation

## Contributing

Contributions to this project are welcome. To contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with descriptive commit messages
4. Push your changes to your fork
5. Submit a pull request to the main repository

Please ensure that your code follows the existing style and includes appropriate tests and documentation.

## Python Scripts

### scripts/generate_readme.py

This is the main script of the project. It performs the following functions:

- Scans the repository for Terraform, Shell, and Python files
- Reads the contents of these files
- Constructs a prompt for the AI model
- Generates README content using either Anthropic or OpenAI's API
- Writes the generated content to a README.md file

The script uses environment or repository variables to determine the AI provider and model to use. It supports both Anthropic and OpenAI as AI providers.

Key functions in the script:

- `scan_repository()`: Scans the repository for relevant files and their contents
- `generate_readme_with_anthropic()`: Generates README content using Anthropic's API
- `generate_readme_with_openai()`: Generates README content using OpenAI's API
- `generate_readme()`: Main function that orchestrates the README generation process

The script is designed to be run from Github Actions.
