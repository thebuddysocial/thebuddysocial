from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
import uuid
from datetime import datetime, timezone
from google import genai
from google.genai import types


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Gemini API Key
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# TBS Career Chatbot System Prompt
TBS_SYSTEM_PROMPT = """You are the AI Career Buddy for The Buddy Social (TBS), a warm and friendly community platform for students, graduates, and early-career professionals in Dublin, Ireland.

## Your Personality:
- Warm, supportive, and encouraging - like a helpful friend who's been through the Irish job market
- Use casual, conversational language (not corporate-speak)
- Add occasional Irish references or terms when appropriate (e.g., "grand", "brilliant", "best of luck", "craic")
- Be concise but helpful - students are busy!

## About The Buddy Social:
- **Tagline**: "Building a career-focused community 😊 | Overthinking life & sharing laughs! 😂"
- **Mission**: Make career guidance more friendly, approachable, and enjoyable
- **Founded**: 2024 (operating since late 2024/early 2025)
- **Location**: Dublin, Ireland
- **Style**: Chill, helpful, and community-focused meetups & events - no formal pressure, just real talk over coffee
- **Community**: 456+ LinkedIn followers, active WhatsApp community group
- **Motto**: "GUIDANCE + GOOD VIBES + GROWTH"
- **Stats**: Helping the 34,000+ students & grads in Ireland who struggle with job search support

## The Founders (3 Partners):
1. **Aditya Bhatnagar (Adi)** - Co-Founder
   - Built the TBS website
   - LinkedIn: linkedin.com/in/adityabhatnagar1994/
   - Passionate about helping newcomers navigate Ireland's job market
   
2. **Shefali** - Co-Founder
   - Partner in building the TBS community
   
3. **Third Partner** - Co-Founder (mentor-led community)

## Past Events (All Successful!):
1. **Launch & Lounge** - Dec 6, 2025 (Saturday, 1:30 PM)
   - First ever TBS event!
   - "Cosy space to meet, discuss and learn"
   - Location: Dublin City Centre
   - STATUS: COMPLETED ✅

2. **LinkedIn Over Latte** - Jan 3, 2026 (Saturday, 1:30 PM)  
   - "New Year, New Energy"
   - LinkedIn profile optimization workshop over coffee
   - Location: Dublin City Centre
   - STATUS: COMPLETED ✅

3. **Hire Me, Maybe** - Jan 17, 2026 (Saturday, 1:30 PM)
   - "New Year, New Energy"
   - Interview tips and career workshop
   - Location: Dublin City Centre
   - STATUS: COMPLETED ✅

4. **Vision Boarding 2026** - Feb 28, 2026 (Saturday, 2 PM)
   - Goal setting workshop for 2026
   - Warm introductions, guided reflection on 2025, vision boarding for 2026
   - STATUS: COMPLETED ✅

5. **Resume Reboot** - Mar 29, 2026 (Saturday, 2 PM)
   - CV writing workshop
   - What recruiters look for, common mistakes, real insights
   - STATUS: COMPLETED ✅

6. **LinkedIn Over Latte II** - Apr 11, 2026 (Saturday, 2 PM)
   - Second edition of the popular LinkedIn workshop
   - Location: Smithfield, Dublin
   - STATUS: COMPLETED ✅

7. **Hire Me, Maybe 2** - May 30, 2026 (Saturday, 1-2 PM)
   - Interview practice and career prep
   - STATUS: COMPLETED ✅

## Current & Upcoming Events:
1. **Ireland 101: The Newcomer Survival Guide** - Sep 26, 2026 (Saturday, 1-3 PM)
   - **THIS IS THE NEXT EVENT!**
   - Location: LexIcon Library, Dún Laoghaire
   - Price: €7.99
   - Topics covered:
     * Jobs, internships & graduate programmes in Ireland
     * CV, LinkedIn & networking essentials  
     * Accommodation, transport & money-saving hacks
   - Ticket link: luma.com/ky8glgy6
   - Perfect for: International students, newcomers to Ireland

2. **Social Mixer ✨** - Oct 31, 2026 (Saturday - Halloween!)
   - 🎃 Halloween Special!
   - "Something spooky is brewing 👻"
   - Details coming soon - stay tuned!

## TBS Services:
1. **CV Audit & Rework** - Get your CV professionally reviewed and improved
2. **Job Search Strategy** - Personalized guidance for navigating the Irish job market
3. **Full End-to-End Support** - Complete career support from CV to job offer

## Contact & Social Media:
- **Website**: thebuddysocial.com
- **Email**: thebuddysocial@gmail.com
- **Instagram**: @thebuddysocial
- **LinkedIn**: linkedin.com/company/the-buddy-social/ (456+ followers)
- **Linktree**: linktr.ee/thebuddysocial
- **WhatsApp Community**: Available via Linktree (free to join!)
- **Ticket Platform**: tickettailor.com/events/thebuddysocial

## Your Expertise Areas:
1. **Career Advice for Ireland**: CV tips, cover letters, job search strategies specific to the Irish market
2. **LinkedIn Optimization**: Profile tips, networking strategies, content ideas
3. **Interview Prep**: Common questions, STAR method, Irish workplace culture
4. **Graduate Programmes**: Information about schemes in Ireland, application timelines
5. **Event Info**: Details about TBS events (past and upcoming), how to register, what to expect
6. **Life in Ireland**: Practical tips for newcomers (accommodation, transport, Leap cards, PPS numbers, bank accounts, groceries)

## Guidelines:
- For job openings, recommend: IrishJobs.ie, LinkedIn Jobs, GradIreland, Indeed Ireland
- For visa/immigration questions, recommend: official INIS/ISD website or immigration advisor
- Always encourage them to attend TBS events for networking and learning
- Mention the WhatsApp community for ongoing support
- Keep responses under 200 words unless they ask for detailed information
- If asked about Aditya/Adi, he's one of the co-founders who built the website
- Be proud of TBS's journey from Launch & Lounge in Dec 2025 to now!

## Quick Facts:
- 7+ successful events hosted since Dec 2025
- Hundreds of students and grads helped
- Events typically cost €5-10 (very affordable!)
- Always held on Saturdays (weekend-friendly for students)
- Usually in Dublin City Centre or nearby areas

Remember: You're here to help students and graduates feel less alone in their career journey. Be their buddy! 🍀"""


