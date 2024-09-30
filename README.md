# README Generator

## Project Description

This project contains a Python script that automatically generates a comprehensive README.md file for a repository. The script scans the repository for specific file types (Terraform, Shell, and Python files) and uses AI-powered text generation to create a detailed README based on the repository's content.

The main features of this project include:

- Scanning the repository for relevant files
- Using AI (either Anthropic or OpenAI) to generate README content
- Supporting multiple AI providers (Anthropic and OpenAI)
- Customizable AI model selection

## Installation

To install and set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the required dependencies:
   ```
   pip install anthropic openai
   ```
4. Set up the necessary environment variables:
   - `AI_PROVIDER`: Set to either 'anthropic' or 'openai'
   - `AI_MODEL`: Set to the desired AI model (e.g., 'gpt-4' for OpenAI or 'claude-2' for Anthropic)
   - `ANTHROPIC_API_KEY`: Your Anthropic API key (if using Anthropic)
   - `OPENAI_API_KEY`: Your OpenAI API key (if using OpenAI)

## Usage

To generate a README for your repository:

1. Navigate to the root directory of your repository.
2. Run the script:
   ```
   python scripts/generate_readme.py
   ```
3. The script will scan your repository, generate the README content using the specified AI provider, and save it as `README.md` in the root directory.

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

The script uses environment variables to determine the AI provider and model to use. It supports both Anthropic and OpenAI as AI providers.

Key functions in the script:

- `scan_repository()`: Scans the repository for relevant files and their contents
- `generate_readme_with_anthropic()`: Generates README content using Anthropic's API
- `generate_readme_with_openai()`: Generates README content using OpenAI's API
- `generate_readme()`: Main function that orchestrates the README generation process

The script is designed to be run from the command line and will output the generated README.md file in the current directory.