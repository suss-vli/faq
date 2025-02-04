---
layout: default
title: Labguide SDK
parent: Coding
nav_order: 4
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
LabGuide is an open-source Jupyter notebook created by SUSS Learning Services, which includes autogradable coding lab.  iLabGuide utilises `learntools` and [`suss`](https://github.com/suss-vli/suss) python packages to power the autograding and autotesting features. This allows students to independently learn and progressively enhance their skills through self-service. 

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
LabGuide is open-sourced and available on GitHub. Access the repository [here](https://github.com/suss-vli/LabGuide).

## Getting Started
Install LabGuide package
```
pip install git+https://github.com/suss-vli/labguide.git
```

### Initial Setup

Create a folder to store all the labs. Navigate to that folder and run the setup command.
```
cd <lab directory>
labguide setup
```
For example:
```
cd labs 
labguide setup
```

The setup will create a `lab0/` folder in your current working directory, and includes `lab0.ipynb` for you to try out.

### Setup for Courses

1. Navigate to the lab folder.

 
```
cd <lab directory>
```

2. To get the labs of the course and set up the LabGuide environment, you can use the command:

 
```
labguide get <course>
```
For example:
```
labguide get ict133
```
This command will `git clone` the course's labs into the `<course>/` folder.

3. Run the `setup` command:

 
```
labguide setup <course>
```
For example:
```
labguide setup ict133
```
This command will install all the dependencies required for the labs.

4. Your labs are now ready for you!