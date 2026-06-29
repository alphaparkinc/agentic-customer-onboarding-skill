import os
from typing import Dict, Any, Optional

class OnboardingAgentClient:
    """
    Client SDK for generating custom customer onboarding checklists and communications.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("ONBOARDING_API_KEY")
        self.mock_mode = self.api_key is None or self.api_key == "mock"

    def plan_onboarding(self, org_name: str, org_size: str, tier: str) -> Dict[str, Any]:
        """
        Creates onboarding items and custom templates depending on segment parameters.
        """
        checklist = [
            "Complete team account provisioning",
            "Verify secure billing details",
            "Configure custom SSO and OAuth credentials"
        ]
        
        if org_size == "enterprise":
            checklist.extend([
                "Schedule a dedicated kickoff sync with a customer success engineer",
                "Review enterprise SLA and security audit docs"
            ])
        else:
            checklist.extend([
                "Follow getting-started quick guide online",
                "Join our community forum for developer tips"
            ])
            
        welcome_email = (
            f"Subject: Welcome to the Platform, {org_name} team!\n\n"
            f"Hi team,\n\n"
            f"We are excited to help you launch on our {tier} tier. "
            f"To get started, please log in to your dashboard and complete your kickoff checklist:\n"
            + "\n".join([f"- {item}" for item in checklist]) + "\n\n"
            f"Best,\nThe Onboarding Success Team"
        )
        
        return {
            "onboarding_checklist": checklist,
            "welcome_email_draft": welcome_email
        }
