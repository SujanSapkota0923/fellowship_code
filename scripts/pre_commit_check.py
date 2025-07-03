# import sys
# import re

# # Allowed types
# ALLOWED_TYPES = ['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore']

# # Read the commit message file
# def main():
#     pre_commit_check = sys.argv[1]
#     with open(pre_commit_check, 'r') as f:
#         message = f.readline().strip()

#     # Define the regex pattern for commit message
#     pattern = r'^(' + '|'.join(ALLOWED_TYPES) + r')(\([a-z0-9\-]+\))?: .{1,72}$'

#     if not re.match(pattern, message):
#         print("\n❌ Commit message does not follow the standard!")
#         print("🔧 Expected format: <type>(<scope>): <short description>")
#         print("✅ Allowed types: " + ", ".join(ALLOWED_TYPES))
#         print("💡 Example: feat(auth): add JWT login support\n")
#         sys.exit(1)

#     print("✅ Commit message is valid.")
#     sys.exit(0)

# if __name__ == "__main__":
#     main()
