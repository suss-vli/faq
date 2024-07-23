---
layout: default
title: Valence
nav_order: 4
has_children: false
permalink: valence/
---

# FAQ - Valence
{: .no_toc }

Here are some key benefits of Valence that each course or programme will gain when they adopt Valence.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## 0. What is Valence
Valence is a virtual lab solution that allows students to access a remote desktop environment for their programming needs.

## 1. Getting Started with Valence

To install the `suss-valence` package directly from GitHub, follow these steps:

1. **Install the Package:**

   You can install the package using `pip` directly from the repository. Use the following command:

   <!-- To be changed accordingly -->
   ```sh
   pip3 install git+http://github.com/suss-vli/valence2
   ```

### Kasm Image Customisation

To customise the Kasm image, follow these steps:

1. **Init & Update submodule**

   ```sh
   git submodule init
   git submodule update
   ```

2. **Navigate to the Kasm Image Directory**

   ```sh
   cd img
   ```
3. **Customise the Kasm Image**

   You can customise the Kasm image by modifying the `Dockerfile` and other files in the `src` directory.

3. **Build the Kasm Image**

   ```sh
   docker build -t <ImageName>:<Tag> -f <Dockerfile> .
   ```
