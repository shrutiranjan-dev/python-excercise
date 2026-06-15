"""
Module 09: Strings
Level 0: Basic string operations
Level 1: String methods (split, join, strip, replace)
Level 2: f-strings and formatting
Level 3: Real world: Prompt template engine
Level 4: Mini challenge: Text cleaning pipeline for RAG
Level 5: Production: Message formatter with multiple templates and validation
"""

# ============================================================
# Level 0: Basic string operations
# ============================================================

print("=== Level 0: Basic string operations ===")

greeting = "Hello, World!"
print(greeting)

single_quote = 'Python strings'
double_quote = "can use either quote style"
triple_quote = """This spans
multiple lines"""
print(single_quote, double_quote)
print(triple_quote)

text = "Python"
print(f"First char: {text[0]}")
print(f"Last char: {text[-1]}")
print(f"Slice [1:4]: {text[1:4]}")
print(f"Reversed: {text[::-1]}")

print(f"Length: {len(text)}")
print(f"Concat: " + "Hello" + " " + "World")

# String repetition
print(f"Repeat: {'Ha' * 3}")

# Membership
print(f"'th' in 'Python': {'th' in 'Python'}")
print(f"'xyz' not in 'Python': {'xyz' not in 'Python'}")

# ============================================================
# Level 1: String methods (split, join, strip, replace)
# ============================================================

print("\n=== Level 1: String methods ===")

csv_line = "apple,banana,cherry,date"
items = csv_line.split(",")
print(f"split: {items}")

tags = ["python", "programming", "strings"]
tag_string = " | ".join(tags)
print(f"join: {tag_string}")

messy = "   Hello, World!   \n"
clean = messy.strip()
print(f"strip: '{clean}'")

sentence = "I like cats and cats are great"
replaced = sentence.replace("cats", "dogs")
print(f"replace: {replaced}")

print(f"upper: {clean.upper()}")
print(f"lower: {clean.lower()}")
print(f"startswith 'Hello': {clean.startswith('Hello')}")
print(f"endswith '!': {clean.endswith('!')}")
print(f"find 'World': {clean.find('World')}")
print(f"find 'xyz': {clean.find('xyz')}")

s = "hello"
print(f"capitalize: {s.capitalize()}")
print(f"title: {'hello world'.title()}")
print(f"swapcase: {'Hello World'.swapcase()}")

# ============================================================
# Level 2: f-strings and formatting
# ============================================================

print("\n=== Level 2: f-strings and formatting ===")

name = "Alice"
age = 30
height = 1.75
score = 0.8567

print(f"Basic: {name} is {age} years old")
print(f"Format float: {score:.2%}")
print(f"Format float: {height:.1f}m")
print(f"Padding: '{name:>10}'")
print(f"Padding: '{name:<10}'")
print(f"Center: '{name:^10}'")
print(f"Repr: {name!r}")

# Expressions
print(f"Math: {2 * 3 + 5}")
print(f"Method: {name.upper()}")

# Dictionaries
data = {"name": "Bob", "job": "developer"}
print(f"Dict: {data['name']} is a {data['job']}")

# Old styles
print("%-formatting: %s is %d" % (name, age))
print(".format(): {} is {}".format(name, age))

# ============================================================
# Level 3: Real world: Prompt template engine
# ============================================================

print("\n=== Level 3: Prompt template engine ===")


class PromptTemplate:
    """A simple prompt template engine."""

    def __init__(self, template):
        self.template = template

    def render(self, **kwargs):
        result = self.template
        for key, value in kwargs.items():
            placeholder = "{" + key + "}"
            result = result.replace(placeholder, str(value))
        return result

    def render_fstring(self, **kwargs):
        return eval(f'f"""{self.template}"""', kwargs)


template = PromptTemplate(
    "You are a {role}. Answer the following question: {question}\n"
    "Context: {context}\n"
    "Be {style} in your response."
)

prompt = template.render(
    role="Python tutor",
    question="What is a string?",
    context="Strings are immutable sequences of characters.",
    style="concise and clear",
)
print(prompt)


class AdvancedPromptTemplate:
    """Prompt template with validation and default values."""

    def __init__(self, template, required_vars=None, defaults=None):
        self.template = template
        self.required_vars = required_vars or []
        self.defaults = defaults or {}

    def render(self, **kwargs):
        merged = {**self.defaults, **kwargs}
        for var in self.required_vars:
            if var not in merged:
                raise ValueError(f"Required variable '{var}' is missing")
        result = self.template
        for key, value in merged.items():
            placeholder = "{" + key + "}"
            result = result.replace(placeholder, str(value))
        return result


