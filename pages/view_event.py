from nicegui import ui, app
from components.header import show_header
from datetime import datetime
from typing import Dict, Any

# Import the global job listings (in a real app, this would be a database query)
from .add_event import global_job_listings

def format_date(date_str: str) -> str:
    """Format date string to a more readable format."""
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return date.strftime('%B %d, %Y')
    except (ValueError, TypeError):
        return date_str or 'Not specified'

def show_event_page(job_id: str = None):
    """Display detailed information about a specific job posting."""
    show_header()
    
    # Find the job by ID
    job = next((j for j in global_job_listings if j['id'] == job_id), None)
    
    if not job:
        with ui.column().classes('w-full max-w-4xl mx-auto p-6'):
            ui.label('Job Not Found').classes('text-2xl font-bold text-red-600')
            ui.label('The requested job could not be found or may have been removed.')
            ui.button('Back to Jobs', on_click=lambda: ui.navigate.to('/jobs')).classes('btn btn-secondary mt-4')
        return
    
    with ui.column().classes('w-full max-w-6xl mx-auto p-4 md:p-8'):
        # Enhanced Header Section with gradient background
        with ui.card().classes('modern-card w-full mb-8 bg-gradient-to-br from-primary to-secondary text-white border-0 shadow-2xl animate-fade-in-up'):
            with ui.column().classes('w-full p-8 space-y-6'):
                # Job Title and Company with enhanced styling
                ui.label(job['job_title']).classes('text-4xl lg:text-5xl font-bold mb-2')
                with ui.row().classes('items-center space-x-3'):
                    ui.icon('business', size='lg').classes('text-white/90')
                    ui.label(job['company']).classes('text-2xl font-semibold text-white/95')
                
                # Enhanced Job Meta Information with chips
                with ui.row().classes('flex-wrap gap-3 mt-6'):
                    # Location chip
                    with ui.chip(f"📍 {job['location']} {'🌍 Remote' if job.get('is_remote') else ''}", 
                               icon='location_on').classes('bg-white/20 text-white border-white/30'):
                        pass
                    
                    # Job type chip
                    with ui.chip(f"💼 {job['job_type']}", icon='work').classes('bg-white/20 text-white border-white/30'):
                        pass
                    
                    # Experience level chip
                    if job.get('experience_level'):
                        with ui.chip(f"📈 {job['experience_level']}", icon='trending_up').classes('bg-white/20 text-white border-white/30'):
                            pass
                    
                    # Salary chip
                    if job.get('min_salary') or job.get('max_salary'):
                        salary_range = []
                        if job.get('min_salary'):
                            salary_range.append(f"${float(job['min_salary']):,.0f}")
                        if job.get('max_salary'):
                            salary_range.append(f"${float(job['max_salary']):,.0f}")
                        salary_text = ' - '.join(salary_range) + ('/year' if not job.get('salary_period') else f" {job['salary_period']}")
                        with ui.chip(f"💰 {salary_text}", icon='attach_money').classes('bg-green-500/30 text-white border-green-300/50'):
                            pass
                
                # Posted date and actions
                with ui.row().classes('w-full justify-between items-center mt-6 pt-4 border-t border-white/20'):
                    ui.label(f"📅 Posted: {format_date(job.get('posted_date'))}").classes('text-white/80')
                    
                    # Enhanced Apply Buttons
                    with ui.row().classes('space-x-3'):
                        ui.button('🔖 Save Job', on_click=lambda: ui.notify('Job saved!', type='positive')).classes('btn btn-secondary')
                        
                        if job.get('application_url'):
                            ui.button('🚀 Apply Now', 
                                    on_click=lambda: ui.navigate.to(job['application_url']),
                                    color='positive').classes('btn btn-primary px-8 py-3')
                        else:
                            ui.button('📧 Apply by Email',
                                    on_click=lambda: ui.notify(f"Send your application to: {job['contact_email']}", type='info'),
                                    color='positive').classes('btn btn-primary px-8 py-3')
        
        # Enhanced Main Content with modern cards
        with ui.row().classes('w-full gap-8'):
            # Left Column - Job Details with enhanced styling
            with ui.column().classes('flex-1 space-y-6'):
                # Job Summary with modern card
                if job.get('job_summary'):
                    with ui.card().classes('modern-card w-full p-6 animate-slide-in-right'):
                        with ui.column().classes('w-full space-y-4'):
                            with ui.row().classes('items-center space-x-2'):
                                ui.icon('description', color='primary')
                                ui.label('📋 Job Summary').classes('text-2xl font-bold text-gray-800')
                            ui.html(f"<div class='prose max-w-none text-gray-700 leading-relaxed'>{job['job_summary']}</div>")
                
                # Job Description with enhanced styling
                with ui.card().classes('modern-card w-full p-6 animate-slide-in-right'):
                    with ui.column().classes('w-full space-y-4'):
                        with ui.row().classes('items-center space-x-2'):
                            ui.icon('work_outline', color='primary')
                            ui.label('💼 Job Description').classes('text-2xl font-bold text-gray-800')
                        ui.html(f"<div class='prose max-w-none text-gray-700 leading-relaxed text-lg'>{job['description']}</div>")
                
                # Requirements with enhanced styling
                if job.get('requirements'):
                    with ui.card().classes('modern-card w-full p-6 animate-slide-in-right'):
                        with ui.column().classes('w-full space-y-4'):
                            with ui.row().classes('items-center space-x-2'):
                                ui.icon('checklist', color='warning')
                                ui.label('✅ Requirements & Qualifications').classes('text-2xl font-bold text-gray-800')
                            ui.html(f"<div class='prose max-w-none text-gray-700 leading-relaxed'>{job['requirements']}</div>")
                
                # Skills/Technologies with enhanced chips
                if job.get('skills'):
                    with ui.card().classes('modern-card w-full p-6 animate-slide-in-right'):
                        with ui.column().classes('w-full space-y-4'):
                            with ui.row().classes('items-center space-x-2'):
                                ui.icon('code', color='secondary')
                                ui.label('🛠️ Skills & Technologies').classes('text-2xl font-bold text-gray-800')
                            with ui.row().classes('flex-wrap gap-3'):
                                for skill in job['skills']:
                                    ui.chip(skill).classes('modern-chip chip-primary text-base px-4 py-2 font-medium')
            
            # Right Column - Enhanced Sidebar
            with ui.column().classes('w-96 space-y-6'):
                # Enhanced Company Card
                with ui.card().classes('modern-card w-full p-6 bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-200'):
                    with ui.column().classes('w-full space-y-4'):
                        with ui.row().classes('items-center space-x-3'):
                            ui.avatar(job['company'][0], color='primary').classes('text-white font-bold text-xl')
                            ui.label('🏢 About the Company').classes('text-xl font-bold text-gray-800')
                        
                        ui.label(job['company']).classes('text-2xl font-bold text-primary')
                        ui.label('We are a leading company in our industry, committed to innovation and excellence. Join our team and be part of something amazing!').classes('text-gray-700 leading-relaxed')
                        
                        # Company stats (mock data)
                        with ui.row().classes('w-full justify-between mt-4 pt-4 border-t border-blue-200'):
                            with ui.column().classes('text-center'):
                                ui.label('500+').classes('text-lg font-bold text-primary')
                                ui.label('Employees').classes('text-xs text-gray-600')
                            with ui.column().classes('text-center'):
                                ui.label('15+').classes('text-lg font-bold text-primary')
                                ui.label('Countries').classes('text-xs text-gray-600')
                            with ui.column().classes('text-center'):
                                ui.label('2010').classes('text-lg font-bold text-primary')
                                ui.label('Founded').classes('text-xs text-gray-600')
                
                # Enhanced Job Details Card
                with ui.card().classes('modern-card w-full p-6 bg-gradient-to-br from-green-50 to-emerald-50 border border-green-200'):
                    with ui.column().classes('w-full space-y-4'):
                        with ui.row().classes('items-center space-x-2'):
                            ui.icon('info', color='positive')
                            ui.label('📊 Job Details').classes('text-xl font-bold text-gray-800')
                        
                        detail_items = [
                            ('🏠 Workplace', 'Remote' if job.get('is_remote') else 'On-site'),
                            ('💼 Job Type', job['job_type']),
                            ('📈 Experience', job.get('experience_level', 'Not specified')),
                            ('🏷️ Category', job.get('job_category', 'Technology')),
                            ('📅 Posted', format_date(job.get('posted_date'))),
                            ('⏰ Deadline', format_date(job.get('deadline')) or 'Open until filled')
                        ]
                        
                        for label, value in detail_items:
                            with ui.row().classes('w-full justify-between items-center py-2'):
                                ui.label(label).classes('text-gray-700 font-medium')
                                ui.chip(value).classes('bg-white text-gray-800 text-sm')
                
                # Enhanced Application Card
                with ui.card().classes('modern-card w-full p-6 bg-gradient-to-br from-purple-50 to-pink-50 border border-purple-200'):
                    with ui.column().classes('w-full space-y-4'):
                        with ui.row().classes('items-center space-x-2'):
                            ui.icon('send', color='secondary')
                            ui.label('🚀 Ready to Apply?').classes('text-xl font-bold text-gray-800')
                        
                        ui.label('Take the next step in your career journey!').classes('text-gray-700 mb-4')
                        
                        if job.get('application_url'):
                            ui.button('🌐 Apply Online', 
                                     on_click=lambda: ui.navigate.to(job['application_url']),
                                     color='positive').classes('w-full btn btn-primary mb-2')
                            ui.label('or').classes('text-center text-gray-500 my-2')
                        
                        ui.button('📧 Email Application',
                                on_click=lambda: ui.notify(f"Send your application to: {job['contact_email']}", type='info'),
                                color='primary').classes('w-full btn btn-secondary')
                        
                        # Application tips
                        with ui.expansion('💡 Application Tips', icon='lightbulb').classes('w-full mt-4'):
                            ui.html('''
                            <div class="text-sm text-gray-600 space-y-2">
                                <p>• Tailor your resume to match the job requirements</p>
                                <p>• Write a compelling cover letter</p>
                                <p>• Highlight relevant experience and skills</p>
                                <p>• Follow up within a week if you don't hear back</p>
                            </div>
                            ''')
        
        # Enhanced Back Button and Share Options
        with ui.card().classes('w-full mt-8 p-4 bg-gray-50'):
            with ui.row().classes('w-full justify-between items-center'):
                ui.button('← Back to Jobs', 
                         on_click=lambda: ui.navigate.to('/jobs'),
                         color='gray').classes('btn btn-secondary')
                
                # Share buttons
                with ui.row().classes('space-x-2'):
                    ui.button('🔗 Share Job', on_click=lambda: ui.notify('Link copied to clipboard!', type='positive')).props('flat').classes('text-primary')
                    ui.button('📤 Refer Friend', on_click=lambda: ui.notify('Referral feature coming soon!', type='info')).props('flat').classes('text-secondary')