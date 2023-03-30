# Alfred workflow

A workflow to be run via Alfred (Pro).

## Version

Current version supports filtering messages and environments only.

Future versions will support more filters.

## Prerequisites

- Python 3

```sh
brew install python
```

## Getting started

### Setup

Download & run `DataDog Query Workflow.alfredworkflow`.

## Examples

### Default environment (production)

---

Input:

- In Alfred search bar type: `ddq "msg to find"`
- In Alfred search bar type: `ddq "msg to find prod"`
- In Alfred search bar type: `ddq "msg to find production"`

Output:

will open DataDog with the message filter and in the default environment - production.

---

---

### Query specific environment

input:

- In Alfred search bar type: `ddq "msg to find" t12345`

- In Alfred search bar type: `ddq "msg to find" 12345`

output:

will open DataDog with the message filter and in the staging environment - t12345.

---

input:

In Alfred search bar type: `ddq "msg to find" master`

output:

will open DataDog with the message filter and in the staging environment - master.
