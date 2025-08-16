# # from nicegui import ui

# # # Set page title
# # ui.page_title('Muhammad Saim Imran - AI Engineer Portfolio')

# # # Background Gradient and Fonts
# # ui.add_head_html("""
# #     <style>
# #         body {
# #             background: linear-gradient(135deg, #1e3c72, #2a5298, #3a6073);
# #             color: white;
# #             font-family: 'Segoe UI', sans-serif;
# #         }
# #         h1, h2, h3 {
# #             color: #f9d423;
# #         }
# #         .card {
# #             background-color: rgba(255, 255, 255, 0.1);
# #             padding: 20px;
# #             border-radius: 10px;
# #             margin: 10px 0;
# #         }
# #         .highlight {
# #             color: #00e5ff;
# #         }
# #         img.profile {
# #             width: 180px;
# #             height: 180px;
# #             border-radius: 50%;
# #             border: 4px solid #f9d423;
# #             object-fit: cover;
# #         }
# #     </style>
# # """)

# # # Top Section with name and profile pic
# # with ui.row().classes('items-center justify-center q-mt-xl'):
# #     with ui.column().classes('items-center'):
# #         ui.image('https://avatars.githubusercontent.com/u/139707770?v=4').classes('profile')  # Replace with personal photo URL if you like
# #         ui.label('Muhammad Saim Imran').classes('text-3xl text-bold text-yellow')
# #         ui.label('AI Engineer | Generative AI Expert | Data Scientist').classes('text-lg text-grey-3')

# # # About Section
# # with ui.column().classes('card'):
# #     ui.label('About Me').classes('text-2xl text-bold')
# #     ui.markdown("""
# #         Hi! I'm **Muhammad Saim Imran**, an 18-year-old passionate **AI Engineer** based in **Lahore, Pakistan**.  
# #         I specialize in **Generative AI**, **Advanced Python Programming**, and **Data Science**.  
# #         I love building intelligent systems that solve real-world problems.
# #     """)

# # # Skills Section
# # with ui.column().classes('card'):
# #     ui.label('Skills').classes('text-2xl text-bold')
# #     ui.markdown("""
# #     - ✅ **Advanced Python Programming**
# #     - 🤖 **Generative AI Expert**
# #     - 📊 **Data Science & Machine Learning**
# #     - 🧠 AI Engineering
# #     """)

# # # Contact Section
# # with ui.column().classes('card'):
# #     ui.label('Contact Info').classes('text-2xl text-bold')
# #     ui.markdown(f"""
# #     - 📞 Phone: +92 336 4665741  
# #     - 📧 Email: [saimimranalpine@gmail.com](mailto:saimimranalpine@gmail.com)  
# #     - 🌍 Location: Lahore, Pakistan  
# #     - 💻 GitHub: [Saimcodes-cloud](https://github.com/Saimcodes-cloud)
# #     """)

# # # Footer
# # with ui.footer().classes('text-center q-mt-xl'):
# #     ui.label('© 2025 Muhammad Saim Imran. All rights reserved.').classes('text-grey-4')

# # ui.run(title='Muhammad Saim Imran Portfolio')

# from nicegui import ui

# # Define color scheme
# primary_color = '#3498db'  # Blue
# secondary_color = '#e74c3c'  # Red
# accent_color = '#2ecc71'  # Green
# dark_bg = '#2c3e50'  # Dark blue-gray
# light_text = '#ecf0f1'  # Light gray

# # Create the main page
# ui.page_title('Muhammad Saim Imran - Portfolio')

# # Create a multicolor gradient background
# ui.add_head_html('''
# <style>
#     body {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #667eea 100%);
#         background-size: 400% 400%;
#         animation: gradient 15s ease infinite;
#         min-height: 100vh;
#         color: white;
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }
#     @keyframes gradient {
#         0% {background-position: 0% 50%;}
#         50% {background-position: 100% 50%;}
#         100% {background-position: 0% 50%;}
#     }
#     .card {
#         background: rgba(255, 255, 255, 0.1);
#         backdrop-filter: blur(10px);
#         border-radius: 15px;
#         padding: 20px;
#         margin: 15px;
#         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
#         border: 1px solid rgba(255, 255, 255, 0.2);
#     }
#     .header {
#         text-align: center;
#         padding: 30px;
#         background: rgba(0, 0, 0, 0.2);
#         border-radius: 15px;
#         margin: 20px;
#     }
#     .skill-badge {
#         display: inline-block;
#         background: rgba(255, 255, 255, 0.2);
#         padding: 8px 15px;
#         margin: 5px;
#         border-radius: 20px;
#         font-weight: bold;
#     }
#     .contact-item {
#         display: flex;
#         align-items: center;
#         margin: 10px 0;
#     }
#     .contact-icon {
#         margin-right: 10px;
#         font-size: 1.2em;
#     }
# </style>
# ''')

