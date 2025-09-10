import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from nicegui import ui
from components.header import show_header
from components.footer import show_footer
from pages.candidate_profile import sample_candidate
from utils.file_upload import save_uploaded_file, delete_file

def save_profile(profile_data, new_avatar=None, new_resume=None):
    """Save profile data (in a real app, this would update the database)."""
    try:
        # Create a copy of the profile data to avoid modifying the original
        updated_data = profile_data.copy()
        
        # Handle avatar upload if there's a new one
        if new_avatar:
            try:
                # Save new avatar
                avatar_path = save_uploaded_file(new_avatar, 'avatars')
                if avatar_path:
                    # Delete old avatar if it exists and is not the default one
                    old_avatar = sample_candidate.get('avatar', '')
                    if old_avatar and 'default-avatar' not in old_avatar:
                        delete_file(old_avatar)
                    updated_data['avatar'] = f'/{avatar_path}'
            except Exception as e:
                ui.notify(f'Error updating profile picture: {str(e)}', type='warning')
        
        # Handle resume upload if there's a new one
        if new_resume:
            try:
                # Save new resume
                resume_path = save_uploaded_file(new_resume, 'resumes')
                if resume_path:
                    # Delete old resume if it exists
                    old_resume = sample_candidate.get('resume')
                    if old_resume:
                        delete_file(old_resume)
                    updated_data['resume'] = f'/{resume_path}'
            except Exception as e:
                ui.notify(f'Error updating resume: {str(e)}', type='warning')
        
        # Update profile data
        for key, value in updated_data.items():
            if value is not None:  # Only update non-None values
                if key in sample_candidate:
                    if isinstance(sample_candidate[key], list) and isinstance(value, list):
                        # Handle list updates (e.g., skills, preferred_work_type, languages)
                        sample_candidate[key] = [item for item in value if item]  # Remove empty strings
                    elif isinstance(sample_candidate[key], dict) and isinstance(value, dict):
                        # Handle dict updates (e.g., social_links)
                        sample_candidate[key].update({
                            k: v for k, v in value.items() if v  # Only keep non-empty values
                        })
                    else:
                        # Handle simple values
                        sample_candidate[key] = value
        
        ui.notify('Profile updated successfully!', type='positive')
        ui.navigate.to(f'/candidate-profile/{sample_candidate["id"]}')
    except Exception as e:
        ui.notify(f'Error saving profile: {str(e)}', type='negative')
        # Log the full error for debugging
        import traceback
        print(f"Error in save_profile: {traceback.format_exc()}")

