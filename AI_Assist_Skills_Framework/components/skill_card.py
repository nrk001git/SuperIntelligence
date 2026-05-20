"""
Skill Card Grid Component
"""

import streamlit as st


def on_skill_click(skill_id):
    """
    Callback function when a skill card is clicked.
    Updates session state to show the skill detail view.
    
    Args:
        skill_id (str): The ID of the clicked skill
    """
    st.session_state.selected_skill_id = skill_id
    st.session_state.current_view = "detail"


def render_skill_grid(skills_data):
    """
    Render a grid of clickable skill cards.
    
    Args:
        skills_data (list): List of skill dictionaries
    """
    # Container for proper spacing
    with st.container():
        # Animated metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Skills Available",
                value="6",
                delta="",
                help="Total number of sales skills in the framework"
            )
        
        with col2:
            st.metric(
                label="Playbook Steps",
                value="24",
                delta="",
                help="Total actionable steps across all skills"
            )
        
        with col3:
            st.metric(
                label="AI Assistant Prompts",
                value="24",
                delta="",
                help="Ready-to-use prompts for AI assistance"
            )
        
        with col4:
            st.metric(
                label="Workflows",
                value="3",
                delta="",
                help="Pre-defined skill chains for common scenarios"
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Intro text
        st.markdown(
            """
            <p style="color: #8B9DB5; font-size: 16px; margin-bottom: 24px;">
                Select a skill to explore its playbook, step-by-step guide, and ready-to-use AI Assistant prompts.
            </p>
            """,
            unsafe_allow_html=True
        )
        
        # Create 2-column grid
        for i in range(0, len(skills_data), 2):
            cols = st.columns(2)
            
            for col_idx in range(2):
                skill_idx = i + col_idx
                if skill_idx < len(skills_data):
                    skill = skills_data[skill_idx]
                    
                    with cols[col_idx]:
                        # Skill card HTML
                        card_html = f"""
                        <div class="skill-card" style="--skill-color: {skill['color']};">
                            <div style="display: flex; align-items: flex-start; justify-content: space-between;">
                                <div style="flex: 1;">
                                    <div style="font-size: 48px; margin-bottom: 12px;">{skill['icon']}</div>
                                    <h3 style="color: #E8EDF3; margin: 0 0 8px 0; font-size: 18px; font-weight: 600;">
                                        {skill['title']}
                                    </h3>
                                    <p style="color: #8B9DB5; margin: 0; font-size: 14px; line-height: 1.4;">
                                        {skill['tagline']}
                                    </p>
                                </div>
                                <div style="color: {skill['color']}; font-size: 24px; font-weight: bold;">
                                    →
                                </div>
                            </div>
                        </div>
                        """
                        
                        st.markdown(card_html, unsafe_allow_html=True)
                        
                        # Invisible button for click handling
                        st.button(
                            f"View {skill['title']}",
                            key=f"skill_btn_{skill['id']}",
                            on_click=on_skill_click,
                            args=(skill['id'],),
                            help=f"Explore {skill['title']}",
                            use_container_width=True
                        )
        
        # Deal Stage Quick Reference
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.expander("🗺️ Quick Reference: Which Skill for Which Deal Stage?", expanded=False):
            st.markdown(
                """
                <style>
                .reference-table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 16px;
                }
                .reference-table th {
                    background: rgba(6, 114, 203, 0.15);
                    color: #E8EDF3;
                    padding: 12px;
                    text-align: left;
                    font-weight: 600;
                    border: 1px solid rgba(6, 114, 203, 0.3);
                }
                .reference-table td {
                    color: #8B9DB5;
                    padding: 12px;
                    border: 1px solid rgba(255, 255, 255, 0.08);
                }
                .reference-table tr:hover td {
                    background: rgba(6, 114, 203, 0.05);
                }
                </style>
                <table class="reference-table">
                    <thead>
                        <tr>
                            <th>Deal Stage</th>
                            <th>Primary Skill</th>
                            <th>Supporting Skill</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Prospecting</td>
                            <td>Discovery & Needs Analysis</td>
                            <td>Product Intelligence</td>
                        </tr>
                        <tr>
                            <td>Qualification</td>
                            <td>Discovery & Needs Analysis</td>
                            <td>Pipeline Management</td>
                        </tr>
                        <tr>
                            <td>Solution Design</td>
                            <td>Solution Architecture</td>
                            <td>Product Intelligence</td>
                        </tr>
                        <tr>
                            <td>Proposal</td>
                            <td>Solution Architecture</td>
                            <td>Objection Handling</td>
                        </tr>
                        <tr>
                            <td>Negotiation</td>
                            <td>Objection Handling</td>
                            <td>Pipeline Management</td>
                        </tr>
                        <tr>
                            <td>Closed-Won</td>
                            <td>Account Expansion</td>
                            <td>Discovery & Needs Analysis</td>
                        </tr>
                    </tbody>
                </table>
                """,
                unsafe_allow_html=True
            )
