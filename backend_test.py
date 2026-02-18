#!/usr/bin/env python3

import requests
import sys
import json
from datetime import datetime

class BackendTester:
    def __init__(self, base_url="https://github-viewer-live.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []
        self.passed_tests = []

    def run_test(self, name, method, endpoint, expected_status, data=None, expected_response=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)

            print(f"Response Status: {response.status_code}")
            
            success = response.status_code == expected_status
            
            if success:
                try:
                    response_json = response.json()
                    print(f"Response Body: {json.dumps(response_json, indent=2, default=str)}")
                    
                    # Check specific expected response if provided
                    if expected_response:
                        if isinstance(expected_response, dict):
                            for key, value in expected_response.items():
                                if key not in response_json or response_json[key] != value:
                                    success = False
                                    print(f"❌ Response validation failed - Expected {key}: {value}, got: {response_json.get(key)}")
                                    break
                        elif isinstance(expected_response, list):
                            if not isinstance(response_json, list):
                                success = False
                                print(f"❌ Response validation failed - Expected list, got: {type(response_json)}")
                    
                    if success:
                        self.tests_passed += 1
                        self.passed_tests.append(f"{name} - Status: {response.status_code}")
                        print(f"✅ Passed - Status: {response.status_code}")
                    else:
                        self.failed_tests.append(f"{name} - Response validation failed")
                        
                except json.JSONDecodeError:
                    print(f"❌ Failed - Invalid JSON response")
                    self.failed_tests.append(f"{name} - Invalid JSON response")
                    success = False
                    
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                self.failed_tests.append(f"{name} - Expected {expected_status}, got {response.status_code}")
                if response.text:
                    print(f"Response Body: {response.text}")

            return success, response.json() if success and response.text else {}

        except requests.exceptions.RequestException as e:
            print(f"❌ Failed - Request Error: {str(e)}")
            self.failed_tests.append(f"{name} - Request Error: {str(e)}")
            return False, {}
        except Exception as e:
            print(f"❌ Failed - Unexpected Error: {str(e)}")
            self.failed_tests.append(f"{name} - Unexpected Error: {str(e)}")
            return False, {}

    def test_root_endpoint(self):
        """Test GET /api/ endpoint"""
        return self.run_test(
            "Root Hello World API",
            "GET",
            "api/",
            200,
            expected_response={"message": "Hello World"}
        )

    def test_create_status_check(self):
        """Test POST /api/status endpoint"""
        test_data = {
            "client_name": f"test_client_{datetime.now().strftime('%H%M%S')}"
        }
        
        success, response = self.run_test(
            "Create Status Check",
            "POST",
            "api/status",
            200,
            data=test_data
        )
        
        if success and 'id' in response:
            print(f"Created status check with ID: {response['id']}")
            return True, response['id']
        return False, None

    def test_get_status_checks(self):
        """Test GET /api/status endpoint"""
        success, response = self.run_test(
            "Get Status Checks",
            "GET",
            "api/status",
            200,
            expected_response=[]  # Expect list format
        )
        return success

def main():
    print("🚀 Starting Backend API Tests...")
    print("=" * 50)
    
    # Setup
    tester = BackendTester()

    # Test 1: Root endpoint
    print("\n📍 Test 1: Root Hello World API")
    tester.test_root_endpoint()

    # Test 2: Create status check
    print("\n📍 Test 2: Create Status Check")
    success, status_id = tester.test_create_status_check()

    # Test 3: Get status checks
    print("\n📍 Test 3: Get Status Checks")
    tester.test_get_status_checks()

    # Print final results
    print("\n" + "=" * 50)
    print("📊 FINAL TEST RESULTS")
    print("=" * 50)
    print(f"✅ Tests passed: {tester.tests_passed}/{tester.tests_run}")
    
    if tester.passed_tests:
        print(f"\n✅ PASSED TESTS:")
        for test in tester.passed_tests:
            print(f"  - {test}")
    
    if tester.failed_tests:
        print(f"\n❌ FAILED TESTS:")
        for test in tester.failed_tests:
            print(f"  - {test}")
    
    success_rate = (tester.tests_passed / tester.tests_run) * 100 if tester.tests_run > 0 else 0
    print(f"\n📈 Success Rate: {success_rate:.1f}%")
    
    return 0 if tester.tests_passed == tester.tests_run else 1

if __name__ == "__main__":
    sys.exit(main())