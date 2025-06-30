# scripts/pre_commit_check.py

print("Running Python pre-commit checks...")

with open("main.py", "r") as f:
    contents = f.read()
    if "TODO" in contents:
        print("Found TODO comments. Remove them before committing.")
        exit(1)

print(" All checks passed.")

