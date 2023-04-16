# Alfred workflow

A workflow to be run via Alfred (Pro).

Supports 2 commands: `ddq`, `ddm`.

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

Download & run `DataDog-Query.alfredworkflow`.

## (ddm) DataDog Message formatter Examples

Used to sanitize a string to a datadog search format.

Input:

In Alfred search bar type: `ddm "LPP-123-456"`

Output:

`*LPP\-123\-456*`

---

## (ddq) DataDog Query Search Examples

Used to find a message in DataDog (opens in the browser).

### Default environment (production)

---

Input:

- In Alfred search bar type: `ddq "msg to find"`
- In Alfred search bar type: `ddq "msg to find prod"`
- In Alfred search bar type: `ddq "msg to find production"`

Output:

will open DataDog with the message filter and in the default environment - production.

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
