"""
Module 10: Modules
Level 0: Importing math module
Level 1: Creating and importing a custom module with __name__ guard
Level 2: Using os, sys, datetime
Level 3: Real world: JSON config loader for LLM settings
Level 4: Mini challenge: Random dataset splitter
Level 5: Production: Plugin-style architecture with dynamic imports
"""

# ============================================================
# Level 0: Importing math module
# ============================================================

print("=== Level 0: Importing math module ===")

import math

print(f"pi: {math.pi}")
print(f"sqrt(16): {math.sqrt(16)}")
print(f"ceil(3.2): {math.ceil(3.2)}")
print(f"floor(3.2): {math.floor(3.2)}")
print(f"sin(0): {math.sin(0)}")
print(f"factorial(5): {math.factorial(5)}")

from math import sqrt, pow
print(f"sqrt via import: {sqrt(25)}")
print(f"pow via import: {pow(2, 10)}")

from math import log as logarithm
print(f"log via alias: {logarithm(100, 10)}")

# ============================================================
# Level 1: Custom module with __name__ guard
# ============================================================

print("\n=== Level 1: Custom module with __name__ guard ===")

import myhelper

print(myhelper.greet("Student"))
print(f"add(10, 20): {myhelper.add(10, 20)}")
print(f"multiply(3, 4): {myhelper.multiply(3, 4)}")
print(f"myhelper.PI: {myhelper.PI}")

# ============================================================
# Level 2: Using os, sys, datetime
# ============================================================

print("\n=== Level 2: Using os, sys, datetime ===")

import os
import sys
from datetime import datetime, timedelta, date

# os module
print(f"Current directory: {os.getcwd()}")
print(f"Home: {os.environ.get('HOME', 'Not set')}")
print(f"All env vars count: {len(os.environ)}")
print(f"Separator: {os.sep}")

# sys module
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Command line args: {sys.argv}")
print(f"sys.path count: {len(sys.path)}")

# datetime module
now = datetime.now()
print(f"Now: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")

future = now + timedelta(days=7, hours=3)
print(f"Future: {future}")

today = date.today()
print(f"Today: {today}")
print(f"ISO format: {today.isoformat()}")

# ============================================================
# Level 3: Real world: JSON config loader for LLM settings
# ============================================================

print("\n=== Level 3: JSON config loader for LLM settings ===")

import json
from pathlib import Path


class LLMConfig:
    """Loads and manages LLM configuration from a JSON file."""

    DEFAULTS = {
        "model": "gpt-4",
        "temperature": 0.7,
        "max_tokens": 1024,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
    }

    def __init__(self, config_path=None):
        self.config = dict(self.DEFAULTS)
        if config_path:
            self.load(config_path)

    def load(self, config_path):
        path = Path(config_path)
        if not path.exists():
            print(f"Warning: {config_path} not found, using defaults")
            return
        with open(path, "r") as f:
            data = json.load(f)
        self.config.update(data)
        print(f"Loaded config from {config_path}")

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __getitem__(self, key):
        return self.config[key]

    def __repr__(self):
        return json.dumps(self.config, indent=2)


config_path = Path("llm_config.json")
config_data = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.5,
    "max_tokens": 2048,
}
with open(config_path, "w") as f:
    json.dump(config_data, f, indent=2)

config = LLMConfig("llm_config.json")
print(f"Model: {config.get('model')}")
print(f"Temperature: {config['temperature']}")
print(f"Max tokens: {config.get('max_tokens')}")
print(f"Using default top_p: {config.get('top_p')}")

config_path.unlink()
print(f"Config file cleaned up")

# ============================================================
# Level 4: Mini challenge: Random dataset splitter
# ============================================================

print("\n=== Level 4: Random dataset splitter ===")

import random


