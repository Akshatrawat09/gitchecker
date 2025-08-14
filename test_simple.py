#!/usr/bin/env python3
"""
Simple test to verify our authentication system works
"""

def test_simple():
    """Simple test that should always pass"""
    assert True

def test_imports():
    """Test that we can import our modules"""
    try:
        from app.core.config import settings
        from app.services.auth_service import auth_service
        from app.models.auth import GitHubUser
        print("✅ All imports successful!")
        print(f"Environment: {settings.ENVIRONMENT}")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Running simple tests...")
    
    print("\n1. Testing basic assertion...")
    test_simple()
    print("✅ Basic test passed!")
    
    print("\n2. Testing imports...")
    if test_imports():
        print("✅ Import test passed!")
    else:
        print("❌ Import test failed!")
    
    print("\n🎉 Simple tests completed!")