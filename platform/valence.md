---
layout: default
title: Valence
parent: Platform
nav_order: 1
permalink: valence/
---

# FAQ - Valence
{: .no_toc }

If your issue cannot be resolved by any of the FAQ, please email <bryanlimyt@suss.edu.sg> for assistance. <!-- <vlisupport@suss.edu.sg> -->

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## What is Valence
Valence is a virtual lab solution that allows students to access a remote desktop environment for their programming needs.

## What's inside Valence
The Virtual Lab team prepares by installing and setting up necessary applications and dependencies, supporting a wide range of tools including

- Chrome
- Chromium
- Git
- Nano
- Python3.9
- Visual Studio Code (VSCode)
- VSCode extensions like `ms-toolsai.jupyter`, `ms-python.python`, `esbenp.prettier-vscode`, `dbaeumer.vscode-selint` and `xdotool`
- Zip 

## Access for Lecturers
Lecturers can request for access to Valence by emailing <bryanlimyt@suss.edu.sg>. <!-- <vlisupport@suss.edu.sg> -->

## Running Valence
1. Pip install valence 2 using `pip install --no-cache-dir git+https://github.com/suss-vli/valence2.git`
   1. Clone valence-core using `git clone https://github.com/suss-vli/valence-core-images.git`
   2. Build the valence-core images using `docker build -t valence/core -f dockerfile-valence-core . `
2. Clone valence-images using `git clone https://github.com/suss-vli/valence-images1.git`
3. Build the valence image using `docker build --build-arg GITHUB_PAT=user:PAT -t ict133 -f dockerfile-ict133-valence-core .`
4. Run a valence container by using `valence local run --name suss_student --img ict133 --module SoftwareEngineering`

