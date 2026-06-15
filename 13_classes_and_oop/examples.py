"""
Module 13: Classes and OOP - Examples
Level 0-5 progressing from basic to production-ready.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


# ============================================================
# LEVEL 0: Basic Class with __init__
# ============================================================

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm in grade {self.grade}."


def level_0_basic_class():
    print("=== LEVEL 0: Basic Class ===")
    s = Student("Alice", 10)
    print(s.introduce())
    print(f"Name: {s.name}, Grade: {s.grade}")


# ============================================================
# LEVEL 1: Instance Methods and Properties
# ============================================================

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9

    def __str__(self):
        return f"{self._celsius:.1f}°C ({self.fahrenheit:.1f}°F)"


def level_1_properties():
    print("\n=== LEVEL 1: Properties ===")
    t = Temperature(25)
    print(t)
    print(f"Fahrenheit: {t.fahrenheit:.1f}")

    t.fahrenheit = 98.6
    print(f"Celsius: {t.celsius:.1f}")

    try:
        t.celsius = -300
    except ValueError as e:
        print(f"Error: {e}")


# ============================================================
# LEVEL 2: Class Methods and Static Methods
# ============================================================

class BankAccount:
    interest_rate = 0.02  # Class variable
    _total_accounts = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount._total_accounts += 1

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    @classmethod
    def set_interest_rate(cls, rate):
        if not 0 <= rate <= 1:
            raise ValueError("Rate must be between 0 and 1")
        cls.interest_rate = rate

    @classmethod
    def from_csv(cls, csv_string):
        owner, balance = csv_string.split(",")
        return cls(owner.strip(), float(balance))

    @classmethod
    def total_accounts(cls):
        return cls._total_accounts

    @staticmethod
    def validate_account_number(account_num):
        return len(str(account_num)) == 10 and str(account_num).isdigit()

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate


def level_2_class_static_methods():
    print("\n=== LEVEL 2: Class & Static Methods ===")

    acct1 = BankAccount("Alice", 1000)
    acct2 = BankAccount("Bob", 500)

    print(f"Total accounts: {BankAccount.total_accounts()}")

    acct1.deposit(500)
    acct1.apply_interest()
    print(f"{acct1.owner}'s balance: ${acct1.balance:.2f}")

    BankAccount.set_interest_rate(0.05)
    acct2.apply_interest()
    print(f"{acct2.owner}'s balance: ${acct2.balance:.2f}")

    acct3 = BankAccount.from_csv("Charlie, 2000")
    print(f"From CSV: {acct3.owner} with ${acct3.balance}")

    print(f"Valid acct #1234567890: {BankAccount.validate_account_number(1234567890)}")
    print(f"Valid acct #123: {BankAccount.validate_account_number(123)}")


# ============================================================
# LEVEL 3: Real World - LLM Client Wrapper Class
# ============================================================

class LLMClient:
    """Wrapper for interacting with an LLM API."""

    def __init__(self, model="gpt-4", temperature=0.7, max_tokens=1024):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.conversation_history = []

    def add_message(self, role, content):
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })

    def generate(self, prompt, system_prompt=None):
        self.add_message("user", prompt)
        response = f"[Simulated response from {self.model} to: {prompt[:50]}...]"
        self.add_message("assistant", response)
        return response

    @property
    def total_messages(self):
        return len(self.conversation_history)

    @property
    def total_tokens_estimate(self):
        total_chars = sum(len(m["content"]) for m in self.conversation_history)
        return total_chars // 4

    def clear_history(self):
        self.conversation_history.clear()

    def __str__(self):
        return f"LLMClient(model={self.model}, temp={self.temperature}, msgs={self.total_messages})"


def level_3_llm_client():
    print("\n=== LEVEL 3: LLM Client Wrapper ===")

    client = LLMClient(model="gpt-4", temperature=0.3)
    print(client)

    response = client.generate("Explain Python classes in one sentence.")
    print(f"Response: {response}")

    response = client.generate("Give me an example of inheritance.")
    print(f"Response: {response}")

    print(f"Total messages: {client.total_messages}")
    print(f"Estimated tokens: {client.total_tokens_estimate}")

    client.clear_history()
    print(f"After clear: {client.total_messages} messages")


# ============================================================
# LEVEL 4: Mini Challenge - Vector Class with Operator Overloading
# ============================================================

class Vector:
    """A 2D vector with operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Vector(self.x / scalar, self.y / scalar)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def dot(self, other):
        return self.x * other.x + self.y * other.y


