import os

tools = [
    "augment-code", "claude-code", "cluely", "codebuddy", "comet", "cursor", "devin-ai",
    "junie", "kiro", "leap-new", "lovable", "manus", "notion-ai", "orchids-app",
    "perplexity", "poke", "qoder", "replit", "same-dev", "trae", "traycer-ai",
    "vscode-agent", "warp-dev", "windsurf", "xcode", "z-ai-code", "dia", "v0"
]

def create_structure():
    for tool in tools:
        tool_dir = tool.lower()
        if not os.path.exists(tool_dir):
            os.makedirs(tool_dir)
            print(f"Created directory: {tool_dir}")

        # Create standard subdirectories
        subdirs = ["system-prompts", "context-templates", "internal-tools"]
        for subdir in subdirs:
            subdir_path = os.path.join(tool_dir, subdir)
            if not os.path.exists(subdir_path):
                os.makedirs(subdir_path)
                # Create a .gitkeep file to ensure the directory is tracked
                with open(os.path.join(subdir_path, ".gitkeep"), "w") as f:
                    pass

        # Create README.md
        readme_path = os.path.join(tool_dir, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, "w") as f:
                f.write(f"# {tool.replace('-', ' ').title()}\n\n")
                f.write(f"This directory contains resources for **{tool.replace('-', ' ').title()}**.\n\n")
                f.write("## Contents\n\n")
                f.write("- `system-prompts/`: Specific instructions for the AI model/agent.\n")
                f.write("- `context-templates/`: Templates for structuring context.\n")
                f.write("- `internal-tools/`: Helper scripts or configurations.\n")
            print(f"Created README for: {tool}")

if __name__ == "__main__":
    create_structure()
