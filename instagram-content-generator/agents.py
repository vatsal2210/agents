# agents.py

class MarketingAgent:
    def __init__(self, role, goal, backstory, tools, delegation_settings):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = tools
        self.delegation_settings = delegation_settings

class LeadMarketAnalyst(MarketingAgent):
    def __init__(self):
        super().__init__(
            role='Lead Market Analyst',
            goal='Analyze market trends and data to inform strategy.',
            backstory='Experienced analyst with a passion for understanding market dynamics.',
            tools=['Excel', 'Tableau', 'Google Trends'],
            delegation_settings=['Delegate data collection tasks', 'Oversee junior analysts']
        )

class ChiefMarketingStrategist(MarketingAgent):
    def __init__(self):
        super().__init__(
            role='Chief Marketing Strategist',
            goal='Develop and oversee the execution of marketing strategies.',
            backstory='Visionary leader with a track record in building successful campaigns.',
            tools=['Marketing Automation Software', 'CRM Systems'],
            delegation_settings=['Lead marketing team', 'Allocate budgets']
        )

class CreativeContentCreator(MarketingAgent):
    def __init__(self):
        super().__init__(
            role='Creative Content Creator',
            goal='Create engaging content that resonates with the audience.',
            backstory='A creative individual with an eye for detail and storytelling.',
            tools=['Adobe Creative Suite', 'Canva'],
            delegation_settings=['Collaborate with designers', 'Review content from teams']
        )

class SeniorPhotographer(MarketingAgent):
    def __init__(self):
        super().__init__(
            role='Senior Photographer',
            goal='Capture high-quality images for marketing materials.',
            backstory='Creative photographer with years of branding experience.',
            tools=['Camera Equipment', 'Photo Editing Software'],
            delegation_settings=['Manage photography team', 'Coordinate shoots']
        )

class ChiefCreativeDirector(MarketingAgent):
    def __init__(self):
        super().__init__(
            role='Chief Creative Director',
            goal='Oversee the creative direction and output of marketing campaigns.',
            backstory='Proven leader with a passion for innovation in advertising.',
            tools=['Project Management Tools', 'Creative Brief Templates'],
            delegation_settings=['Approve creative concepts', 'Guide creative teams']
        )

class MarketingAgents:
    @staticmethod
    def create_lead_market_analyst():
        return LeadMarketAnalyst()

    @staticmethod
    def create_chief_marketing_strategist():
        return ChiefMarketingStrategist()

    @staticmethod
    def create_creative_content_creator():
        return CreativeContentCreator()

    @staticmethod
    def create_senior_photographer():
        return SeniorPhotographer()

    @staticmethod
    def create_chief_creative_director():
        return ChiefCreativeDirector()