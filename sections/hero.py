from nicegui import ui

# Hero image URL - using a direct URL to a professional image
HERO_IMAGE = "https://images.pexels.com/photos/3756681/pexels-photo-3756681.jpeg"

def show_hero_section():
    with ui.column().classes("w-full relative min-h-[500px] md:min-h-[600px] flex items-center overflow-hidden"):
        # Hero image as background
        with ui.column().classes("absolute inset-0 -z-10 overflow-hidden"):
            ui.image(HERO_IMAGE).classes("w-full h-full object-cover")
            # Dark overlay for better text readability with gradient
            ui.element('div').classes("absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-black/20")
        
        # Main Hero Content
        with ui.row().classes("w-full max-w-7xl mx-auto px-4 py-16 md:py-24 lg:py-32"):
            # Left side - Content
            with ui.column().classes("w-full lg:w-2/3 space-y-8 text-white"):
                with ui.column().classes("space-y-6"):
                    ui.label("Find Your Dream Job Today").classes(
                        "text-4xl md:text-5xl lg:text-6xl font-bold leading-tight tracking-tight animate-fade-in"
                    )
                    ui.label(
                        "Join thousands of professionals who found their perfect match through JobCamp. "
                        "Your next career opportunity is just a click away."
                    ).classes("text-lg md:text-xl text-white/90 leading-relaxed max-w-2xl")

                    # Modern search bar with glass effect
                    with ui.column().classes("w-full max-w-2xl space-y-4"):
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
                                    "flex-1 bg-transparent border-0 text-white placeholder-white/70 focus:outline-none focus:ring-0 text-base"
                                ).props('readonly')

                            ui.button(
                                "SEARCH",
                                on_click=lambda: None
                            ).classes(
                                "bg-white text-emerald-600 hover:bg-gray-100 font-semibold px-6 py-3 rounded-xl min-h-[48px] text-sm cursor-not-allowed transition-all duration-300 transform hover:scale-105"
                            ).props('disable')

                    # Trusted by text with company logos
                    with ui.row().classes("w-full max-w-2xl pt-4 items-center text-white/80 text-sm"):
                        ui.label("Trusted by:").classes("mr-4")
                        with ui.row().classes("space-x-6 items-center"):
                            for logo in ["work", "business", "apartment", "corporate_fare"]:
                                ui.icon(logo, size="md").classes("opacity-70 hover:opacity-100 transition-opacity")

                # Right side - Professional workspace image with decorative elements
                with ui.column().classes("hidden lg:flex flex-1 justify-center items-center relative pl-12"):
                    # Main image container with floating animation and 3D effect
                    with ui.column().classes("relative z-10 w-full max-w-md"):
                        # Main image with perspective and 3D transform
                        with ui.element('div').classes("relative transform transition-all duration-700 hover:scale-105"):
                            # Main professional workspace image
                            ui.image("https://images.unsplash.com/uploads/141103282695035fa1380/95cdfeef?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y29udGFjdCUyMGZvcm18ZW58MHx8MHx8fDA%3D")\
                                .classes("w-full h-auto rounded-2xl shadow-2xl border-4 border-white/30 transform hover:rotate-1 transition-transform duration-500")
                        
                        # Decorative elements with floating animation
                        with ui.element('div').classes("absolute -bottom-6 -right-6 w-32 h-32 bg-yellow-400/30 rounded-2xl -z-10 rotate-12 animate-float-slow"):
                            pass
                        
                        # Team collaboration image overlay (smaller, positioned on top)
                        with ui.element('div').classes("absolute -top-10 -left-10 w-48 h-48 bg-white/90 backdrop-blur-sm rounded-2xl p-2 shadow-lg border border-white/20"):
                            ui.image("https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80")\
                                .classes("w-full h-full object-cover rounded-lg")
                    
                    # Floating elements for visual interest with different animation delays
                    with ui.element('div').classes("absolute -bottom-16 -left-16 w-24 h-24 bg-blue-400/20 rounded-full animate-pulse-slow"):
                        pass
                    with ui.element('div').classes("absolute -top-10 -right-10 w-40 h-40 bg-purple-400/15 rounded-full animate-pulse"):
                        pass
                    with ui.element('div').classes("absolute top-1/3 -right-20 w-20 h-20 bg-emerald-400/20 rounded-full animate-pulse-slower"):
                        pass
                with ui.column().classes("hidden lg:flex flex-1 justify-center"):
                    with ui.column().classes("relative"):
                        # Decorative elements
                        with ui.row().classes(
                            "absolute -top-6 -left-6 w-32 h-32 bg-emerald-100 rounded-full -z-10"
                        ):
                            pass
                        with ui.row().classes(
                            "absolute -bottom-6 -right-6 w-40 h-40 bg-gray-800 rounded-full -z-10"
                        ):
                            pass
                        # Main image with shadow and border
                        ui.image(
                            "https://images.unsplash.com/photo-1521737711867-a3b9057faa50?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
                        ).classes(
                            "w-full h-[400px] object-cover rounded-2xl shadow-2xl border-8 border-white transform rotate-1 hover:rotate-0 transition-transform duration-300"
                        )

        # Features Section
        with ui.column().classes("w-full bg-white py-16 md:py-24"):
            with ui.column().classes("w-full max-w-7xl mx-auto px-4"):
                # Section Header
                with ui.column().classes("text-center max-w-4xl mx-auto mb-16"):
                    ui.label("Why Choose Us").classes(
                        "text-sm font-semibold text-emerald-600 mb-3 tracking-wider"
                    )
                    ui.label("Everything You Need to Succeed").classes(
                        "text-3xl md:text-4xl lg:text-5xl font-bold text-gray-900 mb-6 leading-tight"
                    )
                    ui.label(
                        "We provide the tools and resources to help you find your dream job and take your career to the next level."
                    ).classes("text-lg text-gray-600")

                # Features Grid
                with ui.row().classes("w-full grid grid-cols-1 md:grid-cols-3 gap-8"):
                    features = [
                        (
                            "trending_up",
                            "Advanced Search",
                            "Find the perfect job with our powerful search filters and AI recommendations.",
                        ),
                        (
                            "verified_user",
                            "Trusted Companies",
                            "Connect with top employers and startups looking for talent like you.",
                        ),
                        (
                            "rocket_launch",
                            "Quick Apply",
                            "Apply to multiple jobs with just one click using your profile.",
                        ),
                    ]

                    for icon, title, desc in features:
                        with ui.column().classes(
                            "group bg-white rounded-2xl p-8 text-center hover:shadow-xl transition-all duration-300 border border-gray-100"
                        ):
                            with ui.row().classes(
                                "mx-auto w-16 h-16 rounded-full bg-emerald-50 flex items-center justify-center mb-6 group-hover:bg-emerald-100 transition-colors"
                            ):
                                ui.icon(icon, size="1.75rem", color="emerald-600")
                            ui.label(title).classes(
                                "text-xl font-bold text-gray-900 mb-4"
                            )
                            ui.label(desc).classes("text-gray-600 leading-relaxed")

        # How It Works Section
        with ui.column().classes("w-full bg-gray-50 py-16 md:py-24"):
            with ui.column().classes("w-full max-w-7xl mx-auto px-4"):
                with ui.column().classes("text-center max-w-4xl mx-auto mb-16"):
                    ui.label("How It Works").classes(
                        "text-sm font-semibold text-emerald-600 mb-3 tracking-wider"
                    )
                    ui.label("Get Hired in 3 Simple Steps").classes(
                        "text-3xl md:text-4xl lg:text-5xl font-bold text-gray-900 mb-6 leading-tight"
                    )

                with ui.row().classes("w-full grid grid-cols-1 md:grid-cols-3 gap-8"):
                    steps = [
                        (
                            "1",
                            "Create Your Profile",
                            "Sign up and build your professional profile to stand out to employers.",
                        ),
                        (
                            "2",
                            "Find Your Dream Job",
                            "Browse thousands of job listings and get matched with the best opportunities.",
                        ),
                        (
                            "3",
                            "Apply & Get Hired",
                            "Submit your application and start your new career journey.",
                        ),
                    ]

                    for num, title, desc in steps:
                        with ui.column().classes("relative group"):
                            with ui.row().classes(
                                "absolute -top-4 -left-4 w-8 h-8 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center font-bold text-sm"
                            ):
                                ui.label(num)
                            with ui.column().classes(
                                "bg-white p-8 rounded-2xl h-full border border-gray-100 group-hover:shadow-lg transition-all duration-300"
                            ):
                                ui.label(title).classes(
                                    "text-xl font-bold text-gray-900 mb-3"
                                )
                                ui.label(desc).classes("text-gray-600")

        # CTA Section
        with ui.column().classes(
            "w-full bg-gradient-to-r from-emerald-600 to-gray-800 py-16 md:py-24"
        ):
            with ui.column().classes("w-full max-w-4xl mx-auto px-4 text-center"):
                ui.label("Ready to Get Started?").classes(
                    "text-3xl md:text-4xl font-bold text-white mb-6"
                )
                ui.label(
                    "Join thousands of professionals who found their dream jobs with us."
                ).classes("text-lg text-emerald-100 mb-8 max-w-2xl mx-auto")
                with ui.row().classes("flex flex-col sm:flex-row gap-4 justify-center"):
                    ui.button(
                        "Create Free Account",
                        on_click=lambda: ui.navigate.to("/signup"),
                    ).classes(
                        "bg-white text-emerald-700 hover:bg-gray-100 px-8 py-3 rounded-lg font-semibold transition-colors"
                    )
                    ui.button(
                        "Browse Jobs", on_click=lambda: ui.navigate.to("/jobs")
                    ).classes(
                        "bg-transparent border-2 border-white text-white hover:bg-white/10 px-8 py-3 rounded-lg font-semibold transition-colors"
                    )
