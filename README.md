# 🖼️ Pixel Manipulation for Image Encryption (GUI)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Track](https://img.shields.io/badge/Track-Cybersecurity-red.svg)](#)

A modern Graphical User Interface (GUI) tool built in Python using **Tkinter** and **Pillow** to securely encrypt and decrypt image files using pixel manipulation.

This project is completed as part of the **Prodigy InfoTech Cybersecurity Internship (Task 02)**.

---

## 📖 Table of Contents
* [Features](#features)
* [How the Encryption Works](#how-the-encryption-works)
* [Application Preview](#application-preview)
* [Installation & Setup](#installation--setup)
* [How to Run](#how-to-run)
* [Code Structure](#code-structure)
* [Developer](#developer)

---

## Features

* **Sleek Dark GUI**: Styled beautifully with a modern dark theme interface.
* **XOR-Based Encryption**: Uses a secure pixel manipulation technique via bitwise XOR operations on RGB channels.
* **Real-time Image Preview**: Generates an automatic scaled thumbnail preview of the selected target image.
* **Dynamic Key Adjustment**: Allows customizable key values from 0 to 255.
* **Flexible File Saving**: Saves results anywhere on your computer in lossless standard PNG format.

---

## How the Encryption Works

The application manipulates the red, green, and blue (RGB) color values of every single pixel of an image using a mathematical bitwise **XOR operation** combined with a custom security key.

* **Encryption**: The program reads the original image pixels and applies `Pixel XOR Key`. The resulting file will look completely scrambled and distorted.
* **Decryption**: Because XOR is fully symmetric, passing the encrypted file back through the exact same XOR key reverses the distortion and perfectly recovers the original image.

---

## Installation & Setup

### Prerequisites
Make sure you have Python 3 installed. You will need to install the Pillow library for image processing:
```bash
pip install Pillow
