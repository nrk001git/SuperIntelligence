"""
Skills Data Module
Contains all skills content as Python data structures
"""

SKILLS_DATA = [
    {
        "id": "discovery",
        "icon": "🔍",
        "title": "Discovery & Needs Analysis",
        "tagline": "Uncover what the customer actually needs — not what they say they want.",
        "color": "#0672CB",
        "description": "Master the art of discovery using MEDDPICC framework, pain-first questioning, and cost of inaction quantification to uncover customer needs.",
        "when_to_use": [
            "First meeting with prospect",
            "Customer mentions budget planning/digital transformation/infrastructure refresh",
            "Responding to RFP/RFI",
            "Annual business review or QBR preparation"
        ],
        "steps": [
            {
                "title": "Map the Stakeholder Landscape using MEDDPICC",
                "detail": (
                    "Before walking into any meeting, map every stakeholder against the MEDDPICC framework: "
                    "Metrics (what does success look like in numbers?), Economic Buyer (who controls the budget and has final sign-off?), "
                    "Decision Criteria (what factors will they use to choose a vendor?), Decision Process (what are the formal steps — committee review, board approval, legal?), "
                    "Paper Process (what does procurement, legal, and contract signature look like — and how long does it take?), "
                    "Identify Pain (what is the specific, quantified business problem?), Champion (who inside the account is selling for you when you're not in the room?), "
                    "Competition (who else are they evaluating, and what is the incumbent?). "
                    "If you cannot answer at least 5 of these 8 elements before your second meeting, you are flying blind. "
                    "Prioritize finding your Champion early — without one, even the best solution loses."
                )
            },
            {
                "title": "Ask Pain-First Questions",
                "detail": (
                    "The biggest discovery mistake is pitching before the pain is fully understood. "
                    "Open every meeting with broad, strategic questions: 'What are your top 3 IT priorities this year?', "
                    "'Where is your team spending time on problems that shouldn't exist?', 'What happens to the business if this problem isn't solved in 12 months?' "
                    "Then drill down using the 'So what?' technique — every answer they give, ask a follow-up that connects it to business impact. "
                    "If they say 'our storage is slow,' ask 'What workloads are affected, and what does that mean for your teams?' "
                    "Avoid product names entirely until you have surfaced at least two distinct pain points with business consequences. "
                    "Silence is a tool — after they answer, pause for 3 seconds before responding. Customers fill silence with their real concerns."
                )
            },
            {
                "title": "Quantify the Cost of Inaction",
                "detail": (
                    "Customers delay decisions when the pain of change feels greater than the pain of staying put. "
                    "Your job is to reverse that equation by making the cost of doing nothing impossible to ignore. "
                    "Work through four cost categories together: Operational Cost (how many FTE hours per week are lost to workarounds, manual processes, or outages — multiply by fully-loaded hourly rate), "
                    "Revenue Impact (does slow infrastructure delay product releases, affect customer SLAs, or limit transaction throughput?), "
                    "Risk Cost (what is the potential financial exposure from a security breach, compliance failure, or unplanned downtime — use industry benchmarks if they won't share internal data), "
                    "Opportunity Cost (what strategic initiatives are blocked because current infrastructure can't support them?). "
                    "Add these up into an annual 'Cost of Inaction' number. A $400K solution becomes easy to approve when inaction costs $1.2M/year. "
                    "Always build this calculation with the customer, not for them — their numbers carry far more weight than yours."
                )
            },
            {
                "title": "Document & Share Back",
                "detail": (
                    "Within 24 hours of every discovery meeting, send a Discovery Brief — a 1-page document that summarizes: "
                    "what you heard (their stated priorities and pain points), what you observed (gaps or risks they may not have named explicitly), "
                    "and what you propose to explore next. "
                    "This serves three purposes: it proves you were listening, it surfaces any misunderstandings before they become proposal mistakes, "
                    "and it positions you as a strategic partner rather than a vendor. "
                    "Structure it as: Current State → Challenges & Impact → Desired Future State → Proposed Next Steps. "
                    "If the customer corrects or adds to your brief, that is valuable intelligence — it means the conversation is working. "
                    "Share it with your Champion and ask them to forward it to the Economic Buyer as a conversation starter."
                )
            }
        ],
        "ai_prompts": [
            "Help me prepare discovery questions for a mid-market healthcare company evaluating server refresh",
            "Analyze this customer's current IT environment and identify Dell solution opportunities",
            "Draft a Discovery Brief summarizing my meeting notes with [customer]",
            "What MEDDPICC gaps do I have in this deal? Here are my notes: ..."
        ]
    },
    {
        "id": "solution_architecture",
        "icon": "🏗️",
        "title": "Solution Architecture & Positioning",
        "tagline": "Translate customer pain into a Dell solution story they can't ignore.",
        "color": "#007DB8",
        "description": "Build compelling Dell solutions by mapping workloads to platforms, creating value stacks, differentiating against competitors, and crafting winning proposals.",
        "when_to_use": [
            "Building a technical proposal",
            "Customer comparing Dell vs HPE/Lenovo/Cisco/cloud",
            "Need to map Dell portfolio to specific workloads (AI/ML, VDI, SAP, HCI, edge)",
            "Pricing strategy and deal structuring"
        ],
        "steps": [
            {
                "title": "Match Workload to Platform",
                "detail": (
                    "Start with the workload, not the product catalog. Ask: what is this infrastructure actually running? "
                    "For general compute and AI/ML training, PowerEdge (especially the XE series for GPU-dense workloads) is the anchor. "
                    "For block and file storage in mixed enterprise environments, PowerStore offers NVMe-first performance with autonomous management. "
                    "For unstructured data at scale — media, genomics, surveillance — PowerScale (Isilon) is purpose-built. "
                    "For customers wanting a fully converged, VMware-integrated stack, VxRail eliminates integration risk and simplifies lifecycle management. "
                    "For networking, PowerSwitch gives open, programmable fabric that pairs cleanly with the compute and storage layers. "
                    "For customers with variable demand or OpEx mandates, APEX delivers Dell infrastructure as a consumption service. "
                    "The key rule: never lead with a product name. Lead with the workload problem, then introduce the platform as the natural fit. "
                    "Customers trust solutions that feel designed for their problem, not pulled from a price list."
                )
            },
            {
                "title": "Build the Value Stack",
                "detail": (
                    "A winning Dell proposal is never just hardware — it's a layered value stack where each layer reduces customer risk and increases switching cost. "
                    "Layer 1 — Hardware: PowerEdge/PowerStore/VxRail as the foundation, sized to workload requirements with headroom for growth. "
                    "Layer 2 — Management: OpenManage Enterprise for unified infrastructure visibility; reduces FTE overhead and mean time to resolution. "
                    "Layer 3 — Security: Zero-trust BIOS and firmware (Secured Component Verification), PowerProtect Cyber Recovery vault for air-gapped backup, endpoint security integrations. "
                    "Layer 4 — Services: ProSupport Plus with predictive issue detection, deployment and migration services, residency options for complex environments. "
                    "Layer 5 — Financing: Dell Financial Services flexible payment structures, APEX Flex On Demand for true consumption pricing, tech refresh programs. "
                    "Present each layer as solving a specific customer concern identified in discovery. "
                    "A customer worried about downtime cares about Layer 2 and 4. A CFO concerned about cash flow cares about Layer 5. Tailor your emphasis accordingly."
                )
            },
            {
                "title": "Competitive Differentiation",
                "detail": (
                    "Know your competitive positioning cold before entering any evaluation. "
                    "Against HPE: Dell's unified management stack (OpenManage vs HPE's fragmented iLO/OneView/InfoSight tooling) reduces operational complexity. "
                    "Dell's ProSupport with predictive analytics outperforms HPE's reactive support model in most TCO comparisons. Use third-party TCO studies where available. "
                    "Against Lenovo: Dell's breadth of services ecosystem, larger partner network, and faster innovation cadence (especially in AI infrastructure) are key differentiators. "
                    "Lenovo competes on price — counter with total value and risk of a thinner services wrapper. "
                    "Against cloud-only: Lead with data sovereignty, compliance requirements, and predictable cost modeling. "
                    "Build a 3-year TCO showing cloud egress costs, compute-on-demand pricing at scale, and data transfer fees vs. Dell CapEx or APEX OpEx. "
                    "Against Nutanix/Pure Storage point solutions: Dell's integrated portfolio eliminates multi-vendor complexity and provides a single throat to choke for support. "
                    "Critical rule: never badmouth competitors by name in front of the customer. Acknowledge they are credible options, then redirect to what matters most to the customer's specific situation."
                )
            },
            {
                "title": "Create a Compelling Proposal",
                "detail": (
                    "A proposal is not a quote — it is a business case document that makes the Economic Buyer's decision easy to justify internally. "
                    "Structure it in six sections: "
                    "1. Executive Summary (1 page max): restate the customer's pain in their language, the proposed solution in plain terms, and the expected business outcome with numbers. "
                    "2. Current State & Challenges: show you understood what they told you — use their words and metrics where possible. "
                    "3. Proposed Solution: describe the architecture in business terms first, technical terms second. Include a simple diagram. "
                    "4. Business Value: ROI calculation, payback period, TCO comparison, risk reduction quantified. This is the section the CFO reads. "
                    "5. Investment Summary: clear pricing with options (good/better/best if applicable), financing alternatives, and what is included vs. optional. "
                    "6. Why Dell & Why Now: your differentiation points and the compelling event that justifies acting in this quarter. "
                    "Always have your Champion review a draft before formal submission — they will tell you what the Economic Buyer will push back on, and you can address it proactively."
                )
            }
        ],
        "ai_prompts": [
            "Design a Dell solution for a 500-user VDI deployment on VxRail with disaster recovery",
            "Create a competitive comparison: Dell PowerStore vs HPE Alletra for mixed workloads",
            "Help me build a TCO analysis showing Dell PowerEdge vs public cloud for AI inference",
            "Draft a proposal executive summary for this deal: ..."
        ]
    },
    {
        "id": "objection_handling",
        "icon": "🛡️",
        "title": "Objection Handling & Negotiation",
        "tagline": "Turn 'no' into 'tell me more' — and protect your margin while you're at it.",
        "color": "#6B2D8B",
        "description": "Master objection handling using the acknowledge-isolate-respond framework, value sandwiches, DFS financing, and constructive tension techniques.",
        "when_to_use": [
            "Customer says it's too expensive or asks for discount",
            "Prospect goes silent or delays",
            "Competitor drops aggressive counter-offer",
            "Champion loses momentum or executive sponsor changes"
        ],
        "steps": [
            {
                "title": "Acknowledge, Isolate, Respond",
                "detail": (
                    "The worst response to an objection is an immediate counter-argument — it signals you weren't listening and triggers defensiveness. "
                    "Instead, use the three-step framework every time. "
                    "Acknowledge: validate the concern without agreeing with it. 'I hear you — budget is a real constraint and I want to make sure we're solving the right problem.' "
                    "Isolate: test whether this is the only objection or one of several. 'If we could find a way to make the investment work within your budget cycle, is that the last thing standing between us and moving forward?' "
                    "If they say yes, you have a real objection to solve. If they hesitate, there are more objections underneath — keep probing before investing energy in a rebuttal. "
                    "Respond: only now present your evidence — case studies, ROI data, financing options, or a revised scope. "
                    "The most common objections and their root causes: 'Too expensive' usually means value wasn't established early enough. "
                    "'Need to think about it' usually means there's a stakeholder concern you haven't addressed. "
                    "'We're happy with our current vendor' usually means your Champion isn't strong enough yet."
                )
            },
            {
                "title": "Use the Value Sandwich",
                "detail": (
                    "When you must discuss price, never lead with the number. Use the Value Sandwich structure to frame the investment in context. "
                    "Top slice — Value Delivered: open by summarizing the outcomes the customer will achieve. "
                    "'Based on what you've shared, this solution will eliminate 40 hours of weekly manual storage management and reduce your unplanned downtime from an average of 6 hours to under 1 hour per quarter.' "
                    "Filling — The Investment: present the price clearly and without apology. 'The total investment for this solution is $480,000.' "
                    "Bottom slice — ROI and Payback: immediately follow with the return. "
                    "'At your current cost of $18,000 per hour of downtime, and factoring in the FTE savings, you recover this investment in 14 months — and every month after that is pure operational savings.' "
                    "The psychological effect: the customer's brain hears value → price → value, rather than just price. "
                    "Never end a pricing conversation on the number. Always end on the outcome."
                )
            },
            {
                "title": "Leverage Dell Financial Services",
                "detail": (
                    "Price objections are often cash flow objections in disguise — the customer wants the solution but can't absorb a large CapEx hit in the current budget cycle. "
                    "Dell Financial Services (DFS) is one of your most underused tools. Know these options cold: "
                    "CapEx to OpEx conversion: structure the deal as a DFS operating lease, turning a $600K purchase into $18K/month — often fitting within an existing IT operations budget without additional approval. "
                    "Payment deferrals: 90-day or 6-month payment deferrals let customers deploy now and pay later, which is especially powerful at quarter-end or fiscal year-end when budgets are tight. "
                    "Technology refresh programs: built-in refresh cycles every 2-3 years with predictable monthly payments, eliminating the budget spike of a traditional refresh cycle. "
                    "APEX Flex On Demand: true consumption-based pricing where the customer pays only for what they use above a committed baseline — ideal for variable workloads or customers making the cloud-to-on-prem argument. "
                    "Always introduce DFS options before the customer asks for a discount — once you start discounting, you've trained them to ask every time."
                )
            },
            {
                "title": "Create Constructive Tension",
                "detail": (
                    "Deals that stall are deals that die. When a customer goes quiet or delays, you need to re-introduce urgency without being pushy. "
                    "Constructive tension is urgency based on real business consequences — not fake deadlines. "
                    "Quarter-end and year-end incentives: Dell periodically offers accelerated pricing, additional services, or extended financing terms for deals closing within a quarter. "
                    "Be specific: 'The current pricing and the 6-month payment deferral I've built into your proposal are tied to our Q3 program — those terms expire on [date].' "
                    "Supply and lead time: for large PowerEdge configurations or custom builds, manufacturing lead times are real. "
                    "'If we don't place the order by [date], I can't guarantee delivery before your go-live window in [month].' "
                    "Competitive displacement windows: if you know a competitor's contract is expiring or a support agreement is ending, that is a natural trigger. "
                    "'Your HPE support contract renews in 90 days — that's the lowest-friction moment to make a change.' "
                    "Cost of delay: return to the Cost of Inaction you built in discovery. 'Every month this decision is delayed costs your team approximately $38,000 in the inefficiencies we discussed.' "
                    "The key is that all tension must be grounded in fact. Invented urgency destroys trust the moment the customer discovers it."
                )
            }
        ],
        "ai_prompts": [
            "The customer says HPE is 15% cheaper. Help me build a response focused on TCO and services value",
            "My champion told me the CFO wants to push this to next quarter. Give me a re-engagement strategy",
            "Draft an email responding to a customer who says they're moving everything to the cloud",
            "Help me structure a DFS financing option that converts this $2M CapEx deal into monthly OpEx"
        ]
    },
    {
        "id": "pipeline_management",
        "icon": "📊",
        "title": "Pipeline Management & Forecasting",
        "tagline": "Build a pipeline that's predictable, not a prayer.",
        "color": "#C94A16",
        "description": "Build predictable pipelines through honest deal scoring, 3x coverage rules, strategic time-blocking, and effective pipeline reviews.",
        "when_to_use": [
            "Weekly pipeline review or forecast submission",
            "Territory or account planning",
            "Quarter-start goal setting and gap analysis",
            "Deciding which deals to prioritize"
        ],
        "steps": [
            {
                "title": "Score Every Deal Honestly",
                "detail": (
                    "Pipeline inflation is the single biggest cause of missed quarters. Most reps carry deals they hope will close, not deals they know will close. "
                    "Score every deal against six binary checkpoints — and be ruthless: "
                    "1. Budget confirmed: has the Economic Buyer explicitly stated a budget exists, or are you assuming? "
                    "2. Economic Buyer engaged: have you had a direct conversation with the person who can sign the check — not just the technical team? "
                    "3. Timeline defined: does the customer have a specific go-live date or business event driving urgency — or did you suggest a timeline they passively agreed to? "
                    "4. Technical win achieved: has the technical evaluator confirmed your solution meets their requirements, ideally in writing or via a proof of concept? "
                    "5. Paper process understood: do you know exactly what happens after verbal agreement — procurement steps, legal review, contract templates, approval thresholds? "
                    "6. Competition mapped: do you know who else is in the deal and where you stand relative to them? "
                    "Deals missing 1 checkpoint = commit with caution. Missing 2 = best case/upside. Missing 3 or more = do not forecast. "
                    "A smaller, honest pipeline is always more valuable than a large, inflated one."
                )
            },
            {
                "title": "Apply the 3x Rule",
                "detail": (
                    "The 3x pipeline coverage rule exists because not every qualified deal closes, and not every deal closes in the quarter it was forecast. "
                    "Maintain a minimum of 3x your quota target in qualified pipeline at all times — $1M quota requires $3M in pipeline that passes your honest scoring test. "
                    "Break your 3x down by stage: you want roughly 1x in late-stage (proposal/negotiation), 1x in mid-stage (solution/technical evaluation), and 1x in early-stage (discovery/qualification). "
                    "If your late-stage pipeline is thin, your quarter is already in trouble — start pulling mid-stage deals forward immediately. "
                    "If your early-stage pipeline is thin, next quarter is in trouble — block time for prospecting now, before the pressure hits. "
                    "Review your coverage ratio every Monday morning. It is the single most leading indicator of whether you will hit your number. "
                    "The 3x rule is a floor, not a ceiling — complex enterprise deals with long paper processes may require 4-5x coverage."
                )
            },
            {
                "title": "Time-Block by Deal Stage",
                "detail": (
                    "Most reps spend 80% of their time on the deals they feel most comfortable with — usually the ones that are already advanced and need the least attention. "
                    "Intentional time allocation by deal stage is what separates reps who consistently hit quota from those who have a great quarter followed by a terrible one. "
                    "Recommended weekly allocation: "
                    "40% on Proposal/Negotiation stage deals — these are your in-quarter revenue; every day of delay costs you. Focus on removing obstacles, accelerating the paper process, and locking in decisions. "
                    "30% on Discovery/Solution stage deals — these are next quarter's revenue; invest in technical validation, stakeholder expansion, and building your Champion. "
                    "20% on Prospecting — new pipeline creation is non-negotiable, even in a strong quarter. Feast/famine cycles are caused by prospecting only when the pipeline is empty. "
                    "10% on Expansion and existing account QBRs — your installed base is your easiest pipeline source; don't neglect it. "
                    "Block this time in your calendar on Monday morning. Treat it like customer appointments — it doesn't move."
                )
            },
            {
                "title": "Run Effective Pipeline Reviews",
                "detail": (
                    "A pipeline review is not a status update — it is a critical thinking session designed to surface risk and unlock stuck deals. "
                    "For every deal in your forecast, be prepared to answer four questions without looking at your notes: "
                    "1. What changed since last week? If nothing changed, the deal is stalling — what is the specific action you are taking to move it? "
                    "2. What is the next verifiable action, and who owns it? A next step is only real if it is a specific action with a date and a name attached. 'Following up next week' is not a next step. "
                    "3. What is the customer's compelling event? Why do they need this solution by the date you are forecasting? If you cannot answer this, the timeline is yours, not theirs. "
                    "4. What is the single biggest risk to this deal closing? Naming the risk out loud is the first step to mitigating it. "
                    "Stale deals — those with no customer-side activity in 14+ days — are forecasting poison. Either re-engage them aggressively or move them out of the committed forecast. "
                    "The discipline of an honest weekly review is what allows you to give your manager a forecast you can actually defend."
                )
            }
        ],
        "ai_prompts": [
            "Analyze my pipeline and identify the 5 deals most likely to close this quarter. Here are my deals: ...",
            "I have a $500K gap to quota with 6 weeks left. Build me a closing plan",
            "Help me prepare for my pipeline review — identify weak deals and talking points",
            "Create a territory plan for next quarter focused on mid-market manufacturing accounts"
        ]
    },
    {
        "id": "account_expansion",
        "icon": "🚀",
        "title": "Account Expansion & Cross-Sell",
        "tagline": "Your best new customer is your current customer.",
        "color": "#1A8C5E",
        "description": "Drive growth through installed base mining, whitespace mapping, outcome-led expansion, and multi-year roadmap co-creation.",
        "when_to_use": [
            "Customer deployment is 12-18 months old",
            "New Dell product launch relevant to installed base",
            "Customer expands to new locations or acquires a company",
            "Support tickets suggest capacity gaps"
        ],
        "steps": [
            {
                "title": "Mine the Installed Base",
                "detail": (
                    "Your installed base is a goldmine that most reps walk past every day. "
                    "Start by pulling a complete asset inventory for every account: product lines, model generations, purchase dates, warranty and support contract status, and end-of-life timelines. "
                    "Flag three categories of opportunity immediately: "
                    "End-of-life and end-of-support assets (typically 3-5 years old) — these are your highest-urgency refresh conversations because the customer's risk is rising every day they stay on aging hardware. "
                    "Warranty expirations in the next 6 months — a ProSupport renewal conversation is also an upgrade conversation. Never let a warranty renew on old hardware without presenting a refresh alternative. "
                    "Utilization patterns: if you have access to OpenManage telemetry or customer-shared capacity data, look for systems running above 70-80% utilization — these are capacity expansion conversations waiting to happen. "
                    "Cross-reference the installed base against support ticket history. Repeated tickets on the same system are a leading indicator of a failure event — get ahead of it with a proactive refresh proposal before it becomes a reactive crisis."
                )
            },
            {
                "title": "Map the White Space",
                "detail": (
                    "Whitespace mapping answers the question: where is this customer not buying Dell, and why? "
                    "Build a simple account map — a table with every Dell product category on one axis and every business unit or location on the other. "
                    "Mark each cell: Green (Dell installed), Yellow (competitor or legacy installed), Red (known need, no solution yet), White (unknown). "
                    "Your target cells are Yellow and Red — these are your expansion opportunities. "
                    "Prioritize by two factors: size of the potential deal and strength of your existing relationship in that business unit. "
                    "A $500K whitespace opportunity in a BU where you have no relationships is harder than a $200K opportunity where you already have a Champion. "
                    "For Yellow cells, your goal is competitive displacement — understand the contract terms, support renewal dates, and satisfaction level with the incumbent. "
                    "For Red cells, your goal is to be first to frame the problem and the solution — whoever defines the requirements usually wins the deal. "
                    "Review and update your whitespace map every quarter. Accounts that look fully penetrated today will have new whitespace after a reorganization, acquisition, or strategic shift."
                )
            },
            {
                "title": "Lead with Business Outcomes",
                "detail": (
                    "Expansion conversations fail when they feel like upselling. They succeed when they feel like strategic advising. "
                    "The shift is simple: connect every expansion proposal to a business outcome the customer has already told you they care about. "
                    "Before presenting any expansion idea, review your discovery notes and the customer's stated priorities. "
                    "If their top priority is accelerating AI/ML initiatives, your PowerEdge XE expansion conversation becomes: 'You told me in our last QBR that getting your data science team off cloud GPUs and onto on-prem infrastructure was a 2025 priority. Here's what that looks like with your current footprint as the foundation.' "
                    "If their top priority is reducing IT operational costs, your OpenManage or APEX conversation becomes: 'Based on your current environment, here are the three areas where your team is spending the most manual time — and here's how we eliminate that.' "
                    "Always lead with their language, their metrics, and their timeline — never with your product roadmap or your quota. "
                    "Customers expand with vendors who make them look smart to their leadership, not vendors who hit them with features they didn't ask for."
                )
            },
            {
                "title": "Build a Multi-Year Roadmap",
                "detail": (
                    "A co-created technology roadmap is the most powerful account retention and expansion tool available to you — and almost no rep uses it. "
                    "The goal is to become the customer's IT planning partner, not just their hardware vendor. "
                    "Request a dedicated roadmap session (not a sales call) with your Champion and, ideally, the IT Director or CTO. "
                    "Frame it as: 'I'd like to spend 90 minutes helping you map your technology needs against your business priorities for the next 3 years — no selling, just planning.' "
                    "In the session, work through: the customer's business goals by year, the IT capabilities required to support them, the current infrastructure gaps, and a phased investment plan that aligns technology upgrades to budget cycles. "
                    "The output is a shared document — a 3-year roadmap with phases, milestones, and rough investment ranges — that the customer owns and you co-authored. "
                    "Review it every quarter in your QBR. Update it when their business priorities shift. "
                    "A customer with a co-created roadmap is extraordinarily difficult to displace — they are not just buying hardware, they are executing a plan you built together. "
                    "This is how reps turn accounts from transactional to strategic."
                )
            }
        ],
        "ai_prompts": [
            "Analyze this customer's installed base and identify top 3 cross-sell opportunities",
            "Draft a business case for refreshing a 3-year-old PowerEdge environment",
            "Help me build a 3-year technology roadmap for a financial services customer using Dell HCI",
            "Create a talk track for introducing APEX to a customer currently buying CapEx"
        ]
    },
    {
        "id": "product_intelligence",
        "icon": "🧠",
        "title": "Product & Market Intelligence",
        "tagline": "Know more than your customer expects — and more than your competition hopes.",
        "color": "#2C3E50",
        "description": "Stay ahead with 15-minute briefings, vertical playbooks, AI infrastructure knowledge, and weekly competitive tracking.",
        "when_to_use": [
            "Preparing for meeting in unfamiliar vertical",
            "Customer asks about a product line you don't sell daily",
            "Competitor releases new product or makes pricing move",
            "Need to understand AI infrastructure or edge computing trends"
        ],
        "steps": [
            {
                "title": "Use the 15-Minute Briefing",
                "detail": (
                    "Walking into a customer meeting unprepared is the fastest way to lose credibility. "
                    "The 15-minute pre-meeting briefing is a non-negotiable habit for high-performing reps. "
                    "Spend it across five areas: "
                    "Customer news (2 min): check their investor relations page, LinkedIn, and Google News for recent earnings, leadership changes, acquisitions, layoffs, or strategic announcements. Any of these can shift priorities or create urgency. "
                    "Their IT environment (3 min): review your CRM notes, any open support cases, recent purchase history, and known incumbent vendors. "
                    "Dell reference architecture (5 min): pull the most relevant Dell solution brief or reference architecture for the workload you'll be discussing. Know the key specs, differentiators, and 2-3 customer proof points. "
                    "Competitive intel (3 min): check if there are any recent competitor announcements relevant to this account — new product releases, pricing changes, support issues. "
                    "Your ask (2 min): decide exactly what the next step is that you want to walk out of this meeting with, and how you will ask for it. "
                    "Customers notice when you've done your homework. It changes the entire dynamic of the conversation from vendor pitch to peer advisory."
                )
            },
            {
                "title": "Build Your Vertical Playbooks",
                "detail": (
                    "Vertical knowledge is a shortcut to credibility. When a customer hears you speak their industry language — regulatory pressures, operational metrics, peer benchmarks — they stop treating you as a hardware salesperson. "
                    "Build a one-page playbook for each of your top 3 verticals. Each playbook should cover: "
                    "Top business priorities and pressures (e.g., for healthcare: patient data security, Epic EHR performance, HIPAA compliance, staff efficiency). "
                    "Key regulatory drivers (HIPAA, PCI-DSS, FERPA, NERC CIP — know which ones apply and what they require at an infrastructure level). "
                    "Common workloads and their Dell solution fit (e.g., financial services: low-latency trading platforms → PowerEdge with NVMe; large dataset analytics → PowerScale). "
                    "2-3 reference customers and outcomes in that vertical — use these as proof points in conversation. "
                    "Common objections unique to that vertical and how to address them. "
                    "Refresh your playbooks quarterly. Industries shift, regulations update, and new use cases emerge. "
                    "A rep with deep vertical knowledge in manufacturing will consistently outperform a generalist rep in that segment — even if the generalist has better product knowledge."
                )
            },
            {
                "title": "Stay Current on AI Infrastructure",
                "detail": (
                    "AI infrastructure is the fastest-growing and most competitive segment of the Dell portfolio. "
                    "Customers asking about AI are often confused, excited, and vulnerable to vendor hype — your job is to be the trusted voice that cuts through the noise. "
                    "Know the Dell AI portfolio cold: PowerEdge XE9680 (8x GPU, NVIDIA H100/H200 optimized, ideal for LLM training and large-scale inference), "
                    "PowerEdge XE8640 (4x GPU, cost-optimized for mid-scale AI and inferencing), "
                    "PowerEdge R760xa (2x GPU, entry-point for departmental AI and edge inference). "
                    "Know the validated design partnerships: NVIDIA (DGX-ready, NVLink configurations), AMD Instinct, Intel Gaudi — and when each is the right choice. "
                    "Build your TCO narrative for AI on-premises vs. cloud: for sustained AI workloads (training runs that run 24/7 or inference at scale), on-prem typically reaches cost parity with cloud in 12-18 months and becomes significantly cheaper beyond that. "
                    "Know the objections: 'We'll just use AWS/Azure for AI' — counter with data gravity, latency, and long-run TCO. 'AI is a one-time project' — counter with the trend toward continuous model retraining and inference expansion. "
                    "Customers respect a rep who can have a real conversation about GPU memory bandwidth, NVLink topology, or MLPerf benchmarks. You don't need to be an engineer — but you need to be fluent."
                )
            },
            {
                "title": "Track Competitive Moves Weekly",
                "detail": (
                    "Competitive blindspots lose deals. Set up a system that keeps you informed without consuming your selling time. "
                    "Set Google Alerts for: HPE ProLiant, HPE Alletra, Lenovo ThinkSystem, Cisco UCS, Nutanix, Pure Storage — any new product announcement, pricing leak, or support issue becomes actionable intelligence. "
                    "Follow key competitors on LinkedIn and monitor their press release feeds — product launches, executive hires, and partnership announcements often signal strategic shifts before they reach the field. "
                    "Subscribe to analyst sources that track the infrastructure market: IDC, Gartner Magic Quadrant updates, Forrester Wave reports. When Dell is positioned favorably, use it. When gaps are identified, get ahead of them. "
                    "Build a simple competitive cheat sheet for your top 3 competitors with: their latest product positioning, known weaknesses, typical discount levels, and the 2-3 questions that expose their gaps in a competitive evaluation. "
                    "Share competitive intelligence with your team — a rep who encounters a new HPE pricing tactic or a Nutanix FUD campaign should brief the whole team within 24 hours. "
                    "The goal is never to obsess over competitors — it is to ensure that when a customer brings them up, you have a calm, confident, fact-based response ready."
                )
            }
        ],
        "ai_prompts": [
            "Brief me on Dell's latest AI infrastructure solutions for a meeting with a data science team",
            "What are the key IT pain points in healthcare and which Dell solutions address them?",
            "Compare Dell VxRail vs Nutanix for hybrid cloud — give me talking points",
            "Summarize the latest Dell product announcements relevant to my accounts"
        ]
    }
]

WORKFLOWS_DATA = [
    {
        "id": "new_deal_qualification",
        "title": "New Deal Qualification",
        "skills": ["discovery", "solution_architecture", "pipeline_management"],
        "tagline": "Qualify → Design → Track",
        "description": "Chain discovery, solution architecture, and pipeline management to qualify new opportunities effectively."
    },
    {
        "id": "competitive_displacement",
        "title": "Competitive Displacement",
        "skills": ["product_intelligence", "solution_architecture", "objection_handling"],
        "tagline": "Research → Position → Defend",
        "description": "Research competitors, position Dell solutions, and handle objections to displace competitors."
    },
    {
        "id": "installed_base_growth",
        "title": "Installed Base Growth",
        "skills": ["account_expansion", "discovery", "objection_handling"],
        "tagline": "Scan → Discover → Close",
        "description": "Scan installed base for opportunities, discover expansion needs, and close cross-sell deals."
    }
]

def get_skill_by_id(skill_id):
    """
    Retrieve a skill by its ID.

    Args:
        skill_id (str): The ID of the skill to retrieve

    Returns:
        dict: The skill data if found, None otherwise
    """
    for skill in SKILLS_DATA:
        if skill["id"] == skill_id:
            return skill
    return None
