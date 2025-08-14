#!/usr/bin/env python3
"""
Test script for repository service functionality
"""

import asyncio
import httpx
import json
from datetime import datetime, timedelta
from jose import jwt

async def test_repository_endpoints():
    """Test repository endpoints"""
    
    base_url = "http://localhost:8000"
    
    # Create a test JWT token
    token_data = {
        "user_id": 12345,
        "username": "testuser",
        "github_token": "test_github_token",
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    
    token = jwt.encode(token_data, "test_jwt_secret_key_for_testing_only", algorithm="HS256")
    headers = {"Authorization": f"Bearer {token}"}
    
    async with httpx.AsyncClient() as client:
        print("🔍 Testing repository endpoints...")
        
        # Test 1: Get supported extensions
        print("\n1. Testing supported extensions endpoint...")
        try:
            response = await client.get(f"{base_url}/api/repositories/supported-extensions")
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Supported extensions: {len(data['extensions'])}")
                print(f"   Sample extensions: {data['extensions'][:5]}")
            else:
                print(f"   Error: {response.text}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Test 2: List repositories (will fail without real GitHub token)
        print("\n2. Testing repository listing...")
        try:
            response = await client.get(f"{base_url}/api/repositories/", headers=headers)
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Repositories found: {len(data)}")
            else:
                print(f"   Response: {response.json()}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Test 3: Get specific repository (will fail without real GitHub token)
        print("\n3. Testing specific repository retrieval...")
        try:
            response = await client.get(f"{base_url}/api/repositories/octocat/Hello-World", headers=headers)
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Repository: {data['full_name']}")
            else:
                print(f"   Response: {response.json()}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Test 4: List repository files (will fail without real GitHub token)
        print("\n4. Testing repository file listing...")
        try:
            response = await client.get(f"{base_url}/api/repositories/octocat/Hello-World/files", headers=headers)
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Files found: {data['supported_files']}")
            else:
                print(f"   Response: {response.json()}")
        except Exception as e:
            print(f"   Error: {e}")
        
        print("\n✅ Repository endpoint tests completed!")
        print("\n📝 Note: Most endpoints will fail without a valid GitHub token.")
        print("   To test with real data, you need to:")
        print("   1. Complete GitHub OAuth flow")
        print("   2. Use the returned GitHub token")
        print("   3. Test with your own repositories")

if __name__ == "__main__":
    print("🚀 Starting repository service test...")
    asyncio.run(test_repository_endpoints())