"""
Sidebar Navigation Component
"""

import streamlit as st
from streamlit_option_menu import option_menu
from data.skills_data import SKILLS_DATA


def render_sidebar():
    """
    Render the sidebar navigation with Dell branding and navigation options.
    
    Returns:
        str: The selected navigation option
    """
    # Initialize session state if not exists
    if "current_view" not in st.session_state:
        st.session_state.current_view = "Skills Dashboard"
    if "selected_skill_id" not in st.session_state:
        st.session_state.selected_skill_id = None
    
    with st.sidebar:
        # Dell-branded header section
        st.markdown(
            """
            <div style="text-align: center; padding: 20px 0;">
                <div style="
                    width: 80px; 
                    height: 80px; 
                    background: linear-gradient(135deg, #0672CB 0%, #007DB8 100%); 
                    border-radius: 12px; 
                    display: flex; 
                    align-items: center; 
                    justify-content: center; 
                    margin: 0 auto 15px auto;
                    box-shadow: 0 4px 12px rgba(6, 114, 203, 0.3);
                ">
                    <span style="font-size: 48px; font-weight: bold; color: white;">D</span>
                </div>
                <h1 style="color: #E8EDF3; margin: 0; font-size: 24px; font-weight: 600;">Dell Sales Skills</h1>
                <p style="color: #8B9DB5; margin: 5px 0 0 0; font-size: 14px;">Powered by AI Assistant</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("---")
        
        # Navigation section using streamlit-option-menu
        selected = option_menu(
            menu_title=None,
            options=["🎯 Skills Dashboard", "🔗 Workflows", "📋 Prompt Library", "🎯 Deal Analyzer", "ℹ️ How to Use"],
            icons=["target", "link", "clipboard", "crosshairs", "info-circle"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#E8EDF3", "font-size": "18px"},
                "nav-link": {
                    "color": "#E8EDF3",
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "8px 0",
                    "padding": "12px 16px",
                    "border-radius": "8px",
                },
                "nav-link-selected": {
                    "background-color": "#0672CB",
                    "color": "white",
                    "font-weight": "600",
                },
            }
        )
        
        # Update session state
        st.session_state.current_view = selected
        
        st.markdown("---")
        
        # Quick Stats section
        st.markdown(
            """
            <div style="padding: 16px; background-color: #152238; border-radius: 12px; border: 1px solid #1E3A5F;">
                <h3 style="color: #E8EDF3; margin: 0 0 15px 0; font-size: 16px; font-weight: 600;">Quick Stats</h3>
                <div style="display: flex; flex-direction: column; gap: 10px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #8B9DB5; font-size: 14px;">Skills Available</span>
                        <span style="color: #0672CB; font-size: 18px; font-weight: bold;">6</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #8B9DB5; font-size: 14px;">Playbook Steps</span>
                        <span style="color: #0672CB; font-size: 18px; font-weight: bold;">24</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #8B9DB5; font-size: 14px;">Ready-to-Use Prompts</span>
                        <span style="color: #0672CB; font-size: 18px; font-weight: bold;">24</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #8B9DB5; font-size: 14px;">Sales Workflows</span>
                        <span style="color: #0672CB; font-size: 18px; font-weight: bold;">3</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Skill Progress Tracker
    st.markdown("---")
    st.markdown(
        """
        <div style="padding: 16px; background-color: #152238; border-radius: 12px; border: 1px solid #1E3A5F; margin-bottom: 16px;">
            <h3 style="color: #E8EDF3; margin: 0 0 12px 0; font-size: 16px; font-weight: 600;">
                📈 Skill Progress
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    for skill in SKILLS_DATA:
        is_completed = skill['id'] in st.session_state.completed_skills
        if st.checkbox(
            f"{skill['icon']} {skill['title']}",
            value=is_completed,
            key=f"progress_{skill['id']}"
        ):
            st.session_state.completed_skills.add(skill['id'])
        else:
            st.session_state.completed_skills.discard(skill['id'])
    
    # Progress bar
    completed_count = len(st.session_state.completed_skills)
    total_count = len(SKILLS_DATA)
    progress_percent = (completed_count / total_count) * 100
    
    st.markdown(
        f"""
        <div style="margin-top: 12px;">
            <div style="
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 8px;
            ">
                <span style="color: #8B9DB5; font-size: 13px;">Skills Practiced</span>
                <span style="color: #0672CB; font-size: 13px; font-weight: bold;">{completed_count}/{total_count}</span>
            </div>
            <div style="
                width: 100%;
                height: 8px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 4px;
                overflow: hidden;
            ">
                <div style="
                    width: {progress_percent}%;
                    height: 100%;
                    background: linear-gradient(90deg, #0672CB 0%, #007DB8 100%);
                    border-radius: 4px;
                    transition: width 0.3s ease;
                "></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    return selected