advanced = AdvancedPromptTemplate(
    "System: You are {role}\nUser: {query}\nAnswer: {answer}",
    required_vars=["query"],
    defaults={"role": "assistant", "answer": "I need more context."},
)
print(advanced.render(query="What is Python?"))

# ============================================================
# Level 4: Mini challenge: Text cleaning pipeline for RAG
# ============================================================

print("\n=== Level 4: Text cleaning pipeline for RAG ===")


class TextCleaner:
    """Text cleaning pipeline for RAG preprocessing."""

    @staticmethod
    def strip_html(text):
        import re
        return re.sub(r"<[^>]+>", "", text)

    @staticmethod
    def normalize_whitespace(text):
        import re
        return re.sub(r"\s+", " ", text).strip()

    @staticmethod
    def remove_urls(text):
        import re
        return re.sub(r"https?://\S+|www\.\S+", "", text)

    @staticmethod
    def remove_special_chars(text, keep=""):
        import re
        allowed = re.escape(keep)
        return re.sub(f"[^a-zA-Z0-9\\s{allowed}]", "", text)

    @staticmethod
    def truncate(text, max_chars):
        if len(text) <= max_chars:
            return text
        return text[:max_chars].rsplit(" ", 1)[0] + "..."

    def clean(self, text, max_chars=1000, keep_punctuation=".,!?-:;"):
        text = self.strip_html(text)
        text = self.remove_urls(text)
        text = self.normalize_whitespace(text)
        text = self.remove_special_chars(text, keep=keep_punctuation)
        text = text.lower()
        text = self.truncate(text, max_chars)
        return text


cleaner = TextCleaner()
raw_text = (
    "Hello! Check out https://example.com for <b>more info</b>.   "
    "This is a sample   text with    irregular   spacing!!!\n\n"
    "And another paragraph with SPECIAL chars @#$%^&*()."
)
cleaned = cleaner.clean(raw_text)
print(f"Original: {raw_text}")
print(f"Cleaned: {cleaned}")

# ============================================================
# Level 5: Production: Message formatter with multiple templates
# ============================================================

print("\n=== Level 5: Production: Message formatter ===")


class MessageTemplate:
    """Production-grade message formatter with multiple templates and validation."""

    def __init__(self, template_id, template, description=""):
        self.template_id = template_id
        self.template = template
        self.description = description

    def format(self, **kwargs):
        missing = []
        for key, value in kwargs.items():
            if value is None:
                missing.append(key)
        if missing:
            raise ValueError(
                f"Template '{self.template_id}': missing values for {missing}"
            )
        try:
            return self.template.format(**kwargs)
        except KeyError as e:
            raise ValueError(
                f"Template '{self.template_id}': unknown key {e}"
            )
        except ValueError as e:
            raise ValueError(
                f"Template '{self.template_id}': format error - {e}"
            )


class MessageFormatter:
    """Manages multiple message templates and formats messages."""

    def __init__(self):
        self._templates = {}

    def register(self, template_id, template, description=""):
        self._templates[template_id] = MessageTemplate(
            template_id, template, description
        )

    def format(self, template_id, **kwargs):
        if template_id not in self._templates:
            raise KeyError(
                f"Template '{template_id}' not found. "
                f"Available: {list(self._templates.keys())}"
            )
        return self._templates[template_id].format(**kwargs)

    def list_templates(self):
        for tid, tpl in self._templates.items():
            print(f"  [{tid}] {tpl.description}")


formatter = MessageFormatter()

formatter.register(
    "greeting",
    "Hello {name}! Welcome to {platform}. You have {count} notifications.",
    "User greeting with notification count",
)
formatter.register(
    "error",
    "[ERROR] {code}: {message}. Please contact support at {email}.",
    "Error message template",
)
formatter.register(
    "summary",
    "User: {name} | Role: {role} | Status: {status} | Last active: {last_active}",
    "User summary report",
)

print("Registered templates:")
formatter.list_templates()

try:
    msg = formatter.format(
        "greeting",
        name="Alice",
        platform="Python Course",
        count=5,
    )
    print(f"\nFormatted: {msg}")
except (KeyError, ValueError) as e:
    print(f"Error: {e}")

# Validation example
try:
    formatter.format("greeting", name="Bob", platform="Test")
except ValueError as e:
    print(f"Validation caught: {e}")

# Unknown template
try:
    formatter.format("nonexistent")
except KeyError as e:
    print(f"Unknown template: {e}")
