"""
LLM Utility Functions
"""

import streamlit as st
from utils.llm_client import DellOAuth2LLMClient


@st.cache_resource
def get_llm_client():
    """
    Initialize and cache the Dell OAuth2 LLM client.
    
    Returns:
        DellOAuth2LLMClient: Initialized LLM client or None if not configured
    """
    try:
        client_id = st.secrets.get("DELL_CLIENT_ID")
        client_secret = st.secrets.get("DELL_CLIENT_SECRET")
        model = st.secrets.get("DELL_LLM_MODEL", "gpt-oss-20b")
        base_url = st.secrets.get("DELL_LLM_BASE_URL", "https://aia.gateway.dell.com/genai/dev/v1")
        token_endpoint = st.secrets.get("DELL_TOKEN_ENDPOINT")
        
        if not client_id or not client_secret:
            return None
        
        return DellOAuth2LLMClient(
            client_id=client_id,
            client_secret=client_secret,
            model=model,
            base_url=base_url,
            token_endpoint=token_endpoint
        )
    except Exception as e:
        st.error(f"Failed to initialize LLM client: {str(e)}")
        return None


def is_llm_configured():
    """
    Check if LLM client is configured with credentials.
    
    Returns:
        bool: True if configured, False otherwise
    """
    client = get_llm_client()
    return client is not None and client.is_configured()


def generate_llm_response(prompt: str, **kwargs) -> str:
    """
    Generate LLM response using the configured client.
    
    Args:
        prompt: The prompt to send to the LLM
        **kwargs: Additional parameters for the LLM API
        
    Returns:
        str: The LLM response or error message
    """
    client = get_llm_client()
    
    if not client:
        return "LLM client not configured. Please add DELL_CLIENT_ID and DELL_CLIENT_SECRET to .streamlit/secrets.toml"
    
    try:
        with st.spinner("Generating response..."):
            response = client.generate(prompt, **kwargs)
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"
