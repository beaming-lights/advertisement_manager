from nicegui import ui

# Modern color palette
PRIMARY_COLOR = "#4F46E5"  # Indigo
SECONDARY_COLOR = "#10B981"  # Emerald
ACCENT_COLOR = "#F59E0B"  # Amber
DARK_COLOR = "#1F2937"
LIGHT_COLOR = "#F9FAFB"

# Modern gradient text class
gradient_text = "bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-green-500"

def show_hero_section():
    # Hero section with proper containment
    with ui.column().classes("w-full relative min-h-[90vh] flex items-center overflow-hidden"):
        # Background image container
        with ui.element('div').classes("absolute inset-0 w-full h-full -z-10 overflow-hidden"):
            # Background image
            ui.image("https://images.pexels.com/photos/3756681/pexels-photo-3756681.jpeg") \
                .classes("w-full object-cover")
            
            # Dark overlay for better text readability
            ui.element('div').classes("absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-black/20")
        
        # Decorative elements container
        with ui.column().classes("absolute inset-0 -z-10 overflow-visible"):
            # Decorative shapes - positioned within container bounds
            with ui.element('div').classes(f"absolute top-[20%] -left-10 w-48 h-48 rounded-full bg-{PRIMARY_COLOR[1:]}/5 blur-2xl"):
                pass
            with ui.element('div').classes(f"absolute bottom-[30%] -right-10 w-60 h-60 rounded-full bg-{SECONDARY_COLOR[1:]}/5 blur-2xl"):
                pass
        
        # Main content with proper spacing and containment
        with ui.row().classes("w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-20 justify-center") as hero_content:
            # Main content container
            with ui.column().classes("w-full max-w-4xl mx-auto text-center px-4 space-y-8 text-white flex flex-col items-center"):
                # Badge
                with ui.row().classes("inline-flex items-center space-x-2 bg-white/80 backdrop-blur-sm px-4 py-2 rounded-full border border-gray-200 shadow-sm mx-auto"):
                    ui.icon("rocket_launch", size="sm", color=PRIMARY_COLOR)
                    ui.label("Join 10,000+ professionals").classes("text-sm font-medium text-gray-700")
                
                # Main heading with gradient text
                with ui.column().classes("items-center w-full"):
                    ui.label("Find Your Dream").classes("text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-black leading-tight text-white w-full")
                    ui.label("Job Today").classes(f"text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-black leading-tight text-white mb-6 w-full")
                
                # Subheading
                ui.label(
                    "Connect with top companies and land your next career opportunity. "
                    "We've helped over 50,000 professionals find their perfect match."
                ).classes("text-lg text-white/90 max-w-2xl mx-auto leading-relaxed mb-8")
                
                # Modern search bar with glass effect
                with ui.column().classes("w-full max-w-2xl mx-auto space-y-4 mb-8"):
                    with ui.row().classes(
                        "w-full items-center bg-white/10 backdrop-blur-md rounded-xl shadow-lg p-1 border border-white/20"
                    ).style("box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);"):
                        with ui.row().classes("flex-1 items-center px-4 py-3"):
                            ui.icon("search", size="sm", color="white").classes("mr-3")
                            ui.input(
                                placeholder="Job title, keywords, or company"
                            ).classes(
                                "flex-1 bg-transparent border-0 text-white placeholder-white/70 focus:outline-none focus:ring-0 text-base"
                            ).props('readonly')

                        with ui.row().classes("h-8 w-px bg-white/30 mx-2"):
                            pass

                        with ui.row().classes("w-64 items-center px-4 py-3"):
                            ui.icon("location_on", size="sm", color="white").classes("mr-3")
                            ui.input(
                                placeholder="Location (Remote/Anywhere)"
                            ).classes(
                                "flex-1 bg-transparent border-0 text-white placeholder-white focus:outline focus:ring-0 text-base"
                            ).props('')

                        ui.button(
                            "SEARCH",
                            on_click=lambda: ui.navigate.to("/jobs")
                        ).style(f"background-color: {PRIMARY_COLOR} !important")\
                         .classes("hover:opacity-90 text-white font-semibold px-6 py-3 rounded-xl "
                                "min-h-[48px] text-sm transition-all duration-300 transform hover:scale-105 shadow-lg")
                
                # # Trusted by section
                # with ui.row().classes("w-full max-w-2xl pt-2 items-center text-white/80 text-sm"):
                #     ui.label("Trusted by:").classes("mr-4 text-white/70")
                #     with ui.row().classes("space-x-6 items-center"):
                #         for logo in ["work", "business", "apartment", "corporate_fare"]:
                #             ui.icon(logo, size="md").classes("opacity-70 hover:opacity-100 transition-opacity")
                
                # Trusted by section with company logos
                with ui.column().classes("mt-12 items-center w-full"):
                    ui.label("Trusted by leading corporations").classes("text-sm text-white-500 mb-4 text-center")
                    with ui.row().classes("flex flex-wrap justify-center items-center gap-6 md:gap-10 opacity-80"):
                        companies = ["Google", "Microsoft", "Amazon", "Netflix", "Adobe"]
                        for company in companies:
                            with ui.element('div').classes("text-white-700 font-medium text-lg"):
                                ui.label(company)
            
            # Right side - Professional workspace image with decorative elements
            with ui.column().classes("hidden lg:flex flex-1 justify-center items-start relative pl-12 pt-12"):
                # Main card with image
                with ui.column().classes("relative z-10 w-full max-w-md group"):
                    # Main image with 3D effect
                    with ui.element('div').classes("relative transform transition-all duration-500 group-hover:scale-105"):
                        # Gradient overlay container
                        with ui.element('div').classes("absolute inset-0 rounded-2xl overflow-hidden"):
                            # Main hero image
                            ui.image("https://images.unsplash.com/photo-1521737711867-a3b9057faa50?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80").classes(
                                "w-full h-[500px] object-cover rounded-2xl transform rotate-1 group-hover:rotate-0 "
                                "transition-all duration-500"
                            )
                            # Gradient overlay for better text readability
                            ui.element('div').classes(
                                "absolute inset-0 bg-gradient-to-t from-black/40 via-black/10 to-transparent "
                                "rounded-2xl"
                            )
                        
                        # Floating badge with rating
                        with ui.element('div').classes(
                            "absolute -top-4 -right-4 bg-white/95 backdrop-blur-sm rounded-full p-3 shadow-xl "
                            "border border-gray-100 transform transition-all duration-300 hover:scale-110"
                        ):
                            with ui.row().classes("items-center space-x-2"):
                                ui.icon("star", color="#F59E0B").classes("text-xl")
                                ui.label("4.9/5.0").classes("font-bold text-gray-900")
                    
                    # Floating card 1 (Job Seeker)
                    with ui.element('div').classes(
                        "absolute -left-10 -bottom-10 w-64 bg-white rounded-xl p-4 shadow-xl "
                        "transform -rotate-6 group-hover:rotate-0 transition-transform duration-500"
                    ):
                        with ui.row().classes("items-center space-x-3"):
                            ui.avatar("JS", color=PRIMARY_COLOR, text_color="white")
                            with ui.column().classes("space-y-1"):
                                ui.label("John S.").classes("font-semibold text-gray-900")
                                ui.label("Found job as Senior Designer").classes("text-xs text-gray-500")
                        ui.linear_progress(0.8, show_value=False, size="4px").classes("mt-2")
                    
                    # Floating card 2 (Company)
                    with ui.element('div').classes(
                        "absolute -right-10 top-1/3 w-56 bg-white rounded-xl p-4 shadow-xl "
                        "transform rotate-3 group-hover:rotate-0 transition-transform duration-500"
                    ):
                        with ui.row().classes("items-center space-x-3"):
                            ui.avatar("AC", color=SECONDARY_COLOR, text_color="white")
                            with ui.column().classes("space-y-1"):
                                ui.label("Acme Corp").classes("font-semibold text-gray-900")
                                ui.label("Hiring 10+ positions").classes("text-xs text-gray-500")
                        ui.linear_progress(0.6, show_value=False, size="4px").classes("mt-2")
                
                # Decorative elements
                with ui.element('div').classes("absolute -bottom-20 -right-20 w-64 h-64 rounded-full bg-indigo-100/50 blur-3xl -z-10"):
                    pass

        # Features Section
        with ui.column().classes("w-full bg-gradient-to-b from-white to-gray-50 py-24 relative overflow-hidden"):
            # Decorative elements
            with ui.element('div').classes("absolute inset-0 -z-10"):
                with ui.element('div').classes("absolute -top-40 -right-40 w-80 h-80 bg-indigo-100 rounded-full blur-3xl opacity-50"):
                    pass
                with ui.element('div').classes("absolute -bottom-40 -left-40 w-96 h-96 bg-blue-100 rounded-full blur-3xl opacity-50"):
                    pass
            
            with ui.column().classes("w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"):
                # Section Header with animated underline
                with ui.column().classes("text-center max-w-3xl mx-auto mb-16 relative"):
                    ui.label("WHY CHOOSE US").classes(
                        "text-sm font-semibold tracking-widest bg-clip-text text-transparent bg-gradient-to-r from-green-500 to-blue-500 mb-4"
                    )
                    with ui.column().classes("relative inline-block"):
                        ui.label("Everything You Need to Succeed").classes(
                            "text-3xl sm:text-4xl md:text-5xl font-bold text-gray-900 mb-4 leading-tight"
                        )
                        ui.element('div').classes(
                            "absolute -bottom-2 left-1/2 transform -translate-x-1/2 w-24 h-1.5 bg-gradient-to-r from-green-500 to-blue-500 "
                            "transition-all duration-500 hover:w-32"
                        )
                    ui.label(
                        "We've built an ecosystem of tools and services to help you find your dream job "
                        "and take your career to new heights."
                    ).classes("text-lg text-gray-600 mt-4")

                # Modern Features Grid
                with ui.row().classes("grid grid-cols-1 md:grid-cols-3 gap-8 mt-8"):
                    features = [
                        {
                            "icon": "search_off",
                            "title": "Smart Job Matching",
                            "desc": "Our AI-powered algorithm matches you with the perfect jobs based on your preferences.",
                            "color": "indigo"
                        },
                        {
                            "icon": "verified_user",
                            "title": "Verified Companies",
                            "desc": "Connect with trusted employers who are actively hiring and verified by our team.",
                            "color": "emerald"
                        },
                        {
                            "icon": "rocket_launch",
                            "title": "Quick Apply",
                            "desc": "Apply to multiple jobs in seconds with your pre-filled profile and one-click applications.",
                            "color": "amber"
                        }
                    ]

                    for feature in features:
                        with ui.column().classes(
                            "group bg-white rounded-2xl p-8 text-left transition-all duration-500 shadow-xl "
                            "hover:shadow-xl hover:-translate-y-2 border border-gray-100 relative overflow-hidden"
                        ):
                            # Animated border on hover
                            with ui.element('div').classes(
                                f"absolute top-0 left-0 w-1 h-0 bg-gradient-to-b from-{feature['color']}-500 to-{feature['color']}-600 "
                                "transition-all duration-500 group-hover:h-full"
                            ):
                                pass
                            
                            with ui.row().classes("flex items-start space-x-4"):
                                # Icon with gradient background
                                with ui.element('div').classes(
                                    f"flex-shrink-0 w-14 h-14 rounded-xl bg-gradient-to-br from-{feature['color']}-100 to-{feature['color']}-50 "
                                    "flex items-center justify-center group-hover:scale-110 transition-transform duration-300"
                                ):
                                    ui.icon(feature["icon"], size="1.75rem").classes(f"text-{feature['color']}-600")
                                
                                with ui.column().classes("space-y-2"):
                                    ui.label(feature["title"]).classes(
                                        "text-xl font-bold text-gray-900 group-hover:text-gray-800 transition-colors"
                                    )
                                    ui.label(feature["desc"]).classes(
                                        "text-gray-600 leading-relaxed text-sm"
                                    )
                            
                            # Learn more link with arrow animation
                            with ui.row().classes("mt-6 flex items-center space-x-1 group-hover:translate-x-1 transition-transform duration-300"):
                                ui.label("Learn more").classes(
                                    f"text-sm font-medium text-{feature['color']}-600 cursor-pointer"
                                )
                                ui.icon("arrow_forward", size="1rem").classes(f"text-{feature['color']}-600")

        # # How It Works Section with Timeline
        # with ui.column().classes("w-full bg-white py-24 relative"):
        #     # Decorative elements
        #     with ui.element('div').classes("absolute inset-0 -z-10"):
        #         with ui.element('div').classes("absolute -top-40 -right-40 w-80 h-80 bg-indigo-100 rounded-full blur-3xl opacity-50"):
        #             pass
        #         with ui.element('div').classes("absolute -bottom-40 -left-40 w-96 h-96 bg-blue-100 rounded-full blur-3xl opacity-50"):
        #             pass
            
            # with ui.column().classes("w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"):
            #     # Section Header
            #     with ui.column().classes("text-center max-w-3xl mx-auto mb-20"):
            #         ui.label("HOW IT WORKS").classes(
            #             "text-sm font-semibold tracking-widest bg-clip-text text-transparent bg-gradient-to-r from-indigo-500 to-purple-500 mb-4"
            #         )
            #         ui.label("Get Hired in 3 Simple Steps").classes(
            #             "text-3xl sm:text-4xl md:text-5xl font-bold text-gray-900 mb-6 leading-tight"
            #         )
            #         ui.label(
            #             "Our streamlined process makes it easy to find and land your dream job. "
            #             "From creating your profile to getting hired, we've got you covered every step of the way."
            #         ).classes("text-lg text-gray-600")
                
                # # Timeline
                # with ui.column().classes("relative mt-16"):
                #     # Timeline line
                #     with ui.element('div').classes(
                #         "w=full absolute left-1/2 h-full w-0.5 bg-gradient-to-b from-indigo-200 to-blue-200 "
                #         "transform -translate-x-1/2"
                #     ):
                #         pass
                    
                #     # Steps
                #     steps = [
                #         {
                #             "number": "01",
                #             "title": "Create Your Profile",
                #             "description": "Sign up in 30 seconds and create a standout profile that highlights your skills, experience, and career goals.",
                #             "icon": "person_add",
                #             "color": "indigo"
                #         },
                #         {
                #             "number": "02",
                #             "title": "Find Your Dream Job",
                #             "description": "Browse thousands of curated job listings or let our AI match you with the perfect opportunities.",
                #             "icon": "search",
                #             "color": "blue"
                #         },
                #         {
                #             "number": "03",
                #             "title": "Apply & Get Hired",
                #             "description": "Submit your application with one click and track your progress through the hiring process.",
                #             "icon": "check_circle",
                #             "color": "emerald"
                #         }
                #     ]
                    
                #     for i, step in enumerate(steps):
                #         with ui.row().classes(
                #             f"relative w-full mb-16 md:mb-24 last:mb-0 flex flex-col md:flex-row "
                #             f"{'md:flex-row-reverse' if i % 2 == 0 else ''} items-center"
                #         ):
                #             # Left/Right content based on step number
                #             with ui.column().classes(
                #                 f"w-full md:w-1/2 px-4 order-2 md:order-1 "
                #                 f"{'md:pr-16 md:text-right' if i % 2 == 0 else 'md:pl-16'}"
                #             ):
                #                 ui.label(step["title"]).classes(
                #                     "text-2xl font-bold text-gray-900 mb-3"
                #                 )
                #                 ui.label(step["description"]).classes(
                #                     "text-gray-600 mb-4"
                #                 )
                #                 with ui.row().classes("flex items-center space-x-2"):
                #                     ui.label("Learn more").classes(
                #                         f"font-medium text-{step['color']}-600 cursor-pointer hover:underline"
                #                     )
                #                     ui.icon("arrow_forward", size="1rem").classes(f"text-{step['color']}-600")
                            
                #             # Center circle
                #             with ui.column().classes(
                #                 "flex-shrink-0 w-20 h-20 rounded-full bg-white border-4 border-white shadow-lg "
                #                 f"flex items-center justify-center z-10 order-1 md:order-2 mb-6 md:mb-0"
                #             ):
                #                 with ui.element('div').classes(
                #                     f"w-16 h-16 rounded-full bg-gradient-to-br from-{step['color']}-500 to-{step['color']}-600 "
                #                     "flex items-center justify-center text-white"
                #                 ):
                #                     ui.icon(step["icon"], size="2rem")
                            
                #             # # Step number (desktop only)
                #             # with ui.column().classes(
                #             #     f"hidden md:flex absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2 "
                #             #     f"w-12 h-12 rounded-full bg-white border-4 border-white shadow-lg items-center justify-center z-10"
                #             # ):
                #             #     ui.label(step["number"]).classes(
                #             #         f"text-sm font-bold text-{step['color']}-600"
                #             #     )

        # CTA Section
        with ui.column().classes("w-full bg-emerald-800 py-5"):
            with ui.column().classes("w-full max-w-4xl mx-auto px-4 text-center items-center mt-6"):
                ui.label("Ready to Get Started?").classes(
                    "text-3xl md:text-5xl font-bold text-white mb-3"
                )
                ui.label(
                    "Join thousands of professionals who found their dream jobs with us."
                ).classes("text-lg text-emerald-100 mb-8 max-w-2xl mx-auto")
                with ui.row().classes("flex flex-col sm:flex-row gap-4"):
                    ui.button(
                        "Find Jobs",
                        icon="search",
                        on_click=lambda: ui.navigate.to("/jobs"),
                    ).style(f"background-color: {PRIMARY_COLOR} !important")\
                     .classes("hover:opacity-90 text-white font-medium px-8 py-3 rounded-lg "
                            "shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-300")
                    ui.button(
                        "Post a Job",
                        icon="post_add",
                        on_click=lambda: ui.navigate.to("/post-job"),
                    ).style(f"color: {PRIMARY_COLOR} !important; border-color: {PRIMARY_COLOR} !important")\
                     .classes("bg-white hover:bg-opacity-10 hover:text-white border-2 font-medium px-8 py-3 "
                            "rounded-lg shadow-sm hover:shadow-md transition-all duration-300")
                # Trust indicators
                with ui.row().classes("mt-12 flex flex-wrap justify-center items-center gap-6 text-white/80 text-sm"):
                    with ui.row().classes("flex items-center"):
                        for _ in range(5):
                            ui.icon("star", size="1.25rem", color="#F59E0B").classes("text-yellow-400 -mx-0.5")
                        ui.label("4.9/5.0 from 2,000+ reviews").classes("ml-1")
                    
                    with ui.row().classes("hidden sm:flex items-center space-x-2"):
                        ui.icon("groups", size="1.25rem")
                        ui.label("50,000+ professionals hired")
                    
                    with ui.row().classes("hidden md:flex items-center space-x-2"):
                        ui.icon("schedule", size="1.25rem")
                        ui.label("Get matched in under 5 minutes")