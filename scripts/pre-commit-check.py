print("Running Python pre-commit checks...")

with open("README.md", "r") as f:
    contents = f.read()
    if "TODO" in contents:
        print("Found TODO comments. Remove them before committing.")
        exit(1)

print(" All checks passed.")