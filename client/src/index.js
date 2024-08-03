import React from "react";
import App from "./components/App";
import ReactDOM from 'react-dom/client';
import "./index.css";
import routes from '../src/components/routes.js'
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter(routes)

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<RouterProvider router={router} />);






// const container = document.getElementById("root");
// const root = createRoot(container);
// root.render(<App />);

