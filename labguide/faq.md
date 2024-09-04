---
layout: default
title: Labguide
nav_order: 4
has_children: false
permalink: labguide/
---
# FAQ - LabGuide
{: .no_toc }

If your issue cannot be resolved by any of the FAQ, please email  for assistance.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## What is LabGuide
iLabGuide is an interactive study guide with autotestable and autogradable labs which includes jupyter notebooks as questions. This allows students to independently learn and progressively enhance their skills through self-service. 

## Courses covered by LabGuide
LabGuide covers the following courses:
- ICT133
- ICT162
- ICT233
- ANL588

To get your course included in LabGuide, please email the Virtual Lab team at <vlisupport@suss.edu.sg>.

## What's inside LabGuide
The Virtual Lab team prepares by installing and setting up necessary applications and dependencies, supporting a wide range of tools and extensions including:

- `suss` - a Python package that contains helper functions for autograding and autotesting
- `learntools` - a Python package that contains helper functions for autograding and autotesting
- `friendly` - switch on `friendly` to display friendlier output in Jupyter Notebook
- `hello.py` - prints "hello, world!" as a tester plugin 

## Getting Access
LabGuide is open-sourced and available on GitHub. Access the repository [here](https://github.com/suss-vli/ilabguide).

## Getting Started
Follow these steps to get started with LabGuide:
```sh
git clone https://github.com/suss-vli/iLabGuide
git clone https://github.com/suss-vli/suss
git clone https://github.com/suss-vli/learntools
cd iLabGuide
python -m venv venv
source venv/bin/activate
pip3 install ../suss
pip3 install ../learntools 
pip3 install -r requirements.txt 
```

## Importing Labs and Questions
- ICT133
```sh
from learntools.core import binder; 
binder.bind(globals())
from suss.ict133.lab1 import *
```
- ICT162
```sh
from learntools.core import binder; 
binder.bind(globals())
from suss.ict162.lab1 import *
```

## Preparing the Lab for Students
As a lecturer, you can prepare the lab for students by following these commands:
```sh
chmod 700 clean.sh
./clean.sh
```