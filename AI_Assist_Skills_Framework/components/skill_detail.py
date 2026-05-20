"""
Detailed Skill View Component
"""

import streamlit as st
from utils.llm_utils import is_llm_configured, generate_llm_response
from utils.file_reader import render_file_upload, combine_prompt_with_context, format_skill_context, combine_prompt_with_skill_context


def on_back_click():
    """
    Callback function when back button is clicked.
    Returns to the skills grid view.
    """
    st.session_state.current_view = "Skills Dashboard"
    st.session_state.selected_skill_id = None


def on_copy_click(prompt_text):
    """
    Callback function when copy button is clicked.
    Shows a toast message and copies the prompt to clipboard.
    
    Args:
        prompt_text (str): The prompt text to copy
    """
    st.toast("✅ Prompt copied! Paste it into your friendly AI Assistant.", icon="✓")


def on_generate_click(prompt_text, context=None, skill_context=None):
    """
    Callback function when generate button is clicked.
    Generates LLM response and stores in session state.
    
    Args:
        prompt_text (str): The prompt text to send to LLM
        context (str, optional): Additional document context to include
        skill_context (str, optional): Skill framework context to include
    """
    if not is_llm_configured():
        st.error("LLM not configured. Please add DELL_CLIENT_ID and DELL_CLIENT_SECRET to .streamlit/secrets.toml")
        return
    
    # Combine prompt with skill context and document context if provided
    final_prompt = combine_prompt_with_skill_context(prompt_text, skill_context, context)
    
    response = generate_llm_response(final_prompt)
    st.session_state[f"llm_response_{hash(prompt_text)}"] = response


def render_skill_detail(skill):
    """
    Render detailed view of a skill.
    
    Args:
        skill (dict): The skill dictionary containing all skill data
    """
    # Back button
    if st.button("← Back to Skills", key="back_button", on_click=on_back_click, use_container_width=False):
        pass
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Skill header section
    header_html = f"""
    <div style="
        background: linear-gradient(135deg, {skill['color']}20 0%, {skill['color']}10 100%);
        border: 1px solid {skill['color']}40;
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 32px;
    ">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 16px;">
            <div style="font-size: 64px;">{skill['icon']}</div>
            <div>
                <h1 style="color: #E8EDF3; margin: 0; font-size: 32px; font-weight: 700;">
                    {skill['title']}
                </h1>
                <p style="color: {skill['color']}; margin: 8px 0 0 0; font-size: 18px; font-style: italic;">
                    {skill['tagline']}
                </p>
            </div>
        </div>
        <p style="color: #8B9DB5; margin: 0; font-size: 16px; line-height: 1.6;">
            {skill['description']}
        </p>
    </div>
    """
    
    st.markdown(header_html, unsafe_allow_html=True)
    
    # When to Use section
    st.markdown(f"""
    <div class="section-header" style="color: {skill['color']};">
        When to Use
    </div>
    """, unsafe_allow_html=True)
    
    for item in skill['when_to_use']:
        item_html = f"""
        <div class="when-to-use-item" style="
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 8px;
            padding: 12px 16px;
            margin-bottom: 8px;
        ">
            <span style="color: #E8EDF3; font-size: 15px;">{item}</span>
        </div>
        """
        st.markdown(item_html, unsafe_allow_html=True)
    
    # Step-by-Step Playbook section
    st.markdown(f"""
    <div class="section-header" style="color: {skill['color']};">
        Step-by-Step Playbook
    </div>
    """, unsafe_allow_html=True)
    
    for idx, step in enumerate(skill['steps'], 1):
        step_html = f"""
        <div class="step-card" style="--skill-color: {skill['color']};">
            <div style="display: flex; align-items: flex-start;">
                <div class="step-number" style="background: {skill['color']}40; color: {skill['color']};">
                    {idx}
                </div>
                <div style="flex: 1;">
                    <h4 style="color: #E8EDF3; margin: 0 0 8px 0; font-size: 16px; font-weight: 600;">
                        {step['title']}
                    </h4>
                    <p style="color: #8B9DB5; margin: 0; font-size: 14px; line-height: 1.5;">
                        {step['detail']}
                    </p>
                </div>
            </div>
        </div>
        """
        st.markdown(step_html, unsafe_allow_html=True)
    
    # Try These Prompts with your friendly AI Assistant section
    st.markdown(f"""
    <div class="section-header" style="color: {skill['color']};">
        Try These Prompts with your friendly AI Assistant
    </div>
    """, unsafe_allow_html=True)
    
    for idx, prompt in enumerate(skill['ai_prompts'], 1):
        # Show original prompt
        prompt_html = f"""
        <div class="prompt-card">
            "{prompt}"
        </div>
        """
        st.markdown(prompt_html, unsafe_allow_html=True)
        
        # Add editable text area for prompt customization
        edited_prompt = st.text_area(
            "✏️ Edit prompt before generating (optional):",
            value=prompt,
            key=f"edit_prompt_{skill['id']}_{idx}",
            height=100,
            help="Customize the prompt before generating LLM response"
        )
        
        # Add toggle for skill framework context
        include_skill_context = st.checkbox(
            "📚 Include skill framework context",
            key=f"skill_context_{skill['id']}_{idx}",
            help="Include the skill's playbook and methodology as context for the LLM"
        )
        
        # Add file upload for document context
        document_context = render_file_upload(f"skill_{skill['id']}_{idx}")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.button(
                "📋 Copy",
                key=f"copy_btn_{skill['id']}_{idx}",
                on_click=on_copy_click,
                args=(edited_prompt,),
                help="Copy to clipboard",
                use_container_width=True
            )
        
        with col2:
            if is_llm_configured():
                # Prepare skill context if toggle is enabled
                skill_context = format_skill_context(skill) if include_skill_context else None
                
                st.button(
                    "🤖 Generate Response",
                    key=f"generate_btn_{skill['id']}_{idx}",
                    on_click=on_generate_click,
                    args=(edited_prompt, document_context, skill_context),
                    help="Generate LLM response with context",
                    use_container_width=True
                )
        
        # Display LLM response if generated
        response_key = f"llm_response_{hash(edited_prompt)}"
        if response_key in st.session_state:
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
            st.markdown(st.session_state[response_key])
