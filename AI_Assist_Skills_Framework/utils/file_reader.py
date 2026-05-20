"""
File Reader Utility for Document Context
Supports reading text, PDF, and Word documents for LLM context
"""

import streamlit as st
from typing import Optional, List, Dict
import io


def read_uploaded_file(uploaded_file) -> Optional[str]:
    """
    Read content from an uploaded file based on its type.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        str: File content as text, or None if reading fails
    """
    if uploaded_file is None:
        return None
    
    try:
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        if file_extension == 'txt':
            return read_text_file(uploaded_file)
        elif file_extension == 'pdf':
            return read_pdf_file(uploaded_file)
        elif file_extension == 'docx':
            return read_word_file(uploaded_file)
        else:
            st.error(f"Unsupported file type: .{file_extension}. Please upload .txt, .pdf, or .docx files.")
            return None
            
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")
        return None


def read_text_file(uploaded_file) -> str:
    """
    Read a plain text file.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        str: File content
    """
    try:
        content = uploaded_file.read().decode('utf-8')
        return content
    except UnicodeDecodeError:
        # Try with different encoding
        try:
            content = uploaded_file.read().decode('latin-1')
            return content
        except Exception as e:
            st.error(f"Error decoding text file: {str(e)}")
            return ""


def read_pdf_file(uploaded_file) -> str:
    """
    Read a PDF file using PyPDF2.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        str: Extracted text content
    """
    try:
        import PyPDF2
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except ImportError:
        st.warning("PyPDF2 not installed. PDF reading not available. Install with: pip install PyPDF2")
        return ""
    except Exception as e:
        st.error(f"Error reading PDF file: {str(e)}")
        return ""


def read_word_file(uploaded_file) -> str:
    """
    Read a Word document using python-docx.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        str: Extracted text content
    """
    try:
        import docx
        doc = docx.Document(uploaded_file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except ImportError:
        st.warning("python-docx not installed. Word document reading not available. Install with: pip install python-docx")
        return ""
    except Exception as e:
        st.error(f"Error reading Word document: {str(e)}")
        return ""


def render_file_upload(section_key: str) -> Optional[str]:
    """
    Render a file upload component and return the document context.
    
    Args:
        section_key: Unique key for the file upload section (e.g., 'skill_detail', 'prompt_library')
        
    Returns:
        Optional[str]: Document content if file uploaded, None otherwise
    """
    st.markdown(
        """
        <div style="
            background: rgba(6, 114, 203, 0.05);
            border: 1px dashed rgba(6, 114, 203, 0.3);
            border-radius: 8px;
            padding: 16px;
            margin: 8px 0;
        ">
            <p style="color: #0672CB; font-size: 13px; font-weight: 600; margin: 0 0 8px 0;">
                📎 Upload Document for Context (Optional)
            </p>
            <p style="color: #8B9DB5; font-size: 12px; margin: 0 0 12px 0;">
                Upload a document (.txt, .pdf, .docx) to provide additional context for the LLM.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['txt', 'pdf', 'docx'],
        key=f"file_upload_{section_key}",
        help="Upload a document to provide additional context for the AI Assistant"
    )
    
    if uploaded_file:
        content = read_uploaded_file(uploaded_file)
        if content:
            # Display a summary of the uploaded document
            st.markdown(
                f"""
                <div style="
                    background: rgba(26, 140, 94, 0.08);
                    border: 1px solid rgba(26, 140, 94, 0.3);
                    border-radius: 8px;
                    padding: 12px;
                    margin: 8px 0;
                ">
                    <p style="color: #1A8C5E; font-size: 12px; font-weight: 600; margin: 0 0 4px 0;">
                        ✅ Document Uploaded: {uploaded_file.name}
                    </p>
                    <p style="color: #8B9DB5; font-size: 11px; margin: 0;">
                        Size: {uploaded_file.size / 1024:.1f} KB | Content length: {len(content)} characters
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            return content
    
    return None


def combine_prompt_with_context(prompt: str, context: Optional[str]) -> str:
    """
    Combine a prompt with document context for LLM generation.
    
    Args:
        prompt: The original prompt
        context: Optional document context
        
    Returns:
        str: Combined prompt with context
    """
    if not context or not context.strip():
        return prompt
    
    combined_prompt = f"""Context from uploaded document:
---
{context[:10000]}  # Limit context to first 10,000 characters to avoid token limits
---

{prompt}"""
    
    return combined_prompt


def format_skill_context(skill: Dict) -> str:
    """
    Format skill data as context for LLM generation.
    
    Args:
        skill: Skill dictionary containing skill data
        
    Returns:
        str: Formatted skill context
    """
    context = f"""Skill Framework Context:
---
Skill: {skill['title']}
Tagline: {skill['tagline']}
Description: {skill['description']}

When to Use:
"""
    for item in skill['when_to_use']:
        context += f"- {item}\n"
    
    context += "\nStep-by-Step Playbook:\n"
    for idx, step in enumerate(skill['steps'], 1):
        context += f"{idx}. {step['title']}: {step['detail']}\n"
    
    context += "---"
    
    return context


def combine_prompt_with_skill_context(prompt: str, skill_context: Optional[str], document_context: Optional[str] = None) -> str:
    """
    Combine a prompt with skill context and optionally document context.
    
    Args:
        prompt: The original prompt
        skill_context: Optional skill framework context
        document_context: Optional uploaded document context
        
    Returns:
        str: Combined prompt with contexts
    """
    contexts = []
    
    if skill_context and skill_context.strip():
        contexts.append(skill_context)
    
    if document_context and document_context.strip():
        contexts.append(f"Context from uploaded document:\n---\n{document_context[:10000]}\n---")
    
    if not contexts:
        return prompt
    
    combined_prompt = "\n\n".join(contexts) + f"\n\n{prompt}"
    
    return combined_prompt
