import json
import random
from datetime import datetime, timedelta
import anthropic
from typing import Dict, List, Any
import numpy as np

class SocialMediaDataGenerator:
    def __init__(self):
        self.locations = [
            "US", "UK", "Canada", "India", "Australia", "Germany", "France",
            "Brazil", "Spain", "Italy", "Mexico", "Philippines", "Japan",
            "Netherlands", "Sweden"
        ]
        
        self.post_types = ["carousel", "reel", "static"]
        
        self.engagement_bases = {
            'carousel': {
                'likes_base': (1000, 200),  
                'comments_base': (80, 15),
                'shares_base': (40, 10),
                'saves_base': (100, 20),
                'reach_base': (14000, 2000)
            },
            'reel': {
                'likes_base': (2500, 400),
                'comments_base': (180, 30),
                'shares_base': (250, 40),
                'saves_base': (300, 50),
                'reach_base': (24000, 4000)
            },
            'static': {
                'likes_base': (800, 150),
                'comments_base': (40, 8),
                'shares_base': (20, 5),
                'saves_base': (60, 10),
                'reach_base': (9000, 1500)
            }
        }

    def generate_engagement_metrics(self, post_type: str) -> Dict[str, int]:
        base = self.engagement_bases[post_type]
        
        metrics = {}
        for metric, (mean, std) in base.items():
            value = max(int(np.random.normal(mean, std)), 1)
            metrics[metric.replace('_base', '')] = value
        
        reach = metrics['reach']
        metrics['impressions'] = int(reach * random.uniform(1.2, 1.5))
        
        return metrics

    def generate_age_demographics(self) -> Dict[str, float]:
        demo = {
            "18-24": random.uniform(0.3, 0.45),
            "25-34": random.uniform(0.35, 0.5),
            "35-44": random.uniform(0.15, 0.25)
        }
        
        demo["45+"] = 1 - sum(demo.values())
        
        return {k: round(v, 2) for k, v in demo.items()}

    def generate_post(self, post_id: int, date: datetime) -> Dict[str, Any]:
        post_type = random.choice(self.post_types)
        
        top_locations = random.sample(self.locations, 3)
        if "US" not in top_locations:
            top_locations[random.randint(0, 2)] = "US"

        post = {
            "post_id": f"P{str(post_id).zfill(3)}",
            "post_type": post_type,
            "created_at": date.isoformat(),
            "content": {
                "caption_length": random.randint(150, 300),
                "hashtags_count": random.randint(4, 9)
            },
            "engagement": self.generate_engagement_metrics(post_type),
            "audience_demographics": {
                "age_group": self.generate_age_demographics(),
                "top_locations": top_locations
            }
        }

        if post_type == "carousel":
            post["content"]["images_count"] = random.randint(4, 9)
        elif post_type == "reel":
            post["content"]["video_duration"] = random.randint(15, 60)

        return post

    def generate_dataset(self, num_posts: int, start_date: datetime) -> Dict[str, Any]:
        posts = []
        current_date = start_date

        for i in range(1, num_posts + 1):
            # Add random hours to make timestamps more realistic
            post_date = current_date + timedelta(hours=random.randint(0, 12))
            posts.append(self.generate_post(i, post_date))
            current_date += timedelta(days=1)

        return {
            "posts": posts,
            "metadata": {
                "total_posts": num_posts,
                "date_range": {
                    "start": posts[0]["created_at"],
                    "end": posts[-1]["created_at"]
                },
                "post_types": self.post_types,
                "metrics_tracked": [
                    "likes", "comments", "shares", "saves", "reach", "impressions"
                ]
            }
        }


class DataValidator:
    def __init__(self, api_key: str = "dummy_key_12345"):
        self.client = anthropic.Client(api_key=api_key)

    def validate_data(self, data: Dict[str, Any]) -> str:
        prompt = f"""
        Please analyze this social media analytics dataset and provide feedback on its quality and realism. 
        Consider the following aspects:
        1. Engagement metrics and their relationships
        2. Demographic distributions
        3. Geographic distribution
        4. Temporal patterns
        5. Content metrics

        Here's a sample of the data (first 2 posts):
        {json.dumps(data['posts'][:2], indent=2)}

        Summary metrics:
        - Total posts: {data['metadata']['total_posts']}
        - Date range: {data['metadata']['date_range']['start']} to {data['metadata']['date_range']['end']}
        - Post types: {', '.join(data['metadata']['post_types'])}

        Please provide specific feedback on:
        1. Whether the engagement metrics are realistic
        2. If the demographic distributions make sense
        3. Any anomalies or concerns
        4. Suggestions for improvement
        """

        try:
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                system="You are a data quality expert specializing in social media analytics.",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content
        except Exception as e:
            return f"Error in validation: {str(e)}"


def main():
    generator = SocialMediaDataGenerator()
    
    start_date = datetime(2024, 1, 1, 10, 0, 0)
    data = generator.generate_dataset(50, start_date)
    
    with open('social_media_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    validator = DataValidator(api_key="dummy_key_12345")
    feedback = validator.validate_data(data)
    
    print("\nData Generation Complete!")
    print(f"Generated {data['metadata']['total_posts']} posts")
    print("\nValidation Feedback:")
    print(feedback)


if __name__ == "__main__":
    main()