import os
import sys
import glob
import json
from typing import Dict, Callable
import anthropic
import openai

def get_env_var(name: str, default: str = '') -> str:
    """Safely get an environment variable."""
    return os.environ.get(name, default)

def load_file_types() -> Dict[str, str]:
    """Load file types from environment variable."""
    try:
        return json.loads(get_env_var('FILE_TYPES', '{}'))
    except json.JSONDecodeError:
        print("Error: FILE_TYPES environment variable is not valid JSON.", file=sys.stderr)
        return {}

def get_file_contents(file_path: str) -> str:
    """Read and return file contents."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}", file=sys.stderr)
        return ""

def scan_repository(file_types: Dict[str, str]) -> str:
    """Scan repository and return content of matched files."""
    repo_content = []
    for file_type, glob_pattern in file_types.items():
        files = glob.glob(glob_pattern, recursive=True)
        if files:
            repo_content.append(f"\n{file_type}:")
            for file in files:
                content = get_file_contents(file)
                if content:
                    repo_content.append(f"\n--- {file} ---\n{content}")
    return "\n".join(repo_content)

def generate_readme_with_anthropic(prompt: str) -> str:
    """Generate README using Anthropic API."""
    client = anthropic.Anthropic(api_key=get_env_var('ANTHROPIC_API_KEY'))
    message = client.messages.create(
        model=get_env_var('AI_MODEL'),
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

def generate_readme_with_openai(prompt: str) -> str:
    """Generate README using OpenAI API."""
    client = openai.OpenAI(api_key=get_env_var('OPENAI_API_KEY'))
    response = client.chat.completions.create(
        model=get_env_var('AI_MODEL'),
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000
    )
    return response.choices[0].message.content

def get_ai_provider() -> Callable[[str], str]:
    """Get the appropriate AI provider function."""
    ai_provider = get_env_var('AI_PROVIDER', '').lower()
    if ai_provider == 'anthropic':
        if not get_env_var('ANTHROPIC_API_KEY'):
            raise ValueError("ANTHROPIC_API_KEY is not set")
        return generate_readme_with_anthropic
    elif ai_provider == 'openai':
        if not get_env_var('OPENAI_API_KEY'):
            raise ValueError("OPENAI_API_KEY is not set")
        return generate_readme_with_openai
    else:
        raise ValueError(f"Unsupported AI provider: {ai_provider}")

def generate_readme():
    """Main function to generate README."""
    try:
        file_types = load_file_types()
        if not file_types:
            print("No file types specified. Please set the FILE_TYPES repository variable.")
            return

        repo_content = scan_repository(file_types)
        if not repo_content:
            print("No files matching the specified types found in the repository.")
            return

        prompt = f"""Based on the following repository content, generate a comprehensive README.md file.
        Include sections for Project Description, Installation, Usage, and Contributing.
        Only include information about file types that are present in the repository content provided.
        Make sure to accurately reflect the purpose and functionality of the files present.
        Group related files and their descriptions logically.
        Provide appropriate explanations for each file type based on their content and purpose.

        Repository Content:
        {repo_content}

        Please generate the README.md content now:"""

        generate_readme_func = get_ai_provider()
        readme_content = generate_readme_func(prompt)

        with open('README.md', 'w') as f:
            f.write(readme_content)

        print(f"README.md generated successfully using {get_env_var('AI_PROVIDER').capitalize()} ({get_env_var('AI_MODEL')}).")
    except Exception as e:
        print(f"Error generating README: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()