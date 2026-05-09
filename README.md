# Multi-Frontend Demo Repository

This repository is now organized as a **multi-frontend setup** with two separate frontend applications.

## Frontend apps

- `angular-lazy-route-demo` (Angular 19, lazy route demo)
- `react-frontend` (React + Vite starter)

## Run Angular app

```bash
cd angular-lazy-route-demo
npm install
npm start
```

Open `http://localhost:4200`.

## Run React app

```bash
cd react-frontend
npm install
npm run dev
```

Open the URL shown by Vite (usually `http://localhost:5173`).

## Build apps

```bash
cd angular-lazy-route-demo && npm run build
cd react-frontend && npm run build
```
