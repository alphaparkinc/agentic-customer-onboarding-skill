import sys
import json
from onboarding_agent import OnboardingAgentClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== Agentic Customer Onboarding Agent Example ===")
    client = OnboardingAgentClient()
    
    org = "Apex Cybernetics"
    size = "enterprise"
    tier = "Premium Enterprise Support"
    
    result = client.plan_onboarding(org, size, tier)
    print("\n--- Onboarding Checklist ---")
    for step in result["onboarding_checklist"]:
        print(f"[ ] {step}")
        
    print("\n--- Personalized Welcome Email ---")
    print(result["welcome_email_draft"])

if __name__ == "__main__":
    main()