# # Header Section
# with ui.card().classes('header'):
#     ui.image('https://via.placeholder.com/150/3498db/ffffff?text=Profile').classes('rounded-full shadow-lg')
#     ui.label('Muhammad Saim Imran').classes('text-4xl font-bold')
#     ui.label('AI Engineer').classes('text-2xl text-blue-300')
#     ui.separator().classes('my-4')
#     ui.label('Passionate about Artificial Intelligence and Machine Learning').classes('text-lg')

# # About Section
# with ui.card().classes('max-w-3xl mx-auto'):
#     ui.label('About Me').classes('text-3xl font-bold mb-4')
#     with ui.row():
#         ui.image('https://via.placeholder.com/200/e74c3c/ffffff?text=About').classes('rounded-lg shadow-md')
#         with ui.column().classes('ml-4'):
#             ui.label('I am an 18-year-old AI Engineer from Lahore, Pakistan.').classes('text-lg')
#             ui.label('With expertise in Python programming, Generative AI, and Data Science,').classes('text-lg')
#             ui.label('I build intelligent solutions to complex problems.').classes('text-lg')
#             ui.label('I am passionate about leveraging AI to create innovative technologies.').classes('text-lg')
#     ui.separator().classes('my-4')
#     with ui.row():
#         ui.label(f'Age: 18').classes('text-lg font-semibold')
#         ui.label(f'Location: Lahore, Pakistan').classes('text-lg font-semibold')

# # Skills Section
# with ui.card().classes('max-w-3xl mx-auto'):
#     ui.label('Skills').classes('text-3xl font-bold mb-4')
#     with ui.row().classes('flex-wrap justify-center'):
#         ui.label('Advanced Python Programming').classes('skill-badge bg-blue-500')
#         ui.label('Generative AI Expert').classes('skill-badge bg-purple-500')
#         ui.label('Data Scientist').classes('skill-badge bg-green-500')
#         ui.label('Machine Learning').classes('skill-badge bg-yellow-500')
#         ui.label('Deep Learning').classes('skill-badge bg-red-500')
#         ui.label('NLP').classes('skill-badge bg-indigo-500')
    
#     ui.separator().classes('my-4')
#     ui.label('Technical Proficiencies').classes('text-xl font-semibold mb-2')
#     ui.label('• Python, TensorFlow, PyTorch, Scikit-learn').classes('text-lg')
#     ui.label('• GPT, DALL-E, Stable Diffusion').classes('text-lg')
#     ui.label('• Pandas, NumPy, Matplotlib, Seaborn').classes('text-lg')
#     ui.label('• SQL, MongoDB, AWS, Docker').classes('text-lg')

# # Contact Section
# with ui.card().classes('max-w-3xl mx-auto'):
#     ui.label('Contact Information').classes('text-3xl font-bold mb-4')
    
#     with ui.column().classes('contact-container'):
#         with ui.row().classes('contact-item'):
#             ui.icon('phone', color='white').classes('contact-icon')
#             ui.label('+92 336 4665741').classes('text-lg')
        
#         with ui.row().classes('contact-item'):
#             ui.icon('email', color='white').classes('contact-icon')
#             ui.link('saimimranalpine@gmail.com', 'mailto:saimimranalpine@gmail.com').classes('text-lg text-blue-300')
        
#         with ui.row().classes('contact-item'):
#             ui.icon('code', color='white').classes('contact-icon')
#             ui.link('https://github.com/Saimcodes-cloud', target='_blank').classes('text-lg text-blue-300')
        
#         with ui.row().classes('contact-item'):
#             ui.icon('location_on', color='white').classes('contact-icon')
#             ui.label('Lahore, Pakistan').classes('text-lg')

