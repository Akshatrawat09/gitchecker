#!/usr/bin/env python3
"""
Manual test script for GitHub OAuth authentication flow
Run this script to test the authentication endpoints manually
"""

import asyncio
import httpx
import json
from app.core.config import settings

async def test_auth_flow():
    """Test the complete authentication flow"""
    
    base_url = "http://localhost:8000"
    
    async with httpx.AsyncClient() as client:
        print("🔍 Testing authentication endpoints...")
        
        # Test 1: Health check
        print("\n1. Testing health check...")
        try:
            response = await client.get(f"{base_url}/health")
            print(f"   Status: {response.status_code}")
            health_data = response.json()
            print(f"   GitHub configured: {health_data.get('configuration', {}).get('github_configured')}")
            print(f"   JWT configured: {health_data.get('configuration', {}).get('jwt_configured')}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Test 2: GitHub login redirect
        print("\n2. Testing GitHub login redirect...")
        try:
            response = await client.get(f"{base_url}/api/auth/github", follow_redirects=False)
            print(f"   Status: {response.status_code}")
            if response.status_code == 307:
                location = response.headers.get("location")
                print(f"   Redirect URL: {location[:100]}...")
            else:
                print(f"   Response: {response.text}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Test 3: User endpoint without token
        print("\n3. Testing user endpoint without token...")
        try:
            response = await client.get(f"{base_url}/api/auth/user")
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.json()}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Test 4: Callback with invalid code
        print("\n4. Testing callback with invalid code...")
        try:
            response = await client.post(
                f"{base_url}/api/auth/github/callback",
                json={"code": "invalid_test_code"}
            )
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.json()}")
        except Exception as e:
            print(f"   Error: {e}")
        
        print("\n✅ Authentication endpoint tests completed!")
        print("\n📝 To test the complete OAuth flow:")
        print("   1. Start the server: uvicorn main:app --reload")
        print("   2. Visit: http://localhost:8000/api/auth/github")
        print("   3. Complete GitHub OAuth in browser")
        print("   4. Check the callback handling")

if __name__ == "__main__":
    print("🚀 Starting authentication flow test...")
    print(f"📋 Configuration:")
    print(f"   GitHub Client ID: {settings.GITHUB_CLIENT_ID[:10]}..." if settings.GITHUB_CLIENT_ID else "   GitHub Client ID: Not configured")
    print(f"   JWT Secret: {'Configured' if settings.JWT_SECRET_KEY != 'your-secret-key-change-in-production' else 'Using default (change for production)'}")
    print(f"   Environment: {settings.ENVIRONMENT}")
    
    asyncio.run(test_auth_flow())