def show_edit_candidate_profile_page(candidate_id: str = None):
    """Display candidate profile edit page."""
    show_header()
    
    # Use sample data for now, but filter by candidate_id if provided
    candidate = sample_candidate if str(sample_candidate.get('id', '1')) == str(candidate_id) else None
    
    if not candidate:
        with ui.column().classes('w-full h-screen flex items-center justify-center'):
            ui.label('Candidate not found').classes('text-2xl text-gray-500')
            ui.button('Back to Profile', on_click=lambda: ui.navigate.to(f'/candidate-profile/{candidate_id}'))
        return
    
    with ui.column().classes('w-full min-h-screen bg-gray-50 p-4 md:p-8'):
        # Page header
        with ui.row().classes('w-full max-w-7xl mx-auto justify-between items-center mb-8'):
            ui.label('Edit Profile').classes('text-2xl font-bold text-gray-900')
            ui.button('View Profile', on_click=lambda: ui.navigate.to(f'/candidate-profile/{candidate_id}')) \
                .props('outline')
        
        # Main form
        with ui.card().classes('w-full max-w-7xl mx-auto p-6 space-y-6'):
            # Basic Information Section
            ui.label('Basic Information').classes('text-lg font-semibold text-gray-800 border-b pb-2')
            
            # Profile Picture Upload
            with ui.column().classes('w-full items-center mb-6'):
                ui.label('Profile Picture').classes('self-start text-sm font-medium text-gray-700')
                with ui.column().classes('items-center'):
                    # Current avatar
                    ui.image(candidate['avatar']).classes('w-32 h-32 rounded-full object-cover mb-2')
                    # File upload
                    with ui.row().classes('items-center'):
                        file_upload = ui.upload(
                            label='Change Photo',
                            on_upload=lambda e: ui.notify(f'Uploaded {e.name}'),
                            max_file_size=5 * 1024 * 1024  # 5MB
                        ).props('accept=".png,.jpg,.jpeg,.gif"').classes('max-w-xs')
                        
                        # Remove photo button
                        if 'default-avatar' not in candidate.get('avatar', ''):
                            ui.button(
                                'Remove', 
                                on_click=lambda: remove_profile_picture(candidate['id']),
                                icon='delete'
                            ).props('flat dense')
            
            with ui.row().classes('w-full gap-4'):
                name = ui.input('Full Name', value=candidate.get('name', '')).classes('flex-1')
                title = ui.input('Job Title', value=candidate.get('title', '')).classes('flex-1')
            
            with ui.row().classes('w-full gap-4'):
                email = ui.input('Email', value=candidate['email']).classes('flex-1')
                phone = ui.input('Phone', value=candidate['phone']).classes('flex-1')
            
            with ui.row().classes('w-full gap-4'):
                location = ui.input('Location', value=candidate.get('location', '')).classes('flex-1')
                website = ui.input('Website', value=candidate.get('website', '')).classes('flex-1')
            
            # About Section
            ui.label('About Me').classes('text-lg font-semibold text-gray-800 border-b pb-2 mt-8')
            about = ui.textarea('', value=candidate.get('about', '')).classes('w-full').props('rows=5')
            
            # Professional Information
            ui.label('Professional Information').classes('text-lg font-semibold text-gray-800 border-b pb-2 mt-8')
            with ui.row().classes('w-full gap-4'):
                portfolio_url = ui.input('Portfolio URL', value=candidate.get('portfolio_url', '')).classes('flex-1')
                hourly_rate = ui.number('Hourly Rate ($)', value=candidate.get('hourly_rate', 0), min=0, step=5).classes('flex-1')
            
            # Work Preferences
            work_types = ['Full-time', 'Part-time', 'Contract', 'Freelance', 'Remote', 'On-site', 'Hybrid']
            ui.label('Work Preferences').classes('text-md font-medium text-gray-700 mt-4')
            with ui.row().classes('w-full flex-wrap gap-2'):
                work_type_chips = []
                for work_type in work_types:
                    is_selected = work_type in candidate.get('preferred_work_type', [])
                    chip = ui.checkbox(work_type, value=is_selected).classes('m-0')
                    work_type_chips.append((work_type, chip))
            
            # Languages
            ui.label('Languages').classes('text-md font-medium text-gray-700 mt-4')
            with ui.column().classes('w-full'):
                language_inputs = []
                for i, lang in enumerate(candidate.get('languages', [''])):
                    with ui.row().classes('w-full items-center gap-2'):
                        lang_input = ui.input(f'Language {i+1}', value=lang).classes('flex-1')
                        ui.button(icon='delete', on_click=lambda i=i: remove_language(i, language_inputs)) \
                            .props('flat dense')
                        language_inputs.append(lang_input)
                
                def add_language():
                    with ui.row().classes('w-full items-center gap-2'):
                        lang_input = ui.input(f'Language {len(language_inputs) + 1}').classes('flex-1')
                        ui.button(icon='delete', on_click=lambda i=len(language_inputs): remove_language(i, language_inputs)) \
                            .props('flat dense')
                        language_inputs.append(lang_input)
                
                ui.button('Add Language', on_click=add_language, icon='add').props('flat')
            
            # Resume Upload
            ui.label('Resume').classes('text-lg font-semibold text-gray-800 border-b pb-2 mt-8')
            resume_status = ui.row().classes('w-full items-center')
            
            with resume_status:
                if candidate.get('resume'):
                    with ui.row().classes('items-center'):
                        ui.icon('description').classes('text-blue-500')
                        ui.label('Current Resume:').classes('ml-2')
                        ui.link('Download Resume', candidate['resume']).classes('ml-2 text-blue-600 hover:underline')
                        ui.button(icon='delete', on_click=lambda: remove_resume(candidate_id)) \
                            .props('flat dense color=negative')
                else:
                    ui.label('No resume uploaded yet').classes('text-gray-500')
            
            with ui.column().classes('w-full mt-4'):
                resume_upload = ui.upload(
                    label='Upload Resume (PDF, DOC, DOCX)',
                    on_upload=lambda e: handle_resume_upload(e, resume_status, candidate_id),
                    max_file_size=10 * 1024 * 1024,  # 10MB
                    auto_upload=True
                ).props('accept=".pdf,.doc,.docx"').classes('w-full max-w-md')
            
            # Profile Picture Upload
            ui.label('Profile Picture').classes('text-lg font-semibold text-gray-800 border-b pb-2 mt-8')
            with ui.row().classes('w-full items-center'):
                # Current Avatar
                with ui.column().classes('items-center'):
                    avatar_url = candidate.get('avatar', '/static/images/default-avatar.svg')
                    avatar_img = ui.image(avatar_url).classes('w-24 h-24 rounded-full object-cover')
                    
                    # Remove button (only show if not using default avatar)
                    if 'default-avatar' not in avatar_url:
                        with ui.row().classes('mt-2'):
                            ui.button('Remove', on_click=lambda: remove_profile_picture(candidate_id)) \
                                .props('flat dense color=negative')
                
                # File Upload
                with ui.column().classes('flex-1 ml-8'):
                    file_upload = ui.upload(
                        label='Upload new photo',
                        on_upload=lambda e: handle_avatar_upload(e, avatar_img, candidate_id),
                        max_file_size=5 * 1024 * 1024,  # 5MB
                        auto_upload=True
                    ).props('accept="image/*"').classes('w-full')
                    
                    ui.label('JPG, GIF or PNG. Max size 5MB').classes('text-xs text-gray-500 mt-1')
            
            # Social Media Links
            ui.label('Social Media').classes('text-lg font-semibold text-gray-800 border-b pb-2 mt-8')
            social_platforms = [
                ('linkedin', 'LinkedIn', 'fab fa-linkedin-in'),
                ('github', 'GitHub', 'fab fa-github'),
                ('twitter', 'Twitter', 'fab fa-twitter'),
                ('dribbble', 'Dribbble', 'fab fa-dribbble'),
                ('behance', 'Behance', 'fab fa-behance'),
                ('portfolio', 'Portfolio', 'fas fa-globe'),
                ('medium', 'Medium', 'fab fa-medium'),
                ('youtube', 'YouTube', 'fab fa-youtube')
            ]
            
            social_inputs = {}
            for platform, label, icon in social_platforms:
                with ui.row().classes('w-full items-center'):
                    ui.icon(icon).classes('w-8 text-gray-500')
                    social_inputs[platform] = ui.input(
                        label, 
                        value=candidate.get('social_links', {}).get(platform, '')
                    ).classes('flex-1')
            
            # Skills Section
            ui.label('Skills').classes('text-lg font-semibold text-gray-800 border-b pb-2 mt-8')
            skills_input = ui.input('Add Skills (comma separated)').classes('w-full mb-2')
            
            # Current skills chips
            with ui.column().classes('w-full flex flex-wrap gap-2 mb-4'):
                skills_chips = []
                for skill in candidate['skills']:
                    with ui.element('div').classes('relative group'):
                        chip = ui.label(skill).classes('px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm')
                        remove_btn = ui.button(icon='close', on_click=lambda s=skill: remove_skill(s, skills_chips)) \
                            .props('flat dense round size=sm') \
                            .classes('absolute -top-2 -right-2 opacity-0 group-hover:opacity-100 bg-red-500 text-white')
                        skills_chips.append({'skill': skill, 'ui': chip, 'remove_btn': remove_btn})
            
            # Experience Section
            ui.label('Experience').classes('text-lg font-semibold text-gray-800 border-b pb-2 mt-8')
            
            for exp in candidate['experience']:
                with ui.card().classes('w-full p-4 mb-4'):
                    with ui.row().classes('w-full justify-between items-start'):
                        ui.label(exp['title']).classes('text-lg font-medium')
                        ui.button(icon='edit', on_click=lambda e=exp: edit_experience(e)) \
                            .props('flat round dense')
                    ui.label(exp['company']).classes('text-gray-700')
                    ui.label(f"{exp['duration']} • {exp['location']}").classes('text-sm text-gray-500')
            
            # Add Experience Button
            ui.button('Add Experience', on_click=add_experience) \
                .props('outline') \
                .classes('w-full md:w-auto mt-2')
            
            # Education Section
            ui.label('Education').classes('text-lg font-semibold text-gray-800 border-b pb-2 mt-8')
            
            for edu in candidate['education']:
                with ui.card().classes('w-full p-4 mb-4'):
                    with ui.row().classes('w-full justify-between items-start'):
                        ui.label(edu['degree']).classes('text-lg font-medium')
                        ui.button(icon='edit', on_click=lambda e=edu: edit_education(e)) \
                            .props('flat round dense')
                    ui.label(edu['school']).classes('text-gray-700')
                    ui.label(f"{edu['duration']} • {edu['location']}").classes('text-sm text-gray-500')
            
            # Add Education Button
            ui.button('Add Education', on_click=add_education) \
                .props('outline') \
                .classes('w-full md:w-auto mt-2')
            
            # Form Actions
            with ui.row().classes('w-full justify-end space-x-4 mt-8'):
                ui.button('Cancel', on_click=lambda: ui.navigate.to(f'/candidate-profile/{candidate_id}')) \
                    .props('flat')
                ui.button('Save Changes', on_click=lambda: save_profile({
                    'name': name.value,
                    'title': title.value,
                    'email': email.value,
                    'phone': phone.value,
                    'location': location.value,
                    'website': website.value,
                    'portfolio_url': portfolio_url.value,
                    'hourly_rate': hourly_rate.value,
                    'preferred_work_type': [wt for wt, chip in work_type_chips if chip.value],
                    'languages': [lang.value for lang in language_inputs if lang.value],
                    'about': about.value,
                    'social_links': {
                        platform: input.value 
                        for platform, input in social_inputs.items()
                        if input.value
                    }
                }, file_upload.files[0] if file_upload.files else None, 
                   resume_upload.files[0] if resume_upload.files else None)) \
                .props('unelevated') \
                .classes('bg-blue-600 text-white hover:bg-blue-700')