def level_4_vector_class():
    print("\n=== LEVEL 4: Vector Class ===")

    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"3 * v1 = {3 * v1}")
    print(f"v1 / 2 = {v1 / 2}")
    print(f"-v1 = {-v1}")
    print(f"|v1| = {abs(v1):.2f}")
    print(f"v1 . v2 = {v1.dot(v2)}")
    print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")


# ============================================================
# LEVEL 5: Production - Abstract RAG Pipeline Base Class
# ============================================================

@dataclass
class Document:
    """Data class for a retrieved document."""
    content: str
    source: str
    score: float = 0.0


class EmbeddingProvider(ABC):
    @abstractmethod
    def embed(self, text: str) -> list[float]:
        pass


class VectorStore(ABC):
    @abstractmethod
    def search(self, query_vector: list[float], top_k: int = 5) -> list[Document]:
        pass


class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, context: list[Document] = None) -> str:
        pass


class RAGPipeline(ABC):
    """Abstract base class for Retrieval-Augmented Generation pipelines."""

    def __init__(self, embedding_provider, vector_store, llm_provider):
        self.embedder = embedding_provider
        self.vector_store = vector_store
        self.llm = llm_provider

    @abstractmethod
    def retrieve(self, query: str, top_k: int) -> list[Document]:
        pass

    @abstractmethod
    def augment(self, query: str, documents: list[Document]) -> str:
        pass

    @abstractmethod
    def generate_response(self, augmented_prompt: str) -> str:
        pass

    def query(self, question: str, top_k: int = 3) -> dict:
        documents = self.retrieve(question, top_k)
        augmented = self.augment(question, documents)
        answer = self.generate_response(augmented)
        return {
            "question": question,
            "answer": answer,
            "documents": documents,
            "documents_used": len(documents)
        }


class SimpleEmbedder(EmbeddingProvider):
    def embed(self, text: str) -> list[float]:
        return [float(len(text)), float(sum(ord(c) for c in text) % 100)]


class SimpleVectorStore(VectorStore):
    def __init__(self):
        self.documents = [
            Document("Python is a programming language", "docs/python_intro.md", 0.95),
            Document("Classes are blueprints for objects", "docs/oop.md", 0.88),
            Document("File handling uses open() function", "docs/file_io.md", 0.82),
        ]

    def search(self, query_vector: list[float], top_k: int = 5) -> list[Document]:
        sorted_docs = sorted(self.documents, key=lambda d: d.score, reverse=True)
        return sorted_docs[:top_k]


class SimpleLLM(LLMProvider):
    def generate(self, prompt: str, context: list[Document] = None) -> str:
        sources = ", ".join(d.source for d in (context or []))
        return f"Based on {sources}, the answer relates to: {prompt[:30]}..."


class SimpleRAGPipeline(RAGPipeline):
    def __init__(self):
        super().__init__(SimpleEmbedder(), SimpleVectorStore(), SimpleLLM())

    def retrieve(self, query: str, top_k: int = 3) -> list[Document]:
        query_vec = self.embedder.embed(query)
        return self.vector_store.search(query_vec, top_k)

    def augment(self, query: str, documents: list[Document]) -> str:
        context = "\n".join(f"- {d.content} (source: {d.source})" for d in documents)
        return f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"

    def generate_response(self, augmented_prompt: str) -> str:
        return self.llm.generate(augmented_prompt)


def level_5_rag_pipeline():
    print("\n=== LEVEL 5: RAG Pipeline ===")

    pipeline = SimpleRAGPipeline()

    result = pipeline.query("How do classes work in Python?")
    print(f"Question: {result['question']}")
    print(f"Answer: {result['answer']}")
    print(f"Documents used: {result['documents_used']}")

    print("\nRetrieved documents:")
    for doc in result['documents']:
        print(f"  [{doc.score:.2f}] {doc.content[:50]}... (from {doc.source})")

    # Verify it's a proper RAGPipeline
    print(f"\nIs RAGPipeline? {isinstance(pipeline, RAGPipeline)}")
    print(f"Has embedder? {hasattr(pipeline, 'embedder')}")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    level_0_basic_class()
    level_1_properties()
    level_2_class_static_methods()
    level_3_llm_client()
    level_4_vector_class()
    level_5_rag_pipeline()
