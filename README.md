# AI-Powered README Generator

## Project Description

This project is an automated README generator that uses artificial intelligence to create comprehensive and accurate documentation for your repository. It scans your repository for specific file types, analyzes their content, and generates a README.md file that accurately reflects the purpose and functionality of your project.

The system is designed to work with GitHub Actions, automatically updating your README when changes are made to relevant files in your repository. It supports multiple AI providers (Anthropic and OpenAI) and can be easily configured to suit your specific needs.

## Installation

To use this README generator in your own repository, follow these steps:

1. Copy the `generate_readme.py` script to your repository (e.g., in a `.github/scripts/` directory).
2. Copy the `main.yml` workflow file to your repository's `.github/workflows/` directory.
3. Set up the necessary secrets and variables in your GitHub repository settings:
   - `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` (depending on your chosen AI provider)
   - `AI_PROVIDER` (set to either "anthropic" or "openai")
   - `AI_MODEL` (set to the desired model, e.g., "gpt-4" for OpenAI or "claude-2" for Anthropic)
   - `FILE_TYPES` (a JSON object mapping file types to glob patterns)

4. Install the required Python packages:
   ```
   pip install anthropic openai
   ```

## Usage

Once installed and configured, the README generator will automatically run when:

1. Changes are pushed to the main branch (excluding changes to `.github/**` files).
2. The workflow is manually triggered.

The generator will:

1. Scan the repository for files matching the specified types.
2. Generate a README based on the content of these files using the chosen AI provider.
3. Commit and push the new README to a `readme-update` branch if changes are detected.

You can customize the behavior by modifying the `FILE_TYPES` variable to include or exclude specific file types.

## Contributing

Contributions to improve the README generator are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request with a clear description of your changes.

When contributing, please ensure that you:

- Follow the existing code style and conventions.
- Update any relevant documentation.
- Add or update tests as necessary.
- Ensure all tests pass before submitting your pull request.

## File Descriptions

### Python Scripts

#### generate_readme.py

This is the core script that handles the README generation process. It includes functions for:

- Loading file type configurations from environment variables.
- Scanning the repository for specified file types.
- Generating README content using either the Anthropic or OpenAI API.
- Writing the generated content to a README.md file.

The script is designed to be flexible and can be easily extended to support additional AI providers or file types.

### YAML Files

#### main.yml

This GitHub Actions workflow file automates the README generation process. It:

- Sets up the Python environment.
- Installs necessary dependencies.
- Determines which files have changed in the repository.
- Runs the `generate_readme.py` script if relevant files have been modified.
- Commits and pushes the updated README to a new branch if changes are detected.

The workflow is designed to be efficient, only generating a new README when necessary and avoiding unnecessary API calls or commits.

---

This README generator streamlines the process of keeping your project documentation up-to-date and comprehensive, leveraging the power of AI to create accurate and detailed README files with minimal manual effort.