def remove_skill(skill, skills_chips):
    """Remove a skill from the list."""
    for i, chip in enumerate(skills_chips):
        if chip['skill'] == skill:
            chip['ui'].delete()
            if 'remove_btn' in chip:
                chip['remove_btn'].delete()
            skills_chips.pop(i)
            break

def remove_language(index, language_inputs):
    """Remove a language input field."""
    if len(language_inputs) > 1:  # Keep at least one language field
        language_inputs[index].delete()
        language_inputs.pop(index)

def handle_avatar_upload(e, avatar_img, candidate_id):
    """Handle avatar upload and update the UI."""
    try:
        # Save the uploaded file
        file_path = save_uploaded_file(e, 'avatars')
        if not file_path:
            ui.notify('Failed to save avatar', type='negative')
            return
        
        # Update the candidate's avatar
        candidate = sample_candidate if str(sample_candidate.get('id', '1')) == str(candidate_id) else None
        if candidate:
            # Delete old avatar if it exists and is not the default one
            old_avatar = candidate.get('avatar', '')
            if old_avatar and 'default-avatar' not in old_avatar:
                delete_file(old_avatar)
            
            # Update the avatar URL
            candidate['avatar'] = f'/{file_path}'
            
            # Update the image source
            avatar_img.source = candidate['avatar']
            avatar_img.update()
            
            ui.notify('Profile picture updated', type='positive')
    except Exception as e:
        ui.notify(f'Error uploading avatar: {str(e)}', type='negative')

