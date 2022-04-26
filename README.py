FILES = [
    "load_schema",
    "make_tree",
]


def get_docstring(file: str) -> str:
    exec(f"import {file}")
    return eval(f"{file}.__doc__")


if __name__ == "__main__":
    docs = ["# " + file + ".py\n" + get_docstring(file) for file in FILES]
    with open("README.md", "w") as f:
        f.write("\n\n---\n\n".join(docs))
