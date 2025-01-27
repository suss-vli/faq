---
layout: default
title: Docker
parent: Platform
nav_order: 4
permalink: docker/
---

# FAQ - Docker
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

## Pre-requisites
- **Operating System**: macOS (ARM-based), Windows (AMD-based)

## Docker Installation
### macOS (ARM-based)
- **Install Docker Desktop**: Download the latest version of Docker Desktop from the official site [here](https://docs.docker.com/desktop/mac/install/).

### Windows (AMD-based)
- **WSL (Windows Subsystem for Linux)**: Ensure that WSL 2 is enabled on your Windows machine. Follow the instructions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
- **Install Docker Desktop**: Download the latest version of Docker Desktop from the official site [here](https://docs.docker.com/desktop/windows/install/).

## Verify Docker Installation
After installing Docker Desktop, verify the installation by running the following command in your terminal:
```bash
docker --version
```

## Using LinuxServer Images with Docker
The VLI team heavily relies on LinuxServer images based on Kasm, and here are some of the key ones used:
1. `linuxserver/code-server`: Provides a web-based Visual Studio Code environment.
    - Repository: [linuxserver/docker-code-server](https://github.com/linuxserver/docker-code-server)
2. `linuxserver/docker-baseimage-alpine`: Lightweight base image using Alpine Linux.
    - Repository: [linuxserver/docker-baseimage-alpine](https://github.com/linuxserver/docker-baseimage-alpine)
3. `linuxserver/docker-kasm`: A Kasm-based container image
    - Repository: [linuxserver/docker-kasm](https://github.com/linuxserver/docker-kasm)
4. `linuxserver/baseimage-kasmvnc`: A Kasm VNC-based container image
    - Repository: [linuxserver/docker-baseimage-kasmvnc](https://github.com/linuxserver/docker-baseimage-kasmvnc)

## How to decide which LinuxServer image to use
It depends on your project requirements. For example, if you need a web-based Visual Studio Code environment, you can use `linuxserver/code-server`. If you need a Kasm-based container image, you can use `linuxserver/docker-kasm`.

## Is Docker Desktop required for macOS and Windows?
Yes, Docker Desktop is required for macOS and Windows. It is a tool that allows you to run Docker containers on your local machine. 