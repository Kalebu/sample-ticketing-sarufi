<samp>

# sample-ticketing-sarufi

## Description
This is a simple ticketing system that allows users to create tickets,trigger payments and view tickets, plus send SMS notifications to users.


## Technologies Used

FastAPI, Python, Africastalking API, HTTPX


To install the requirements

```bash
pip install -r requirements.txt
```

you will need to have a .env file with the following variables

```bash
AT_USER_NAME=your_username
AT_API_KEY=your_api_key
```


To run the application

```bash
uvicorn main:app --reload
```

You can Deploy it to cloud or use Ngrok to expose the local server to the internet.

```bash
ngrok http 8000
```

Copy the generated URL and use it to trigger the endpoints on the application.


Here are some references links to the technologies used:
1. [FastAPI](https://fastapi.tiangolo.com/)
2. [Africastalking API](https://africastalking.com/)
3. [Sarufi](https://sarufi.io/)
4. https://docs.sarufi.io/docs/sarufi-dashboard/middleware
5. https://ngrok.com/
6. https://www.youtube.com/@neurotechafrica/videos

</samp>
