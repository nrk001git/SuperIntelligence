"""
Dell OAuth2 LLM Client
A reusable module for integrating with Dell's LLM services using OAuth2 authentication
"""

import os
import logging
import time
import httpx
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)


class DellOAuth2LLMClient:
    """
    Dell OAuth2 LLM Client for integrating with Dell's LLM services
    
    Supports OAuth2 authentication using Dell's aia_auth module with fallback
    to standard OAuth2 client credentials flow.
    """
    
    def __init__(self, client_id: str, client_secret: str, model: str,
                 base_url: str = None, token_endpoint: str = None):
        """
        Initialize Dell OAuth2 LLM Client
        
        Args:
            client_id: OAuth2 client ID
            client_secret: OAuth2 client secret
            model: LLM model name (e.g., gpt-oss-20b, gpt-oss-120b)
            base_url: LLM API base URL (default: from env or http://localhost:8000/v1)
            token_endpoint: OAuth2 token endpoint (optional, uses Dell auth if not provided)
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.model = model
        self.base_url = base_url or os.getenv("DELL_LLM_BASE_URL", "https://aia.gateway.dell.com/genai/dev/v1")
        self.token_endpoint = token_endpoint or os.getenv("DELL_TOKEN_ENDPOINT")
        self.access_token = None
        self.token_expiry = None
        self.http_client = httpx.Client(verify=False)  # Disable SSL verification for self-signed certificates
        
    def _get_access_token(self) -> str:
        """Get or refresh OAuth2 access token using Dell auth pattern"""
        logger.info(f"Attempting to get OAuth2 access token")
        
        # Check if token is still valid (with 5 minute buffer)
        if self.access_token and self.token_expiry and time.time() < self.token_expiry - 300:
            logger.info("Using cached OAuth2 access token (still valid)")
            return self.access_token
        
        logger.info("Requesting new OAuth2 access token")
        
        # Try to use Dell auth pattern
        try:
            from aia_auth import auth
            logger.info("Using Dell aia_auth.client_credentials() pattern")
            
            access_token_obj = auth.client_credentials(self.client_id, self.client_secret)
            self.access_token = access_token_obj.token
            # Assume 1 hour expiry for Dell tokens
            self.token_expiry = time.time() + 3600
            
            logger.info(f"Successfully obtained OAuth2 access token via Dell aia_auth")
            logger.info(f"Token expiry time: {self.token_expiry}")
            return self.access_token
            
        except ImportError:
            logger.warning("Dell aia_auth module not available, falling back to standard OAuth2")
            return self._get_access_token_standard()
        except Exception as e:
            logger.error(f"Dell aia_auth failed: {str(e)}")
            logger.info("Falling back to standard OAuth2")
            return self._get_access_token_standard()
    
    def _get_access_token_standard(self) -> str:
        """Get OAuth2 access token using standard OAuth2 flow"""
        if not self.token_endpoint:
            raise ValueError("Token endpoint required for standard OAuth2 flow")
            
        logger.info(f"Attempting standard OAuth2 token request to: {self.token_endpoint}")
        
        try:
            logger.info(f"Sending OAuth2 token request to: {self.token_endpoint}")
            logger.info(f"Using client_id: {self.client_id[:10]}... (truncated)")
            logger.warning("SSL verification disabled for self-signed certificates")
            
            response = self.http_client.post(
                self.token_endpoint,
                data={
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "grant_type": "client_credentials"
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            
            logger.info(f"OAuth2 token response status: {response.status_code}")
            response.raise_for_status()
            
            token_data = response.json()
            self.access_token = token_data.get("access_token")
            expires_in = token_data.get("expires_in", 3600)
            self.token_expiry = time.time() + expires_in
            
            logger.info(f"Successfully obtained OAuth2 access token, expires in {expires_in} seconds")
            logger.info(f"Token expiry time: {self.token_expiry}")
            return self.access_token
        except Exception as e:
            logger.error(f"OAuth2 token request failed: {str(e)}")
            logger.error(f"Error type: {type(e).__name__}")
            raise
    
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate text using Dell LLM API
        
        Args:
            prompt: Text prompt for LLM
            **kwargs: Additional parameters for LLM API (e.g., max_tokens, temperature)
            
        Returns:
            Generated text response
            
        Raises:
            ImportError: If OpenAI library is not installed
            Exception: If API call fails
        """
        try:
            logger.info(f"Generating text with model: {self.model}")
            logger.info(f"Base URL: {self.base_url}")
            
            import openai
            import urllib3
            # Disable SSL warnings
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            
            access_token = self._get_access_token()
            logger.info("Successfully obtained access token for API call")
            
            client = openai.OpenAI(
                base_url=self.base_url,
                http_client=self.http_client,
                api_key=access_token
            )
            
            logger.info("Sending request to LLM API")
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            logger.info("Successfully received response from LLM API")
            return response.choices[0].message.content
        except ImportError:
            logger.error("OpenAI library not installed. Install with: pip install openai")
            raise
        except Exception as e:
            logger.error(f"Dell LLM API error: {str(e)}")
            logger.error(f"Error type: {type(e).__name__}")
            raise
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Generate response using Dell LLM chat API
        
        Args:
            messages: List of chat messages with 'role' and 'content'
            **kwargs: Additional parameters for LLM API (e.g., max_tokens, temperature)
            
        Returns:
            Generated text response
            
        Raises:
            ImportError: If OpenAI library is not installed
            Exception: If API call fails
        """
        try:
            logger.info(f"Chat with model: {self.model}")
            logger.info(f"Base URL: {self.base_url}")
            logger.info(f"Number of messages: {len(messages)}")
            
            import openai
            import urllib3
            # Disable SSL warnings
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            
            access_token = self._get_access_token()
            logger.info("Successfully obtained access token for chat API call")
            
            client = openai.OpenAI(
                base_url=self.base_url,
                http_client=self.http_client,
                api_key=access_token
            )
            
            logger.info("Sending chat request to LLM API")
            response = client.chat.completions.create(
                model=self.model,
                messages=messages,
                **kwargs
            )
            logger.info("Successfully received chat response from LLM API")
            return response.choices[0].message.content
        except ImportError:
            logger.error("OpenAI library not installed. Install with: pip install openai")
            raise
        except Exception as e:
            logger.error(f"Dell LLM API error: {str(e)}")
            logger.error(f"Error type: {type(e).__name__}")
            raise
    
    def is_configured(self) -> bool:
        """Check if client is configured with credentials"""
        return bool(self.client_id and self.client_secret)