def train_val_test_split(data, train_pct=0.7, val_pct=0.15, test_pct=0.15):
    """
    Split dataset into train/val/test sets.

    Args:
        data: List of items to split
        train_pct: Proportion for training
        val_pct: Proportion for validation
        test_pct: Proportion for testing

    Returns:
        dict with keys 'train', 'val', 'test'
    """
    assert abs(train_pct + val_pct + test_pct - 1.0) < 1e-9, "Proportions must sum to 1"

    indices = list(range(len(data)))
    random.shuffle(indices)

    n = len(data)
    n_train = int(n * train_pct)
    n_val = int(n * val_pct)

    train_idx = indices[:n_train]
    val_idx = indices[n_train:n_train + n_val]
    test_idx = indices[n_train + n_val:]

    return {
        "train": [data[i] for i in train_idx],
        "val": [data[i] for i in val_idx],
        "test": [data[i] for i in test_idx],
    }


dataset = [f"sample_{i}" for i in range(100)]
split = train_val_test_split(dataset, train_pct=0.8, val_pct=0.1, test_pct=0.1)

print(f"Train: {len(split['train'])} samples")
print(f"Val: {len(split['val'])} samples")
print(f"Test: {len(split['test'])} samples")
print(f"Total: {sum(len(v) for v in split.values())} samples")

# Stratified seed for reproducibility
random.seed(42)
split2 = train_val_test_split(dataset)
random.seed(42)
split3 = train_val_test_split(dataset)
print(f"Reproducible: {split2['train'][:3] == split3['train'][:3]}")

# ============================================================
# Level 5: Production: Plugin-style architecture with dynamic imports
# ============================================================

print("\n=== Level 5: Plugin-style architecture with dynamic imports ===")

import importlib
from typing import Any


class PluginRegistry:
    """Plugin registry with dynamic module loading."""

    def __init__(self):
        self._plugins = {}

    def discover(self, package_name, prefix="plugin_"):
        """Discover plugins in a package by naming convention."""
        try:
            package = importlib.import_module(package_name)
            package_path = Path(package.__file__).parent
            for file_path in package_path.glob(f"{prefix}*.py"):
                module_name = f"{package_name}.{file_path.stem}"
                self.register(file_path.stem, module_name)
        except ImportError as e:
            print(f"Could not discover plugins: {e}")

    def register(self, name, module_path):
        """Register a plugin module path."""
        self._plugins[name] = module_path

    def load(self, name):
        """Dynamically import and return a plugin module."""
        if name not in self._plugins:
            raise KeyError(f"Plugin '{name}' not found")
        return importlib.import_module(self._plugins[name])

    def get_plugin(self, name):
        """Load a plugin and call its main entry point if it exists."""
        module = self.load(name)
        if hasattr(module, "run"):
            return module.run
        return module

    def list_plugins(self):
        return list(self._plugins.keys())


# Create plugin modules dynamically for demo
import tempfile

plugin_dir = Path(tempfile.mkdtemp())
plugin_pkg = "demo_plugins"

# Create a package directory
pkg_path = plugin_dir / plugin_pkg
pkg_path.mkdir(exist_ok=True)
(pkg_path / "__init__.py").write_text("")

# Create plugin modules
plugin1_code = '''
def run(data):
    return {"status": "processed", "data": data.upper(), "plugin": "uppercase"}
'''
plugin2_code = '''
def run(data):
    return {"status": "processed", "data": data[::-1], "plugin": "reverse"}
'''
plugin3_code = '''
def run(data):
    return {"status": "processed", "data": len(data), "plugin": "length"}
'''

(pkg_path / "plugin_uppercase.py").write_text(plugin1_code)
(pkg_path / "plugin_reverse.py").write_text(plugin2_code)
(pkg_path / "plugin_length.py").write_text(plugin3_code)

registry = PluginRegistry()
registry.discover(plugin_pkg)

print(f"Discovered plugins: {registry.list_plugins()}")

for plugin_name in registry.list_plugins():
    plugin_func = registry.get_plugin(plugin_name)
    result = plugin_func("Hello World")
    print(f"  {plugin_name}: {result}")

# Cleanup
import shutil
shutil.rmtree(plugin_dir)
print(f"Plugin directory cleaned up")
