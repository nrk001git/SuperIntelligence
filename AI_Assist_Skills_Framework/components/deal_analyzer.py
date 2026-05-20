"""
Deal Analyzer Interactive Tool
"""

import streamlit as st
from utils.styles import colored_header
from utils.llm_utils import is_llm_configured, generate_llm_response
from utils.file_reader import render_file_upload, combine_prompt_with_context


def on_copy_prompt(prompt_text):
    """
    Callback function when copy button is clicked.
    Shows a toast message.
    
    Args:
        prompt_text (str): The prompt text to copy
    """
    st.toast("✅ Prompt copied! Paste it into your friendly AI Assistant.", icon="✓")


def on_generate_click(prompt_text, context=None):
    """
    Callback function when generate button is clicked.
    Generates LLM response and stores in session state.
    
    Args:
        prompt_text (str): The prompt text to send to LLM
        context (str, optional): Additional document context to include
    """
    if not is_llm_configured():
        st.error("LLM not configured. Please add DELL_CLIENT_ID and DELL_CLIENT_SECRET to .streamlit/secrets.toml")
        return
    
    # Combine prompt with document context if provided
    final_prompt = combine_prompt_with_context(prompt_text, context)
    
    response = generate_llm_response(final_prompt)
    st.session_state["deal_analyzer_llm_response"] = response


