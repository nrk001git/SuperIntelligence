"""
Dell Sales Skills Framework - Main Streamlit Application
"""

import streamlit as st
from data.skills_data import SKILLS_DATA, WORKFLOWS_DATA, get_skill_by_id
from components.sidebar import render_sidebar
from components.skill_card import render_skill_grid
from components.skill_detail import render_skill_detail
from components.workflow_view import render_workflows
from components.prompt_library import render_prompt_library
from components.deal_analyzer import render_deal_analyzer
from utils.styles import inject_custom_css, colored_header


def render_how_to_use():
    """Render the How to Use static page."""
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #0672CB20 0%, #007DB810 100%);
            border: 1px solid #0672CB40;
            border-radius: 16px;
            padding: 32px;
            margin-bottom: 32px;
        ">
            <h1 style="color: #E8EDF3; margin: 0 0 16px 0; font-size: 32px; font-weight: 700;">
                📘 How to Use the Dell Sales Skills Framework
            </h1>
            <p style="color: #8B9DB5; margin: 0; font-size: 16px; line-height: 1.6;">
                Your comprehensive guide to mastering sales skills with AI-powered assistance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Getting Started
    colored_header("Getting Started")
    st.markdown(
        """
        <div class="step-card">
            <p style="color: #E8EDF3; margin: 0; font-size: 15px; line-height: 1.6;">
                The Dell Sales Skills Framework provides 6 core sales competencies with step-by-step playbooks and ready-to-use your friendly AI Assistant prompts. Each skill includes:
            </p>
            <ul style="color: #8B9DB5; margin: 12px 0 0 24px; font-size: 14px; line-height: 1.8;">
                <li>Clear description of when to apply the skill</li>
                <li>4-step actionable playbook with specific tactics</li>
                <li>24 pre-written your friendly AI Assistant prompts for immediate use</li>
                <li>Workflow chains for common sales scenarios</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # How to Use Each Skill
    colored_header("How to Use Each Skill")
    st.markdown(
        """
        <div class="step-card">
            <p style="color: #E8EDF3; margin: 0; font-size: 15px; line-height: 1.6;">
                <strong>1. Navigate to Skills Dashboard</strong> — Browse all 6 skills and select the one relevant to your current sales situation.<br><br>
                <strong>2. Review the Playbook</strong> — Read through the step-by-step guide to understand the framework and tactics.<br><br>
                <strong>3. Copy a Prompt</strong> — Use the "📋 Copy" button to copy a prompt, then paste it into your friendly AI Assistant with your specific context.<br><br>
                <strong>4. Iterate and Refine</strong> — Use follow-up prompts to refine your friendly AI Assistant's output based on your customer and deal details.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Using with your friendly AI Assistant
    colored_header("Using with your friendly AI Assistant")
    st.markdown(
        """
        <div class="step-card">
            <p style="color: #E8EDF3; margin: 0; font-size: 15px; line-height: 1.6;">
                <strong>Best Practices:</strong>
            </p>
            <ul style="color: #8B9DB5; margin: 12px 0 0 24px; font-size: 14px; line-height: 1.8;">
                <li>Always provide context after the prompt (meeting notes, deal details, customer info)</li>
                <li>Be specific about customer industry, size, and current technology stack</li>
                <li>Request specific output formats (tables, emails, talk tracks, battle cards)</li>
                <li>Chain skills in a single conversation for complex scenarios</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Workflows
    colored_header("Sales Workflows")
    st.markdown(
        """
        <div class="step-card">
            <p style="color: #E8EDF3; margin: 0; font-size: 15px; line-height: 1.6;">
                Use the <strong>Workflows</strong> tab to see pre-defined skill chains for common scenarios:
            </p>
            <ul style="color: #8B9DB5; margin: 12px 0 0 24px; font-size: 14px; line-height: 1.8;">
                <li><strong>New Deal Qualification</strong> — Discovery → Solution Architecture → Pipeline Management</li>
                <li><strong>Competitive Displacement</strong> — Product Intelligence → Solution Architecture → Objection Handling</li>
                <li><strong>Installed Base Growth</strong> — Account Expansion → Discovery → Objection Handling</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Prompt Library
    colored_header("Prompt Library")
    st.markdown(
        """
        <div class="step-card">
            <p style="color: #E8EDF3; margin: 0; font-size: 15px; line-height: 1.6;">
                Access all 24 prompts in the <strong>Prompt Library</strong> tab. Search by keyword or filter by skill to find the right prompt for your situation. Each prompt is ready to copy and use immediately.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Additional Resources
    colored_header("Additional Resources")
    st.markdown(
        """
        <div style="
            background: rgba(6, 114, 203, 0.08);
            border: 1px solid rgba(6, 114, 203, 0.2);
            border-radius: 12px;
            padding: 20px;
            margin-top: 16px;
        ">
            <p style="color: #8B9DB5; margin: 0; font-size: 14px; line-height: 1.6;">
                For additional Dell sales resources, training materials, and internal tools, please refer to the Dell Sales Enablement Portal or contact your sales enablement manager.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def main():
    """Main application function."""
    try:
        # Page configuration
        st.set_page_config(
            page_title="Dell Sales Skills Framework",
            page_icon="🔵",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Inject custom CSS
        inject_custom_css()
        
        # Initialize session state
        if "current_view" not in st.session_state:
            st.session_state.current_view = "Skills Dashboard"
        if "selected_skill_id" not in st.session_state:
            st.session_state.selected_skill_id = None
        if "completed_skills" not in st.session_state:
            st.session_state.completed_skills = set()
        
        # Render sidebar and get selected navigation
        selected_nav = render_sidebar()
        
        # Main content routing
        if selected_nav == "🎯 Skills Dashboard":
            if st.session_state.selected_skill_id:
                # Show skill detail view
                skill = get_skill_by_id(st.session_state.selected_skill_id)
                if skill:
                    render_skill_detail(skill)
                else:
                    # If skill not found, reset to grid
                    st.session_state.selected_skill_id = None
                    render_skill_grid(SKILLS_DATA)
            else:
                # Show skills grid
                render_skill_grid(SKILLS_DATA)
        
        elif selected_nav == "🔗 Workflows":
            # Check if a workflow button was clicked (sets selected_skill_id)
            if st.session_state.selected_skill_id:
                # Navigate to skill detail view
                skill = get_skill_by_id(st.session_state.selected_skill_id)
                if skill:
                    # Switch to Skills Dashboard view for consistency
                    st.session_state.current_view = "Skills Dashboard"
                    render_skill_detail(skill)
                else:
                    # If skill not found, reset and show workflows
                    st.session_state.selected_skill_id = None
                    render_workflows(WORKFLOWS_DATA)
            else:
                # Show workflows
                render_workflows(WORKFLOWS_DATA)
        
        elif selected_nav == "📋 Prompt Library":
            render_prompt_library(SKILLS_DATA)
        
        elif selected_nav == "🎯 Deal Analyzer":
            render_deal_analyzer()
        
        elif selected_nav == "ℹ️ How to Use":
            render_how_to_use()
        
        # Footer
        st.markdown(
            """
            <div style="
                text-align: center;
                padding: 32px 0 16px 0;
                margin-top: 48px;
                border-top: 1px solid rgba(255, 255, 255, 0.08);
            ">
                <p style="color: #5A6D85; margin: 0; font-size: 13px;">
                    Built for Dell Sales Teams | Powered by your friendly AI Assistant | v1.0
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.markdown(
            """
            <div style="
                background: rgba(201, 74, 22, 0.1);
                border: 1px solid rgba(201, 74, 22, 0.3);
                border-radius: 12px;
                padding: 20px;
            ">
                <p style="color: #C94A16; margin: 0; font-size: 14px;">
                    <strong>Application Error</strong><br>
                    Please refresh the page. If the error persists, please contact support.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()
