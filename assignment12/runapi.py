import asyncio
import httpx
import json

servers = [
    "http://172.20.49.75:8000",
    "http://172.20.49.55:8000",
    "http://172.20.49.56:8000",
    "http://172.20.50.40:8000"
]

async def fetch_data(client, server):
    result = {}

    # Fetch /students
    try:
        r = await client.get(f"{server}/Students")
        r.raise_for_status()
        students = r.json()
        result["server"] = server
        result["student_count"] = len(students)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error fetching /students from {server}: {e}")

    # Fetch /analytics/group
    try:
        r = await client.get(f"{server}/analytics/group")
        r.raise_for_status()
        groups = r.json()
        print(json.dumps({"server": server, "group_analytics": groups}, indent=2))
    except Exception as e:
        print(f"Error fetching /analytics/group from {server}: {e}")

    # Fetch /analytics/year
    try:
        r = await client.get(f"{server}/analytics/year")
        r.raise_for_status()
        years = r.json()
        print(json.dumps({"server": server, "year_analytics": years}, indent=2))
    except Exception as e:
        print(f"Error fetching /analytics/year from {server}: {e}")

async def main():
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [fetch_data(client, server) for server in servers]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
