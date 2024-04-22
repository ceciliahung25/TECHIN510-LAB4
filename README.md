# Lab 4: Accessing Web Resources with Python

## Goal
Create a Python-based web scraper to collect book data from [Books to Scrape](http://books.toscrape.com/), store the data in a PostgreSQL database, and build a Streamlit application to query and interactively filter the data.

## Getting Started
To set up this project locally, follow these installation steps:

```
python -m venv venv                         # Create a virtual environment
source venv/bin/activate                    # Activate the virtual environment (macOS/Linux)
venv\Scripts\activate                       # Activate the virtual environment (Windows)
pip install -r requirements.txt             # Install dependencies
streamlit run app.py                        # Run the Streamlit application
```

## Lessons Learned

During the development of this web scraping project, I learned several important aspects of software development and data handling:

- **Web Scraping Techniques**: Gained expertise in using `requests` and `BeautifulSoup` to scrape data efficiently from web pages.
- **Database Operations**: Enhanced my skills in PostgreSQL for storing, querying, and managing data efficiently.
- **Streamlit for Web Apps**: Explored how Streamlit can be utilized for building interactive web applications, simplifying the process of data visualization and user interaction.
- **Secure Configuration Management**: Learned the importance of securely managing sensitive information such as database credentials using environment variables and `.env` files.
- **Dynamic Query Handling**: Developed the ability to construct dynamic SQL queries that respond to user inputs to filter and sort data according to specified criteria.

## Reflections and Questions

As I reflect on the project and plan further improvements, I am considering the following questions to guide my learning and development:

- **State Management**: How can I effectively manage state in a Streamlit app to handle complex user interactions and data updates without performance degradation?
- **Advanced Streamlit Features**: What are the best practices for leveraging advanced features of Streamlit to enhance user experience and app functionality?
- **UI Customization**: How can I apply custom CSS or themes to improve the aesthetic appeal of the Streamlit app while maintaining its functional integrity?

## Next Steps

To continue enhancing the functionality and user experience of the book explorer app, these are my immediate goals:

- **Implement User Authentication**: Introduce a user authentication system to ensure a secure and personalized user experience.
- **Ensure UI Responsiveness**: Improve the UI to ensure that the app is responsive and functions smoothly across different devices and screen sizes.
- **Broaden Data Features**: Expand the range of queryable data and interactive elements within the app to provide users with more granular control over the data displayed.
- **Develop User Guides**: Create comprehensive documentation and user guides within the app to assist users in navigating and making the most of the application’s features.
