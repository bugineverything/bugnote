import os

# Git commands
commands = [
    "git clone https://github.com/bugineverything/bugnote",
    "cd bugnote",
    "echo 1>new",
    "git init",
    "git remote add origin https://github.com/bugineverything/bugnote",
    "git branch -M main",
    "git add .",
    'git commit -m "ok"',
    "git push -u origin main",
    "echo %cd%"
]

# Execute Git commands
for command in commands:
    os.system(command)

print("Git commands executed successfully.")