# # Footer
# ui.label('© 2023 Muhammad Saim Imran. All rights reserved.').classes('text-center mt-8 text-gray-300')

# ui.run()     
from nicegui import ui

# Custom Styling
ui.add_head_html("""
    <style>
        body {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            color: #fbd14b;
        }
        .card {
            background-color: rgba(255, 255, 255, 0.08);
            padding: 20px;
            border-radius: 12px;
            margin: 10px 0;
        }
        .highlight {
            color: #00e5ff;
        }
        img.profile {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            border: 4px solid #fbd14b;
            object-fit: cover;
        }
        .section-title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>
""")

# Header Section
with ui.row().classes('items-center justify-center q-mt-xl'):
    with ui.column().classes('items-center'):
        ui.image('https://avatars.githubusercontent.com/u/139707770?v=4').classes('profile')  # Your GitHub avatar
        ui.label('Muhammad Saim Imran').classes('text-3xl text-bold text-yellow')
        ui.label('AI Engineer | Generative AI Expert | Data Scientist').classes('text-lg text-grey-3')

# About Me Section
with ui.column().classes('card'):
    ui.label('About Me').classes('section-title')
    with ui.row():
        with ui.column():
            ui.image('https://miro.medium.com/v2/resize:fit:1200/format:webp/1*J1RLLNn4o1Oa3kCgI6W3ug.png').classes('rounded-borders')  # AI banner
        with ui.column():
            ui.markdown("""
Hi! I'm **Muhammad Saim Imran**, an 18-year-old AI enthusiast from **Lahore, Pakistan**.  
I have a deep passion for building intelligent systems and exploring the frontier of **Generative AI**, **Deep Learning**, and **Data Science**.

My journey in AI started from curiosity and self-learning, and now I specialize in creating smart, scalable, and impactful machine learning solutions.  
I’ve worked with powerful tools like **TensorFlow**, **PyTorch**, and **Hugging Face**, and I love crafting AI applications that can transform industries.

In my free time, I experiment with new AI models, contribute to open-source, and write code that pushes boundaries.  
My goal? To make AI accessible and beneficial for everyone — and to keep learning every day.
            """)

# Skills Section
with ui.column().classes('card'):
    ui.label('Skills & Expertise').classes('section-title')
    ui.markdown("""
- 🐍 **Advanced Python Programming**  
- 🤖 **Generative AI & LLMs**  
- 📊 **Data Science & Machine Learning**  
- 🧠 **Neural Networks & Deep Learning**  
- ⚙️ Tools: PyTorch, TensorFlow, Scikit-learn, Hugging Face, Pandas, NumPy
- 🌐 API Development & AI Integration
    """)

# Optional Projects Section (Optional)
with ui.column().classes('card'):
    ui.label('Projects & Experiments').classes('section-title')
    with ui.row():
        with ui.column():
            ui.image('https://miro.medium.com/v2/resize:fit:1200/format:webp/1*vOwZncQDhhf5PfFVJi1Yqg.png').classes('rounded-borders')
            ui.markdown("**AI Chatbot using GPT-4 API**\nCreated a fully interactive chatbot using OpenAI's GPT-4 and deployed on the web.")
        with ui.column():
            ui.image('https://i.ibb.co/SXrrcK6/gen-ai.png').classes('rounded-borders')
            ui.markdown("**Image Generation using Stable Diffusion**\nBuilt a custom pipeline for generating art using AI and fine-tuned Stable Diffusion.")

# Contact Info
with ui.column().classes('card'):
    ui.label('Contact Me').classes('section-title')
    ui.markdown(f"""
- 📞 Phone: +92 336 4665741  
- 📧 Email: [saimimranalpine@gmail.com](mailto:saimimranalpine@gmail.com)  
- 🌍 Location: Lahore, Pakistan  
- 💻 GitHub: [Saimcodes-cloud](https://github.com/Saimcodes-cloud)
    """)

# Footer
with ui.footer().classes('text-center q-mt-xl'):
    ui.label('© 2025 Muhammad Saim Imran. Crafted with ❤️ using NiceGUI').classes('text-grey-4')

ui.run(title='Muhammad Saim Imran - AI Portfolio')


