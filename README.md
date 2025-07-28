# 🌤️ Weather Assistant

An AI-powered weather information application that provides real-time weather data for any city worldwide using advanced language models and weather APIs.

![Weather Assistant](https://img.shields.io/badge/Weather-Assistant-blue?style=for-the-badge&logo=weather)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3+-green?style=for-the-badge&logo=flask)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange?style=for-the-badge&logo=openai)

## ✨ Features

- 🤖 **AI-Powered Assistant**: Natural language weather conversations using OpenAI GPT-4.1
- 🌍 **Global Coverage**: Access weather data for cities worldwide
- ⚡ **Real-time Data**: Current weather conditions with temperature, wind, and humidity
- 🎨 **Modern UI**: Beautiful, responsive design with smooth animations
- 📱 **Mobile Friendly**: Optimized for all device sizes
- 🔍 **Smart Search**: Quick access to popular cities

## 🚀 Live Demo

Experience the Weather Assistant in action! The application provides:

- **Intelligent Weather Queries**: Ask about weather in natural language
- **Comprehensive Data**: Temperature, conditions, wind speed, and humidity
- **Global City Support**: Any city worldwide
- **Instant Results**: Real-time weather information

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask**: Web framework for API endpoints
- **LangChain**: AI/LLM integration framework
- **OpenAI GPT-4**: Advanced language model for natural conversations
- **Open-Meteo API**: Free weather data service

### Frontend
- **HTML5/CSS3**: Modern, responsive design
- **JavaScript**: Interactive user interface
- **Font Awesome**: Beautiful icons
- **Inter Font**: Clean typography
- **CSS Animations**: Smooth transitions and effects

### APIs & Services
- **OpenAI API**: GPT-4 language model
- **Open-Meteo API**: Weather data and geocoding
- **Geocoding API**: City name to coordinates conversion

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher
- OpenAI API key
- Internet connection for API calls

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/weather_app.git
cd weather-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**Important**: Replace `your_openai_api_key_here` with your actual OpenAI API key.

### 5. Run the Application

```bash
python app.py
```

The application will be available at: `http://localhost:5000`

## 🏗️ Project Structure

```
weather_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore file
├── README.md            # This file
└── templates/
    └── index.html       # Main web interface
```

## 🔌 API Endpoints

### GET `/`
- **Description**: Main application page
- **Response**: HTML interface

### POST `/weather`
- **Description**: Get weather information for a city
- **Request Body**: `{"city": "London"}`
- **Response**: 
  ```json
  {
    "success": true,
    "response": "Weather for London: 18°C, partly cloudy. Wind: 12 km/h, Humidity: 65%"
  }
  ```

## 🎯 Usage Examples

### Basic Weather Query
1. Enter a city name (e.g., "London", "Tokyo", "New York")
2. Click the search button or press Enter
3. Get instant weather information

### Popular Cities
Quick access buttons for popular cities:
- London
- New York
- Tokyo
- Paris
- Sydney
- Dubai
- Istanbul

### Natural Language Queries
The AI assistant can handle various question formats:
- "What's the weather in London?"
- "How's the weather in Tokyo?"
- "Temperature in New York"

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Customization

You can customize the application by modifying:

- **Weather API**: Change Open-Meteo to other weather services
- **AI Model**: Switch to different OpenAI models
- **UI Design**: Modify CSS in `templates/index.html`
- **Language**: Update prompts and responses

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider:

1. **WSGI Server**: Use Gunicorn or uWSGI
2. **Reverse Proxy**: Nginx or Apache
3. **Environment**: Set `FLASK_ENV=production`
4. **Security**: Use HTTPS and secure headers

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Development Guidelines

- Follow PEP 8 Python style guide
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI**: For providing the GPT-4.1 language model
- **Open-Meteo**: For free weather data API
- **Font Awesome**: For beautiful icons
- **Inter Font**: For clean typography

## 📞 Support

If you encounter any issues or have questions:

1. **Check Issues**: Look for similar problems in the issues section
2. **Create Issue**: Open a new issue with detailed information
3. **Contact**: Reach out to the maintainers


<div align="center">

**Made with ❤️ by the Weather Assistant Team**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/weather-assistant?style=social)](https://github.com/yourusername/weather-assistant)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/weather-assistant?style=social)](https://github.com/yourusername/weather-assistant)

</div> 