"""
AI Service

Wrapper around Claude/OpenAI API for generating completions.

Supports both Anthropic (Claude) and OpenAI as providers.
Configure via ANTHROPIC_API_KEY or OPENAI_API_KEY in .env.

TODO: Implement each function.
"""


async def generate_completion(
    system_prompt: str,
    messages: list[dict],
    max_tokens: int = 2048,
    temperature: float = 0.3,
) -> str:
    """Generate a text completion using Claude or OpenAI.

    Args:
        system_prompt: System instructions for the AI.
        messages: List of message dicts [{"role": "user"|"assistant", "content": "..."}].
        max_tokens: Max tokens in the response.
        temperature: Creativity level (0.0 = deterministic, 1.0 = creative).

    Returns:
        The AI's response text.

    Hints (Anthropic/Claude):
        - import anthropic
        - client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        - response = client.messages.create(
              model="claude-sonnet-4-20250514",
              max_tokens=max_tokens,
              system=system_prompt,
              messages=messages
          )
        - return response.content[0].text

    Hints (OpenAI):
        - import openai
        - client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        - Prepend system message to messages list
        - response = client.chat.completions.create(
              model="gpt-4o",
              messages=[{"role": "system", "content": system_prompt}] + messages
          )
        - return response.choices[0].message.content

    Decision:
        - Check which API key is set in settings
        - Prefer Anthropic if both are set
    """
    pass


async def generate_structured_output(
    system_prompt: str,
    user_prompt: str,
    output_schema: dict,
) -> dict:
    """Generate a structured JSON response from the AI.

    Args:
        system_prompt: System instructions.
        user_prompt: The user's question/request.
        output_schema: Expected JSON structure for the response.

    Returns:
        Parsed dict matching the output_schema.

    Hints:
        - Add instructions to the prompt asking for JSON output
        - Parse the response with json.loads()
        - Validate against output_schema
        - Retry once if parsing fails
    """
    pass
