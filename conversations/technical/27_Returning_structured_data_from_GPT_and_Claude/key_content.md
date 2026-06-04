# Key Content from: Returning structured data from GPT and Claude
Date: 2025-11-24
Total substantial assistant responses: 17

================================================================================
**User asked:** What is the most up to date way to return structured data from 1) GPT and 2) Claude? I know I can pass GPT a Pydantic model. I'm not sure about Claude....
**Response (msg #1, 5169 chars):**

The user is asking about the most up-to-date ways to get structured data output from both GPT (OpenAI) and Claude (Anthropic). They mention knowing about passing Pydantic models to GPT, and they're unsure about Claude.

This is a technical question about API features. Since these features change over time and the user is asking for the "most up to date" way, I should search for current information about:
1. OpenAI's structured output features
2. Anthropic/Claude's structured output features

My knowledge cutoff is January 2025, so I may have information about this, but since the user is specifically asking for the "most up to date" way, I should search to make sure I'm giving them the latest information.

Let me search for information about structured outputs for both APIs.I'll search for the most current information on structured outputs for both APIs.
```
This block is not supported on your current device yet.
```

Good, I found information about OpenAI's structured outputs. Now let me search for Claude/Anthropic's structured outputs feature.
```
This block is not supported on your current device yet.
```

Great! I found information about Claude's structured outputs. Let me now search for more specific information about how to use Claude's structured outputs feature with the API.
```
This block is not supported on your current device yet.
```

Perfect! Now I have comprehensive information about both OpenAI's and Claude's structured output capabilities. Let me summarize the key points:

For GPT/OpenAI:
1. They have a Structured Outputs feature (released in August 2024)
2. Uses `client.beta.chat.completions.parse()` method
3. Can pass Pydantic models directly via `response_format` parameter
4. Achieves 100% reliability on their benchmarks
5. Available on gpt-4o-2024-08-06, gpt-4o-mini, and later models
6. Two approaches: function calling with `strict: true` or response format with Pydantic models

For Claude/Anthropic:
1. Structured Outputs feature released in November 2024 (public beta)
2. Available for Claude Sonnet 4.5 and Opus 4.1 (Haiku 4.5 coming soon)
3. Two modes:
   - JSON outputs mode: uses `output_format` parameter with JSON schema
   - Strict tool use mode: uses `strict: true` in tool definitions
4. Requires beta header: `anthropic-beta: structured-outputs-2025-11-13`
5. Python SDK has helpers to work with Pydantic models using `transform_schema()`
6. Can also use third-party libraries like Instructor for Pydantic support

Now I can provide a comprehensive answer to the user.Based on the latest information, here's how to get structured data from both APIs:

## **GPT (OpenAI)**

OpenAI's Structured Outputs feature was introduced in August 2024 and achieves 100% reliability through constrained decoding. You can pass Pydantic models directly:

```python
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."}
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed
```

This works with gpt-4o-2024-08-06, gpt-4o-mini, and any fine-tuned models based on them.

## **Claude (Anthropic)**

Claude's Structured Outputs feature launched in November 2024 (public beta) for Sonnet 4.5 and Opus 4.1. There are two approaches:

**1. Direct JSON Schema (native approach):**

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    betas=["structured-outputs-2025-11-13"],
    messages=[{"role": "user", "content": "Extract: John Smith..."}],
    output_format={
        "type": "json_schema",
        "schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "email": {"type": "string"}
            },
            "required": ["name", "email"]
        }
    }
)
```

**2. With Pydantic (using SDK helpers):**

```python
from pydantic import BaseModel
from anthropic import Anthropic, transform_schema

class ContactInfo(BaseModel):
    name: str
    email: str

client = Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    betas=["structured-outputs-2025-11-13"],
    messages=[{"role": "user", "content": "Extract..."}],
    output_format=transform_schema(ContactInfo)
)
```

**3. Using Instructor library (third-party):**

The Instructor library provides seamless Pydantic integration:

```python
import instructor
from anthropic import Anthropic

client = instructor.from_anthropic(Anthropic())

user = client.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Create a user..."}],
    response_model=User  # Your Pydantic model
)
```

Both APIs now support guaranteed schema compliance, making structured outputs production-ready!

================================================================================
**User asked:** Awesome. Let's take some code I have already for cross-platform inference with freeform text output and make it Pydantic-constrained....
**Response (msg #3, 860 chars):**

The user wants to modify their existing code to add Pydantic-constrained structured outputs. They mentioned they have code for "cross-platform inference with freeform text output", which suggests they have code that works with both OpenAI and Claude (or possibly other providers).

I should ask them to share their existing code so I can help them modify it to support Pydantic models for structured outputs. I'll want to see what their current implementation looks like so I can provide the most helpful modifications.Great! Please share your existing code and I'll help you add Pydantic-constrained structured outputs to it. 

I'll need to see:
1. Your current inference code
2. What structure you want to extract (so I can help create the Pydantic model if needed)

Just paste the code and let me know what kind of structured data you're trying to get back!

================================================================================
**User asked:** I don't have the pydantic model yet, but it will have some dict, list, string (freeform), and date fields, and at least one constrained-value text field (5 choices) -- please generate a model like tha...
**Response (msg #5, 15071 chars):**

The user wants me to:
1. Take their existing cross-platform inference code (supports OpenAI, Claude, and Mistral)
2. Add Pydantic-constrained structured outputs
3. Create a sample Pydantic model with:
   - dict field
   - list field
   - string (freeform) field
   - date field
   - constrained text field with 5 choices (using Literal)

I should modify their `ModelWrapper` class to support structured outputs while maintaining backward compatibility. I'll need to:

1. Create a sample Pydantic model with the requested field types
2. Add a parameter to enable structured output mode
3. Implement structured outputs for both OpenAI and Claude (skip Mistral for now since it's commented out)
4. Update the response methods to handle Pydantic models

For OpenAI:
- Use `client.beta.chat.completions.parse()` with `response_format` parameter

For Claude:
- Use the `output_format` parameter with `transform_schema()` or raw JSON schema
- Need to add the beta header `structured-outputs-2025-11-13`

Let me create a comprehensive solution.I'll help you add Pydantic-constrained structured outputs to your ModelWrapper. Here's the updated code with a sample model and structured output support:

```python
import re
import os
import json
import time
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime, timedelta, date
from typing import Optional, List, Dict, Literal
from pydantic import BaseModel, Field
import anthropic

from agentic.custom_logging import CustomLogger

logger = CustomLogger()
load_dotenv()


# Sample Pydantic Model with the requested field types
class AnalysisResult(BaseModel):
    """Sample structured output model for testing"""
    summary: str = Field(description="Freeform text summary of the analysis")
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level - must be one of 5 choices"
    )
    metadata: Dict[str, str] = Field(
        description="Dictionary of key-value metadata pairs"
    )
    tags: List[str] = Field(
        description="List of relevant tags or categories"
    )
    due_date: date = Field(
        description="Target completion date in YYYY-MM-DD format"
    )
    scores: Optional[Dict[str, float]] = Field(
        default=None,
        description="Optional dictionary of numeric scores"
    )


def remove_markdown_from_json(json_text):
    # remove markdown formatting: "json ```" -> ""
    text_without_formatting = re.sub("```", "", json_text)
    text_without_formatting = re.sub("json", "", text_without_formatting)
    return text_without_formatting


