#!/usr/bin/env python3
"""
Debug script to test routes individually
"""

from nicegui import ui

@ui.page('/')
def index():
    ui.label('Route Debug Test').classes('text-2xl font-bold mb-4')
    
    with ui.column().classes('space-y-2'):
        ui.link('Test /candidates', '/candidates').classes('text-blue-600')
        ui.link('Test /candidate-profile/1', '/candidate-profile/1').classes('text-blue-600')
        ui.link('Test /company-profile/1', '/company-profile/1').classes('text-blue-600')
        ui.link('Test /company-list', '/company-list').classes('text-blue-600')

@ui.page('/candidates')
def test_candidates():
    ui.label('Candidates Page Works!').classes('text-xl text-green-600')
    ui.link('Back to home', '/').classes('text-blue-600')

@ui.page('/candidate-profile/{candidate_id}')
def test_candidate_profile(candidate_id: str):
    ui.label(f'Candidate Profile {candidate_id} Works!').classes('text-xl text-green-600')
    ui.link('Back to home', '/').classes('text-blue-600')

@ui.page('/company-profile/{company_id}')
def test_company_profile(company_id: str):
    ui.label(f'Company Profile {company_id} Works!').classes('text-xl text-green-600')
    ui.link('Back to home', '/').classes('text-blue-600')

@ui.page('/company-list')
def test_company_list():
    ui.label('Company List Works!').classes('text-xl text-green-600')
    ui.link('Back to home', '/').classes('text-blue-600')

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Route Debug Test", port=8082)