def handle_resume_upload(e, resume_status, candidate_id):
    """Handle resume upload and update the UI."""
    try:
        # Save the uploaded file
        file_path = save_uploaded_file(e, 'resumes')
        if not file_path:
            ui.notify('Failed to save resume', type='negative')
            return
        
        # Update the candidate's resume
        candidate = sample_candidate if str(sample_candidate.get('id', '1')) == str(candidate_id) else None
        if candidate:
            # Delete old resume if it exists
            old_resume = candidate.get('resume')
            if old_resume:
                delete_file(old_resume)
            
            # Update the resume URL
            candidate['resume'] = f'/{file_path}'
            
            # Update the UI
            resume_status.clear()
            with resume_status:
                with ui.row().classes('items-center'):
                    ui.icon('description').classes('text-blue-500')
                    ui.label('Current Resume:').classes('ml-2')
                    ui.link('Download Resume', candidate['resume']).classes('ml-2 text-blue-600 hover:underline')
                    ui.button(icon='delete', on_click=lambda: remove_resume(candidate_id)) \
                        .props('flat dense color=negative')
            
            ui.notify('Resume uploaded successfully', type='positive')
    except Exception as e:
        ui.notify(f'Error uploading resume: {str(e)}', type='negative')

def remove_resume(candidate_id):
    """Remove the current resume."""
    try:
        candidate = sample_candidate if str(sample_candidate.get('id', '1')) == str(candidate_id) else None
        if not candidate or not candidate.get('resume'):
            return
        
        # Delete the resume file
        if delete_file(candidate['resume']):
            # Remove resume from profile
            candidate['resume'] = None
            ui.notify('Resume removed', type='info')
            
            # Refresh the page to update the UI
            ui.navigate.to(f'/candidate-profile/{candidate_id}/edit')
    except Exception as e:
        ui.notify(f'Error removing resume: {str(e)}', type='negative')