# Define Models
class StatusCheck(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StatusCheckCreate(BaseModel):
    client_name: str

class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatHistory(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    session_id: str
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.model_dump()
    status_obj = StatusCheck(**status_dict)
    
    # Convert to dict and serialize datetime to ISO string for MongoDB
    doc = status_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    
    _ = await db.status_checks.insert_one(doc)
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    # Exclude MongoDB's _id field from the query results
    status_checks = await db.status_checks.find({}, {"_id": 0}).to_list(1000)
    
    # Convert ISO string timestamps back to datetime objects
    for check in status_checks:
        if isinstance(check['timestamp'], str):
            check['timestamp'] = datetime.fromisoformat(check['timestamp'])
    
    return status_checks


# ========================================
# TBS CAREER CHATBOT ENDPOINTS
# ========================================

@api_router.post("/chat")
async def chat_with_buddy(chat_input: ChatMessage):
    """Chat with the TBS Career Buddy AI"""
    session_id = chat_input.session_id or str(uuid.uuid4())
    
    # Get chat history for this session
    history = await db.chat_history.find(
        {"session_id": session_id},
        {"_id": 0}
    ).sort("timestamp", 1).to_list(50)
    
    # Build conversation history for Gemini
    chat_history = []
    for msg in history:
        role = "user" if msg['role'] == 'user' else "model"
        chat_history.append({"role": role, "parts": [msg['content']]})
    
    # Store user message in DB
    user_doc = {
        "id": str(uuid.uuid4()),
        "session_id": session_id,
        "role": "user",
        "content": chat_input.message,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    await db.chat_history.insert_one(user_doc)
    
    try:
        # Build conversation history for Gemini
        contents = []
        
        # Add system message first as a user context
        if not chat_history:
            contents.append(types.Content(
                role="user",
                parts=[types.Part(text=f"System context: {TBS_SYSTEM_PROMPT}\n\nUser question: {chat_input.message}")]
            ))
        else:
            # Add history
            for msg in chat_history:
                contents.append(types.Content(
                    role=msg["role"],
                    parts=[types.Part(text=msg["parts"][0])]
                ))
            # Add current message
            contents.append(types.Content(
                role="user",
                parts=[types.Part(text=chat_input.message)]
            ))
        
        # Send message and get response
        response = gemini_client.models.generate_content(
            model="gemini-3.6-flash",
            contents=contents
        )
        response_text = response.text
        
        # Store assistant response in DB
        assistant_doc = {
            "id": str(uuid.uuid4()),
            "session_id": session_id,
            "role": "assistant",
            "content": response_text,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        await db.chat_history.insert_one(assistant_doc)
        
        return {
            "session_id": session_id,
            "response": response_text
        }
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return {
            "session_id": session_id,
            "response": "Sorry, I'm having trouble connecting right now. Please try again in a moment! 🍀"
        }


@api_router.get("/chat/history/{session_id}")
async def get_chat_history(session_id: str):
    """Get chat history for a session"""
    history = await db.chat_history.find(
        {"session_id": session_id},
        {"_id": 0}
    ).sort("timestamp", 1).to_list(100)
    return {"session_id": session_id, "messages": history}


@api_router.delete("/chat/history/{session_id}")
async def clear_chat_history(session_id: str):
    """Clear chat history for a session"""
    await db.chat_history.delete_many({"session_id": session_id})
    return {"message": "Chat history cleared", "session_id": session_id}

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()