class ModelWrapper(object):
    no_validation_required = False
    
    def __init__(
        self, 
        model_type="claude", 
        model_version=None, 
        system_message=None, 
        validation=True, 
        sec_model="openai", 
        test=False
    ):
        self.no_validation_required = False or not validation
        self.test = test
        self.conversation_thread = []
        self.model_type = model_type
        self.sec_model = sec_model
        self.token_count = []
        
        if model_type == "openai":
            self.model_version = model_version or "gpt-4o-2024-08-06"
            self.client = OpenAI()
            self.system_message = system_message or "You are a technical assistant, skilled in answering questions in a friendly but succinct way."    
        elif model_type == "mistral":
            api_key = os.environ["MISTRAL_API_KEY"]
            self.client = Mistral(api_key=api_key)
            self.model_version = model_version or "mistral-large-latest"
            self.system_message = system_message or "You are a technical assistant, skilled in answering questions in a succinct way."  
        elif model_type == "claude":
            self.client = anthropic.Anthropic()
            self.model_version = model_version or "claude-sonnet-4-5"
            self.system_message = system_message or "You are a technical assistant, skilled in answering questions in a succinct way."  
        else:
            raise Exception("Model type not supported")
            
        logger.info(f"ModelWrapper initialized with model_type: {model_type}, model_version: {self.model_version}")

    def response(
        self, 
        prompt, 
        context=None, 
        system_message=None, 
        json_out=True, 
        conversation_thread=True, 
        max_tokens=1024, 
        sec_check=True, 
        callback=None,
        response_model: Optional[BaseModel] = None  # NEW: Pydantic model for structured output
    ):
        """
        Get a response from the model.
        
        Args:
            response_model: Optional Pydantic model to enforce structured output.
                          If provided, returns a Pydantic model instance.
                          If None, returns plain text (legacy behavior).
        """
        logger.info(f"response callback {callback}")
        system_message = system_message or self.system_message
        messages = [
            {"role": "system", "content": system_message},
        ] if system_message else []

        # convert context information from sender/text to role/content
        if context and context[0].get("sender"):
            def switch_keys(el):
                return dict(role=el["sender"], content=el["text"])
            context = [switch_keys(a) for a in context]

        if conversation_thread: 
            messages.extend(self.conversation_thread)
        if context:
            messages.extend(context)

        if prompt != None:
            messages.append({"role": "user", "content": prompt})

        logger.info(f"Model response: {self.__class__.__name__}")
        logger.info("No security check required")
        
        # Route to appropriate method based on structured output need
        if self.model_type == "openai":
            resp = self.response_openai(messages, callback=callback, response_model=response_model)
        elif self.model_type == "mistral":
            if response_model:
                raise NotImplementedError("Structured outputs not yet implemented for Mistral")
            resp = self.response_mistral(messages)
        elif self.model_type == "claude":
            assert max_tokens and type(max_tokens) == int, f"max_tokens must be an integer; found {max_tokens}"
            resp = self.response_claude(messages, max_tokens, callback=callback, response_model=response_model)
        else:
            raise Exception("Model type not supported")

        # Only apply markdown removal for plain text JSON responses
        if json_out and not response_model and isinstance(resp, str):
            resp = remove_markdown_from_json(resp)
            
        logger.output(f"Response: {resp}")
        return resp

    def response_openai(self, messages, callback=None, response_model: Optional[BaseModel] = None):
        messages_str = "\n".join([f"{el['role'].upper()}: {el['content']}" for el in messages])
        logger.prompt(f"OPENAI - messages: {messages_str}")

        if response_model:
            # Use structured outputs with Pydantic
            completion = self.client.beta.chat.completions.parse(
                model=self.model_version,
                messages=messages,
                response_format=response_model,
            )
            resp = completion.choices[0].message.parsed
        else:
            # Legacy text output
            completion = self.client.chat.completions.create(
                model=self.model_version,
                messages=messages,
            )
            resp = completion.choices[0].message.content
            
        if callback is not None:
            tokens_in = int(len(messages_str))
            resp_text = resp if isinstance(resp, str) else resp.model_dump_json()
            callback(tokens_in, messages_str, resp_text)
            
        return resp
    
    def response_mistral(self, messages):
        logger.prompt(f"MISTRAL - messages: {messages}")
        completion = self.client.chat.complete(
            model=self.model_version,
            messages=messages,
        )
        return completion.choices[0].message.content
    
    def response_claude(
        self, 
        messages, 
        max_tokens, 
        check_tokens=True, 
        callback=None,
        response_model: Optional[BaseModel] = None
    ):
        def truncate_string(s):
            tokens = self.count_tokens_claude(s)
            logger.info(f"Token count: {tokens}")
            if tokens > 40000:
                excess_tokens = tokens - 40000
                excess_chars = max(int(excess_tokens * 2.4), 1000)
                s = s[:len(s) - excess_chars]
                logger.info(f"Truncated prompt to {len(s)} characters, {tokens} tokens")
            return s, tokens

        prompt = messages[-1]["content"]
        prompt, tokens = truncate_string(prompt)
        
        if check_tokens:
            while tokens > 40000:
                prompt, tokens = truncate_string(prompt)
            messages[-1]["content"] = prompt
            
            while True:
                tokens_last_minute = [t['tokens'] for t in self.token_count if t["time"] > datetime.now() - timedelta(minutes=1)]
                tokens_last_minute = sum(tokens_last_minute)
                if tokens_last_minute + tokens > 40000:
                    print("Token count would be: ", tokens_last_minute + tokens, "Waiting 5 seconds.")
                    time.sleep(5)
                else:
                    break
                    
        logger.prompt(f"CLAUDE - messages: {messages}")
        system_message = [a for a in messages if a["role"] == "system"][0]['content']
        messages = [b for b in messages if b['role'] != "system"]
        
        if self.test:
            return "This is a test response"
        
        if response_model:
            # Use structured outputs with Pydantic
            from anthropic import transform_schema
            
            ret = self.client.beta.messages.create(
                system=system_message,
                model=self.model_version,
                max_tokens=max_tokens,
                messages=messages,
                betas=["structured-outputs-2025-11-13"],
                output_format=transform_schema(response_model)
            )
            # Parse the JSON response into Pydantic model
            resp_text = ret.content[0].text
            resp = response_model.model_validate_json(resp_text)
        else:
            # Legacy text output
            ret = self.client.messages.create(
                system=system_message,
                model=self.model_version,
                max_tokens=max_tokens,
                messages=messages
            )
            resp = ret.content[0].text
        
        print(f"calling callback {callback}")
        if callback is not None: 
            resp_text = resp if isinstance(resp, str) else resp.model_dump_json()
            callback(tokens, prompt, resp_text)
            
        return resp
    
    def count_tokens_claude(self, prompt=None, messages=None):
        if not messages:
            messages = [
                {"role": "user", "content": prompt},
            ]
        response = self.client.messages.count_tokens(
            model=self.model_version,
            messages=[{"role": "user", "content": prompt}]
        )
        tokens = response.input_tokens
        logger.info(f"Input token count: {tokens} at {datetime.now()}")
        return tokens


# Example usage functions
def test_structured_output_openai():
    """Test structured output with OpenAI"""
    model = ModelWrapper(model_type="openai", validation=False)
    
    prompt = """Analyze this task: 
    'Fix the critical authentication bug in the login system. 
    This affects user security and needs immediate attention. 
    Related to: oauth, security, backend'"""
    
    result = model.response(
        prompt=prompt,
        response_model=AnalysisResult,
        max_tokens=2000
    )
    
    print("OpenAI Structured Result:")
    print(f"Type: {type(result)}")
    print(f"Summary: {result.summary}")
    print(f"Priority: {result.priority}")
    print(f"Tags: {result.tags}")
    print(f"Due Date: {result.due_date}")
    print(f"Metadata: {result.metadata}")
    print(f"\nFull JSON:\n{result.model_dump_json(indent=2)}")
    return result


def test_structured_output_claude():
    """Test structured output with Claude"""
    model = ModelWrapper(model_type="claude", validation=False)
    
    prompt = """Analyze this task: 
    'Update the documentation for the new API endpoints. 
    This is medium priority and should be done by next week. 
    Related to: documentation, api, developer-experience'"""
    
    result = model.response(
        prompt=prompt,
        response_model=AnalysisResult,
        max_tokens=2000
    )
    
    print("Claude Structured Result:")
    print(f"Type: {type(result)}")
    print(f"Summary: {result.summary}")
    print(f"Priority: {result.priority}")
    print(f"Tags: {result.tags}")
    print(f"Due Date: {result.due_date}")
    print(f"Metadata: {result.metadata}")
    print(f"\nFull JSON:\n{result.model_dump_json(indent=2)}")
    return result


def test_legacy_text_output():
    """Test that legacy plain text output still works"""
    model = ModelWrapper(model_type="claude", validation=False)
    
    result = model.response(
        prompt="What is the capital of France?",
        max_tokens=100
    )
    
    print("Legacy Text Result:")
    print(f"Type: {type(result)}")
    print(f"Content: {result}")
    return result


if __name__ == "__main__":
    print("=" * 80)
    print("Testing Structured Outputs")
    print("=" * 80)
    
    # Test structured output with both providers
    test_structured_output_openai()
    print("\n" + "=" * 80 + "\n")
    test_structured_output_claude()
    print("\n" + "=" * 80 + "\n")
    test_legacy_text_output()
```

**Key changes:**

1. **Added `response_model` parameter** - Pass any Pydantic model to get structured output
2. **Sample `AnalysisResult` model** with all requested field types:
   - `summary`: Freeform string
   - `priority`: Literal with 5 choices
   - `metadata`: Dictionary
   - `tags`: List of strings
   - `due_date`: Date field
   - `scores`: Optional dictionary

3. **OpenAI implementation** - Uses `client.beta.chat.completions.parse()` with `response_format`
4. **Claude implementation** - Uses `transform_schema()` and the beta header for structured outputs
5. **Backward compatible** - Without `response_model`, works exactly like before
6. **Returns Pydantic instances** - When using structured mode, you get type-safe objects

The test functions show how to use both modes. You can now do:
```python
# Structured output
result = model.response("Analyze this...", response_model=AnalysisResult)
print(result.priority)  # Type-safe access

# Legacy text output
text = model.response("Tell me about...")  # Still works as before
```

================================================================================
**User asked:** Great! Does the AI model see the field description in the Pydantic definition?...
**Response (msg #7, 2904 chars):**

The user is asking whether the AI model can see the field descriptions that are defined in the Pydantic model using the `Field()` function with the `description` parameter.

This is an important question because it affects how well the model can understand what to populate in each field.

From what I know:
1. For OpenAI's structured outputs, the Pydantic model gets converted to a JSON schema, and the descriptions ARE included in that schema and sent to the model.
2. For Claude's structured outputs with `transform_schema()`, the descriptions should also be included in the JSON schema that gets sent to the model.

The descriptions are very helpful for the model to understand what each field should contain. They're part of the JSON schema specification, so yes, the model does see them.

I should confirm this is true and explain how it works.**Yes!** The AI model absolutely sees the field descriptions. They're crucial for helping the model understand what to put in each field.

When you use `Field(description="...")`, that description gets included in the JSON schema that's sent to the model. Here's what actually happens:

**Behind the scenes:**

Your Pydantic model:
```python
class AnalysisResult(BaseModel):
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level - must be one of 5 choices"
    )
    tags: List[str] = Field(
        description="List of relevant tags or categories"
    )
```

Gets converted to JSON schema like:
```json
{
  "type": "object",
  "properties": {
    "priority": {
      "type": "string",
      "enum": ["critical", "high", "medium", "low", "info"],
      "description": "Priority level - must be one of 5 choices"
    },
    "tags": {
      "type": "array",
      "items": {"type": "string"},
      "description": "List of relevant tags or categories"
    }
  }
}
```

The model uses these descriptions to understand what you want, so **good descriptions are important!** They act like inline prompts for each field.

**Best practices for descriptions:**

```python
class BetterAnalysisResult(BaseModel):
    summary: str = Field(
        description="A concise 1-2 sentence summary of the main issue or task"
    )
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level: critical=security/data loss, high=blocks work, medium=important but not urgent, low=nice to have, info=FYI only"
    )
    tags: List[str] = Field(
        description="Relevant technical tags like programming languages, systems, or categories. Use lowercase kebab-case (e.g., 'oauth', 'api-security')"
    )
    due_date: date = Field(
        description="Target completion date. Use today's date + appropriate days based on priority (critical=today, high=3 days, medium=1 week)"
    )
