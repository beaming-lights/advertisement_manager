#!/usr/bin/env python3
"""
Simple test script to verify profile pages work correctly
"""

from nicegui import ui

# Test imports
try:
    from pages.candidate_profile import show_candidate_profile_page, show_candidate_list_page
    print("✓ Candidate profile imports successful")
except Exception as e:
    print(f"✗ Candidate profile import error: {e}")

try:
    from pages.company_profile import show_company_profile_page, show_company_list_page
    print("✓ Company profile imports successful")
except Exception as e:
    print(f"✗ Company profile import error: {e}")

@ui.page('/')
def test_page():
    ui.label('Profile Pages Test').classes('text-2xl font-bold mb-4')
    
    with ui.column().classes('space-y-4'):
        ui.button('Test Candidate Profile', 
                 on_click=lambda: ui.navigate.to('/candidate-profile/1')).classes('bg-blue-600 text-white')
        ui.button('Test Company Profile', 
                 on_click=lambda: ui.navigate.to('/company-profile/1')).classes('bg-green-600 text-white')
        ui.button('Test Candidates List', 
                 on_click=lambda: ui.navigate.to('/candidates')).classes('bg-purple-600 text-white')
        ui.button('Test Company List', 
                 on_click=lambda: ui.navigate.to('/company-list')).classes('bg-orange-600 text-white')

# Routes are defined in main.py - no need to duplicate them here

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Profile Pages Test", port=8081)
