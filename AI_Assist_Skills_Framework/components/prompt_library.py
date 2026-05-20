"""
Copyable Prompt Library Component
"""

import streamlit as st
from utils.llm_utils import is_llm_configured, generate_llm_response
from utils.file_reader import render_file_upload, combine_prompt_with_context, format_skill_context, combine_prompt_with_skill_context


def on_copy_prompt(prompt_text):
    """
    Callback function when copy button is clicked.
    Shows a toast message.
    
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
    st.session_state[f"lib_llm_response_{hash(prompt_text)}"] = response


def render_prompt_library(skills_data):
    """
    Render copyable prompt library with search and filtering.
    
    Args:
        skills_data (list): List of skill dictionaries
    """
    # Get all skill names for filter
    skill_names = [skill['title'] for skill in skills_data]
    
    # Search bar
    search_query = st.text_input(
        "🔍 Search prompts...",
        placeholder="Search prompts... (e.g., 'TCO', 'healthcare', 'pipeline')",
        key="prompt_search"
    )
    
    # Skill filter
    selected_skills = st.multiselect(
        "Filter by Skill",
        options=skill_names,
        default=skill_names,
        key="skill_filter"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Flatten all prompts with their skill info
    all_prompts = []
    for skill in skills_data:
        if skill['title'] in selected_skills:
            for prompt in skill['ai_prompts']:
                all_prompts.append({
                    'skill': skill,
                    'prompt': prompt
                })
    
    # Filter by search query
    if search_query:
        search_query_lower = search_query.lower()
        all_prompts = [
            p for p in all_prompts
            if search_query_lower in p['prompt'].lower() or
               search_query_lower in p['skill']['title'].lower() or
               search_query_lower in p['skill']['tagline'].lower()
        ]
    
    # Show count
    st.markdown(
        f"""
        <p style="color: #8B9DB5; font-size: 14px; margin-bottom: 24px;">
            Showing <strong>{len(all_prompts)}</strong> of 24 prompts
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # Group prompts by skill for display
    prompts_by_skill = {}
    for prompt_item in all_prompts:
        skill_title = prompt_item['skill']['title']
        if skill_title not in prompts_by_skill:
            prompts_by_skill[skill_title] = {
                'skill': prompt_item['skill'],
                'prompts': []
            }
        prompts_by_skill[skill_title]['prompts'].append(prompt_item['prompt'])
    
    # Render prompts grouped by skill
    for skill_title, data in prompts_by_skill.items():
        skill = data['skill']
        prompts = data['prompts']
        
        # Skill section header
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, {skill['color']}20 0%, {skill['color']}10 100%);
                border: 1px solid {skill['color']}40;
                border-radius: 12px;
                padding: 16px 20px;
                margin: 24px 0 16px 0;
            ">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <span style="font-size: 32px;">{skill['icon']}</span>
                    <h3 style="color: #E8EDF3; margin: 0; font-size: 20px; font-weight: 600;">
                        {skill['title']}
                    </h3>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Render each prompt
        for idx, prompt in enumerate(prompts, 1):
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
                key=f"lib_edit_prompt_{skill['id']}_{idx}",
                height=100,
                help="Customize the prompt before generating LLM response"
            )
            
            # Add toggle for skill framework context
            include_skill_context = st.checkbox(
                "📚 Include skill framework context",
                key=f"lib_skill_context_{skill['id']}_{idx}",
                help="Include the skill's playbook and methodology as context for the LLM"
            )
            
            # Add file upload for document context
            document_context = render_file_upload(f"lib_{skill['id']}_{idx}")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.button(
                    "📋 Copy",
                    key=f"lib_copy_{skill['id']}_{idx}",
                    on_click=on_copy_prompt,
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
                        key=f"lib_generate_{skill['id']}_{idx}",
                        on_click=on_generate_click,
                        args=(edited_prompt, document_context, skill_context),
                        help="Generate LLM response with context",
                        use_container_width=True
                    )
            
            st.markdown(
                """
                <p style="color: #0672CB; font-size: 12px; margin: -8px 0 16px 0;">
                    Use in your friendly AI Assistant →
                </p>
                """,
                unsafe_allow_html=True
            )
            
            # Display LLM response if generated
            response_key = f"lib_llm_response_{hash(edited_prompt)}"
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
    
    # Tips section
    st.markdown("<br>", unsafe_allow_html=True)
    
    tips_html = """
    <div style="
        background: rgba(6, 114, 203, 0.08);
        border: 1px solid rgba(6, 114, 203, 0.2);
        border-radius: 12px;
        padding: 24px;
        margin-top: 32px;
    ">
        <h3 style="color: #0672CB; margin: 0 0 16px 0; font-size: 18px; font-weight: 600;">
            💡 Tips for Better Prompts
        </h3>
        <div style="display: flex; flex-direction: column; gap: 12px;">
            <div style="display: flex; gap: 12px;">
                <span style="color: #0672CB; font-weight: bold;">•</span>
                <p style="color: #8B9DB5; margin: 0; font-size: 14px; line-height: 1.5;">
                    Always provide context: paste your meeting notes, deal details, or customer info after the prompt
                </p>
            </div>
            <div style="display: flex; gap: 12px;">
                <span style="color: #0672CB; font-weight: bold;">•</span>
                <p style="color: #8B9DB5; margin: 0; font-size: 14px; line-height: 1.5;">
                    Be specific: include the customer's industry, size, and current technology stack
                </p>
            </div>
            <div style="display: flex; gap: 12px;">
                <span style="color: #0672CB; font-weight: bold;">•</span>
                <p style="color: #8B9DB5; margin: 0; font-size: 14px; line-height: 1.5;">
                    Ask for format: request tables, emails, talk tracks, or battle cards specifically
                </p>
            </div>
            <div style="display: flex; gap: 12px;">
                <span style="color: #0672CB; font-weight: bold;">•</span>
                <p style="color: #8B9DB5; margin: 0; font-size: 14px; line-height: 1.5;">
                    Iterate: use follow-up prompts to refine your friendly AI Assistant's output
                </p>
            </div>
        </div>
    </div>
    """
    
    st.markdown(tips_html, unsafe_allow_html=True)