def remove_profile_picture(candidate_id):
    """Remove the current profile picture and set a default one."""
    try:
        candidate = sample_candidate if str(sample_candidate.get('id', '1')) == str(candidate_id) else None
        if not candidate:
            return
        
        # Delete the old avatar file if it exists and is not the default one
        old_avatar = candidate.get('avatar', '')
        if old_avatar and 'default-avatar' not in old_avatar:
            if delete_file(old_asset_path=old_avatar):
                # Only update if file was successfully deleted
                candidate['avatar'] = '/static/images/default-avatar.svg'
                ui.notify('Profile picture removed', type='info')
                # Refresh the page to update the UI
                ui.navigate.to(f'/candidate-profile/{candidate_id}/edit')
    except Exception as e:
        ui.notify(f'Error removing profile picture: {str(e)}', type='negative')

def add_experience():
    """Open dialog to add new experience."""
    with ui.dialog() as dialog, ui.card():
        with ui.column().classes('w-96 p-4 space-y-4'):
            ui.label('Add Experience').classes('text-xl font-semibold')
            
            title = ui.input('Job Title').classes('w-full')
            company = ui.input('Company').classes('w-full')
            
            with ui.row().classes('w-full gap-2'):
                start_date = ui.date('Start Date').classes('flex-1')
                end_date = ui.date('End Date').classes('flex-1')
            
            current_job = ui.checkbox('I currently work here')
            location = ui.input('Location').classes('w-full')
            description = ui.textarea('Description').classes('w-full').props('rows=3')
            
            with ui.row().classes('w-full justify-end space-x-2'):
                ui.button('Cancel', on_click=dialog.close).props('flat')
                ui.button('Save', on_click=lambda: save_experience({
                    'title': title.value,
                    'company': company.value,
                    'start_date': start_date.value,
                    'end_date': end_date.value if not current_job.value else 'Present',
                    'location': location.value,
                    'description': description.value
                }, dialog))
    
    dialog.open()

