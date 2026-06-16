## System Workflow

```mermaid
flowchart TD
    classDef user fill:#3B82F6,stroke:#2563EB,stroke-width:3px,color:white,rx:20,ry:20;
    classDef hub fill:#10B981,stroke:#059669,stroke-width:3px,color:white,rx:20,ry:20;
    classDef ai fill:#8B5CF6,stroke:#7C3AED,stroke-width:3px,color:white,rx:20,ry:20;
    classDef decision fill:#F59E0B,stroke:#D97706,stroke-width:3px,color:white,rx:25,ry:25;
    classDef reward fill:#22C55E,stroke:#16A34A,stroke-width:3px,color:white;
    classDef penalty fill:#EF4444,stroke:#DC2626,stroke-width:3px,color:white;

    A[User Submits Content<br/>Post or Comment]:::user
    --> B[Interaction Hub<br/>Main Controller]:::hub

    B --> C[Send Content to LLM<br/>for Intelligent Analysis]:::ai

    C --> D[LLM Evaluates Quality<br/>Returns Score 1-10]:::ai

    D --> E{Content Quality}:::decision

    E -->|High Quality 8-10| F[High Reward<br/>+15 Reputation<br/>+8 Tokens]:::reward
    E -->|Medium Quality 4-7| G[Medium Reward<br/>+7 Reputation<br/>+4 Tokens]:::reward
    E -->|Low Quality 1-3| H[Penalty<br/>-10 Reputation]:::penalty

    F --> I[Update User Profile]:::hub
    G --> I
    H --> I

    I --> J[User Views Results<br/>my_score & my_balance]:::user


## Step-by-Step Process

User Input — User submits content (post or comment)
Interaction Hub — Receives and processes the submission
LLM Analysis — Sends content to AI model for quality evaluation
AI Decision — LLM returns a quality score (1-10)
Reward Logic — System applies appropriate rewards or penalties based on AI judgment
State Update — Updates user's reputation and token balance
User Feedback — User can view updated profile and history

Key Benefits

Fully automated and intelligent content moderation
Uses real LLM judgment (non-deterministic)
Transparent and fair reputation system
Designed specifically for SocialFi platforms on GenLayer


