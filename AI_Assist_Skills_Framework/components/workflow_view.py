"""
Workflow Chaining View Component
"""

import streamlit as st
from data.skills_data import SKILLS_DATA, get_skill_by_id


def on_workflow_click(first_skill_id):
    """
    Callback function when a workflow card is clicked.
    Navigates to the first skill in the workflow chain.
    
    Args:
        first_skill_id (str): The ID of the first skill in the workflow
    """
    st.session_state.selected_skill_id = first_skill_id
    st.session_state.current_view = "detail"


def render_workflows(workflows_data):
    """
    Render workflow chaining view.
    
    Args:
        workflows_data (list): List of workflow dictionaries
    """
    # Intro text
    st.markdown(
        """
        <p style="color: #8B9DB5; font-size: 16px; margin-bottom: 32px;">
            Combine skills for common sales scenarios. Each workflow chains skills in the optimal sequence.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # Render each workflow card
    for workflow in workflows_data:
        # Get skill names for badges
        skill_names = []
        for skill_id in workflow['skills']:
            skill = get_skill_by_id(skill_id)
            if skill:
                skill_names.append(skill['title'])
        
        # Workflow card using expander for better rendering
        with st.expander(f"**{workflow['title']}**", expanded=True):
            st.markdown(f"*{workflow['description']}*")
            
            # Skill badges as markdown
            badge_text = " → ".join([f"`{name}`" for name in skill_names])
            st.markdown(f"**Skills:** {badge_text}")
            
            st.markdown(f"*{workflow['tagline']}*")
            
            # Click handler button
            if workflow['skills']:
                st.button(
                    f"Explore {workflow['title']}",
                    key=f"workflow_btn_{workflow['id']}",
                    on_click=on_workflow_click,
                    args=(workflow['skills'][0],),
                    help=f"Start with {skill_names[0] if skill_names else 'first skill'}",
                    use_container_width=True
                )
    
    # Pro Tip box
    pro_tip_html = """
    <div style="
        background: rgba(26, 140, 94, 0.08);
        border: 1px solid rgba(26, 140, 94, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin-top: 32px;
    ">
        <div style="display: flex; align-items: flex-start; gap: 12px;">
            <div style="font-size: 32px;">💡</div>
            <div style="flex: 1;">
                <h4 style="color: #1A8C5E; margin: 0 0 8px 0; font-size: 16px; font-weight: 600;">
                    Pro Tip: Chaining Skills in your friendly AI Assistant
                </h4>
                <p style="color: #8B9DB5; margin: 0; font-size: 14px; line-height: 1.6;">
                    You can chain these skills in a single your friendly AI Assistant conversation. Start with discovery questions, then ask your friendly AI Assistant to architect a solution based on the answers, then generate objection-handling talk tracks for the proposal. Each step builds on the context from the previous one.
                </p>
            </div>
        </div>
    </div>
    """
    
    st.markdown(pro_tip_html, unsafe_allow_html=True)