```

The more specific your descriptions, the better the model's output will be!

================================================================================
**User asked:** Thanks. I added that token counter for Claude because earlier (May 2025) I was burning through my rate limit and getting errors. Do I still need to do that, or is there a better way now?...
**Response (msg #9, 6656 chars):**

The user is asking about the token counting and rate limiting logic they have in their code for Claude. Let me search for the latest information about Claude's rate limits and best practices for handling them.

Looking at their code, they have:
1. Token truncation logic to stay under 40K tokens
2. A manual rate limiting system that tracks tokens used in the last minute and waits if approaching 40K tokens/minute

This is from May 2025 and they're asking if there's a better way now (we're in November 2025).

I should search for:
1. Current Claude API rate limits
2. Best practices for rate limiting
3. Whether there are built-in retry mechanisms or better approaches
```
This block is not supported on your current device yet.
```

Good information. Let me search for more specific information about error handling and retry mechanisms.
```
This block is not supported on your current device yet.
```

Great, I have enough information. Let me provide a comprehensive answer about whether the user still needs their custom token counter or if there's a better way now.

Key points:
1. The API now includes rate limit headers that show current usage
2. Exponential backoff with retry is the modern best practice
3. Token bucket algorithm is what Claude uses (continuous refill, not fixed reset)
4. The user's manual tracking is outdated - there are better approaches
5. The 40K tokens per minute limit still exists but varies by tier**Good news: You can replace that custom tracking with a much simpler approach!** Your manual token counting was a reasonable workaround in May 2025, but there are better methods now:

## What's Changed

The Claude API now includes response headers that show your current rate limit status:

```python
# The API returns these headers with every response:
# anthropic-ratelimit-requests-limit
# anthropic-ratelimit-requests-remaining  
# anthropic-ratelimit-requests-reset
# anthropic-ratelimit-tokens-limit
# anthropic-ratelimit-tokens-remaining
# anthropic-ratelimit-tokens-reset
```

Claude uses a token bucket algorithm with continuous replenishment rather than fixed reset windows, so your approach of tracking "tokens in the last minute" was fighting against how the system actually works.

## Modern Best Practice: Exponential Backoff with Retries

Here's the recommended approach for your `ModelWrapper`:

```python
import time
from anthropic import RateLimitError, APIError

class ModelWrapper(object):
    def __init__(self, ...):
        # Remove self.token_count = []
        self.max_retries = 5
        self.base_delay = 1.0
        # ... rest of your init

    def response_claude(self, messages, max_tokens, callback=None, response_model=None):
        """Claude response with built-in retry logic"""
        
        system_message = [a for a in messages if a["role"] == "system"][0]['content']
        messages = [b for b in messages if b['role'] != "system"]
        
        if self.test:
            return "This is a test response"
        
        # Retry with exponential backoff
        for attempt in range(self.max_retries):
            try:
                if response_model:
                    from anthropic import transform_schema
                    ret = self.client.beta.messages.create(
                        system=system_message,
                        model=self.model_version,
                        max_tokens=max_tokens,
                        messages=messages,
                        betas=["structured-outputs-2025-11-13"],
                        output_format=transform_schema(response_model)
                    )
                    resp_text = ret.content[0].text
                    resp = response_model.model_validate_json(resp_text)
                else:
                    ret = self.client.messages.create(
                        system=system_message,
                        model=self.model_version,
                        max_tokens=max_tokens,
                        messages=messages
                    )
                    resp = ret.content[0].text
                
                # Log rate limit info from headers (optional)
                # You can access these from ret.headers if needed
                
                if callback is not None:
                    resp_text = resp if isinstance(resp, str) else resp.model_dump_json()
                    # Use actual token counts from response
                    input_tokens = ret.usage.input_tokens
                    callback(input_tokens, messages[-1]["content"], resp_text)
                    
                return resp
                
            except RateLimitError as e:
                if attempt == self.max_retries - 1:
                    raise  # Final attempt failed
                    
                # Exponential backoff with jitter
                delay = self.base_delay * (2 ** attempt)
                jitter = delay * 0.1 * (2 * time.random() - 1)  # ±10% jitter
                wait_time = delay + jitter
                
                logger.warning(f"Rate limit hit. Waiting {wait_time:.2f}s before retry {attempt + 1}/{self.max_retries}")
                time.sleep(wait_time)
                
            except APIError as e:
                logger.error(f"API error: {e}")
                raise
```

## Key Improvements Over Your Old Approach

1. **No manual token tracking** - The API tells you when you hit limits
2. **Exponential backoff** - Industry standard: wait 1s, 2s, 4s, 8s, etc. between retries
3. **Jitter** - Adds random delay to prevent "retry storms" when multiple clients retry simultaneously
4. **Simpler** - No need to track `self.token_count` or calculate windows
5. **Works with token bucket** - Continuous refill means retrying after a delay actually works

## Optional: Rate Limit Monitoring

If you want visibility into your limits without manual tracking:

```python
def log_rate_limits(self, response):
    """Optional: log current rate limit status from API headers"""
    if hasattr(response, 'headers'):
        remaining = response.headers.get('anthropic-ratelimit-tokens-remaining')
        limit = response.headers.get('anthropic-ratelimit-tokens-limit')
        reset = response.headers.get('anthropic-ratelimit-tokens-reset')
        
        if remaining and limit:
            logger.info(f"Rate limit: {remaining}/{limit} tokens remaining. Resets at {reset}")
```

**Bottom line:** Remove the manual `token_count` tracking and `while True` loop. Just add exponential backoff retry logic and let the API tell you when you've hit limits. It's simpler, more reliable, and aligns with how the system actually works!

================================================================================
**User asked:** result = model.response(     281     prompt=prompt,     282     response_model=AnalysisResult,     283     max_tokens=2000     284 )

BadRequestError: Error code: 400 - {'error': {'message': "Invalid ...
**Response (msg #11, 3963 chars):**

The error is indicating that there's an issue with the JSON schema generated from the Pydantic model. The error says that 'required' must be an array including every key in properties, but there's an extra required key 'metadata' supplied.

Looking at the AnalysisResult model I provided:

```python
class AnalysisResult(BaseModel):
    summary: str = Field(description="Freeform text summary of the analysis")
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level - must be one of 5 choices"
    )
    metadata: Dict[str, str] = Field(
        description="Dictionary of key-value metadata pairs"
    )
    tags: List[str] = Field(
        description="List of relevant tags or categories"
    )
    due_date: date = Field(
        description="Target completion date in YYYY-MM-DD format"
    )
    scores: Optional[Dict[str, float]] = Field(
        default=None,
        description="Optional dictionary of numeric scores"
    )
```

The issue is that `metadata` is likely a reserved/special field name in Pydantic or there's something about the schema transformation. Actually, looking at the error more carefully - it says "Extra required key 'metadata' supplied" - this suggests that the JSON schema has 'metadata' in the required array but it shouldn't be there, or there's a conflict.

Actually, "metadata" is a special key in JSON Schema itself! It's used for schema metadata. So when Pydantic converts to JSON schema, there might be a conflict.

The fix is simple: rename the field from `metadata` to something else like `meta_info`, `data`, or `attributes`.The issue is that **`metadata` is a reserved keyword in JSON Schema**! It conflicts with the schema's own metadata field. Let's rename it:

```python
from datetime import date
from typing import Optional, List, Dict, Literal
from pydantic import BaseModel, Field

class AnalysisResult(BaseModel):
    """Sample structured output model for testing"""
    summary: str = Field(description="Freeform text summary of the analysis")
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level - must be one of 5 choices"
    )
    attributes: Dict[str, str] = Field(  # Changed from 'metadata'
        description="Dictionary of key-value attribute pairs"
    )
    tags: List[str] = Field(
        description="List of relevant tags or categories"
    )
    due_date: date = Field(
        description="Target completion date in YYYY-MM-DD format"
    )
    scores: Optional[Dict[str, float]] = Field(
        default=None,
        description="Optional dictionary of numeric scores"
    )
```

**Alternative fix if you really need the field named "metadata":**

Use Pydantic's `alias` feature to map a different internal name:

```python
class AnalysisResult(BaseModel):
    summary: str = Field(description="Freeform text summary of the analysis")
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level - must be one of 5 choices"
    )
    meta_info: Dict[str, str] = Field(
        alias="metadata",  # Will appear as "metadata" in JSON
        description="Dictionary of key-value metadata pairs"
    )
    tags: List[str] = Field(description="List of relevant tags or categories")
    due_date: date = Field(description="Target completion date in YYYY-MM-DD format")
    scores: Optional[Dict[str, float]] = Field(
        default=None,
        description="Optional dictionary of numeric scores"
    )
    
    class Config:
        populate_by_name = True  # Allow access by alias or field name
```

**The simplest solution is to just rename it** to `attributes`, `properties`, `custom_data`, or similar. Common alternatives:
- `attributes` - generic key-value pairs
- `properties` - property bag
- `custom_fields` - user-defined fields  
- `extra_data` - additional information

Replace the model definition and try again!

================================================================================
**User asked:** Changed:


```python
class AnalysisResult(BaseModel):
    """Sample structured output model for testing"""
    summary: str = Field(description="Freeform text summary of the analysis")
    priority: L...
