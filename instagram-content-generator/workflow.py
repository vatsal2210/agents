"""Workflow Orchestration for Instagram Content Generator

This module orchestrates the multi-agent workflow, coordinating task execution
and managing context flow between agents.
"""

from typing import Dict, Any, List
from agents import MarketingAgents
from tasks import MarketingTasks


class InstagramContentWorkflow:
    """Main workflow orchestrator for Instagram content generation"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.agents = MarketingAgents()
        self.tasks = MarketingTasks()
        self.context = []
        
    def run(self, product_website: str, product_details: str) -> Dict[str, str]:
        """Execute the complete workflow"""
        print("\n🎯 Phase 1: Content Strategy Workflow")
        print("=" * 60)
        
        # Initialize agents for Crew 1
        market_analyst = self.agents.lead_market_analyst()
        strategist = self.agents.chief_marketing_strategist()
        creative = self.agents.creative_content_creator()
        
        # Task 1: Product Analysis
        print("\n📊 Step 1: Analyzing product...")
        product_task = self.tasks.product_analysis(product_website, product_details)
        product_analysis = self._execute_task(market_analyst, product_task)
        self.context.append(product_analysis)
        print("✓ Product analysis complete")
        
        # Task 2: Competitor Analysis
        print("\n🔍 Step 2: Analyzing competitors...")
        competitor_task = self.tasks.competitor_analysis(product_website, product_details)
        competitor_analysis = self._execute_task(market_analyst, competitor_task)
        self.context.append(competitor_analysis)
        print("✓ Competitor analysis complete")
        
        # Task 3: Campaign Development
        print("\n💡 Step 3: Developing campaign strategy...")
        campaign_task = self.tasks.campaign_development(product_website, product_details)
        campaign_strategy = self._execute_task(strategist, campaign_task, self.context)
        self.context.append(campaign_strategy)
        print("✓ Campaign strategy complete")
        
        # Task 4: Ad Copy Creation
        print("\n✍️  Step 4: Creating Instagram ad copy...")
        copy_task = self.tasks.instagram_ad_copy()
        ad_copy = self._execute_task(creative, copy_task, self.context)
        print("✓ Ad copy complete")
        
        # Phase 2: Visual Production
        print("\n\n📸 Phase 2: Visual Production Workflow")
        print("=" * 60)
        
        # Initialize agents for Crew 2
        photographer = self.agents.senior_photographer()
        director = self.agents.chief_creative_director()
        
        # Task 5: Photograph Conceptualization
        print("\n🎨 Step 5: Conceptualizing photographs...")
        photo_task = self.tasks.photograph_concept(ad_copy, product_website, product_details)
        photo_concepts = self._execute_task(photographer, photo_task, [ad_copy, campaign_strategy])
        print("✓ Photo concepts complete")
        
        # Task 6: Creative Review
        print("\n👔 Step 6: Creative director review...")
        review_task = self.tasks.creative_review(product_website, product_details)
        final_photos = self._execute_task(director, review_task, [photo_concepts, ad_copy])
        print("✓ Creative review complete")
        
        return {
            'ad_copy': ad_copy,
            'photo_descriptions': final_photos,
            'campaign_strategy': campaign_strategy
        }
    
    def _execute_task(self, agent, task: Any, context: List[str] = None) -> str:
        """Execute a single task with context"""
        # In production, this would call your LLM with the agent's prompt and task
        # For now, return a placeholder that demonstrates the structure
        
        result = f"""
=== {agent.role} Output ===

Task: {task.description[:100]}...

[This is a placeholder output. In production, this would be the actual LLM response
based on the agent's role, backstory, and the task description.]

Expected Output: {task.expected_output}
        """
        
        return result.strip()


if __name__ == "__main__":
    # Test the workflow
    workflow = InstagramContentWorkflow()
    results = workflow.run(
        "https://example.com",
        "Innovative eco-friendly water bottle"
    )
    
    print("\n\n" + "=" * 60)
    print("WORKFLOW TEST COMPLETE")
    print("=" * 60)
    print(f"\nAd Copy Length: {len(results['ad_copy'])} chars")
    print(f"Photo Descriptions Length: {len(results['photo_descriptions'])} chars")
