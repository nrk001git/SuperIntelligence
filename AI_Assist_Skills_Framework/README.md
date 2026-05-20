# Dell Sales Skills Framework

![Dell Sales Skills Framework](https://img.shields.io/badge/Project-Dell%20Sales-blue)
![Powered by your friendly AI Assistant](https://img.shields.io/badge/Powered%20By-your friendly AI Assistant-purple)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)

A comprehensive Streamlit application designed for Dell sales teams to master core sales competencies with AI-powered assistance from your friendly AI Assistant.

## Screenshot

![App Screenshot](assets/screenshot.png)
*(Add a screenshot of the application here)*

## Features

### 🎯 Skills Dashboard
- **6 Core Sales Skills** with detailed playbooks:
  - Discovery & Needs Analysis
  - Solution Architecture & Positioning
  - Objection Handling & Negotiation
  - Pipeline Management & Forecasting
  - Account Expansion & Cross-Sell
  - Product & Market Intelligence
- **24 Playbook Steps** - 4 actionable steps per skill
- **24 Ready-to-Use your friendly AI Assistant Prompts** - Copy and paste directly into your friendly AI Assistant
- **Animated Metrics** - Track skills, steps, prompts, and workflows at a glance
- **Quick Reference Table** - Map deal stages to recommended skills

### 🔗 Sales Workflows
- **New Deal Qualification** - Discovery → Solution Architecture → Pipeline Management
- **Competitive Displacement** - Product Intelligence → Solution Architecture → Objection Handling
- **Installed Base Growth** - Account Expansion → Discovery → Objection Handling
- Pro tips for chaining skills in your friendly AI Assistant conversations

### 📋 Prompt Library
- **Search & Filter** - Find prompts by keyword or skill
- **All 24 Prompts** - Organized by skill with copy functionality
- **Usage Tips** - Best practices for better prompt results

### 🎯 Deal Analyzer
- **Interactive Form** - Quick deal health check
- **Health Score (0-100)** - Color-coded assessment
- **Gap Analysis** - Identify weaknesses and recommended skills
- **Auto-Generated Prompts** - Contextual your friendly AI Assistant prompts based on deal details

### 📈 Skill Progress Tracker
- **Checkboxes** - Mark skills you've practiced
- **Progress Bar** - Visual tracking of completion
- **Session Persistence** - Progress saved during session

### ℹ️ How to Use Guide
- Comprehensive documentation for all features
- Best practices for using with your friendly AI Assistant
- Sales workflow explanations

## Installation

### Prerequisites
- Python 3.12 or higher
- pip package manager

### Steps

1. **Clone or download the repository:**
   ```bash
   cd "C:\Users\Ramakrishna_Nanduri\OneDrive - Dell Technologies\RK\Dell_PINE_n_More\Models\Model Reports\GEN_AI\Python_JupyterNBs\Dell_Skills_Framework"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser:**
   Navigate to `http://localhost:8501`

## Deployment

### Streamlit Community Cloud

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy to Streamlit Community Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Select `app.py` as the main file
   - Click "Deploy"

### Heroku Deployment

1. **Install Heroku CLI and login**

2. **Create a Heroku app:**
   ```bash
   heroku create dell-sales-skills
   ```

3. **Deploy:**
   ```bash
   git push heroku main
   ```

## Folder Structure

```
Dell_Skills_Framework/
├── app.py                      # Main Streamlit application
├── requirements.txt             # Python dependencies
├── README.md                   # This file
├── .gitignore                  # Git ignore rules
├── Procfile                    # Heroku deployment config
├── runtime.txt                 # Python version specification
├── .streamlit/
│   └── config.toml            # Streamlit configuration (Dell theme)
├── data/
│   └── skills_data.py         # Skills and workflows data layer
├── components/
│   ├── __init__.py
│   ├── sidebar.py             # Sidebar navigation
│   ├── skill_card.py          # Skill cards grid
│   ├── skill_detail.py        # Skill detail view
│   ├── workflow_view.py       # Workflows view
│   ├── prompt_library.py      # Prompt library
│   └── deal_analyzer.py       # Deal analyzer tool
├── utils/
│   ├── __init__.py
│   └── styles.py              # Custom CSS styling
└── assets/
    └── dell_logo.png          # Dell logo (placeholder)
```

## Dependencies

- `streamlit>=1.38.0` - Web framework
- `streamlit-option-menu>=0.3.6` - Navigation menu component
- `streamlit-extras>=0.4.0` - Additional Streamlit utilities

## Built for Dell Sales Teams

This application was specifically designed for Dell sales teams to enhance their sales skills with AI-powered assistance from your friendly AI Assistant. It provides a structured approach to mastering core sales competencies with ready-to-use prompts and interactive tools.

## License

Internal use for Dell Sales Teams.

## Support

For issues or questions, please contact your sales enablement manager or refer to the Dell Sales Enablement Portal.

---

**Built for Dell Sales Teams | Powered by your friendly AI Assistant | v1.0**
