# ☀️ SolarIQ Pro — AI Powered Rooftop Solar Intelligence Platform

> 🛰️ AI-powered rooftop solar analysis using **SAM (Segment Anything Model)**, **OpenCV**, **PVGIS Solar Data**, and **Financial Intelligence** to estimate solar feasibility, rooftop usability, ROI, annual energy generation, and deployment recommendations.

---

# 🌞 SolarIQ Pro

🚀 **An Intelligent Rooftop Solar Analysis & Recommendation Platform**  
Developed for automated rooftop solar feasibility assessment using **Artificial Intelligence + Computer Vision + Solar Irradiance Intelligence**.

✨ Built with:

🛰️ SAM-based rooftop segmentation

🚧 OpenCV-based obstacle detection and filtering

☀️ Rooftop usable area estimation

📡 PVGIS solar irradiance analysis

⚡ Annual solar energy estimation

💰 Financial analysis and ROI payback calculation

🤖 Intelligent recommendation generation

📥 Downloadable rooftop solar assessment report

🎨 Interactive Streamlit dashboard UI  

---

## 🖼️ Project Preview

> Add screenshots of your project UI here

Example:

```md
![Dashboard](images/dashboard.png)
![Analysis](images/analysis.png)
```

---

# 🎯 Project Objective

The goal of **SolarIQ Pro** is to automate rooftop solar feasibility analysis by intelligently identifying rooftop regions, filtering unusable areas, estimating solar generation potential, and calculating financial viability.

Instead of manually estimating rooftop capacity and installation feasibility, the system provides an **AI-assisted solar intelligence workflow** using image processing and solar analytics.

---

# 🚀 Key Features

## 🏠 SAM Rooftop Segmentation

Uses **Meta AI’s Segment Anything Model (SAM)** to automatically identify rooftop regions from uploaded rooftop or aerial imagery.

✔ Detects rooftop surfaces  
✔ Separates rooftop from surroundings  
✔ Creates rooftop mask for analysis  
✔ Works automatically without manual annotation

---

## 🚧 OpenCV Obstacle Detection

Uses **OpenCV image processing techniques** to detect darker rooftop regions that may represent:

- 🌳 Trees
- 🧱 Structures
- 🛰️ Equipment
- 🌑 Shadow regions
- ⚡ Rooftop obstacles

Processing includes:

✔ Grayscale conversion  
✔ Gaussian blurring  
✔ Threshold-based filtering  
✔ Morphological dilation  
✔ Obstacle masking

---

## 📐 Rooftop Usable Area Estimation

The system combines:

🛰️ **SAM Rooftop Segmentation**  
+  
🚧 **Obstacle Detection**

to estimate the **solar deployable rooftop surface area**.

This helps determine how much rooftop space is realistically usable for solar panel deployment.

---

## ☀️ PVGIS Solar Irradiance Intelligence

The platform integrates **PVGIS (Photovoltaic Geographical Information System)** to retrieve solar irradiance information based on:

📍 Latitude  
📍 Longitude

This data helps estimate:

- ☀️ Solar energy generation
- ⚡ Annual energy output
- 📈 Rooftop solar potential

---

## 💰 Financial Intelligence

SolarIQ Pro estimates:

💸 Installation Cost  
⚡ Annual Energy Production  
💵 Annual Savings  
📊 ROI Payback Period

Financial metrics are calculated dynamically using:

- Rooftop usable area
- Electricity tariff
- Installation cost
- Solar irradiance values

---

## 🤖 AI Solar Recommendations

The platform provides practical rooftop solar recommendations including:

✅ Installation guidance  
✅ Solar deployment suggestions  
✅ Maintenance recommendations  
✅ Financial outlook insights  
✅ ROI interpretation

> Current implementation uses **rule-based recommendation logic** generated from rooftop and financial metrics.

---

# 🧠 How The Project Works

## Step 1 — 📷 Upload Rooftop Image

User uploads:

- Rooftop satellite image
- Drone image
- Rooftop aerial image

---

## Step 2 — 🛰️ Rooftop Detection Using SAM

The uploaded image is processed using **Segment Anything Model (SAM)**.

SAM automatically:

❌ Removes irrelevant background  
✅ Identifies rooftop region  
✅ Creates rooftop segmentation mask

Example:

Before:

```text
Trees + Road + Rooftop + Shadows
```

After SAM:

```text
Only Rooftop Region
```

---

## Step 3 — 🚧 Obstacle Detection Using OpenCV

OpenCV performs:

🩶 Grayscale conversion  
🌫️ Gaussian blur  
⚫ Dark object filtering  
🔍 Thresholding  
🧩 Morphological operations

to identify unusable rooftop regions.

---

## Step 4 — 📐 Rooftop Usability Estimation

The system combines:

**SAM Mask + Obstacle Mask**

to estimate deployable rooftop area.

This produces:

🏠 Rooftop Mask  
🚧 Obstacle Mask  
☀️ Final Usable Area Mask

---

## Step 5 — ☀️ PVGIS Solar Analysis

Using rooftop coordinates:

📍 Latitude  
📍 Longitude

PVGIS returns solar irradiance information.

This is used for:

⚡ Annual Energy Estimation  
☀️ Solar Potential Analysis

---

## Step 6 — 💰 Financial Analysis

The system estimates:

💸 Installation Cost  
💵 Annual Savings  
📈 ROI Payback Period

using rooftop size and solar irradiance.

---

## Step 7 — 🤖 AI Recommendation Generation

The system generates practical solar deployment suggestions using:

- Rooftop size
- Estimated energy output
- Installation cost
- ROI metrics

---

## Step 8 — 📥 Report Generation

Users can download:

📄 Solar Analysis Report

containing:

✔ Rooftop area  
✔ Energy generation estimate  
✔ Installation cost  
✔ Annual savings  
✔ ROI payback period  
✔ Recommendations

---

# 🧰 Tech Stack

## 👨‍💻 Programming Language

- 🐍 Python

## 🧠 Artificial Intelligence

- 🛰️ Segment Anything Model (SAM)

## 👁️ Computer Vision

- 👁️ OpenCV
- 🔢 NumPy

## 🌍 Solar Intelligence

- ☀️ PVGIS API

## 🎨 Frontend/UI

- ⚡ Streamlit

## 📊 Visualization

- 📈 Matplotlib

---

# 🔮 Future Improvements

🚀 Improve rooftop segmentation accuracy  
🚀 Add GIS-scale rooftop analysis  
🚀 Integrate advanced solar ML models  
🚀 Add real solar subsidy estimation  
🚀 Multi-rooftop detection  
🚀 Better obstacle classification  
🚀 Smart solar panel placement optimization


---

# 👩‍💻 Author

## **Parshvi Goyal**

🎓 AIML Engineering Student  
☀️ AI • Computer Vision • Solar Intelligence

### 🔗 GitHub
https://github.com/parshvigoyal/solar-industry-ai-assistant

### 🌐 Streamlit Deployment
https://parshvigoyal-solar-ai.streamlit.app/

---

# 📜 Copyright & Usage Notice

```text
Copyright © 2026 Parshvi Goyal.
All Rights Reserved.

Unauthorized copying, redistribution, reuse,
academic submission, modification, reverse engineering,
or claiming this work as original is prohibited.
```

---

# ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub.

🌞 Built with AI for Sustainable Energy Intelligence

