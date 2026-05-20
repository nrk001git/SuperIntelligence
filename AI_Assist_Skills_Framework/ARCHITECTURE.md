# Dell Sales Skills Framework - Architecture Overview

## Executive Summary

The Dell Sales Skills Framework is a modern web-based application designed to empower Dell sales teams with AI-powered assistance. It provides a structured approach to mastering core sales competencies through interactive playbooks, ready-to-use prompts, and direct integration with Dell's LLM services.

**Key Value Proposition:**
- **24/7 AI Coaching**: Instant access to sales expertise through AI-powered prompts
- **Structured Learning**: 6 core sales skills with step-by-step playbooks
- **Workflow Automation**: Pre-defined skill chains for common sales scenarios
- **Deal Intelligence**: Interactive deal analyzer with gap identification
- **Seamless Integration**: Direct LLM integration with Dell's secure AI services
- **Document Context**: Upload documents (.txt, .pdf, .docx) to provide additional context for AI responses

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     User Interface Layer                        │
│                  (Streamlit Web Application)                    │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Presentation Layer                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Skills       │  │ Workflows    │  │ Prompt       │          │
│  │ Dashboard    │  │ View         │  │ Library      │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐                            │
│  │ Deal         │  │ How to Use   │                            │
│  │ Analyzer     │  │ Guide        │                            │
│  └──────────────┘  └──────────────┘                            │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Business Logic Layer                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Session      │  │ Navigation   │  │ LLM          │          │
│  │ Management   │  │ Controller   │  │ Integration  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                       Data Layer                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Skills       │  │ Workflows    │  │ User         │          │
│  │ Data Store   │  │ Data Store   │  │ Session      │          │
│  └──────────────┘  └──────────────┘  │ State        │          │
│                                      └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                  External Integration Layer                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Dell LLM     │  │ Dell OAuth2  │  │ Clipboard    │          │
│  │ API Gateway  │  │ Auth Service │  │ API          │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Architecture

### 1. User Interface Layer (Streamlit)

**Technology:** Streamlit (Python Web Framework)

**Purpose:** Provides an intuitive, interactive web interface for sales teams.

**Key Features:**
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Real-time Interactivity**: Instant feedback without page reloads
- **Dell-Branded UI**: Consistent with Dell's visual identity
- **Accessible**: WCAG 2.1 compliant for inclusive user experience

**Components:**
- **Sidebar Navigation**: Quick access to all features
- **Skills Dashboard**: Grid view of 6 core sales competencies
- **Skill Detail View**: Deep dive into individual skills with playbooks
- **Workflows View**: Pre-defined skill chains for common scenarios
- **Prompt Library**: Searchable repository of 24 ready-to-use prompts
- **Deal Analyzer**: Interactive tool for deal health assessment
- **How to Use Guide**: Comprehensive documentation

---

### 2. Presentation Layer

**Components:**

#### Skills Dashboard
- Displays 6 core sales skills in a card grid
- Shows animated metrics (Skills, Steps, Prompts, Workflows)
- Quick reference table mapping deal stages to skills
- Click-to-explore functionality for detailed views

#### Skill Detail View
- 4-step actionable playbook for each skill
- "When to Use" scenarios
- 4 ready-to-use AI Assistant prompts per skill
- Editable prompt input before LLM generation
- Document upload for additional context (.txt, .pdf, .docx)
- Direct LLM response display

#### Workflows View
- 3 pre-defined workflow chains:
  - New Deal Qualification
  - Competitive Displacement
  - Installed Base Growth
- Visual skill chaining with navigation arrows
- Pro tips for optimal workflow usage

#### Prompt Library
- Search by keyword
- Filter by skill category
- All 24 prompts in one location
- Editable prompts before generation
- Document upload for additional context (.txt, .pdf, .docx)
- Usage best practices

#### Deal Analyzer
- Interactive form for deal information
- Health score calculation (0-100)
- Gap identification with skill recommendations
- Auto-generated contextual prompts
- Document upload for additional context (.txt, .pdf, .docx)
- LLM integration for strategy generation

---

### 3. Business Logic Layer

#### Session Management
- **Purpose**: Maintains user state during session
- **Capabilities**:
  - Track selected skills and navigation state
  - Store completed skills for progress tracking
  - Cache LLM responses for efficiency
  - Persist user preferences during session

#### Navigation Controller
- **Purpose**: Manages routing between different views
- **Capabilities**:
  - Handle skill selection and detail navigation
  - Workflow to skill navigation
  - Back button functionality
  - Error handling and recovery