**Response (msg #13, 4364 chars):**

Interesting - the error message says "'required' is required to be supplied and to be an array including every key in properties. Extra required key 'analysis' supplied."

This is an OpenAI-specific error about JSON schema validation. The issue is that OpenAI's structured outputs have stricter requirements. Let me think about what's happening:

1. The error says "Extra required key 'analysis' supplied" - this suggests that the schema is being generated with 'analysis' in the required array, but OpenAI is rejecting it
2. The message says "'required' is required to be supplied and to be an array including every key in properties"

Wait, I think I see the issue. When Pydantic generates the JSON schema, it might be adding fields to `required` that OpenAI doesn't expect, or there's a mismatch.

Actually, looking at the error more carefully: "Extra required key 'analysis' supplied" - this suggests that 'analysis' is in the required array but shouldn't be there according to OpenAI's validation.

But wait - all the fields are required in the Pydantic model (they don't have defaults). So they should all be in required.

Let me re-read: "In context=(), 'required' is required to be supplied and to be an array including every key in properties."

This means required must include EVERY key in properties. But then it says "Extra required key 'analysis' supplied" - which is contradictory.

Unless... maybe there's an issue with how the schema is being transformed? Or maybe 'analysis' is also a reserved word in OpenAI's schema?

Actually, looking at the user's code, they're using `response_format=response_model` for OpenAI. Let me check the implementation in their code:

```python
if response_model:
    # Use structured outputs with Pydantic
    completion = self.client.beta.chat.completions.parse(
        model=self.model_version,
        messages=messages,
        response_format=response_model,
    )
```

I suspect the problem involves reserved keywords in OpenAI's JSON schema validation. Certain field names like 'metadata', 'properties', 'type', 'items', 'required', and 'additionalProperties' could be causing conflicts. The 'analysis' field might be triggering a specific validation restriction that's not immediately obvious.

A strategic approach would be renaming potentially problematic fields to unique, non-standard names that avoid JSON schema reserved terms.It looks like `analysis` is also causing issues! This suggests the JSON Schema transformation is having problems with certain field names. Let me give you a model with field names that definitely won't conflict:

```python
from datetime import date
from typing import Optional, List, Dict, Literal
from pydantic import BaseModel, Field

class AnalysisResult(BaseModel):
    """Sample structured output model for testing"""
    summary: str = Field(description="Freeform text summary of the analysis")
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level - must be one of 5 choices"
    )
    key_values: Dict[str, str] = Field(  # Changed from 'analysis'
        description="Dictionary of key-value pairs"
    )
    tags: List[str] = Field(
        description="List of relevant tags or categories"
    )
    due_date: date = Field(
        description="Target completion date in YYYY-MM-DD format"
    )
    scores: Optional[Dict[str, float]] = Field(
        default=None,
        description="Optional dictionary of numeric scores"
    )
```

**Alternatively, let's debug this properly.** Can you add this debug code to see what schema is actually being generated?

```python
# Add before the API call in response_openai():
if response_model:
    schema = response_model.model_json_schema()
    print("Generated schema:")
    print(json.dumps(schema, indent=2))
    
    # Then make the API call
    completion = self.client.beta.chat.completions.parse(...)
```

This will show us exactly what JSON schema Pydantic is generating, which might reveal the issue. 

**Also try simplifying to test:**

```python
class SimpleTest(BaseModel):
    name: str
    value: int
```

If even this simple model fails, there might be an issue with your OpenAI SDK version or the model string. Make sure you're using:
- `openai>=1.40.0` 
- `model="gpt-4o-2024-08-06"` or newer

What happens when you try the `SimpleTest` model?

================================================================================
**User asked:** Completions' object has no attribute 'parse'...
**Response (msg #15, 3359 chars):**

Ah! The user is getting an error that `Completions` object has no attribute `parse`. This means they're using the wrong path in the OpenAI client.

The correct path is `client.beta.chat.completions.parse()`, not `client.chat.completions.parse()`.

Looking at my code, I have:
```python
completion = self.client.beta.chat.completions.parse(
```

But it seems like maybe the user's SDK doesn't have the `beta` accessor, or there's a version issue.

Let me check what I recommended:
- In the initial code I provided, I used `self.client.beta.chat.completions.parse()`
- This is correct for structured outputs

The error suggests either:
1. Old OpenAI SDK version (needs to be >= 1.40.0 for structured outputs)
2. The client isn't being accessed correctly

Let me provide a fix that checks the version and provides the correct import/usage.Ah! You need to update your OpenAI library. The `parse()` method for structured outputs requires **OpenAI SDK version 1.40.0 or higher**.

**Quick fix:**

```bash
pip install --upgrade openai
```

**Then verify your version:**

```python
import openai
print(openai.__version__)  # Should be >= 1.40.0
```

**If you can't upgrade right now, here's a fallback using the older approach:**

```python
def response_openai(self, messages, callback=None, response_model: Optional[BaseModel] = None):
    messages_str = "\n".join([f"{el['role'].upper()}: {el['content']}" for el in messages])
    logger.prompt(f"OPENAI - messages: {messages_str}")

    if response_model:
        # Check if SDK supports structured outputs
        try:
            # New way (OpenAI SDK >= 1.40.0)
            completion = self.client.beta.chat.completions.parse(
                model=self.model_version,
                messages=messages,
                response_format=response_model,
            )
            resp = completion.choices[0].message.parsed
        except AttributeError:
            # Fallback for older SDK versions
            import json
            schema = response_model.model_json_schema()
            
            completion = self.client.chat.completions.create(
                model=self.model_version,
                messages=messages,
                response_format={"type": "json_object"},
                functions=[{
                    "name": "structured_output",
                    "description": "Return structured data",
                    "parameters": schema
                }],
                function_call={"name": "structured_output"}
            )
            
            # Parse the function call result
            func_args = completion.choices[0].message.function_call.arguments
            resp = response_model.model_validate_json(func_args)
    else:
        # Legacy text output
        completion = self.client.chat.completions.create(
            model=self.model_version,
            messages=messages,
        )
        resp = completion.choices[0].message.content
        
    if callback is not None:
        tokens_in = int(len(messages_str))
        resp_text = resp if isinstance(resp, str) else resp.model_dump_json()
        callback(tokens_in, messages_str, resp_text)
        
    return resp
```

**But honestly, just upgrade:**

```bash
pip install "openai>=1.40.0"
```

The new `.parse()` method is much cleaner and more reliable than the old function-calling workaround!

================================================================================
**User asked:** BadRequestError: Error code: 400 - {'error': {'message': "Invalid schema for response_format 'AnalysisResult': In context=(), 'required' is required to be supplied and to be an array including every k...
**Response (msg #17, 3381 chars):**

The user is still getting the error about the 'analysis' field even though they changed it to `key_values`. This is strange. Let me think about what could be happening:

1. The error message still says "Extra required key 'analysis' supplied" - which suggests they might not have restarted their Python process or the old model is still cached
2. Or they might still have the old field name somewhere

But wait, looking at the error message more carefully: "In context=(), 'required' is required to be supplied and to be an array including every key in properties."

This is a schema validation error from OpenAI. The issue is that OpenAI expects the 'required' field in the JSON schema to list ALL properties, but Pydantic is generating a schema where some field is in 'required' that isn't in 'properties', or vice versa.

Actually, the issue with `date` type! The `date` field type might not be directly supported by OpenAI's structured outputs. Let me check - OpenAI's structured outputs support a subset of JSON Schema, and `date` is a Python type that gets converted to a string format in JSON Schema.

Let me suggest:
1. Make sure they've restarted/reloaded
2. Try changing `date` to `str` with a description
3. Show them how to see the actual schema being generated

The error message specifically mentions 'analysis' still, so they either:
- Haven't saved the file
- Haven't restarted the Python interpreter
- Are looking at a different file
- Have a cached import

Let me address this.The error still mentions `'analysis'` - which means your code change **hasn't taken effect**. This happens when:

1. **You haven't restarted your Python process** (if running in a REPL/notebook)
2. **The module hasn't been reloaded** (cached import)
3. **You're editing a different file** than the one being executed

**Fix:**

```python
# If in Jupyter/IPython, restart the kernel
# If running a script, just re-run it fresh

# Or add at the top of your test script:
import importlib
import your_module_name
importlib.reload(your_module_name)
```

**But also, the `date` type might be causing issues.** Try this simpler model first:

```python
from typing import Optional, List, Dict, Literal
from pydantic import BaseModel, Field

class AnalysisResult(BaseModel):
    """Sample structured output model for testing"""
    summary: str = Field(description="Freeform text summary of the analysis")
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level - must be one of 5 choices"
    )
    key_values: Dict[str, str] = Field(
        description="Dictionary of key-value pairs"
    )
    tags: List[str] = Field(
        description="List of relevant tags or categories"
    )
    due_date: str = Field(  # Changed from date to str
        description="Target completion date in YYYY-MM-DD format"
    )
    scores: Optional[Dict[str, float]] = Field(
        default=None,
        description="Optional dictionary of numeric scores"
    )
```

**To verify the schema being sent, add this debugging:**

```python
# Before calling the API:
if response_model:
    import json
    schema = response_model.model_json_schema()
    print("=" * 80)
    print("GENERATED SCHEMA:")
    print(json.dumps(schema, indent=2))
    print("=" * 80)
```

This will show you exactly what's being sent to OpenAI. Share the output if it still fails!

================================================================================
**User asked:** BadRequestError: Error code: 400 - {'error': {'message': "Invalid schema for response_format 'AnalysisResult': In context=(), 'required' is required to be supplied and to be an array including every k...
**Response (msg #19, 4351 chars):**

The error is saying that there's an extra required key being supplied. The error message is "In context=(), 'required' is required to be supplied and to be an array including every key in properties. Extra required key 'key_values' supplied."

This is strange. It seems like the schema transformation is having issues. Let me think about what could be wrong.

The issue might be with how Pydantic generates the JSON schema and how OpenAI's structured outputs expects it. OpenAI expects all fields in `properties` to be listed in `required`, but it seems like there's an extra field being added somehow.

Wait, I notice the user is using `transform_schema` for Claude but for OpenAI they're using `response_format=response_model` directly. Let me check if there's an issue with how the Pydantic model is being passed.

Actually, looking at the error pattern - it keeps saying "Extra required key" for whatever field name we use. This suggests the issue is with the schema generation itself, not the field names.

The problem might be that Pydantic is generating additional keys in the schema that OpenAI doesn't expect. Let me suggest using Pydantic's `ConfigDict` to control schema generation more strictly.

Or maybe the issue is with `Optional[Dict[str, float]]` - the optional field might be causing schema issues.

Let me suggest removing the optional field first to see if that's the issue.Ah! The pattern is clear now - **every field name triggers the same error**. The issue is with the **schema generation**, not the field names.

The problem is likely the `Optional` field causing schema issues. Let's test without it:

```python
from typing import List, Dict, Literal
from pydantic import BaseModel, Field

class AnalysisResult(BaseModel):
    """Sample structured output model for testing"""
    summary: str = Field(description="Freeform text summary of the analysis")
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level - must be one of 5 choices"
    )
    key_values: Dict[str, str] = Field(
        description="Dictionary of key-value pairs"
    )
    tags: List[str] = Field(
        description="List of relevant tags or categories"
    )
    due_date: str = Field(
        description="Target completion date in YYYY-MM-DD format"
    )
    
    # Remove Optional field for now
```

**If that still fails, the issue is with OpenAI's new schema validation. Try this workaround:**

In your `response_openai` method, use the JSON schema directly instead of passing the Pydantic model:

```python
def response_openai(self, messages, callback=None, response_model: Optional[BaseModel] = None):
    messages_str = "\n".join([f"{el['role'].upper()}: {el['content']}" for el in messages])
    logger.prompt(f"OPENAI - messages: {messages_str}")

    if response_model:
        # Get the schema and fix it for OpenAI
        schema = response_model.model_json_schema()
        
        # OpenAI wants a strict schema - remove extra keys
        clean_schema = {
            "type": "object",
            "properties": schema.get("properties", {}),
            "required": list(schema.get("properties", {}).keys()),
            "additionalProperties": False
        }
        
        completion = self.client.beta.chat.completions.parse(
            model=self.model_version,
            messages=messages,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": response_model.__name__,
                    "schema": clean_schema,
                    "strict": True
                }
            }
        )
        
        # Parse the response
        resp_text = completion.choices[0].message.content
        resp = response_model.model_validate_json(resp_text)
    else:
        completion = self.client.chat.completions.create(
            model=self.model_version,
            messages=messages,
        )
        resp = completion.choices[0].message.content
        
    if callback is not None:
        tokens_in = int(len(messages_str))
        resp_text = resp if isinstance(resp, str) else resp.model_dump_json()
        callback(tokens_in, messages_str, resp_text)
        
    return resp
```

This manually constructs a clean schema that OpenAI expects. Try this and let me know if it works!

================================================================================
**User asked:** Ok, that worked. Now running claude:
BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': "output_format.type: Input should be 'json_schema'"}, 'r...
**Response (msg #23, 4318 chars):**

The user is now getting an error from Claude. The error says `"output_format.type: Input should be 'json_schema'"`. 

Looking at the code I provided earlier for Claude, I used `transform_schema()` which might not be formatting it correctly. Let me check what the correct format should be based on the search results I got earlier.

From the search results, I saw that Claude's structured outputs require:
- The beta header: `"structured-outputs-2025-11-13"`
- The `output_format` parameter with `type: "json_schema"` and a `schema` definition

In the code I provided, I used:
```python
output_format=transform_schema(response_model)
```

But `transform_schema()` might be returning the wrong format. Based on the documentation, it should be:
```python
output_format={
    "type": "json_schema",
    "schema": {...}
}
```

Let me fix the Claude implementation.The issue is with how we're formatting the schema for Claude. The `transform_schema()` helper might not be returning the right format. Let's fix the `response_claude` method:

```python
def response_claude(
    self, 
    messages, 
    max_tokens, 
    check_tokens=True, 
    callback=None,
    response_model: Optional[BaseModel] = None
):
    def truncate_string(s):
        tokens = self.count_tokens_claude(s)
        logger.info(f"Token count: {tokens}")
        if tokens > 40000:
            excess_tokens = tokens - 40000
            excess_chars = max(int(excess_tokens * 2.4), 1000)
            s = s[:len(s) - excess_chars]
            logger.info(f"Truncated prompt to {len(s)} characters, {tokens} tokens")
        return s, tokens

    prompt = messages[-1]["content"]
    prompt, tokens = truncate_string(prompt)
    
    if check_tokens:
        while tokens > 40000:
            prompt, tokens = truncate_string(prompt)
        messages[-1]["content"] = prompt
        
        while True:
            tokens_last_minute = [t['tokens'] for t in self.token_count if t["time"] > datetime.now() - timedelta(minutes=1)]
            tokens_last_minute = sum(tokens_last_minute)
            if tokens_last_minute + tokens > 40000:
                print("Token count would be: ", tokens_last_minute + tokens, "Waiting 5 seconds.")
                time.sleep(5)
            else:
                break
                
    logger.prompt(f"CLAUDE - messages: {messages}")
    system_message = [a for a in messages if a["role"] == "system"][0]['content']
    messages = [b for b in messages if b['role'] != "system"]
    
    if self.test:
        return "This is a test response"
    
    if response_model:
        # Use structured outputs with proper format for Claude
        schema = response_model.model_json_schema()
        
        # Clean schema for Claude (similar to OpenAI)
        clean_schema = {
            "type": "object",
            "properties": schema.get("properties", {}),
            "required": list(schema.get("properties", {}).keys()),
            "additionalProperties": False
        }
        
        ret = self.client.beta.messages.create(
            system=system_message,
            model=self.model_version,
            max_tokens=max_tokens,
            messages=messages,
            betas=["structured-outputs-2025-11-13"],
            output_format={
                "type": "json_schema",
                "schema": clean_schema
            }
        )
        # Parse the JSON response into Pydantic model
        resp_text = ret.content[0].text
        resp = response_model.model_validate_json(resp_text)
    else:
        # Legacy text output
        ret = self.client.messages.create(
            system=system_message,
            model=self.model_version,
            max_tokens=max_tokens,
            messages=messages
        )
        resp = ret.content[0].text
    
    print(f"calling callback {callback}")
    if callback is not None: 
        resp_text = resp if isinstance(resp, str) else resp.model_dump_json()
        callback(tokens, prompt, resp_text)
        
    return resp
```

The key change is:
```python
output_format={
    "type": "json_schema",  # Must be exactly this
    "schema": clean_schema   # Not "json_schema" wrapper
}
```

Instead of:
```python
output_format=transform_schema(response_model)  # Wrong format
```

Try this and it should work for both OpenAI and Claude!

================================================================================
**User asked:** Now:  I am storing my data in mongodb and displaying it in Pandas. I have a Datastore class that uses Pydantic models to normalize each collection. Here is the class:


```python

class DataStore:
   ...
**Response (msg #27, 5954 chars):**

The user is showing me their DataStore class that uses Pydantic models with MongoDB and Pandas. They named one method `asdf` which is clearly a placeholder/temporary name. They're probably asking me to help improve this class or identify issues.

Let me review the code:

1. The class uses Pydantic models for validation
2. It has basic CRUD operations
3. There's a method called `asdf` that converts to DataFrame - this is obviously a placeholder name

Issues I notice:
1. The `asdf` method should have a better name like `to_dataframe` or `as_dataframe`
2. The method could be more efficient - it's converting docs to models then back to dicts
3. The `find` method returns raw cursor/docs but doesn't use `_from_doc` to convert to Pydantic models
4. There's inconsistency - `find` returns raw docs, `find_one` returns a Pydantic model
5. The `asdf` method calls `_from_doc` on objects from `find()`, but `find()` returns raw MongoDB documents, not Pydantic models, so this should work but is inefficient

Let me suggest improvements.Nice DataStore class! I see you have a method called `asdf` 😄 - I'm guessing you want a better name for that?

Here are some suggestions to improve the class:

```python
class DataStore:
    def __init__(self, collection_name, model_cls, local=True, db_name="rainmaker"):
        self.client = MongoClient(LOCAL_URI if local else REMOTE_URI)
        self.coll = self.client[db_name][collection_name]
        self.model_cls = model_cls

    def insert(self, model):
        """Insert a single Pydantic model."""
        self.coll.insert_one(model.model_dump(by_alias=True))
        return model

    def find(self, query=None, as_models=True):
        """
        Find documents matching query.
        
        Args:
            query: MongoDB query dict
            as_models: If True, return Pydantic models; if False, return raw dicts
        """
        docs = self.coll.find(query or {})
        if as_models:
            return [self._from_doc(doc) for doc in docs]
        return list(docs)

    def find_one(self, **query):
        """Find a single document and return as Pydantic model."""
        doc = self.coll.find_one(query)
        return self._from_doc(doc)
    
    def update_one(self, query, update):
        """Update a single document. Raises error if multiple match."""
        if self.coll.count_documents(query) > 1:
            raise ValueError("update_one called but multiple documents match the query")
        self.coll.update_one(query, {"$set": update}, upsert=True)
    
    def save(self, obj):
        """Insert or replace document by _id."""
        doc = self._to_doc(obj, by_alias=True)
        if not doc.get("_id"):
            raise ValueError("Cannot save document without _id field")
        self.coll.replace_one({"_id": doc.get("_id")}, doc, upsert=True)
        return obj
    
    def delete_one(self, query):
        """Delete a single document matching query."""
        return self.coll.delete_one(query)
    
    def delete_many(self, query):
        """Delete all documents matching query."""
        return self.coll.delete_many(query)
    
    def count_documents(self, query=None):
        """Count documents matching query."""
        return self.coll.count_documents(query or {})

    def _to_doc(self, obj, by_alias=False):
        """Convert a Pydantic model to a Mongo document."""
        return obj.model_dump(by_alias=by_alias)

    def _from_doc(self, doc):
        """Rebuild a Pydantic model from a Mongo document."""
        if not doc:
            return None
        return self.model_cls.model_validate(doc)

    def to_dataframe(self, query=None, exclude_id=True):
        """
        Return documents as a pandas DataFrame.
        
        Args:
            query: MongoDB query dict
            exclude_id: If True, exclude MongoDB's _id field from DataFrame
        """
        docs = list(self.coll.find(query or {}))
        if not docs:
            return pd.DataFrame()
        
        # Convert to Pydantic models then to dicts for consistent field handling
        data = [self._from_doc(doc).model_dump() for doc in docs]
        df = pd.DataFrame(data)
        
        # Optionally remove MongoDB _id field
        if exclude_id and '_id' in df.columns:
            df = df.drop(columns=['_id'])
        
        return df
    
    def from_dataframe(self, df, batch_size=100):
        """
        Insert multiple records from a pandas DataFrame.
        
        Args:
            df: pandas DataFrame with data to insert
            batch_size: Number of documents to insert at once
        """
        records = df.to_dict('records')
        models = [self.model_cls.model_validate(record) for record in records]
        docs = [model.model_dump(by_alias=True) for model in models]
        
        # Insert in batches
        inserted = 0
        for i in range(0, len(docs), batch_size):
            batch = docs[i:i + batch_size]
            self.coll.insert_many(batch)
            inserted += len(batch)
        
        return inserted
```

**Key improvements:**

1. **Renamed `asdf` → `to_dataframe`** with better options
2. **Added `from_dataframe`** for inserting from pandas
3. **Made `find()` consistent** - now returns Pydantic models by default
4. **Added `delete_one` and `delete_many`** for completeness
5. **Better docstrings** explaining parameters
6. **Added `exclude_id` option** to remove MongoDB's `_id` from DataFrames (usually not needed for analysis)
7. **Return values** from `insert` and `save` for method chaining

**Usage examples:**

```python
# Get data as DataFrame
df = store.to_dataframe(query={"priority": "high"})

# Insert from DataFrame
new_df = pd.DataFrame([...])
count = store.from_dataframe(new_df)

# Find as models (new default)
models = store.find({"status": "active"})

# Find as raw dicts (if needed)
raw_docs = store.find({"status": "active"}, as_models=False)
```

Does this look good?

================================================================================
**User asked:** No! asdf = asDataFrame. Gotta keep it light....
**Response (msg #29, 1369 chars):**

Haha, I love it! The user wants to keep `asdf` as a shorthand for "asDataFrame" - it's intentionally punny/convenient. I totally misread that as a typo. That's actually pretty clever for quick interactive work.

I should acknowledge this and maybe suggest keeping it but also offering some other improvements to the class that are actually useful, not trying to "fix" their naming choice.Ha! I love it - `asdf` = "asDataFrame" 🤣 That's actually brilliant for quick exploratory work. Keep it!

My bad for trying to "fix" your genius abbreviation. The class looks solid as-is then!

Only real suggestions would be:

1. **Maybe add a proper `__repr__`** for debugging:
```python
def __repr__(self):
    return f"DataStore(collection={self.coll.name}, model={self.model_cls.__name__}, count={self.count_documents()})"
```

2. **Batch insert** if you ever need it:
```python
def insert_many(self, models):
    """Insert multiple Pydantic models at once."""
    docs = [m.model_dump(by_alias=True) for m in models]
    return self.coll.insert_many(docs)
```

3. **Maybe a convenience method for common queries**:
```python
def all(self):
    """Get all documents as Pydantic models."""
    return [self._from_doc(doc) for doc in self.find()]
```

But honestly, your class is clean and practical. `asdf()` is staying in my mental toolkit now for quick DataFrame conversions! 😄

================================================================================
**User asked:** Ok, good suggestions. What about more type checking/indication?...
**Response (msg #31, 6155 chars):**

The user wants better type hints/type checking for their DataStore class. Let me add comprehensive type annotations using Python's typing module. This will help with IDE autocomplete, type checking with mypy, and general code clarity.

Key things to add:
1. Type hints for all parameters and return types
2. Use generics so DataStore[MyModel] knows what model type it works with
3. Type hints for MongoDB-specific types
4. Optional type hints for things that can be None
5. Use TypeVar for the generic model class

Let me write a well-typed version:Great idea! Let's add proper type hints. Here's a fully typed version:

```python
from typing import TypeVar, Generic, Type, Optional, Dict, Any, List
from pydantic import BaseModel
import pandas as pd
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.results import InsertOneResult, UpdateResult, DeleteResult

# Generic type for any Pydantic model
T = TypeVar('T', bound=BaseModel)


class DataStore(Generic[T]):
    """
    Type-safe MongoDB wrapper with Pydantic model validation.
    
    Usage:
        class User(BaseModel):
            name: str
            age: int
        
        store = DataStore[User]("users", User)
        user = store.find_one(name="Alice")  # Returns User | None
        users = store.find()  # Returns List[User]
        df = store.asdf()  # Returns pd.DataFrame
    """
    
    def __init__(
        self, 
        collection_name: str, 
        model_cls: Type[T], 
        local: bool = True, 
        db_name: str = "rainmaker"
    ):
        self.client: MongoClient = MongoClient(LOCAL_URI if local else REMOTE_URI)
        self.coll: Collection = self.client[db_name][collection_name]
        self.model_cls: Type[T] = model_cls

    def insert(self, model: T) -> InsertOneResult:
        """Insert a single Pydantic model."""
        return self.coll.insert_one(model.model_dump(by_alias=True))
    
    def insert_many(self, models: List[T]) -> List[Any]:
        """Insert multiple Pydantic models at once."""
        docs = [m.model_dump(by_alias=True) for m in models]
        result = self.coll.insert_many(docs)
        return result.inserted_ids

    def find(self, query: Optional[Dict[str, Any]] = None) -> List[T]:
        """Find documents matching query and return as Pydantic models."""
        docs = self.coll.find(query or {})
        return [self._from_doc(doc) for doc in docs]

    def find_one(self, **query: Any) -> Optional[T]:
        """Find a single document and return as Pydantic model."""
        doc = self.coll.find_one(query)
        return self._from_doc(doc)
    
    def update_one(self, query: Dict[str, Any], update: Dict[str, Any]) -> UpdateResult:
        """Update a single document. Raises error if multiple match."""
        if self.coll.count_documents(query) > 1:
            raise ValueError("update_one called but multiple documents match the query")
        return self.coll.update_one(query, {"$set": update}, upsert=True)
    
    def save(self, obj: T) -> T:
        """Insert or replace document by _id. Returns the object."""
        doc = self._to_doc(obj, by_alias=True)
        if not doc.get("_id"):
            raise ValueError("Cannot save document without _id field")
        self.coll.replace_one({"_id": doc.get("_id")}, doc, upsert=True)
        return obj
    
    def delete_one(self, query: Dict[str, Any]) -> DeleteResult:
        """Delete a single document matching query."""
        return self.coll.delete_one(query)
    
    def delete_many(self, query: Dict[str, Any]) -> DeleteResult:
        """Delete all documents matching query."""
        return self.coll.delete_many(query)
    
    def count_documents(self, query: Optional[Dict[str, Any]] = None) -> int:
        """Count documents matching query."""
        return self.coll.count_documents(query or {})
    
    def all(self) -> List[T]:
        """Get all documents as Pydantic models."""
        return self.find()

    def _to_doc(self, obj: T, by_alias: bool = False) -> Dict[str, Any]:
        """Convert a Pydantic model to a Mongo document."""
        return obj.model_dump(by_alias=by_alias)

    def _from_doc(self, doc: Optional[Dict[str, Any]]) -> Optional[T]:
        """Rebuild a Pydantic model from a Mongo document."""
        if not doc:
            return None
        return self.model_cls.model_validate(doc)

    def asdf(self, query: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        """Return all documents as a pandas DataFrame."""
        objs = self.coll.find(query or {})
        docs = [self._from_doc(o) for o in objs]
        if not docs:
            return pd.DataFrame()
        return pd.DataFrame([d.model_dump() for d in docs if d is not None])
    
    def __repr__(self) -> str:
        return (
            f"DataStore[{self.model_cls.__name__}]("
            f"collection={self.coll.name}, "
            f"count={self.count_documents()})"
        )
```

**Key improvements:**

1. **`Generic[T]`** - Makes the class generic over the model type
2. **`Type[T]`** - Indicates `model_cls` is a class, not an instance
3. **`Optional[T]`** - Methods that can return None are properly typed
4. **`List[T]`** - Collections of models are typed
5. **MongoDB result types** - `InsertOneResult`, `UpdateResult`, etc.
6. **All parameters and returns typed** - Full IDE autocomplete support

**Usage with full type safety:**

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

# Type hints tell your IDE what to expect
store: DataStore[User] = DataStore("users", User)

# IDE knows user is Optional[User]
user = store.find_one(name="Alice")
if user:
    print(user.name)  # ✓ IDE autocompletes User fields
    
# IDE knows users is List[User]
users = store.find({"age": {"$gt": 18}})
for u in users:
    print(u.email)  # ✓ IDE autocompletes

# IDE knows df is pd.DataFrame
df = store.asdf()
print(df.shape)  # ✓ IDE knows DataFrame methods
```

**With mypy/type checking:**

```bash
pip install mypy
mypy your_file.py  # Will catch type errors at dev time
```

Now your DataStore has full type safety! 🎯

================================================================================
**User asked:** What is this syntax? class DataStore(Generic[T]):
And can you explain how you're used/improved type-safety here?...
**Response (msg #33, 4546 chars):**

The user is asking about:
1. The `Generic[T]` syntax - what it means and how it works
2. How the type safety improvements actually help in practice

Let me explain both clearly.

## Generic[T] Syntax

`Generic[T]` is Python's way of creating generic classes - classes that can work with different types while maintaining type safety. It's like creating a template or container that can hold different types of things.

## How Type Safety Improved

Let me explain both the syntax and the practical benefits.Great question! Let me break down both.

## What is `Generic[T]`?

`Generic[T]` makes your class **generic** - meaning it can work with different types while the type checker knows which specific type you're using.

Think of it like this:

```python
# WITHOUT Generic[T] - type checker is clueless
store = DataStore("users", User)
user = store.find_one(name="Alice")  
# ❌ Type checker thinks: user could be anything! No autocomplete

# WITH Generic[T] - type checker is smart
store: DataStore[User] = DataStore("users", User)
user = store.find_one(name="Alice")
# ✅ Type checker knows: user is Optional[User]! Full autocomplete
```

**The syntax breakdown:**

```python
T = TypeVar('T', bound=BaseModel)  # Create a type variable
# "T can be any class that inherits from BaseModel"

class DataStore(Generic[T]):  
# "This class is generic over type T"
# Meaning: DataStore can work with User, Product, Order, etc.

    def __init__(self, collection_name: str, model_cls: Type[T]):
        #                                    ^^^^^^^^
        # "model_cls is a CLASS (not instance) of type T"
        self.model_cls: Type[T] = model_cls
    
    def find_one(self, **query) -> Optional[T]:
        #                          ^^^^^^^^^^^
        # "Returns either None or an instance of T"
        doc = self.coll.find_one(query)
        return self._from_doc(doc)
    
    def find(self, query=None) -> List[T]:
        #                         ^^^^^^^^
        # "Returns a list of T instances"
        ...
```

## How Type Safety Actually Helps

**Before (without types):**

```python
store = DataStore("users", User)
user = store.find_one(name="Alice")

# Your IDE doesn't know what 'user' is
user.  # <-- No autocomplete! Could be anything
print(user.name)  # ❌ IDE won't warn if User doesn't have 'name'
```

**After (with Generic[T]):**

```python
store: DataStore[User] = DataStore("users", User)
user = store.find_one(name="Alice")

# Your IDE KNOWS user is Optional[User]
if user:
    user.  # <-- ✅ Autocomplete shows: name, age, email, etc.
    print(user.name)  # ✅ IDE validates this field exists
    print(user.xyz)   # ❌ IDE warns: User has no field 'xyz'
```

**More examples:**

```python
# Type checker catches errors at DEVELOPMENT time (not runtime)

store: DataStore[User] = DataStore("users", User)

# ✅ Type checker is happy
users: List[User] = store.find({"age": {"$gt": 18}})
for u in users:
    print(u.email)  # Autocomplete works!

# ❌ Type checker warns you
users: List[str] = store.find()  # ERROR: find() returns List[User], not List[str]

# ❌ Type checker warns you
store.save("not a user")  # ERROR: save() expects User, not str

# ✅ Type checker is happy
new_user = User(name="Bob", age=25, email="bob@example.com")
store.save(new_user)
```

## Practical Benefits

1. **IDE Autocomplete** - Your editor knows what methods/fields are available
2. **Catch bugs early** - Type errors found while coding, not at runtime
3. **Self-documenting** - Types show what functions expect and return
4. **Refactoring safety** - Rename a field? Type checker finds all broken references
5. **Better teamwork** - Others know exactly what your code expects

## Do You Actually Need Generic[T]?

**Short answer: Not required, but VERY helpful for larger projects.**

You can keep it simpler:

```python
class DataStore:
    """Simpler version - still works, less type safety"""
    def __init__(self, collection_name: str, model_cls, local: bool = True):
        self.model_cls = model_cls
        # ...
    
    def find_one(self, **query):
        # Type checker doesn't know what this returns
        doc = self.coll.find_one(query)
        return self._from_doc(doc)
```

**When to use Generic[T]:**
- ✅ Working on a team
- ✅ Codebase with 1000+ lines
- ✅ Using mypy or IDE type checking
- ✅ Want autocomplete and safety

**When simpler types are fine:**
- ✅ Quick scripts / prototypes
- ✅ Solo projects
- ✅ You know your code well

Want me to show you a middle-ground version with some types but not full `Generic[T]`?

================================================================================
**User asked:** Sure. Also, should we require that the save() function receive a Pydantic object? 
And: let's say we have an AI model that uses Pydantic as the formatter to output the analysis related to an object. W...
**Response (msg #35, 10616 chars):**

The user is asking for:
1. A middle-ground version with some types but not full Generic[T]
2. Whether save() should require a Pydantic object (yes, it should for type safety)
3. How to merge AI output with additional data before saving

For the third question, they want to:
- Get structured output from AI (Pydantic model)
- Add extra fields (like the input prompt, timestamp, etc.)
- Save the combined data to MongoDB

Let me provide practical examples of how to do this.Great questions! Let me address all three:

## 1. Middle-Ground Typing (Practical, Not Full Generic)

```python
from typing import Optional, Dict, Any, List
from pydantic import BaseModel
import pandas as pd
from pymongo import MongoClient

class DataStore:
    """
    MongoDB wrapper with Pydantic validation.
    Uses simple types without Generic[T] - still helpful, less complex.
    """
    
    def __init__(
        self, 
        collection_name: str, 
        model_cls: type[BaseModel],  # Simple: "a Pydantic model class"
        local: bool = True, 
        db_name: str = "rainmaker"
    ):
        self.client: MongoClient = MongoClient(LOCAL_URI if local else REMOTE_URI)
        self.coll = self.client[db_name][collection_name]
        self.model_cls = model_cls

    def insert(self, model: BaseModel) -> Any:
        """Insert a single Pydantic model."""
        return self.coll.insert_one(model.model_dump(by_alias=True))
    
    def insert_many(self, models: List[BaseModel]) -> List[Any]:
        """Insert multiple Pydantic models."""
        docs = [m.model_dump(by_alias=True) for m in models]
        result = self.coll.insert_many(docs)
        return result.inserted_ids

    def find(self, query: Optional[Dict[str, Any]] = None) -> List[BaseModel]:
        """Find documents and return as Pydantic models."""
        docs = self.coll.find(query or {})
        return [self._from_doc(doc) for doc in docs]

    def find_one(self, **query: Any) -> Optional[BaseModel]:
        """Find a single document as Pydantic model."""
        doc = self.coll.find_one(query)
        return self._from_doc(doc)
    
    def update_one(self, query: Dict[str, Any], update: Dict[str, Any]) -> Any:
        """Update a single document."""
        if self.coll.count_documents(query) > 1:
            raise ValueError("update_one called but multiple documents match the query")
        return self.coll.update_one(query, {"$set": update}, upsert=True)
    
    def save(self, obj: BaseModel) -> BaseModel:
        """
        Insert or replace document by _id.
        Requires a Pydantic model instance.
        """
        if not isinstance(obj, BaseModel):
            raise TypeError(f"save() requires a Pydantic model, got {type(obj)}")
        
        doc = obj.model_dump(by_alias=True)
        if not doc.get("_id"):
            raise ValueError("Cannot save document without _id field")
        
        self.coll.replace_one({"_id": doc.get("_id")}, doc, upsert=True)
        return obj
    
    def delete_one(self, query: Dict[str, Any]) -> Any:
        """Delete a single document."""
        return self.coll.delete_one(query)
    
    def delete_many(self, query: Dict[str, Any]) -> Any:
        """Delete all documents matching query."""
        return self.coll.delete_many(query)
    
    def count_documents(self, query: Optional[Dict[str, Any]] = None) -> int:
        """Count documents matching query."""
        return self.coll.count_documents(query or {})
    
    def all(self) -> List[BaseModel]:
        """Get all documents as Pydantic models."""
        return self.find()

    def _from_doc(self, doc: Optional[Dict[str, Any]]) -> Optional[BaseModel]:
        """Rebuild a Pydantic model from a Mongo document."""
        if not doc:
            return None
        return self.model_cls.model_validate(doc)

    def asdf(self, query: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        """Return documents as a pandas DataFrame."""
        docs = list(self.coll.find(query or {}))
        if not docs:
            return pd.DataFrame()
        models = [self._from_doc(doc) for doc in docs]
        return pd.DataFrame([m.model_dump() for m in models if m is not None])
    
    def __repr__(self) -> str:
        return (
            f"DataStore(collection={self.coll.name}, "
            f"model={self.model_cls.__name__}, "
            f"count={self.count_documents()})"
        )
```

**Benefits of this approach:**
- ✅ Still get type hints for parameters and returns
- ✅ IDE autocomplete works
- ✅ Much simpler than `Generic[T]`
- ✅ Runtime type checking in `save()`
- ❌ Less specific (returns `BaseModel` instead of `User`)

## 2. Yes, `save()` Should Require Pydantic

I added this check:
```python
def save(self, obj: BaseModel) -> BaseModel:
    if not isinstance(obj, BaseModel):
        raise TypeError(f"save() requires a Pydantic model, got {type(obj)}")
    # ...
```

This prevents errors like:
```python
store.save({"name": "Bob"})  # ❌ TypeError at runtime
store.save(user_model)        # ✅ Works
```

## 3. Merging AI Output with Additional Data

Here's the pattern for adding data to AI-generated Pydantic models:

**Option A: Create a wrapper model that includes everything**

```python
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId

# AI generates this
class AnalysisResult(BaseModel):
    """What the AI returns"""
    summary: str
    priority: str
    tags: List[str]
    # ... other AI fields

# You save this to MongoDB
class AnalysisRecord(BaseModel):
    """Complete record with AI output + metadata"""
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    
    # The AI-generated analysis
    analysis: AnalysisResult
    
    # Your added metadata
    input_prompt: str
    input_text: str
    model_used: str
    timestamp: datetime = Field(default_factory=datetime.now)
    user_id: Optional[str] = None
    
    class Config:
        populate_by_name = True


# Usage:
model = ModelWrapper(model_type="claude")

# Get AI analysis
input_text = "Fix the critical authentication bug..."
ai_result = model.response(
    prompt=f"Analyze this task: {input_text}",
    response_model=AnalysisResult,
    max_tokens=2000
)

# Create complete record with metadata
record = AnalysisRecord(
    analysis=ai_result,
    input_prompt=f"Analyze this task: {input_text}",
    input_text=input_text,
    model_used="claude-sonnet-4-5",
    user_id="user123"
)

# Save to MongoDB
store = DataStore("analyses", AnalysisRecord)
store.save(record)
```

**Option B: Use model_copy() to add fields**

```python
from pydantic import BaseModel, Field

class AnalysisResult(BaseModel):
    """AI output + storage fields combined"""
    # MongoDB ID
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    
    # AI-generated fields
    summary: str
    priority: str
    tags: List[str]
    
    # Metadata fields (optional, added after AI generation)
    input_prompt: Optional[str] = None
    input_text: Optional[str] = None
    model_used: Optional[str] = None
    timestamp: Optional[datetime] = None
    
    class Config:
        populate_by_name = True


# Usage:
ai_result = model.response(
    prompt=f"Analyze this: {input_text}",
    response_model=AnalysisResult,
    max_tokens=2000
)

# Add metadata using model_copy
complete_record = ai_result.model_copy(update={
    "input_prompt": f"Analyze this: {input_text}",
    "input_text": input_text,
    "model_used": "claude-sonnet-4-5",
    "timestamp": datetime.now()
})

store.save(complete_record)
```

**Option C: Helper method in DataStore**

```python
class DataStore:
    # ... existing methods ...
    
    def save_with_metadata(
        self, 
        obj: BaseModel, 
        **extra_fields: Any
    ) -> BaseModel:
        """
        Save a Pydantic model with additional fields.
        
        Example:
            store.save_with_metadata(
                ai_result,
                input_prompt="...",
                timestamp=datetime.now(),
                user_id="123"
            )
        """
        # Add metadata to the model
        updated = obj.model_copy(update=extra_fields)
        return self.save(updated)
```

**Option D: Dedicated analysis storage class**

```python
from datetime import datetime
from typing import Optional, Any, Dict
from pydantic import BaseModel, Field
from bson import ObjectId

class AIAnalysisStore(DataStore):
    """Specialized store for AI-generated analyses"""
    
    def save_analysis(
        self,
        ai_output: BaseModel,
        input_prompt: str,
        input_text: str,
        model_name: str,
        user_id: Optional[str] = None,
        **extra_metadata: Any
    ) -> BaseModel:
        """
        Save AI analysis with automatic metadata.
        
        Args:
            ai_output: The Pydantic model returned by AI
            input_prompt: The prompt sent to the AI
            input_text: The original text being analyzed
            model_name: Which AI model was used
            user_id: Optional user identifier
            **extra_metadata: Any additional fields to store
        """
        # Create complete record
        record_data = {
            "_id": str(ObjectId()),
            "analysis": ai_output.model_dump(),
            "input_prompt": input_prompt,
            "input_text": input_text,
            "model_used": model_name,
            "timestamp": datetime.now(),
            "user_id": user_id,
            **extra_metadata
        }
        
        # Validate and save
        record = self.model_cls.model_validate(record_data)
        return self.save(record)


# Define the storage model
class TaskAnalysisRecord(BaseModel):
    id: str = Field(alias="_id")
    analysis: AnalysisResult  # The AI output
    input_prompt: str
    input_text: str
    model_used: str
    timestamp: datetime
    user_id: Optional[str] = None
    
    class Config:
        populate_by_name = True


# Usage:
store = AIAnalysisStore("task_analyses", TaskAnalysisRecord)

ai_output = model.response(
    prompt=f"Analyze: {task_text}",
    response_model=AnalysisResult,
    max_tokens=2000
)

# One-line save with all metadata
record = store.save_analysis(
    ai_output=ai_output,
    input_prompt=f"Analyze: {task_text}",
    input_text=task_text,
    model_name="claude-sonnet-4-5",
    user_id="user123"
)
```

**My recommendation:** Use **Option A** (wrapper model) or **Option D** (specialized store). They're the most explicit and type-safe.

Which approach fits your workflow best?

================================================================================
**User asked:** How would I avoid repeating my attribute names in Pydantic? Maybe StoreAnalysis could inherit the Analysis (Ai model output) class?...
**Response (msg #37, 5371 chars):**

Yes! That's a great insight. Instead of nesting or repeating fields, you can use inheritance to extend the Pydantic model. This is a very clean pattern.

Let me show them how to do this properly with Pydantic inheritance.**Yes! Exactly!** Pydantic inheritance is perfect for this. Here's the clean way:

```python
from datetime import datetime
from typing import Optional, List, Literal
from pydantic import BaseModel, Field
from bson import ObjectId

# ============================================================================
# AI Output Model (what Claude/GPT returns)
# ============================================================================
class AnalysisResult(BaseModel):
    """Pure AI output - no storage concerns"""
    summary: str = Field(description="Freeform text summary")
    priority: Literal["critical", "high", "medium", "low", "info"] = Field(
        description="Priority level"
    )
    key_values: dict[str, str] = Field(description="Key-value pairs")
    tags: List[str] = Field(description="Relevant tags")
    due_date: str = Field(description="Target date YYYY-MM-DD")
    scores: Optional[dict[str, float]] = Field(
        default=None,
        description="Optional numeric scores"
    )


# ============================================================================
# Storage Model (extends AI output with metadata)
# ============================================================================
class StoredAnalysis(AnalysisResult):
    """
    Extends AnalysisResult with storage metadata.
    Inherits all AI fields + adds MongoDB/tracking fields.
    """
    # MongoDB ID
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    
    # Metadata about the analysis
    input_prompt: str
    input_text: str
    model_used: str
    timestamp: datetime = Field(default_factory=datetime.now)
    user_id: Optional[str] = None
    
    class Config:
        populate_by_name = True


# ============================================================================
# Usage
# ============================================================================

# 1. Get AI analysis
model = ModelWrapper(model_type="claude")
task_text = "Fix the critical authentication bug in the login system"

ai_result: AnalysisResult = model.response(
    prompt=f"Analyze this task: {task_text}",
    response_model=AnalysisResult,  # AI returns pure AnalysisResult
    max_tokens=2000
)

# 2. Convert to storage model by adding metadata
stored = StoredAnalysis(
    **ai_result.model_dump(),  # Unpack all AI fields
    input_prompt=f"Analyze this task: {task_text}",
    input_text=task_text,
    model_used="claude-sonnet-4-5",
    user_id="user123"
)

# 3. Save to MongoDB
store = DataStore("analyses", StoredAnalysis)
store.save(stored)

# 4. Later, retrieve and use
analysis = store.find_one(user_id="user123")
print(analysis.summary)      # ✅ AI field
print(analysis.priority)     # ✅ AI field  
print(analysis.model_used)   # ✅ Metadata field
print(analysis.timestamp)    # ✅ Metadata field
```

**Why this is great:**

1. **No repetition** - Fields defined once in `AnalysisResult`
2. **Separation of concerns** - AI model doesn't know about storage
3. **Type safety** - `StoredAnalysis` has ALL fields from both classes
4. **Clean conversion** - Just `**ai_result.model_dump()` to upgrade
5. **Reusable** - Can use `AnalysisResult` in other contexts without storage baggage

**You can even add a helper method:**

```python
class StoredAnalysis(AnalysisResult):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    input_prompt: str
    input_text: str
    model_used: str
    timestamp: datetime = Field(default_factory=datetime.now)
    user_id: Optional[str] = None
    
    @classmethod
    def from_ai_result(
        cls,
        ai_result: AnalysisResult,
        input_prompt: str,
        input_text: str,
        model_used: str,
        user_id: Optional[str] = None
    ) -> "StoredAnalysis":
        """Create StoredAnalysis from AI output + metadata."""
        return cls(
            **ai_result.model_dump(),
            input_prompt=input_prompt,
            input_text=input_text,
            model_used=model_used,
            user_id=user_id
        )
    
    class Config:
        populate_by_name = True


# Usage becomes even cleaner:
stored = StoredAnalysis.from_ai_result(
    ai_result=ai_result,
    input_prompt=f"Analyze: {task_text}",
    input_text=task_text,
    model_used="claude-sonnet-4-5",
    user_id="user123"
)
store.save(stored)
```

**Pattern for multiple AI models:**

```python
# Base AI output
class AnalysisResult(BaseModel):
    summary: str
    priority: str
    # ...

# Storage version
class StoredAnalysis(AnalysisResult):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    input_prompt: str
    # ... metadata fields

# Different AI output
class SentimentResult(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"]
    confidence: float
    keywords: List[str]

# Its storage version
class StoredSentiment(SentimentResult):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    input_text: str
    model_used: str
    timestamp: datetime = Field(default_factory=datetime.now)
```

This is the Pydantic-idiomatic way to handle this! Much cleaner than nesting or repetition. 🎯
