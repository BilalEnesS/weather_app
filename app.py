from flask import Flask, render_template, request, jsonify
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Get current weather conditions (temperature and description) for a city using Open-Meteo API."""
    
    # 1. Get latitude and longitude from city name (via geocoding)
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    try:
        geo_res = requests.get(geo_url, timeout=10)
        
        if geo_res.status_code != 200 or not geo_res.json().get("results"):
            return f"❌ Location not found for '{city}'."
        
        location = geo_res.json()["results"][0]
        lat, lon = location["latitude"], location["longitude"]
        
        # 2. Get current weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code,wind_speed_10m,relative_humidity_2m&timezone=auto"
        weather_res = requests.get(weather_url, timeout=10)
        
        if weather_res.status_code != 200:
            return "❌ Unable to fetch weather data."
        
        weather_data = weather_res.json()["current"]
        temp = weather_data["temperature_2m"]
        code = weather_data["weather_code"]
        wind_speed = weather_data.get("wind_speed_10m", 0)
        humidity = weather_data.get("relative_humidity_2m", 0)
        
        # Weather code descriptions
        code_map = {
            0: "clear sky", 1: "mainly clear", 2: "partly cloudy", 3: "overcast",
            45: "foggy", 48: "depositing rime fog", 51: "light drizzle", 53: "moderate drizzle",
            55: "dense drizzle", 61: "slight rain", 63: "moderate rain", 65: "heavy rain",
            71: "slight snow", 73: "moderate snow", 75: "heavy snow", 80: "slight rain showers",
            81: "moderate rain showers", 82: "violent rain showers", 95: "thunderstorm"
        }
        desc = code_map.get(code, "unknown weather condition")
        
        return f"Weather for {location['name']}: {temp}°C, {desc}. Wind: {wind_speed} km/h, Humidity: {humidity}%"
    
    except requests.RequestException:
        return "❌ Weather service is currently unavailable."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

# LLM and Agent setup
llm = ChatOpenAI(model="gpt-4.1", temperature=0)
tools = [get_weather]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant that helps users with weather-related questions. Respond in English and use tools when necessary."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

agent = create_tool_calling_agent(llm, tools, prompt=prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather_info():
    try:
        data = request.get_json()
        city = data.get('city', '').strip()
        
        if not city:
            return jsonify({'error': 'Please enter a city name.'}), 400
        
        # Execute the agent
        response = executor.invoke({"input": f"{city} weather"})
        
        return jsonify({
            'success': True,
            'response': response["output"]
        })
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)