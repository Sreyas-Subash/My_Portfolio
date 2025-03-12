import json

# Define career timeline data
career_data = {
    "events": [
        {
            "start_date": {"year" : "2024", "month" : "11"},
            "end_date": {"year" : "2025", "month" : "2"},
            "text": {"headline": "StepOutPlay - Performance Analysis Trainer",
                     "text": "Worked on backend development using Python and Django. Developed APIs and optimized database queries."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Company A Office"},
            "background": {"color": "#FF5858"}
        },
        {
            "start_date": {"year" : "2024", "month" : "3"},
            "end_date": {"year" : "2024", "month" : "11"},
            "text": {"headline": "StepOutPlay - Tech Ops and Training Lead",
                     "text": "Led a team of developers to build scalable web applications. Implemented microservices architecture."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Team at Company B"},
            "background": {"color": "#FF5858"}
        },
        {
            "start_date": {"year": "2023", "month": "8"},
            "end_date": {"year": "2024", "month": "3"},
            "text": {"headline": "StepOutPlay - Performance Analyst Intern",
                     "text": "Led a team of developers to build scalable web applications. Implemented microservices architecture."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Team at Company B"},
            "background": {"color": "#FF5858"}
        },
        {
            "start_date": {"year": "2023", "month": "6"},
            "end_date": {"year": "2023", "month": "8"},
            "text": {"headline": "Gofreelab Technologies - Training Intern",
                     "text": "Led a team of developers to build scalable web applications. Implemented microservices architecture."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Team at Company B"},
            "background": {"color": "#FF5858"}
        },
        {
            "start_date": {"year": "2022", "month": "10"},
            "end_date": {"year": "2023", "month": "6"},
            "text": {"headline": "Gofreelab Technologies - Data Analysis Bootcamp",
                     "text": "Led a team of developers to build scalable web applications. Implemented microservices architecture."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Team at Company B"},
            "background": {"color": "#FF5858"}
        },
        {
            "start_date": {"year": "2022", "month": "6"},
            "end_date": {"year": "2022", "month": "9"},
            "text": {"headline": "SportsKPI - Data Analyst Intern",
                     "text": "Led a team of developers to build scalable web applications. Implemented microservices architecture."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Team at Company B"},
            "background": {"color": "#FF5858"}
        },
        {
            "start_date": {"year": "2021", "month": "8"},
            "end_date": {"year": "2022", "month": "8"},
            "text": {"headline": "Career Break",
                     "text": "Led a team of developers to build scalable web applications. Implemented microservices architecture."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Team at Company B"},
            "background": {"color": "#FF5858"}
        },
        {
            "start_date": {"year": "2018", "month": "5"},
            "end_date": {"year": "2021", "month": "8"},
            "text": {"headline": "SB College - BSc Mathematics",
                     "text": "Led a team of developers to build scalable web applications. Implemented microservices architecture."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Team at Company B"},
            "background": {"color": "#FF5858"}
        },
        {
            "start_date": {"year": "2017"},
            "end_date": {"year": "2018"},
            "text": {"headline": "12th Standard - 88%",
                     "text": "Led a team of developers to build scalable web applications. Implemented microservices architecture."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Team at Company B"},
            "background": {"color": "#FF5858"}
        },
        {
            "start_date": {"year": "2015"},
            "end_date": {"year": "2016"},
            "text": {"headline": "10th Standard - %",
                     "text": "Led a team of developers to build scalable web applications. Implemented microservices architecture."},
            "media": {"url": "https://via.placeholder.com/400", "caption": "Team at Company B"},
            "background": {"color": "#FF5858"}
        }
    ]
}

# Convert to JSON
career_json = json.dumps(career_data)