#### LLM Integration
- **Purpose**: Direct integration with Dell's AI services
- **Capabilities**:
  - OAuth2 authentication with Dell's auth service
  - Token management and caching
  - Prompt generation and response handling
  - Error handling with user-friendly messages
  - Conditional rendering based on configuration
  - Document context integration for enhanced responses

#### File Reader
- **Purpose**: Read and process uploaded documents for LLM context
- **Capabilities**:
  - Support for multiple file formats (.txt, .pdf, .docx)
  - File type validation and error handling
  - Content extraction and text processing
  - Context length limiting (10,000 character limit)
  - User feedback on upload status

---

### 4. Data Layer

#### Skills Data Store
- **Format**: Python data structures (JSON-like)
- **Content**: 6 core sales competencies
- **Structure per Skill**:
  - ID, icon, title, tagline
  - Color theming
  - Description
  - When to use scenarios
  - 4-step playbook
  - 4 AI Assistant prompts

#### Workflows Data Store
- **Format**: Python data structures
- **Content**: 3 pre-defined workflow chains
- **Structure per Workflow**:
  - ID, title, tagline
  - Description
  - Ordered skill chain
  - Use case scenarios

#### User Session State
- **Storage**: Streamlit session state (in-memory)
- **Data**:
  - Current navigation view
  - Selected skill ID
  - Completed skills set
  - LLM responses cache
  - Edited prompts

---

### 5. External Integration Layer

#### Dell LLM API Gateway
- **Endpoint**: `https://aia.gateway.dell.com/genai/dev/v1`
- **Purpose**: Provides access to Dell's AI models
- **Authentication**: OAuth2 client credentials flow
- **Models**: Configurable (e.g., gpt-oss-20b, gpt-oss-120b)
- **Security**: SSL/TLS encryption

#### Dell OAuth2 Auth Service
- **Purpose**: Authentication and token management
- **Method**: Client credentials flow
- **Fallback**: Standard OAuth2 if Dell auth unavailable
- **Token Caching**: 1-hour token expiry with 5-minute buffer
- **Security**: Credentials stored in secure secrets file

#### Clipboard API
- **Purpose**: Copy prompts to system clipboard
- **Use Case**: Manual paste into external AI tools
- **Fallback**: If LLM not configured

---

## Data Flow

### 1. User Navigation Flow

```
User Clicks Skill
     ↓
Session State Updated
     ↓
Navigation Controller Routes
     ↓
Skill Detail View Rendered
     ↓
User Interacts with Prompts
     ↓
Session State Updated
```

### 2. LLM Integration Flow

```
User Edits/Selects Prompt
     ↓
User Uploads Document (Optional)
     ↓
Document Content Extracted (.txt, .pdf, .docx)
     ↓
User Clicks "Generate Response"
     ↓
LLM Client Initialized
     ↓
OAuth2 Token Retrieved (Cached if Valid)
     ↓
Prompt Combined with Document Context
     ↓
Enhanced Prompt Sent to Dell LLM API
     ↓
Response Received and Cached
     ↓
Response Displayed to User
```

### 3. Deal Analyzer Flow

```
User Enters Deal Information
     ↓
Health Score Calculated
     ↓
Gaps Identified
     ↓
Recommended Skills Mapped
     ↓
Contextual Prompt Generated
     ↓
User Can Generate LLM Response
```

---

## Technology Stack

### Frontend
- **Streamlit**: Python web framework for rapid UI development
- **HTML/CSS**: Custom styling for Dell branding
- **JavaScript**: Minimal, handled by Streamlit

### Backend
- **Python 3.12+**: Core application logic
- **Streamlit**: Web server and runtime

### Libraries
- **streamlit-option-menu**: Enhanced navigation
- **streamlit-extras**: Additional UI components
- **httpx**: HTTP client for API calls
- **openai**: LLM API client library
- **PyPDF2**: PDF document reading and text extraction
- **python-docx**: Word document reading and text extraction

### Deployment
- **Heroku**: Cloud deployment platform
- **Docker**: Containerization (optional)
- **Procfile**: Process management
- **runtime.txt**: Python version specification

---

## Security Architecture

### Authentication
- **OAuth2**: Secure token-based authentication
- **Client Credentials**: Machine-to-machine authentication
- **Token Caching**: Reduces authentication overhead
- **Token Expiry**: Automatic refresh before expiry

### Data Protection
- **Secrets Management**: Credentials in `.streamlit/secrets.toml`
- **Environment Variables**: Sensitive data not in code
- **SSL/TLS**: Encrypted communication with LLM API
- **No Persistent Storage**: User data not stored permanently

