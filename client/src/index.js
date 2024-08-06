import React from "react";
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Context, ContextProvider } from "./components/Context";
import "./index.css";
import routes from '../src/components/routes.js'
import { createClient } from '@supabase/supabase-js'
import { SessionContextProvider } from '@supabase/auth-helpers-react'

const supabase = createClient(
    "https://ixnvqjgbujylgejxwnxl.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml4bnZxamdidWp5bGdlanh3bnhsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE1MDM4NDIsImV4cCI6MjAzNzA3OTg0Mn0.m2aMQpVyrjh6tCupuB5cQ6B0Jg4Xgb3V8sHBUPUcKDs"
);


const router = createBrowserRouter(routes)

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <ContextProvider>
        <RouterProvider router={router} /> 
    </ContextProvider>
);







// const container = document.getElementById("root");
// const root = createRoot(container);
// root.render(<App />);

