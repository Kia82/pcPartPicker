# pcPartPicker

A **lightweight Python/HTML web app** inspired by PCPartPicker that enables advanced part search, price comparison, and compatibility validation in one intuitive place.

## 🔍 Overview

pcPartPicker connects to component databases to let users:

- 🔧 **Search and filter** by price, benchmarks, specs (e.g., wattage, socket, performance)
- ⚙️ **Check component compatibility** (CPU ↔ motherboard, PSU power, RAM capacity)
- 💰 **Compare vendor prices** in real-time if integrated with live data feeds
- 📊 **Review detailed spec sheets** to inform better build decisions

## 🚀 Why use it?

- Ideal for students, DIY PC builders, hobbyists or developers prototyping a PC-building assistant.
- Acts as a base for automating build-generation, price tracking, or hardware research.

## 🛠️ Tech Stack

- **Python** backend handling data retrieval, compatibility logic, and filter processing  
- **SQL** (or lightweight in-memory store) for part catalog integration  
- **HTML/CSS + minimal JS** UI for a responsive, browser-based experience  

## 📦 Features

- **Interactive search filters**: stuff like “price ≤ $100”, “socket = AM5”, “TDP < 95 W”
- **Compatibility layer**: verifies constraints like socket compatibility, RAM type, and PSU wattage
- **Easy deployment**: runs as a standalone web service, no complex setup required
- **Extensible design**: plug in extra data sources (e.g., live price APIs, vendor availability)
