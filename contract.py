# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class AIReputationJudge(gl.Contract):

    scores: TreeMap[Address, u256]
    reasons: TreeMap[Address, str]
    evaluations: TreeMap[Address, u256]

    def __init__(self):
        pass

    @gl.public.write
    def evaluate_contribution(
        self,
        contribution: str,
        category: str,
        evidence: str
    ) -> None:

        contributor = gl.message.sender_address

        def get_input() -> str:
            return f"""
Contribution:
{contribution}

Category:
{category}

Evidence:
{evidence}
"""

        result = gl.eq_principle.prompt_non_comparative(
            get_input,
            task="""
You are an impartial reputation evaluator.

Analyze the contribution and evaluate:

1. Contribution Quality
2. Community Impact
3. Originality
4. Evidence Credibility

Return EXACTLY in this format:

Score: <number>
Reason: <short explanation>

Keep the response concise.
""",
            criteria="""
The response must contain:

- Score between 0 and 100
- A short reason
- No extra sections
"""
        )

        self.reasons[contributor] = result

        current_count = self.evaluations.get(
            contributor,
            u256(0)
        )

        self.evaluations[contributor] = current_count + u256(1)

        score_value = u256(0)

        for i in range(101):
            if f"Score: {i}" in result:
                score_value = u256(i)

        self.scores[contributor] = score_value

    @gl.public.view
    def get_my_score(self) -> u256:
        return self.scores.get(
            gl.message.sender_address,
            u256(0)
        )

    @gl.public.view
    def get_my_reason(self) -> str:
        return self.reasons.get(
            gl.message.sender_address,
            "No evaluation found"
        )

    @gl.public.view
    def get_my_evaluation_count(self) -> u256:
        return self.evaluations.get(
            gl.message.sender_address,
            u256(0)
        )

    @gl.public.view
    def get_my_profile(self) -> str:

        score = self.scores.get(
            gl.message.sender_address,
            u256(0)
        )

        reason = self.reasons.get(
            gl.message.sender_address,
            "No evaluation found"
        )

        count = self.evaluations.get(
            gl.message.sender_address,
            u256(0)
        )

        return f"""
Score: {score}

Evaluations: {count}

Latest Evaluation:
{reason}
"""