### Access Control
- **Internal Use**: Restricted to Dell sales teams
- **No User Accounts**: Session-based access only
- **Audit Trail**: Session state tracking (in-memory)

---

## Scalability Considerations

### Current Capacity
- **Concurrent Users**: Limited by Streamlit server resources
- **LLM Calls**: Limited by Dell API rate limits
- **Data Storage**: In-memory only (no database)

### Scaling Options
1. **Horizontal Scaling**: Deploy multiple Streamlit instances behind load balancer
2. **Session Storage**: Add Redis for distributed session state
3. **Database**: Add PostgreSQL for persistent user data
4. **Caching**: Implement response caching for common prompts
5. **CDN**: Static asset delivery for improved performance

---

## Integration Points

### Current Integrations
- **Dell LLM API**: AI response generation
- **Dell OAuth2**: Authentication service
- **Clipboard API**: System clipboard access

### Future Integration Opportunities
- **Salesforce CRM**: Deal data integration
- **Dell Internal Systems**: Customer data access
- **Analytics Platform**: Usage tracking and insights
- **Learning Management**: Skill certification tracking
- **Collaboration Tools**: Team prompt sharing

---

## Performance Optimization

### Current Optimizations
- **Token Caching**: Reduces authentication overhead
- **Session State Caching**: Avoids redundant computations
- **Lazy Loading**: Components loaded on demand
- **CSS Injection**: Single stylesheet load

### Future Optimizations
- **Response Caching**: Cache common LLM responses
- **Prompt Templates**: Pre-compile frequently used prompts
- **Async Operations**: Non-blocking LLM calls
- **Image Optimization**: Compress static assets

---

## Monitoring and Observability

### Current Monitoring
- **Streamlit Metrics**: Built-in performance monitoring
- **Error Handling**: Try-catch blocks with user feedback
- **Session Logging**: In-memory state tracking

### Future Monitoring
- **Application Performance Monitoring (APM)**
- **Usage Analytics**: Feature adoption tracking
- **Error Tracking**: Automated error reporting
- **User Feedback**: In-app feedback mechanism

---

## Compliance and Governance

### Data Privacy
- **No PII**: No personally identifiable information collected
- **Session-Only**: Data not persisted beyond session
- **Internal Use**: Restricted to Dell employees

### Accessibility
- **WCAG 2.1**: Compliance with web accessibility standards
- **Keyboard Navigation**: Full keyboard support
- **Screen Reader**: Compatible with assistive technologies

### Branding
- **Dell Visual Identity**: Consistent with brand guidelines
- **Professional Tone**: Business-appropriate content
- **Internal Use**: Dell-specific terminology and context

---

## Deployment Architecture

### Development Environment
```
Local Machine
  ↓
Python Virtual Environment
  ↓
Streamlit Development Server
  ↓
Local Testing
```

### Production Environment
```
Heroku Cloud Platform
  ↓
Dell LLM API Gateway
  ↓
Dell OAuth2 Service
  ↓
End Users (Dell Sales Teams)
```

### Deployment Pipeline
1. **Code Commit**: Push to version control
2. **Automated Testing**: Run test suite
3. **Build**: Create deployment package
4. **Deploy**: Push to Heroku
5. **Health Check**: Verify deployment success
6. **Monitor**: Track performance and errors

---

## Future Roadmap

### Phase 1: Enhanced Features (Q2 2026)
- User authentication and personalization
- Prompt sharing and collaboration
- Advanced analytics and reporting
- Mobile app development

### Phase 2: Integration Expansion (Q3 2026)
- Salesforce CRM integration
- Dell customer data integration
- Multi-language support
- Voice-activated prompts

### Phase 3: AI Enhancement (Q4 2026)
- Custom fine-tuned models
- Context-aware prompt suggestions
- Real-time coaching during calls
- Predictive deal scoring

---

## Summary

The Dell Sales Skills Framework is a modern, secure, and scalable web application that empowers sales teams with AI-powered assistance. Built on Streamlit with direct integration to Dell's LLM services, it provides:

- **Structured Learning**: 6 core sales skills with actionable playbooks
- **AI-Powered Coaching**: Direct LLM integration for instant expertise
- **Workflow Automation**: Pre-defined skill chains for common scenarios
- **Deal Intelligence**: Interactive analyzer with gap identification
- **Enterprise Security**: OAuth2 authentication and secure data handling

The architecture is designed for ease of use, maintainability, and future scalability, positioning Dell sales teams for success in an AI-enabled sales environment.

---

**Document Version**: 1.1  
**Last Updated**: April 2026  
**Architecture Owner**: Dell Sales Enablement Team  
**Changes**: Added document upload functionality for LLM context  
