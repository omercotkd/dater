FROM node:18-alpine as build

WORKDIR /front

COPY ./front /front

RUN npm install

RUN npm run build


# now using python image to run the fastapi server that serves the front end
FROM python:3.9-slim

COPY . .

COPY --from=build /front/dist /front/dist

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]


