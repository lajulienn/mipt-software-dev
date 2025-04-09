# Setting Up Pre-commit Hooks

Pre-commit hooks are scripts that run automatically before a commit to a repository

## Installing Pre-commit

`pip install pre-commit`

## Choose the hooks

You can find a list of existing pre-commit hooks in the [pre-commit's official 
repository](https://github.com/pre-commit/pre-commit-hooks) or explore other repositories on GitHub. 
Each hook typically comes with documentation on how to use them.

## Create a Configuration File

Create a `.pre-commit-config.yaml` file in the root of your repository. 

Example configuration:

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
```

## Installing the Hooks
Run `pre-commit install` to set up the hooks to run automatically before 
each commit.

## Running Hooks Manually

Use `pre-commit run --all-files` to manually run hooks on all files in 
the repository.

## Setting up Ruff in pre-commit

To run Ruff on changed files before each commit, you can configure it in 
your `.pre-commit-config.yaml` like this

```yaml
repos:
-   repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.289
    hooks:
    -   id: ruff
```

This will ensure that Ruff, along with any other configured hooks, 
runs on the files that are staged for commit. The `--fix` argument can be 
added to automatically fix certain issues.

## Testing the Setup

Make some changes to your Python files and attempt to commit them. 
You should see Ruff and other pre-commit hooks in action, preventing the 
commit if issues are found.