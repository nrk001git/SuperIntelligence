"""
Custom CSS and Styling Utilities
"""

import streamlit as st


def inject_custom_css():
    """
    Inject custom CSS for the Dell Sales Skills Framework app.
    """
    custom_css = """
    <style>
    /* GLOBAL STYLES */
    .stApp {
        background: linear-gradient(135deg, #0B1622 0%, #152238 100%);
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #0B1622;
    }
    ::-webkit-scrollbar-thumb {
        background: #1E3A5F;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #0672CB;
    }
    
    /* SKILL CARD STYLES */
    .skill-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        border-left: 3px solid var(--skill-color, #0672CB);
        padding: 20px;
        transition: all 0.25s ease;
        cursor: pointer;
    }
    
    .skill-card:hover {
        background: rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        transform: translateY(-2px);
    }
    
    /* DETAIL VIEW STYLES */
    .step-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 12px;
    }
    
    .step-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 32px;
        height: 32px;
        background: var(--skill-color, #0672CB);
        background: rgba(6, 114, 203, 0.2);
        border-radius: 50%;
        color: #E8EDF3;
        font-weight: bold;
        font-size: 14px;
        margin-right: 12px;
    }
    
    .when-to-use-item {
        display: flex;
        align-items: center;
        padding: 8px 0;
        color: #8B9DB5;
    }
    
    .when-to-use-item::before {
        content: "→";
        margin-right: 10px;
        color: #0672CB;
        font-weight: bold;
    }
    
    .section-header {
        color: #0672CB;
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin: 24px 0 16px 0;
    }
    
    /* PROMPT CARD STYLES */
    .prompt-card {
        background: rgba(6, 114, 203, 0.08);
        border: 1px solid rgba(6, 114, 203, 0.2);
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 12px;
        font-family: 'Courier New', monospace;
        font-size: 13px;
        color: #E8EDF3;
        position: relative;
    }
    
    .prompt-card:hover {
        border-color: rgba(6, 114, 203, 0.4);
        background: rgba(6, 114, 203, 0.12);
    }
    
    /* WORKFLOW CARD STYLES */
    .workflow-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
    }
    
    .workflow-skill-badge {
        display: inline-block;
        background: rgba(6, 114, 203, 0.15);
        border: 1px solid rgba(6, 114, 203, 0.3);
        border-radius: 8px;
        padding: 6px 12px;
        font-size: 13px;
        color: #E8EDF3;
        margin: 4px;
    }
    
    .workflow-arrow {
        color: #0672CB;
        font-weight: bold;
        margin: 0 8px;
    }
    
    /* HEADER STYLES */
    .dell-header {
        text-align: center;
        padding: 20px 0;
    }
    
    .dell-logo-icon {
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #0672CB 0%, #007DB8 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 12px auto;
        box-shadow: 0 4px 12px rgba(6, 114, 203, 0.3);
    }
    
    .dell-title {
        color: #E8EDF3;
        font-size: 22px;
        font-weight: bold;
        margin: 0;
    }
    
    .dell-subtitle {
        color: #7B9CC2;
        font-size: 13px;
        margin: 4px 0 0 0;
    }
    
    /* BUTTON STYLES */
    .stButton > button {
        background-color: #0672CB;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: #007DB8;
        transform: translateY(-1px);
    }
    
    .back-button {
        background: transparent !important;
        color: #0672CB !important;
        border: none !important;
        padding: 8px 16px !important;
        font-size: 14px;
    }
    
    .back-button:hover {
        background: rgba(6, 114, 203, 0.1) !important;
    }
    
    /* TEXT STYLES */
    h1, h2, h3, h4, h5, h6 {
        color: #E8EDF3;
    }
    
    p, span, div {
        color: #E8EDF3;
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        color: #0672CB;
    }
    
    .metric-label {
        font-size: 14px;
        color: #8B9DB5;
        margin-top: 8px;
    }
    
    /* RESPONSIVE STYLES */
    @media (max-width: 768px) {
        .skill-card {
            padding: 16px;
        }
        
        .skill-card h3 {
            font-size: 16px;
        }
        
        .step-card {
            padding: 12px;
        }
        
        .prompt-card {
            font-size: 12px;
            padding: 12px;
        }
        
        .dell-title {
            font-size: 18px;
        }
        
        .section-header {
            font-size: 12px;
        }
    }
    
    @media (max-width: 480px) {
        .skill-card {
            padding: 12px;
        }
        
        .skill-card h3 {
            font-size: 14px;
        }
        
        .skill-card p {
            font-size: 12px;
        }
        
        .step-card {
            padding: 10px;
        }
        
        .step-number {
            width: 28px;
            height: 28px;
            font-size: 12px;
        }
        
        .prompt-card {
            font-size: 11px;
            padding: 10px;
        }
    }
    </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)


def colored_header(text, color="#0672CB"):
    """
    Render a styled section header with custom color.
    
    Args:
        text (str): The header text
        color (str): The color for the header (default: Dell Blue)
    """
    st.markdown(
        f"""
        <div class="section-header" style="color: {color};">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )
