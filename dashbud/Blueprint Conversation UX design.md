# Blueprint Conversation UX design
_Project doc, created 2025-10-28_

Blueprint Conversation UX 

Executive Summary 

The Blueprint Conversation is our AI-driven approach to data preparation that inverts the traditional configuration workflow. Rather than asking the user to add context and metadata from scratch, the Blueprint Agent detects legible features on its own and asks the user to clarify ambiguities, provide any needed context, and fill in the blanks through a natural language conversation with the blueprint asset itself (a tabular structure shown to the side of the conversation panel) updates in real time. This document outlines the user experience design; our goal is to make complex data configuration simple and efficient while enabling enterprise-grade precision at the analysis stage. 

Design Philosophy 

Core Principle: Automate first, Clarify when needed 

Traditional BI tools force users to understand and configure technical semantics before they can analyze data. Our approach inverts this model: 

The AI does the heavy lifting - automatically interpreting schemas, suggesting descriptions, and creating semantics 

Users provide context only when needed - answering targeted questions rather than filling out forms 

Workspaces organize naturally - encouraging users to think functionally (sales, marketing, operations) 

Key UX Tenets 

Minimal technical jargon: Users shouldn't need to understand technical terms except as necessary.  

Conversational interaction: Natural back-and-forth dialogue; add selections or form fields later, as needed 

Live asset (blueprint) updates: right rail shows current blueprint and allows direct blueprint editing 

Progressive disclosure: Start simple, add complexity when the data demands it 

Workspace-centric thinking: Help users organize data by business function, not database structure 

User Journey 

Entry Point: The "Get Started" Experience 

When users enter a new workspace with connected data sources, they encounter a clean interface with a single action: "Get Started" 

This button initiates an intelligent analysis where the AI: 

Examines the schema(s) at a high level 

Determines the appropriate conversation strategy based on data complexity 

Generates an initial response tailored to the specific scenario 

The Right-Side Blueprint Panel 

As the conversation progresses, a live preview of the developing blueprint appears in the right pane (naturally associated with document editing). This shows: 

Data source names with type indicators (PostgreSQL Database, Excel File, etc.) 

Table listings with metadata (column count, row estimates) 

Tooltips for additional context 

Editable fields for power users who want to manually add synonyms 

The left pane remains dedicated to the conversational flow, maintaining clear separation between dialogue and output. 

Treatment of Database Schemas 

In database systems like PostgreSQL and SQL Server, schemas function as namespaces that organize tables into logical groups. Schemas serve multiple purposes, for example: logical organization by business domain (sales, marketing, finance), multi-tenant isolation (e.g. separating different clients' data); application separation and versioning/testing environments.  

When our blueprint agent encounters a database connection, it analyzes schema organization to understand how users already think about their data. For single-schema databases (typically just "public"), schemas are ignored as implementation details and the AI focuses on table-level organization. For multi-schema databases with meaningful names, the AI leverages this existing structure—allowing users to select entire schemas at once (e.g., "include all sales schema tables") rather than individual tables; it also detects patterns like multi-tenant structures (client_abc, client_xyz schemas) or versioning setups (v1, staging, production) and adapts its prompting accordingly. This schema-awareness makes workspace creation more intuitive by aligning with existing organizational structures rather than fighting against them.  

Data Scenarios & Initial Prompts 

The AI adapts its opening message based on data complexity. Here are four representative scenarios: 

Scenario 1: Single Table Upload 

Context: User uploads "Global Superstore Sales.xlsx" - one comprehensive table 

AI Opening: 

"I've reviewed your sales data table. It looks like a retail analytics dataset with 9,994 orders across product categories, regions, and customer segments. I've created a blueprint with descriptions for your columns like Order Date, Sales, Profit, and Customer Name. 

Would you like me to clarify anything about how I've interpreted your data, or shall we move to exploring it?" 

Rationale: With a single, self-explanatory table, jump straight to confirmation. The structure is obvious, so generate the complete blueprint immediately. 

Scenario 2: Small, Coherent Database 

Context: User connects a PostgreSQL database with 5 related tables (Customers, Orders, OrderItems, Products, Regions) 

AI Opening: 

"I'm looking at your database with 5 tables that appear to form an e-commerce order management system. I can see relationships between customers, their orders, and product inventory. 

I've started building a blueprint for this workspace. A few quick questions: 

The 'status' column in Orders - does this track order fulfillment stages, payment status, or both? 

Should 'unit_cost' in Products represent wholesale cost or retail price?" 

Rationale: The domain is clear (e-commerce), but some column semantics need clarification. Generate the blueprint with targeted follow-up questions for ambiguous fields. 

Scenario 3: Large, Diverse Database 

Context: User connects an enterprise database with 47 tables spanning CRM, inventory, HR, and finance 

AI Opening: 

"I see you've connected a database with 47 tables covering diverse business areas - customer relationship management, inventory, HR records, and financial transactions. 

To make this workspace most useful, what would you like to focus on? For example: 

Sales & Customer Analytics - I'd include tables like Customers, Opportunities, Quotes, Orders 

Inventory & Supply Chain - Tables like Products, Warehouses, Shipments, Vendors 

Financial Reporting - Tables like Invoices, Payments, Expenses, GL_Accounts 

Everything - Keep all 47 tables (though this might make analysis conversations less focused) 

What's your primary goal for this workspace?" 

Rationale: Too many tables for automatic inclusion. Focus on workspace purpose first, then curate relevant tables. This teaches users to think in terms of business domains. 

Scenario 4: Medical Practice Database (Anonymized Real Client) 

Context: User connects a pediatric practice management system with 12 tables (Appointments, Patients, Procedures, Billing, Insurance, Providers, etc.) 

AI Opening: 

"I'm analyzing your healthcare practice database with 12 tables. This looks like a clinic management system tracking patient appointments, procedures, billing, and insurance. 

I've created a blueprint for all tables. A few things I'd like to clarify: 

In your Procedures table, 'proc_status' - does this indicate completion, billing status, or approval status? 

The 'provider_id' appears in multiple tables - should I create a semantic link so you can easily ask questions like 'Show me Dr. Johnson's patients'? 

I notice diagnosis codes in abbreviated form - would you like me to recognize common medical code formats (ICD-10, CPT) automatically?" 

Rationale: Healthcare databases have specialized terminology. The domain is clear, but medical semantics benefit from expert confirmation. Generate the full blueprint but ask domain-specific clarification questions. 

Interaction Patterns 

The AI's Conversational Strategy 

Throughout the blueprint conversation, the AI follows these patterns: 

1. Generate First, Ask Second 

Never ask users to define what a "synonym" or "table description" is 

Always provide a working blueprint, then refine through dialogue 

2. Ask Targeted Questions 

"What does 'status_code' represent in your Orders table?" 

NOT: "Would you like to add synonyms for status_code?" 

3. Explain Decisions Transparently 

"I've interpreted 'cust_name' as referring to customer names, so you can ask about 'clients' or 'buyers' and I'll understand" 

4. Adapt to User Sophistication 

Power users can jump into the right-pane blueprint and directly edit 

Novice users can simply answer conversational questions 

User Response Patterns 

Users can respond in natural language: 

"Focus on sales and inventory" → AI removes HR/finance tables 

"Status means fulfillment stage, not payment" → AI updates semantic understanding 

"Looks good, let's go" → Blueprint is finalized, user moves to data exploration 

Direct edits in right panel → Changes reflected immediately 

Technical Considerations 

Performance Optimization 

Initial schema analysis must complete quickly (<3 seconds ideal) 

For v2.0: synchronous generation on "Get Started" click 

Future enhancement: pre-generate when data sources are added (async) 

Realistic Testing Data 

To validate this UX, use: 

Anonymized real client schemas (modified to protect confidentiality) 

Standard datasets (Tableau's Global Superstore) 

Varying complexity levels (1 table → 50+ tables) 

Prompt Engineering 

We should keep the prompting visible internally as we develop the AI UX.  

Success Metrics 

A successful blueprint conversation achieves: 

Effective process: When the blueprint process ends (when the user and agent agree the agent has enough information), the blueprint is an effective guide to creating queries from natural language. I.e., the next phase (data anlysis) works. 

Minimal user input; maximum time-efficiency: Users answer as few clarifying questions; we will develop some sense of what a realistic user time-efficiency target is as we go. 

High accuracy and confidence: 90%+ of automatically generated semantics are basically correct. User feels a high level of confidence that the AI understand its data, asks good questions. 

Intuitive flow: Users understand the process and workspace organization without training 

Competitive advantage: Faster and better than competitors, from CoPilot to Camel and Vizoo. 

 