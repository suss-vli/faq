<!-- ---
layout: default
title: iLabGuide
nav_order: 3
parent: Coding
permalink: iLabGuide/
--- -->

# FAQ - iLabGuide
{: .no_toc }

Here are some key benefits of iLabGuide that each course or programme will gain when they adopt iLabGuide.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## 0. iLabGuide
LabGuide is an open-source Jupyter notebook created by SUSS learning services, which includes autogradable coding lab. iLabGuide utilises `learntools` and [`suss`](https://github.com/suss-vli/suss) python packages to power the autograding and autotesting features.

iLabGuide covers the following courses:
- ICT133
- ICT233
- ICT162

## 1. Getting Started as a Student

1. Set up your environment
2. Clone the repository 
```bash
git clone https://github.com/suss-vli/ilabguide.git
```

3.Run Jupyter Notebook:
- Start Jupyter Notebook in your terminal:
```bash
jupyter notebook
```
- Open the lab guide notebook for your course

4. Follow the instructions in the notebook to complete the lab exercises.
- Use the interactive tools provided to enhance your understanding

5. Submit your work:
- Save your work and submit it for grading using the provided instructions.


## 2. Getting Started as a Lecturer

1. Set up your environment
2. Clone the repository 
```bash
git clone https://github.com/suss-vli/ilabguide.git
```
3. Customize Lab Guides:
- Edit the Jupyter notebooks to create or modify lab exercises according to your course syllabus.
- Implement autograding tests using pytest and testbook.

4. Package Solutions:
- Use packaging techniques to hide solutions, ensuring students cannot view them directly.

5. Integrate Additional Tools:
- Plan for integration with Git, GitHub Classroom, and other educational tools as mentioned in the repository documentation.

6. Deploy and Monitor:
- Share the lab guides with your students via a platform like GitHub or a learning management system.
- Monitor student progress and provide feedback based on their submissions.