# treeless-checkout-action

Basic script action to check out a repository with `--filter=tree:0`.

## Inputs

| Input      | Description                        | Default                    | Required? |
|------------|------------------------------------|----------------------------|-----------|
| ref        | Ref to checkout (SHA, branch, tag) | `${{ github.ref }}`        | no        |
| repository | Repository name (foo/bar)          | `${{ github.repository }}` | no        |
| server-url | GitHub server url                  | `${{ github.server_url }}` | no        |

## Example Usage

This action is used in Void Linux's [packaging](https://github.com/void-linux/void-packages/blob/master/.github/workflows/build.yaml) and [documentation](https://github.com/void-linux/void-docs/blob/master/.github/workflows/ci.yaml) CI.

```yaml
name: Treeless Checkout Example
on:
  pull_request:

jobs:
  checkout:
    name: Checkout Repo - Treeless style
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: classabbyamp/treeless-checkout-action@v1
      - name: Show repo contents
        runs: ls -lR
```