def render_deal_analyzer():
    """Render the Deal Analyzer interactive tool."""
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
                🎯 Quick Deal Health Check
            </h1>
            <p style="color: #8B9DB5; margin: 0; font-size: 16px; line-height: 1.6;">
                Assess your deal's health and get actionable recommendations.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.form("deal_analyzer_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            deal_name = st.text_input("Deal Name", placeholder="e.g., Acme Corp - Server Refresh")
            deal_value = st.number_input("Deal Value ($)", min_value=0, step=10000, value=0)
            deal_stage = st.selectbox(
                "Deal Stage",
                ["Prospecting", "Qualification", "Solution Design", "Proposal", "Negotiation", "Verbal Commit"],
                index=0
            )
        
        with col2:
            budget_confirmed = st.radio(
                "Budget Confirmed?",
                ["Yes", "No", "Unknown"],
                horizontal=True
            )
            decision_maker = st.radio(
                "Decision Maker Identified?",
                ["Yes", "No", "Unknown"],
                horizontal=True
            )
            compelling_event = st.radio(
                "Compelling Event / Timeline?",
                ["Yes, specific date", "Vague", "None"],
                horizontal=True
            )
        
        st.markdown("---")
        
        col3, col4 = st.columns(2)
        
        with col3:
            champion = st.radio(
                "Champion Engaged?",
                ["Yes, actively", "Passive", "No champion"],
                horizontal=True
            )
            technical_win = st.radio(
                "Technical Win?",
                ["Won", "In progress", "Not started", "Lost"],
                horizontal=True
            )
        
        with col4:
            competition = st.multiselect(
                "Competition",
                ["HPE", "Lenovo", "Cisco", "Nutanix", "Pure Storage", "Cloud-only", "None/Unknown"],
                default=["None/Unknown"]
            )
        
        submitted = st.form_submit_button("Analyze Deal", use_container_width=True)
    
    if submitted:
        # Calculate deal health score
        score = 0
        gaps = []
        
        # Budget: +20 (yes), +5 (unknown), 0 (no)
        if budget_confirmed == "Yes":
            score += 20
        elif budget_confirmed == "Unknown":
            score += 5
        else:
            gaps.append({"area": "Budget", "score": 0, "skill": "Objection Handling", "action": "build a business case and justify investment"})
        
        # Decision maker: +20 (yes), +5 (unknown), 0 (no)
        if decision_maker == "Yes":
            score += 20
        elif decision_maker == "Unknown":
            score += 5
        else:
            gaps.append({"area": "Decision Maker", "score": 0, "skill": "Discovery & Needs Analysis", "action": "identify and engage the decision maker"})
        
        # Compelling event: +20 (specific), +10 (vague), 0 (none)
        if compelling_event == "Yes, specific date":
            score += 20
        elif compelling_event == "Vague":
            score += 10
        else:
            gaps.append({"area": "Compelling Event", "score": 0, "skill": "Discovery & Needs Analysis", "action": "identify a compelling event or timeline"})
        
        # Champion: +20 (active), +10 (passive), 0 (none)
        if champion == "Yes, actively":
            score += 20
        elif champion == "Passive":
            score += 10
        else:
            gaps.append({"area": "Champion", "score": 0, "skill": "Discovery & Needs Analysis", "action": "identify and develop a champion"})
        
        # Technical win: +20 (won), +15 (in progress), +5 (not started), 0 (lost)
        if technical_win == "Won":
            score += 20
        elif technical_win == "In progress":
            score += 15
        elif technical_win == "Not started":
            score += 5
        else:
            gaps.append({"area": "Technical Win", "score": 0, "skill": "Solution Architecture", "action": "develop a technical win strategy"})
        
        # Determine health status
        if score >= 80:
            status = "🟢 Strong"
            message = "This deal is well-qualified. Focus on closing."
            color = "#1A8C5E"
        elif score >= 60:
            status = "🟡 Moderate"
            message = "Good progress. Shore up the gaps below."
            color = "#C9A227"
        elif score >= 40:
            status = "🟠 At Risk"
            message = "Significant gaps. Needs immediate attention."
            color = "#C94A16"
        else:
            status = "🔴 Weak"
            message = "This deal needs re-qualification or deprioritization."
            color = "#C91616"
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Display score
        st.markdown(
            f"""
            <div style="
                background: {color}20;
                border: 2px solid {color};
                border-radius: 16px;
                padding: 32px;
                text-align: center;
                margin-bottom: 32px;
            ">
                <h2 style="color: {color}; margin: 0 0 8px 0; font-size: 48px; font-weight: 700;">
                    {status}
                </h2>
                <div style="color: #E8EDF3; font-size: 64px; font-weight: 700; margin: 16px 0;">
                    {score}/100
                </div>
                <p style="color: #E8EDF3; margin: 0; font-size: 18px;">
                    {message}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Recommended Skills
        if gaps:
            colored_header("Recommended Skills to Address Gaps")
            
            for gap in gaps:
                st.markdown(
                    f"""
                    <div class="step-card" style="border-left: 3px solid #0672CB;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <h4 style="color: #E8EDF3; margin: 0; font-size: 16px; font-weight: 600;">
                                {gap['area']} Gap
                            </h4>
                            <span style="color: #C94A16; font-weight: bold; font-size: 14px;">{gap['score']} pts</span>
                        </div>
                        <p style="color: #8B9DB5; margin: 0; font-size: 14px; line-height: 1.5;">
                            Use <strong style="color: #0672CB;">{gap['skill']}</strong> to {gap['action']}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.markdown(
                """
                <div style="
                    background: rgba(26, 140, 94, 0.08);
                    border: 1px solid rgba(26, 140, 94, 0.3);
                    border-radius: 12px;
                    padding: 20px;
                ">
                    <p style="color: #1A8C5E; margin: 0; font-size: 16px; font-weight: 600;">
                        ✅ No gaps identified! This deal is well-positioned.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Suggested AI Assistant Prompt
        colored_header("Suggested AI Assistant Prompt")
        
        if gaps:
            gap_descriptions = ", ".join([f"{gap['area']} ({gap['skill']})" for gap in gaps])
            prompt = f"I have a ${deal_value:,.0f} deal at {deal_stage} stage. Gaps: {gap_descriptions}. Help me address these gaps and move this deal forward."
        else:
            prompt = f"I have a ${deal_value:,.0f} deal at {deal_stage} stage with no identified gaps. Help me create a closing strategy and next steps."
        
        # Show suggested prompt
        st.markdown(
            f"""
            <div class="prompt-card">
                "{prompt}"
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Add editable text area for prompt customization
        edited_prompt = st.text_area(
            "✏️ Edit prompt before generating (optional):",
            value=prompt,
            key="deal_analyzer_edit_prompt",
            height=100,
            help="Customize the prompt before generating LLM response"
        )
        
        # Add file upload for document context
        document_context = render_file_upload("deal_analyzer")
        
        col5, col6 = st.columns([1, 1])
        
        with col5:
            st.button(
                "📋 Copy",
                key="deal_analyzer_copy",
                on_click=on_copy_prompt,
                args=(edited_prompt,),
                help="Copy to clipboard",
                use_container_width=True
            )
        
        with col6:
            if is_llm_configured():
                st.button(
                    "🤖 Generate Response",
                    key="deal_analyzer_generate",
                    on_click=on_generate_click,
                    args=(edited_prompt, document_context),
                    help="Generate LLM response with document context",
                    use_container_width=True
                )
        
        # Display LLM response if generated
        if "deal_analyzer_llm_response" in st.session_state:
            st.markdown(
                f"""
                <div style="
                    background: rgba(6, 114, 203, 0.08);
                    border: 1px solid rgba(6, 114, 203, 0.3);
                    border-radius: 12px;
                    padding: 16px;
                    margin: 8px 0;
                ">
                    <div style="color: #0672CB; font-weight: 600; font-size: 14px; margin-bottom: 8px;">
                        🤖 LLM Response
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(st.session_state["deal_analyzer_llm_response"])
