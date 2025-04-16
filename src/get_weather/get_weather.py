"""
ファイル名: get_weather.py
概要:
    Model Context Protocol (MCP)を用いた天気情報取得サーバーです。
    OpenWeatherMap APIを使用し、LLMアプリケーションが都市名からリアルタイムの天気情報を取得できるようにします。

使用方法:
    対応LLMアプリケーション（例: Claude Desktop）から接続してください。
    環境変数 `OPENWEATHER_API_KEY` に有効なAPIキーを設定する必要があります。
"""

from typing import Any
import httpx
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

# OpenWeatherMap APIの設定
API_BASE = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY", "default_key_here")  # 環境変数から取得


# 天気取得ツールを定義
@mcp.tool()
async def get_weather(city: str) -> str:
    """指定した都市の現在の天気を取得します。

    Args:
        city: 都市名（例: Tokyo）
    """
    async with httpx.AsyncClient() as client:
        try:
            url = f"{API_BASE}?q={city}&appid={API_KEY}&units=metric"
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"{city}の現在の天気: {desc}, 気温: {temp}°C"
        except httpx.HTTPStatusError:
            return f"エラー: {city}の天気情報が見つかりませんでした。"
        except Exception as e:
            return f"エラー: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