def save_experience(exp_data, dialog):
    """Save experience data."""
    # In a real app, you would save this to a database
    dialog.close()
    ui.notify('Experience added successfully!', type='positive')

def edit_experience(exp):
    """Open dialog to edit experience."""
    with ui.dialog() as dialog, ui.card():
        with ui.column().classes('w-96 p-4 space-y-4'):
            ui.label('Edit Experience').classes('text-xl font-semibold')
            
            title = ui.input('Job Title', value=exp.get('title', '')).classes('w-full')
            company = ui.input('Company', value=exp.get('company', '')).classes('w-full')
            
            with ui.row().classes('w-full gap-2'):
                start_date = ui.date('Start Date', value=exp.get('start_date', '')).classes('flex-1')
                end_date = ui.date('End Date', value=exp.get('end_date', '')).classes('flex-1')
            
            current_job = ui.checkbox('I currently work here', value=exp.get('current', False))
            location = ui.input('Location', value=exp.get('location', '')).classes('w-full')
            description = ui.textarea('Description', value=exp.get('description', '')).classes('w-full').props('rows=3')
            
            with ui.row().classes('w-full justify-between'):
                ui.button('Delete', on_click=lambda: delete_experience(exp, dialog)) \
                    .props('flat color=negative')
                
                with ui.row().classes('space-x-2'):
                    ui.button('Cancel', on_click=dialog.close).props('flat')
                    ui.button('Save', on_click=lambda: update_experience(exp, {
                        'title': title.value,
                        'company': company.value,
                        'start_date': start_date.value,
                        'end_date': end_date.value if not current_job.value else 'Present',
                        'location': location.value,
                        'description': description.value
                    }, dialog)) \
                    .props('unelevated')
    
    dialog.open()

def update_experience(exp, new_data, dialog):
    """Update experience data."""
    # In a real app, you would update this in the database
    exp.update(new_data)
    dialog.close()
    ui.notify('Experience updated successfully!', type='positive')

def delete_experience(exp, dialog):
    """Delete experience."""
    # In a real app, you would remove this from the database
    dialog.close()
    ui.notify('Experience deleted successfully!', type='positive')

def add_education():
    """Open dialog to add new education."""
    with ui.dialog() as dialog, ui.card():
        with ui.column().classes('w-96 p-4 space-y-4'):
            ui.label('Add Education').classes('text-xl font-semibold')
            
            degree = ui.input('Degree').classes('w-full')
            school = ui.input('School').classes('w-full')
            
            with ui.row().classes('w-full gap-2'):
                start_year = ui.input('Start Year').classes('flex-1')
                end_year = ui.input('End Year').classes('flex-1')
            
            current_school = ui.checkbox('I currently study here')
            location = ui.input('Location').classes('w-full')
            
            with ui.row().classes('w-full justify-end space-x-2'):
                ui.button('Cancel', on_click=dialog.close).props('flat')
                ui.button('Save', on_click=lambda: save_education({
                    'degree': degree.value,
                    'school': school.value,
                    'start_year': start_year.value,
                    'end_year': end_year.value if not current_school.value else 'Present',
                    'location': location.value
                }, dialog))
    
    dialog.open()

def save_education(edu_data, dialog):
    """Save education data."""
    # In a real app, you would save this to a database
    dialog.close()
    ui.notify('Education added successfully!', type='positive')
