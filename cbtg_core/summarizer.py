from pathlib import Path
from typing import List, Dict
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
)

MODEL = "gpt-4o"  # You can change this to any supported OpenRouter model


def read_file_content(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding="utf-8")
    except Exception:
        return ""


def summarize_section(
    section_name: str, file_paths: List[str], root_path: Path
) -> Dict[str, str]:
    contents = []
    for rel_path in file_paths:
        file_path = root_path / rel_path
        content = read_file_content(file_path)
        if content:
            contents.append(f"# {rel_path}\n{content[:1000]}")

    prompt = (
        f"You are an expert software engineer helping onboard new developers.\n"
        f"Summarize the purpose of the following files in the '{section_name}' section.\n\n"
        f"{'=' * 40}\n\n" + "\n\n".join(contents)
    )

    messages: List[ChatCompletionMessageParam] = [
        {
            "role": "system",
            "content": "You are a friendly and concise code tour guide.",
        },
        {"role": "user", "content": prompt},
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.4,
            max_tokens=300,
        )
        summary = response.choices[0].message.content.strip()
    except Exception as e:
        summary = f"(AI summary failed: {e})"

    return {"section": section_name, "summary": summary}
